import lxml.html
import requests


class Site:
    def get_name(self):
        pass

    def get_url(self):
        pass

    def _get_req(self, session: requests.Session, relative_url: str, params=None):
        response = session.get(f"{self.get_url()}/{relative_url}", stream=True, params=params)
        response.raw.decode_content = True
        return lxml.html.parse(response.raw)
