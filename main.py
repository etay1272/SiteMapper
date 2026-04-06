from crawler.crawler import crawl
import os


def main():
    url = os.getenv("START_URL")

    links = crawl(url)
    print(links)


if __name__ == "__main__":
    main() 
    