import requests
from bs4 import BeautifulSoup


def fetch_page(url: str) -> str:
    """
    Fetch HTML content from a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url, verify=False)
    return response.text


def extract_links(html: str) -> list[str]:
    """
    Extract all links from HTML content.

    Args:
        html (str): The HTML content of a page.

    Returns:
        list[str]: A list of URLs found in the HTML.
    """ 
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        links.append(href)

    return links


def crawl(start_url: str) -> list[str]:
    """
    Crawl a website starting from a given URL.

    Args:
        start_url (str): The starting URL for the crawl.

    Returns:
        list[str]: A list of all visited URLs.
    """
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