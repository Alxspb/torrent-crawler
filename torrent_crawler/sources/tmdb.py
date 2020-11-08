import requests

from torrent_crawler.content import ContentType, Content
from torrent_crawler.source import Source

_category_to_content_type = {
    'TV Shows': ContentType.Series,
    'Movies': ContentType.Film
}

_default_params = {
    'language': 'en-US'
}


class _Category:
    def __init__(self, content_type, count, url):
        self.content_type = content_type
        self.count = count
        self.url = url


class _Item:
    def __init__(self, title, url, date, content_type):
        self.title = title
        self.url = url
        self.date = date
        self.content_type = content_type


def _parse_category(view):
    name = view.xpath('a/text()')[0]
    category_type = _category_to_content_type.get(name)
    if category_type is None:
        return None
    return _Category(category_type, view.xpath('span/text()'), view.xpath('a/@href'))


def _parse_categories(view):
    categories = []
    elements = view.xpath('//*[@id="search_menu_scroller"]/ul/li')
    for element in elements:
        category = _parse_category(element)
        if category is not None:
            categories.append(category)
    return categories


def _parse_item(view, content_type: ContentType):
    title_element = view.xpath('.//div[@class="title"]')[0]
    title = title_element.xpath('a/h2/text()')
    url = title_element.xpath('a/@href')
    date = title_element.xpath('span/text()')
    return _Item(title, url, date, content_type=content_type)


def _parse_items(view, content_type: ContentType) -> list[_Item]:
    items = []
    elements = view.xpath('//*[@id="main"]/section/div/div/div[2]/section/div[1]/div/div[position() < last()]')
    for element in elements:
        item = _parse_item(element, content_type)
        if item is not None:
            items.append(item)
    return items


class Tmdb(Source):
    def __init__(self):
        self.params = _default_params

    def get_name(self):
        return 'tmdb'

    def get_url(self):
        return 'https://www.themoviedb.org'

    def search(self, session: requests.Session, query: str):
        view = self._search_category(session, query)
        categories = _parse_categories(view)
        items = _parse_items(view, categories[0].content_type)
        return list(map(lambda x: Content(x.title, x.content_type, x.date), items))

    def _search_category(self, session: requests.Session, query: str, category: str = None):
        url = "search"
        if category is not None:
            url += "/" + category
        return self._get_req(session, url, self._get_params('query', query))

    def _get_params(self, key: str, value):
        params = self.params.copy()
        params[key] = value
        return params
