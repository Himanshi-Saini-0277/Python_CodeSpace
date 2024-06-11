import os

folders = os.mkdir("data")

for i in range (0, 100):
  os.mkdir(f"data/Day{i+1}")
  os.rename(f"data/Day{i+1}" ,f"data/Terminal{i+1}")

print(os.listdir("data"))

folders = os.listdir("data")

for i in folders:
  print(i)
  print (os.listdir(f"data/{i}"))

print (os.getcwd())
