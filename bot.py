import requests
from bs4 import BeautifulSoup
import pandas as pd


urls = ["https://example1.com/blog", "https://example2.com/news", "https://example3.com/articles"]


topic = "AI"

data = []


for url in urls:
 
    response = requests.get(url)
   
    soup = BeautifulSoup(response.content, "html.parser")
   
    articles = soup.find_all("article")
    
    for article in articles:
        if topic in article.text:
            data.append(article.text)


df = pd.DataFrame(data, columns=["text"])


df.to_csv("topic_data.csv", index=False)