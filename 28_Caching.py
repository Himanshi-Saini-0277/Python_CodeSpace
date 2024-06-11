from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(3)
  return n*5

print(fx(20))
print(fx(60))
print(fx(50))
print(fx(20))
print(fx(60))
print(fx(50))
print(fx(10))