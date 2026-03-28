import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url, verify=False)
    return response.text

def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        links.append(href)

    return links