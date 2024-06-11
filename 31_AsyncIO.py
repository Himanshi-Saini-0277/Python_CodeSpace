import asyncio
import time


async def f1():
  print("f1")
  time.sleep(1)
  return "f1"


async def f2():
  print("f2")
  time.sleep(2)
  return "f2"


async def main():
  l = await asyncio.gather(
    f1(), 
    f2())
  
  print(l)


asyncio.run(main())
