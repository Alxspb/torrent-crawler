from typing import List

import requests

from torrent_crawler.result import Result


class Tracker:
    def get_name(self) -> str:
        pass

    def get_link(self) -> str:
        pass

    def search(self, session: requests.Session, text: str) -> List[Result]:
        pass
