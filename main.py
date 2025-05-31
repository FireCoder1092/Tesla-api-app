import requests as r
import os
from send_email import send_email

api_key = os.getenv("NewsApiKey")
url = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2025-04-30&sortBy=publishedAt&apiKey=95ac2c9588"
       "624285b77362492f8f7909")

re = r.get(url)
content = re.json()
body = ""
for article in content["articles"]:
       if article["title"] and article["description"] is not None:
              body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)