import requests

from torrent_crawler.content import Content
from torrent_crawler.site import Site


class Source(Site):
    def search(self, session: requests.Session, query: str) -> list[Content]:
        pass
