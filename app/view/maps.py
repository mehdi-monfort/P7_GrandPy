# coding: utf-8
import os
import requests
from .settings import API_KEY, GEOCODE_BASE_URL


class Maps:
    """obtaining coordinates"""
    def geocode(address):
        """obtaining coordinates: longitude, latitude"""
        params = {
            "address": address,
            "key": API_KEY,
            "region": 'FR',
            }
        url = f"{GEOCODE_BASE_URL}"
        try:
            result = requests.get(url, params=params)
            response_map = result.json()
            return response_map['results'][0]['geometry']['location']
        except IndexError as err:
            print(err)
