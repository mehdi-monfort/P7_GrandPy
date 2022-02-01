# coding: utf-8
import requests


class Wiki:

    def extract(latitude, longitude):

        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{latitude}|{longitude}"
        }

        response = requests.get(url, params=params)
        geosearch_data = response.json()
        page_id = geosearch_data['query']['geosearch'][0]['pageid']

        params = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "explaintext": 1,
            "exsentences": 1,
            "exintro": True,
            "pageids": page_id
        }

        result = requests.get(url, params=params)
        result.raise_for_status()

        response_wiki = result.json()
        return response_wiki['query']['pages'][str(page_id)]['extract']
