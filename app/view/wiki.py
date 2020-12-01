# coding: utf-8
import requests
from pprint import pprint

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
        # pprint(geosearch_data)

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
        # print(response_wiki['query']['pages'][str(page_id)]['extract'])
        return response_wiki['query']['pages'][str(page_id)]['extract']

# faire class puis faire les test avec pytest
# Wiki.extract("48.858370", "2.294481")