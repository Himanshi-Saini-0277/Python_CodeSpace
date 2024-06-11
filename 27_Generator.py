def generator():
  for i in range (5000):
    yield i

# yield do not store the value in memory it just show the value when called
# at a particular instance

gen = generator()
for j in gen:
  print(j)