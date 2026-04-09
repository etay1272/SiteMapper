from crawler.crawler import crawl
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    url = os.getenv("START_URL")

    links = crawl(url)
    print(links)


if __name__ == "__main__":
    main()
    