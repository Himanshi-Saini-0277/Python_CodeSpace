import multiprocessing
import requests
import concurrent.futures

def file(url, name):
  print(f"Started downloading {name}")
  r = requests.get(url) 
  open(f"file/{name}.jpg", "wb").write(r.content)
  print(f"Finished downloading {name}")

url = "https://picsum.photos/200/300"
pros = []
for i in range(5):
  p = multiprocessing.Process(target= file, args =[url,i])
  p.start()
  pros.append(p)

for p in pros:
  p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(5)]
  l2 = list(range(5))
  result = executor.map (file, l1,l2)
  for r in result:
    print(r)