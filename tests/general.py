import sys

from torrent_crawler.crawler import TorrentCrawler

if __name__ == "__main__":
    crawler = TorrentCrawler()
    results = crawler.search(sys.argv[1])
    for result in results:
        print(result)
