# Minor Classes
from pprint import pprint
from random import*


class Province(object):
	def __init__ (self, name, _resource, _quality, _type, _culture):
		self.name = name
		self.ocean = True
		self.resource = _resource
		self.development_level = 0
		self.worked = False
		self.workers = 0
		self.powered = False
		self.quality = _quality
		self.type = _type  # civilized, old, uncivilized
		self.colony = False
		self.culture = _culture
		self.religion = ""
		self.AI_priority = 0
		self.borders = set()
		self.x = 0
		self.y = 0
		#self.fortress_level = 0
		#self.factories = set()
		#self.desirability =_desirability
		#self.abb = ""
		#self.ruler =  ""
		#self.occupier = ""
		#self.friendly_units_present = []
		#self.occupying_units_present = []

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
		self.harsh = False

class Relation(object):
	def __init__ (self, _relata):
		self.relata = _relata
		self.relationship = 0
		self.non_aggression = False
		self.defensive_alliance = False
		self.full_alliance = False
		self.war = False
