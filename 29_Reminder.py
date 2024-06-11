import pyttsx3
import time
import ctypes

def show_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)

engine = pyttsx3.init()

while True:
    engine.say("Hey Himanshi, Drink Water")
    engine.runAndWait()
    show_notification("Reminder", "Hey Himanshi, Drink Water")

    time.sleep(10)
