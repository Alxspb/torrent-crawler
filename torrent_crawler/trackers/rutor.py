import requests

from torrent_crawler.torrent import Torrent
from torrent_crawler.tracker import Tracker

_table_xpath = '//*[@id="index"]'
_pages_xpath = f'{_table_xpath}/b[1]/a/@href'


def _parse_search_page(view):
    torrents = []
    rows = view.xpath(f'{_table_xpath}//tr')
    for row in rows[1:]:
        columns = row.xpath('.//td')
        res = Torrent()
        res.magnet = columns[1].xpath('a[2]/@href')
        res.name = columns[1].xpath('a[3]/text()')
        res.size = columns[-2].text
        torrents.append(res)
    return torrents


def _get_search_pages(view):
    pages = view.xpath(_pages_xpath)
    return pages


class Rutor(Tracker):
    def get_name(self) -> str:
        return "rutor"

    def get_url(self) -> str:
        return "http://rutorc6mqdinc4cz.onion"

    def search(self, session: requests.Session, text: str, all_pages=False) -> list[Torrent]:
        view = self._get_req(session, f"search/0/0/000/2/{text}")  # '2' here for sorting seeders desc
        result = _parse_search_page(view)
        pages = _get_search_pages(view)
        if all_pages:
            for page_url in pages:
                view = self._get_req(session, page_url)
                result.extend(_parse_search_page(view))
        return result
