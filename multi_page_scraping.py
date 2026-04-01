import requests
from bs4 import BeautifulSoup
import csv

page = 1

with open("quotes_full_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    while True:
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")
        tag_boxes = soup.find_all("div", class_="tags")

        if not quotes:
            break

        for q, a, t in zip(quotes, authors, tag_boxes):
            tags = [tag.text for tag in t.find_all("a", class_="tag")]
            tags_str = ", ".join(tags) 

            writer.writerow([
                q.text.strip(),
                a.text.strip(),
                tags_str
            ])

        page += 1