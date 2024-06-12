import threading
import time
from concurrent.futures import ThreadPoolExecutor

def f(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)

time1 = time.perf_counter()

f(4)
f(2)
f(1)

time2 = time.perf_counter()
print(time2-time1)

t1 = threading.Thread(target=f, args=[4])
t2 = threading.Thread(target=f, args=[2])
t3 = threading.Thread(target=f, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time3 = time.perf_counter()
print(time3-time2)


with ThreadPoolExecutor() as executor:
  future = executor.submit(f, 2)
  future2 = executor.submit(f, 4)
  future3 = executor.submit(f, 6)
  
  print(future.result())
  print(future2.result())
  print(future3.result())

  l = [3, 5, 7]
  r = executor.map(f,l)
  for i in r:
    print(i)