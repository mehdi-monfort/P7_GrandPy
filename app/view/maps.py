# coding: utf-8
import requests
from .settings import API_KEY, GEOCODE_BASE_URL


class Maps:

    def __init__(self):
        self.key = API_KEY
    """get coordinates using here api"""
    def geocode(self, address):
        """obtaining coordinates: longitude, latitude"""
        params = {
            "q": address,
            "apikey": self.key,
            }
        url = f"{GEOCODE_BASE_URL}"
        try:
            result = requests.get(url=url, params=params)
            response_map = result.json()
            position = response_map['items'][0]['position']
            return position
        except IndexError as err:
            print(err)
