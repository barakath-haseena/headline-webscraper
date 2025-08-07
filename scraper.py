import requests
from bs4 import BeautifulSoup

url = "https://inshorts.com/en/read"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all("span", itemprop="headline")

    print("\n📰 Latest Inshorts Headlines:\n")
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, headline in enumerate(headlines[:10], 1):  # Top 10 headlines
            print(f"{idx}. {headline.text}")
            file.write(f"{idx}. {headline.text}\n")
else:
    print("Failed to fetch headlines.")
