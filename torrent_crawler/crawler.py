import torpy.http.requests

from torrent_crawler.trackers.rutor import Rutor


class TorrentCrawler:
    def search(self, text: str):
        with torpy.http.requests.tor_requests_session() as session:
            result = []
            for tracker in self.trackers:
                result.extend(tracker.search(session, text))
            return result

    trackers = [Rutor()]
