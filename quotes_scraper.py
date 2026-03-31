import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)

# ⚡ Encoding fix
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# CSV file create
with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Quote", "Author"])

    # Data save
    for q, a in zip(quotes, authors):
        clean_quote = q.text.strip().replace("“", "").replace("”", "")
        clean_author = a.text.strip()

        writer.writerow([clean_quote, clean_author])

print("CSV file succesfully clean  ✅")