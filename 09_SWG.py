a = int (input("For snake enter 0, for water enter 1, for gun enter 2: "))

computer = [0,1,2]

import random
b = random.choice(computer)
print ("Computer:", b)

if (a == 0 and b == 0):
  print ("its a draw")

elif (a == 0 and b == 1):
  print ("you win")

elif (a == 0 and b == 2) or (a == 1 and b == 0):
  print ("you lose")

elif (a == 1 and b == 1):
  print ("its a draw")

elif (a == 1 and b == 2) or (a == 2 and b == 0):
  print ("you win")

elif (a == 2 and b == 1):
  print ("you lose")

elif (a == 2 and b == 2):
  print ("its a draw")

else :
  print ("invalid input")