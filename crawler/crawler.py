import requests
from bs4 import BeautifulSoup


def fetch_page(url: str) -> str:
    """Fetch HTML content from a URL."""
    response = requests.get(url, verify=False)
    return response.text


def extract_links(html: str) -> list[str]:
    """Extract all links from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        links.append(href)

    return links


def crawl(start_url: str):
    """Crawl a website starting from a URL."""
    visited = []
    to_visit = [start_url]

    while to_visit:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        visited.append(current_url)

        html = fetch_page(current_url)
        links = extract_links(html)

        for link in links:
            if link not in visited:
                to_visit.append(link) 
                return visited 