from torrent_crawler.content import Content


class Series(Content):
    def __init__(self, name, content_type, date, seasons: int):
        super().__init__(name, content_type, date)

        self.seasons = seasons
