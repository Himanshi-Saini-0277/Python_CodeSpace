import pyttsx3

names = ["Himanshi", "Parshav", "Deepak"]

engine = pyttsx3.init()

for name in names:
  shoutout = f"Shoutout to {name}"
  print(shoutout)
  engine.say(shoutout)

engine.runAndWait()