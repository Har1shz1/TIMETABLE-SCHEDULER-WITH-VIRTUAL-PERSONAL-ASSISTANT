# TIMETABLE-SCHEDULER-WITH-VIRTUAL-PERSONAL-ASSISTANT
The goal of this project is to make the disorganized process of creating timetables more effective and user-friendly for the benefit of all parties involved in the academic environment.
# Features
• Automated timetable creation to reduce errors, save time, and offer a simple, reliable solution to schedule academic schedules effectively.

• Develop a scheduler that ensures no overlapping or conflicting slots adhering to predefined rules and constraints.

• Provide reminders for upcoming classes using extracted timetable details and answer general queries enhancing user convenience.

• To increase the productivity of the faculties and scholars in their day to day activities.

• To replace the existing manual scheduling of timetables.

• Show a proof of concept to actually implement this in the university for real time use.

# Proposed System
The system that we have developed can be seen as two different parts. The first part is the timetable scheduler part where we wrote our custom coded algorithm which implements all the constraints for scheduling the timetable for research scholars. The second part is the virtual personal assistant which uses Google’s Gemini API as it’s backbone and also has the additional function of providing reminders to the user for upcoming classes using the output of the timetables scheduled using the timetable scheduler algorithm. The following block diagram shows the system architecture of this project.

![image](https://github.com/user-attachments/assets/26acfe1b-baef-4bb3-acfa-ee3a62e5c912)

# Working Methodology
The personal assistant and the timetable scheduler are the two main elements of the
project. Together, these elements create timetables free of conflicts and offer smooth assistance
with academic task management. The technique starts by entering the necessary information, such
as courses, faculty/research scholar details, rooms list and open slots in the form of a csv file. In
order to keep pertinent attributes like course code, credits, necessary theory and lab slots, and
faculty/research scholar details like name, gender, courses taken, and priority, we have created
classes for courses and faculties/research scholars.

The main component of the system is the timetable scheduler, which assigns lab slots
using a brute-force approach. This algorithm looks for limits like preventing conflicting times,
making sure there aren't any ongoing lab sessions, and following gender-based guidelines like not
allowing female teachers to work in the evenings. While maintaining fairness and adherence to all
restrictions, the scheduler iterates through each faculty/research scholar in the provided input and
for each faculty it iterates through the courses they have taken and assigns slots to each course.
For assigning a slot, it randomly picks a slot and room combination from the list of rooms and
available slots. The process generates a new random slot until a valid one is identified if a clash is
detected. For now the scheduler only gives a structured output for lab slots for each research
scholar.

After that, the virtual personal assistant takes over and pulls up the timetable information,
including the venue, time, slot, and course code, to send out reminders for upcoming lessons. It
also handles general user inquiries using audio input. All we have to do is talk to it and it uses the
“SpeechRecognition” python library to convert the audio to text which is then sent to Google’s
Gemini API (gemini-1.5-flash) which processes the prompt and gives its output. This output is
then converted to audio using the text-to-speech library named “pyttsx3”. In order to ensure
efficiency and user comfort, the schedules are finally saved in an excel file for convenient access
and sharing using the “OpenPyXL” python library.

# Output Format
• The Excel (.xlsx) format used to construct the timetables is compatible with Google
Sheets, Microsoft Excel, and other spreadsheet programs. This guarantees that users
are able to browse, edit, or print timetables as required.

• The virtual personal assistant uses the text-to-speech library named “pyttsx3” to
convert the Gemini API’s output to audio format so that it can be read out to the user
through the virtual character.

• The system also provides system notification using the “Plyer” library for reminding
users of upcoming classes from the timetable.

# Timetable Scheduler Output

![image](https://github.com/user-attachments/assets/6bc7266d-894e-4659-8604-250850024dfe)

![image](https://github.com/user-attachments/assets/c7d13b1b-395a-4918-9c5b-191ff89f6958)

![image](https://github.com/user-attachments/assets/91525cb3-a871-4103-843c-673cc321f8b5)

![image](https://github.com/user-attachments/assets/df6e6ea3-7748-46fa-b454-63294812df27)

# Virtual Personal Assistant

![image](https://github.com/user-attachments/assets/8e9da6cf-f20a-46b2-b6ad-5f5377f68290)






