# Minor Classes
from pprint import pprint
from random import*


class Province(object):
	def __init__ (self, name, _resource, _quality, _type, player):
		self.name = name
		self.resource = _resource
		self.development_level = 0
		self.worked = False
		self.powered = False
		self.quality = _quality
		self.type = _type  # core or colony
		self.culture = player
		self.AI_priority = 0
		#self.desirability =_desirability

class Uncivilized_minor(object):
	def __init__(self, _name):
		self.name = _name
		self.provinces = {}  #always 2
		self.number_irregulars = randint(2, 3)
		provinces = {}
		self.irregulars = {
			"attack": 0.5,
			"defense": 0.65,
			"manouver": 0.75,
			"ammo_use": 0.025
			}

class Railroad(object):
	def __init__(self, powered, level):
		self.powered = False
		self.level = 0


class Relation(object):
	def __init__ (self, _relata):
		self.relata = _relata
		self.relationship = 0
		self.non_aggression = False
		self.defensive_alliance = False
		self.full_alliance = False
		self.war = False
