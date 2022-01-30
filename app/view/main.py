# coding: utf-8
import random
from .sortword import Sortword
from .maps import Maps
from .wiki import Wiki


class Main:

    def __init__(self):

        self.listData = [
            "Bip Bip, j'ai une réponse pour toi",
            "Bip Bip, Données complête, la réponse est",
            "Bip Bip, j'ai une histoire à ce sujet",
            "Biiip, je connais très bien, voici la réponse"
            ]
        self.listNoData = [
            "Bip Bip, données incomplête bip!",
            "bip bip, error! errooorrr!",
            "Bip Bip, mémoire erronée"
            ]
        self.response = []
        self.noresponse = []
    
    def query(self, input):

        sort = Sortword()
        sort_input = sort.regword(input)
        if sort_input:
            location = Maps.geocode(" ".join(sort_input))
            if location is None:
                self.noresponse.append(input)
                self.noresponse.append(random.choice(self.listNoData))
                return self.noresponse
                pass
            else:
                self.response.append(input)
                self.response.append(random.choice(self.listData))
                self.response.append(location)
                lat = location["lat"]
                lng = location["lng"]
                self.response.append(Wiki.extract(lat, lng))
                return self.response
        else:
            self.noresponse.append(input)
            self.noresponse.append(random.choice(self.listNoData))
            return self.noresponse
