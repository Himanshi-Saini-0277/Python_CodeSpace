import time

def uwhile():
  i = 0
  while i < 5000:
    print(i)
    i = i + 1

def ufor():
  for i in range (5000):
    print(i)

a = time.time()
uwhile()
t1 = (time.time() - a)

b = time.time()
ufor()
t2 = (time.time() - b)

print(t1)
print(t2)