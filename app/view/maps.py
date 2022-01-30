# coding: utf-8
import os
import requests
from .settings import API_KEY, GEOCODE_BASE_URL


class Maps:
    """obtaining coordinates"""
    def geocode(address):
        """obtaining coordinates: longitude, latitude"""
        params = {
            "q": address,
            "apikey": API_KEY,
            }
        url = f"{GEOCODE_BASE_URL}"
        try:
            result = requests.get(url=url, params=params)
            response_map = result.json()
            position = response_map['items'][0]['position']
            print(address)
            print(response_map)
            return position
        
        except IndexError as err:
            print(err)
            