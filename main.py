import requests as r

api_key = "95ac2c9588624285b77362492f8f7909"
url = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2025-04-30&sortBy=publishedAt&apiKey=95ac2c9588"
       "624285b77362492f8f7909")

re = r.get(url)
content = re.json()
for article in content["articles"]:
       print(article["title"])
       print(article["description"])