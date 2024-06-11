f = open("data/Terminal10/read.md", "r")
i=0
while True:
  i = i+1

  line = f.readline()

  if not line:
    break

  m1 = line.split(" ")[0]
  m2 = line.split(" ")[1]

  print (f"{i} {m1}")
  print (f"{i} {m2}")

  print (line)

f = open("data/Terminal10/read.md", "w")
with open("data/Terminal10/read.md", "a"):
  f.write("Hello")

f = open("data/Terminal10/read.md", "w")

lines =['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()