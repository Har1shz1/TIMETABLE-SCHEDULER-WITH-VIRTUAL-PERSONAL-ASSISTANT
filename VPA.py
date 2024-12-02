import tkinter as tk
from PIL import Image, ImageTk
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import threading
import pandas as pd
from plyer import notification
from datetime import datetime, timedelta
import time as t

# Configuring Google Generative AI API key
gapi = ""
genai.configure(api_key=gapi)
model = genai.GenerativeModel('gemini-1.5-flash')

class InteractiveCharacterWithAPI:
    def _init_(self, root):
        self.root = root
        self.root.title("Interactive Character")
        self.root.geometry("300x250")
        self.tts_engine = pyttsx3.init()
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", "#000000")
        self.root.wm_attributes("-topmost", True)
        self.gif_image = Image.open("a.gif")  # Update with your GIF path
        self.gif_frames = []

        try:
            while True:
                frame = self.gif_image.copy()
                if frame.mode in ('RGBA', 'P'):
                    frame = frame.convert('RGBA')
                else:
                    frame = frame.convert('RGBA')
                self.gif_frames.append(ImageTk.PhotoImage(frame))

                self.gif_image.seek(self.gif_image.tell() + 1)
        except EOFError:
            pass  # End of GIF frames

        self.current_frame = 0
        self.label = tk.Label(self.root, image=self.gif_frames[self.current_frame], bg="#000000")
        self.label.pack(fill=tk.BOTH, expand=True)
        # Start the animation loop
        self.animate_gif()
        # Create an entry widget for user input
        self.entry = tk.Entry(self.root, font=("Arial", 12), bg="#ffffff", fg="#000000", bd=1)
        self.entry.pack(pady=10)
        self.ask_button = tk.Button(self.root, text="Ask", command=self.answer_question, bg="#ffffff", fg="#000000",
                                    bd=1)
        self.ask_button.pack(pady=5)
        self.response_label = tk.Label(self.root, text="", font=("Arial", 12), bg="white")
        self.response_label.pack(pady=10)
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)
        self.speech_thread = threading.Thread(target=self.listen_for_speech)
        self.speech_thread.daemon = True
        self.speech_thread.start()

    def animate_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.label.config(image=self.gif_frames[self.current_frame])
        self.root.after(100, self.animate_gif)  # Adjust the delay (100 ms) as needed for smoother or faster animation

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def answer_question(self):
        question = self.entry.get()
        for o in question:
            if o=="explain":
                question+"briefly in 200 words"
        response = self.get_response_from_api(question)
        self.response_label.config(text=response)
        self.speak(response)
        self.entry.delete(0, tk.END)

    def listen_for_speech(self):#speech listener
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                print("Listening for speech...")
                audio = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio)
                    print(f"Heard: {text}")


                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, text)


                    if text.strip():#automatic click ask button (if filled)
                        self.root.after(1000, self.check_and_ask)

                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    self.response_label.config(text="Sorry, there was an error with the speech recognition service.")

    def check_and_ask(self):
        current_text = self.entry.get()
        if current_text.strip():
            self.ask_button.invoke()  # Simulate button click

    def get_response_from_api(self, question):
        try:
            response = model.generate_content(question)
            return response.text
        except Exception as E:
            return f"An error occurred: {E}"

    def speak(self, text):
        if len(text)>200:
            q=text[:200]
            self.tts_engine.say(q)
            self.tts_engine.runAndWait()
        else:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()

def check_schedule():
    current_time = datetime.now()
    current_day = current_time.strftime('%A')  # Get the current day (e.g., Monday, Tuesday)
    current_time_only = current_time.time()  # Get the current time

    for _, row in schedule.iterrows():
        try:
            # Check if the day matches
            if row['Day'] == current_day:
                class_time = row['Start Time']
                reminder_time = (datetime.combine(datetime.today(), class_time) - timedelta(minutes=10)).time()

                # Debugging: Print times
                print(f"Current time: {current_time_only}, Reminder time: {reminder_time}, Class time: {class_time}")

                # If current time matches the reminder time
                if current_time_only >= reminder_time and current_time_only < class_time:
                    notification.notify(
                        title="Class Reminder",
                        message=f"Day: {row['Day']}, Slot: {row['Slot']}, "
                                f"Subject Code: {row['Subject Code']}, Venue: {row['Venue']}",
                        timeout=10  # Notification duration in seconds
                    )
        except Exception as E:
            print(f"Error processing row: {E}")

if _name_ == "_main_":
    root = tk.Tk()
    app = InteractiveCharacterWithAPI(root)
    root.mainloop()
# Load and preprocess the CSV file
csv_file = "C:/Users/LENOVO/Downloads/t2.xlsx" # Replace with your actual CSV file name
try:
    schedule = pd.read_csv(csv_file)
    # Ensure correct time parsing
    schedule['Start Time'] = pd.to_datetime(
        schedule['Timing'].str.split('-').str[0], format='%H.%M'
    ).dt.time
    print("Remainder service is running...")
    while True:
        check_schedule()
        t.sleep(60)
except Exception as E:
    print(f"Error loading or processing CSV: {E}")
    exit()



