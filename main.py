from crawler.crawler import crawl
import os 
import time
from dotenv import load_dotenv


def main():
    load_dotenv()

    url = os.getenv("START_URL") 
    start = time.time()

    links = crawl(url) 
    end = time.time()
    print(links) 
    print("Pages scanned:", len(links), "(limit:", MAX_PAGES, ")")
    print("Time taken:", round(end - start, 2), "seconds")


if __name__ == "__main__":
    main()
    