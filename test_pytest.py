# coding: utf-8
import pytest
from app.view.maps import Maps
from app.view.sortword import Sortword
from app.view.wiki import Wiki


def test_geocode():

	address = "paris"
	assert Maps.geocode(address) == {'lat': 48.85717, 'lng': 2.3414}


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
