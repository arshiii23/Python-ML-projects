Real-Time Notification System

A simple desktop notification application built using Python and the Plyer library. This project demonstrates how to send real-time system notifications directly from Python.


---

Features

Desktop notifications

Real-time reminders

Lightweight and beginner-friendly

Cross-platform support

Simple Python implementation



---

Technologies Used

Python

Plyer Library


---

Installation

1. Clone the Repository

git clone https://github.com/your-username/notification-system.git


---

2. Navigate to Project Folder

cd notification-system


---

3. Create Virtual Environment (Optional)

python -m venv myenv

Activate environment:

Windows

myenv\Scripts\activate

Mac/Linux

source myenv/bin/activate


---

4. Install Required Library

pip install plyer

Or install using requirements file:

pip install -r requirements.txt


---

Python Code

from plyer import notification

notification.notify(
    title="Reminder",
    message="Time to study Python!",
    timeout=10
)

print("Notification sent")


---

How to Run the Project

Run the Python file:

python main.py


---

Expected Output

Terminal Output

Notification sent


---

Desktop Output

A system notification popup will appear on your desktop:

Reminder
Time to study Python!

---

Concepts Learned

Python Notifications

Desktop Automation

Third-Party Libraries

Real-Time Alerts

Python Package Management

---

Future Improvements

Scheduled reminders

Daily task notifications

Alarm system

GUI interface

Sound notifications

Email reminders

---

Author
Arsheen Shaikh
---
