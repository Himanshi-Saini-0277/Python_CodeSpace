# web scraping

import requests
from bs4 import BeautifulSoup

r = requests.get (url = "https://www.geeksforgeeks.org/python-programming-language/")
print (r.text)

soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())

for heading in soup.find_all("h2"):
  print (heading.text)