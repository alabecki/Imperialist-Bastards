# Minor Classes
from pprint import pprint
from random import*


class Province(object):
	def __init__ (self, name, _owner, _resource, _quality, _type, _culture):
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
		self.position = ""
		#self.fortress_level = 0
		#self.factories = set()
		#self.desirability =_desirability
		#self.abb = ""
		self.owner = _owner
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

class MarketItem(object):
	def __init__ (self, ID, kind, owner):
		self.ID = ID 
		self.kind = kind
		self.owner = owner

# Place each item to be sold in the queue for its kind 
# Price of a kind determined by the number of kind in queue
# When buying, AI will try first to buy from minors (probably just resources)
# It will decide who do buy from based on their relations with that player.
# For each player there is a list of players with whom he does not wish to trad

class FinishedGood(object):
	def __init__(self, kind, maker, owner):
		self.kind = kind
		self.maker = maker
		self.owner = owner
		self.sold = False

class CB(object):
	def __init__ (self, owner, opponent, action, province, time):
		self.owner = owner
		self.opponent = opponent
		self.action = action
		self.province = province
		self.time = time
# actions : annex (province), free (province)

class Factory(object):
	def __init__ (self, owner, kind):
		self.owner = owner
		self.kind = kind
		self.size = 1
		self.used = False

