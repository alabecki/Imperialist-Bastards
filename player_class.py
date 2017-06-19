

import random
import minor_classes
from technologies import technology_dict


stability_map = {
	-3.0: 0.8,
	-2.5: 0.85,
	-2.0: 0.875,
	-1.5: 0.9,
	-1.0: 0.9525,
	-0.5: 0.975,
	0.0: 1.0,
	0.5: 1.025,
	1.0: 1.05,
	1.5: 1.075,
	2.0: 1.1,
	2.5: 1.175,
	3.0: 1.2
}

development_map = {
	0.0: 1.0,
	1.0: 1.75,
	2.0: 2.5
}

m_priority_map = {
	"1": 0.3,
	"2": 0.25,
	"3": 0.2,
	"4": 0.15,
	"5": 0.1
}

class Player(object):

	player_count = 0

	def __init__ (self, _name, _type, number):
		# Basic Attributes
		self.type = _type
		self.name = _name
		self.number = number
		self.stability = 0.0
		self.stability_mod = 0.0
		self.AP = 0.0

		self.provinces = {}
		self.borders = set()

		#General POP Attributes
		self.POP = 5.8
		self.POP_growth_mod = 1.0
		self.freePOP = 5.0
		self.proPOP = 0.0
		self.production_modifier = 1.0
		self.milPOP = 0.8
		self.POP_increased = 0

		self.midPOP = {
		"researchers": {"number": 0.0, "priority": 0.2},
		"officers": {"number": 0.0, "priority": 0.2},
		"bureaucrats": {"number": 0.0, "priority": 0.2},
		"artists": {"number": 0.0, "priority": 0.2},
		"managers": {"number": 0.0, "priority": 0.2}
		}

		self.midGrowth = True
		self.numMidPOP = 0.0
		self.numLowerPOP = 5.0

		#Good and Resources
		self.resources = {
			"gold": 10.0,
			"food": 0.0,
			"iron": 0.0,
			"wood": 0.0,
			"coal": 0.0,
			"cotton": 0.0,
			"spice": 1.0,
			"dyes": 0.0
		}

		self.goods = {
			"parts": 0.0,
			"clothing": 0.0,
			"paper": 0.0,
			"cannons": 0.0,
			"furniture": 0.0,
			"chemicals": 0.0
		}

		self.goods_produced = {
			"parts": 0.0,
			"clothing": 0.0,
			"paper": 0.0,
			"cannons": 0.0,
			"furniture": 0.0,
			"chemicals": 0.0
		}

		#Industry
		self.new_development = 0.0
		self.number_developments = 0.0
		self.factories = set()
		self.factory_throughput = 4.0
		self.material_mod = 1.0

		#Technology
		self.technologies = set()
		self.research = 0
		self.techModifier = 1

		self.chemicals = set()
		#self.tech_added = 0.0

        #diplomacy
		self.reputation = 1.0
		self.diplo_action = 0.0
		self.CB = set()

			#Military

		self.military = {
			"irregulars": 0.0,
			"infantry": 2.0,
			"cavalry": 1.0,
			"artillery": 0.0,
			"frigates": 1.0,
			"iron_clad": 0.0
		}

		self.number_units = 4.0

		self.irregulars = {
			"attack": 0.5,
			"defend": 0.625,
			"manouver": 0.75,
			"ammo_use": 0.025
			}

		self.infantry = {
			"attack": 1.0,
			"defend": 1.25,
			"manouver": 1.0,
			"ammo_use": 0.1
			}

		self.artillery = {
			"attack": 1.75,
			"defend": 1.75,
			"manouver": 0.5,
			"ammo_use": 0.2
			}

		self.cavalry = {
			"attack": 1.5,
			"defend": 1.0,
			"manouver": 2.0,
			"ammo_use": 0.1
		}

		self.frigates = {
			"attack": 2.0,
			"ammo_use": 0.2
		}

		self.iron_clad = {
			"attack": 4.0,
			"ammo_use": 0.2
			}

		self.colonization = 0.0
		self.num_colonies = 0

		self.fortification = 1.0
		self.max_fortification = 1.1
		self.steam_ship_yard = False
		self.steam_ship_port = False

		Player.player_count += 1



	def collect_resources(self):
		print("%s collects resources: \n" % (self.name))
		stab_rounds = round(self.stability * 2) / 2
		for k, p in self.provinces.items():
			#if(self.provinces[i]["worked"] == True):
			if(p.worked == True):
				quality = p.quality
				dev = p.development_level
				if p.resource == "gold":
					if p.powered == True:
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality * 5
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain
					else:
						gain = stability_map[stab_rounds] * p.quality * 5
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain
				else:
					if p.powered == True:
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain
					else:
						gain = stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain

	def collect_goods(self):
		print("%s collects: " % (self.name))
		for k, p in self.goods_produced.items():
			print("%s: %s " % (k, p))
			self.goods[k] += p
		for k in self.goods_produced.keys():
			self.goods_produced[k] = 0
		#self.goods_produced = dict.fromkeys(self.goods_produced, 0)


	def payMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.4) + self.military["cavalry"] * 0.1
		if(self.resources["food"] < mFood ):
			self.freePOP -= (self.resources["food"] - mFood)
			self.stability -= 0.25
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["food"] = 0.0
			self.midGrowth = False
		else:
			self.resources["food"] -= mFood

		if(self.resources["coal"] < 0.25 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")
			while(self.resources["coal"]  >= 0.3 ):
				for k, prov in self.provinces.items():
					if(prov.development_level == 1):
						self.resources["coal"]  -= 0.25
						self.provinces[k].powered = True
					elif(prov.development_level == 2):
						self.resources["coal"]  -= 0.5
						self.provinces[k].powered = True
		else:
			self.resources["coal"] -= self.number_developments * 0.25
			for k, prov in self.provinces.items():
				self.provinces[k].powered = True

		#return stab_change

	def turn(self):
		stab_rounds = round(self.stability * 2) / 2
		self.collect_resources()
		self.collect_goods()
		self.payMaintenance()
		self.stability += self.midPOP["artists"]["number"] * 0.25
		if self.stability > 3.0:
			self.stability = 3.0
		self.AP = int(self.proPOP) * self.production_modifier
		research_gain = 0.3 + self.midPOP["researchers"]["number"] * 0.6 * stability_map[stab_rounds] * self.techModifier
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		diplo_gain = 0.15 + ((self.midPOP["bureaucrats"]["number"]) * self.reputation)/2
		self.diplo_action += diplo_gain
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  ((self.military["frigates"] + self.military["iron_clad"])/6 + self.midPOP["bureaucrats"]["number"]/4)
		self.colonization += col_gain
		print("Colonization point gain: %s" % (col_gain))
		self.POP_increased = 0
