import requests
from bs4 import BeautifulSoup


def latest_news(f):
    page = requests.get(f)
    soup = BeautifulSoup(page.text, "html.parser")

    for headline in soup.find_all(class_="LatestNews-headline"):

        if headline.a:
            print(headline.a.text.replace("\n", " ").strip())
        else:
            print(headline.contents[0].strip())

        print(headline.get("href"))


cnbc = "https://www.cnbc.com/"
print("Latest News of CNBC:\n")
latest_news(cnbc)
