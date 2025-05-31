import requests as r
import os
from send_email import send_email

topic = "tesla"

api_key = os.getenv("NewsApiKey")
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-04-30&"
       "sortBy=publishedAt&"
       "apiKey=95ac2c9588624285b77362492f8f7909&"
       "language=en")

re = r.get(url)
content = re.json()
body = ""
for article in content["articles"][:5]:
       if article["title"] and article["description"] is not None:
              body = (body + "Subject: Today's News" + "\n" + article["title"] + "\n" +
                      article["description"] + "\n" +
                      article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)