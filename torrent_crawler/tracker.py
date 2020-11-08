from typing import List

import requests

from torrent_crawler.torrent import Torrent
from torrent_crawler.site import Site


class Tracker(Site):
    def search(self, session: requests.Session, text: str) -> List[Torrent]:
        pass
