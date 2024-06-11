import time

a = int(time.strftime('%H'))

if (a < 12):
  print("Good Morning Mam")

elif (a > 12 & a < 15):
  print("Good Afternoon Mam")

else:
  print("Good Evening Mam")

print(time.strftime('%H:%M:%S'))
if (a < 12):
  print("AM")
else:
  print("PM")
