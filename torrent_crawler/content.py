from enum import Enum


class ContentType(Enum):
    Film = 0
    Series = 1


class Content:
    def __init__(self, name, content_type, date):
        self.name = name
        self.content_type = content_type
        self.date = date

    def __str__(self) -> str:
        return f"name='{self.name}'; type={self.content_type}; date={self.date}"


