import requests
from bs4 import BeautifulSoup
import pandas as pd

# list of URLs of the blogs you want to scrape
urls = ["https://example1.com/blog", "https://example2.com/news", "https://example3.com/articles"]

# topic you want to filter by
topic = "AI"

data = []

# loop through each URL
for url in urls:
    # make a request to the website
    response = requests.get(url)
    # parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # find all the article elements on the page
    articles = soup.find_all("article")
    # extract the text from each article
    for article in articles:
        if topic in article.text:
            data.append(article.text)

# create a dataframe with the data
df = pd.DataFrame(data, columns=["text"])

# save the dataframe to a CSV file
df.to_csv("topic_data.csv", index=False)