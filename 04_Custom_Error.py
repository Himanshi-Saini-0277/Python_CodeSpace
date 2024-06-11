a = input("Enter a number between 2 and 9: ")

if a.isdigit():
  if (int(a)>2 or int(a)<9):
    print("successful")

  elif (int(a) < 2 or int(a) > 9):
    raise ValueError ("Incorrect number")

elif a.lower() == "quit":
  print("You have quit the program")