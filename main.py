import requests
from bs4 import BeautifulSoup
import re


class OLXCarScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.car_pattern = re.compile(r'(car|seat cover|alto|swift|honda|maruti|kia|vehicle)', re.IGNORECASE)
        self.exclusion_keywords = ['flat', 'bhk']
        self.entries = []

    def fetch_page(self):
        return requests.get(self.url, headers=self.headers)

    def parse_items(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find_all('li')

    def filter_items(self, items):
        for item in items:
            text = item.get_text(strip=True)
            if self.car_pattern.search(text) and not any(keyword in text.lower() for keyword in self.exclusion_keywords):
                self.entries.append(text)

    def save_results(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for entry in self.entries:
                f.write(entry + "\n")

    def run(self, filename):
        response = self.fetch_page()
        if response.status_code == 200:
            items = self.parse_items(response.text)
            self.filter_items(items)
            if self.entries:
                self.save_results(filename)


if __name__ == "__main__":
    scraper = OLXCarScraper("https://www.olx.in/items/q-car-cover")
    scraper.run("cars_list.txt")
