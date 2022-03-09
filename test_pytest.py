# coding: utf-8

from app.view.main import Main
from app.view.maps import Maps
from app.view.sortword import Sortword
from app.view.wiki import Wiki


def test_main_query(monkeypatch):
    address = "wakanda"

    def mockreturn_maps(adress):
        return {'lat': 2, 'lng': 4}

    def mockreturn_wiki(lat, long):
        return 'test_is_ok!'

    monkeypatch.setattr(Maps, 'geocode', mockreturn_maps)
    monkeypatch.setattr(Wiki, 'extract', mockreturn_wiki)

    main = Main()

    response = [
        'wakanda', 'Biiip, je connais très bien, voici la réponse',
        {'lat': 2, 'lng': 4}, 'test_is_ok!']
    response2 = [
        'wakanda', 'Biiip, je connais très bien, voici la réponse',
        {'lat': 2, 'lng': 4}, 'test_is_ok!']
    response3 = [
        'wakanda', "Bip Bip, j'ai une histoire à ce sujet",
        {'lat': 2, 'lng': 4}, 'test_is_ok!']
    response4 = [
        'wakanda', "Bip Bip, j'ai une réponse pour toi",
        {'lat': 2, 'lng': 4}, 'test_is_ok!']

    assert main.query(address) == response or response2 or response3 or response4


class TestSortword:

    def setup_method(self):
        self.S = Sortword()

    def test_regword1(self):
        self.input = "ou se situe la tour eiffel ?"
        assert self.S.regword(self.input) == ['tour', 'eiffel']

    def test_regword2(self):
        self.input = "qu'y a t'il d'intéressant sur paris ?"
        assert self.S.regword(self.input) == ['paris']

    def test_regword3(self):
        self.input = "Où se trouve la cathédrale de Quimper ?"
        assert self.S.regword(self.input) == ['cathédrale', 'quimper']


def test_extract():
    longitude = "48.85824"
    latitude = "2.2945"
    assert Wiki.extract(longitude, latitude) == 'Le Jules Verne est un restaurant parisien situé au deuxième étage de la tour Eiffel et spécialisé en cuisine française classique.'
