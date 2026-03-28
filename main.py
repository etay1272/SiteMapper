from crawler.crawler import fetch_page, extract_links

url = "https://example.com"

html = fetch_page(url)

links = extract_links(html)

print(links)  