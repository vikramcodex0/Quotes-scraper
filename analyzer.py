import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}/"

authors_list = []
total = 0

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    page = 1

    while True:
        url = base_url.format(page)
        response = requests.get(url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        if not quotes:
            break

        for q, a in zip(quotes, authors):
            clean_quote = q.text.strip().replace("“", "").replace("”", "")
            clean_author = a.text.strip()

            writer.writerow([clean_quote, clean_author])

            authors_list.append(clean_author)
            total += 1

        page += 1

print("Total Quotes:", total)

# Author frequency
unique_authors = set(authors_list)

for author in unique_authors:
    print(author, ":", authors_list.count(author))