from torrent_crawler.crawler import TorrentCrawler

if __name__ == "__main__":
    crawler = TorrentCrawler()
    results = crawler.search("movie")
    a = 0
