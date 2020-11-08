import torpy.http.requests

from torrent_crawler.sources.tmdb import Tmdb
from torrent_crawler.trackers.rutor import Rutor


class TorrentCrawler:
    def search(self, text: str):
        with torpy.http.requests.tor_requests_session() as session:
            result = []
            for source in self.sources:
                result.extend(source.search(session, text))
            return result

    sources = [Tmdb()]
    trackers = [Rutor()]
