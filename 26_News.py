import requests
import json

query = input ("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-11&sortBy=publishedAt&apiKey=63f791c19b9f4c5e9d2b65b7600a409b"
r = requests.get(url)
print(r.text)

news = json.loads(r.text)
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
