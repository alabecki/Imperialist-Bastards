

import random
import minor_classes
from technologies import technology_dict


stability_map = {
	-3.0: 0.67,
	-2.5: 0.75,
	-2.0: 0.82,
	-1.5: 0.88,
	-1.0: 0.93,
	-0.5: 0.97,
	0.0: 1.0,
	0.5: 1.02,
	1.0: 1.05,
	1.5: 1.09,
	2.0: 1.14,
	2.5: 1.20,
	3.0: 1.25
}

development_map = {
	0.0: 1.0,
	1.0: 1.75,
	2.0: 2.5
}


government_map = {
	"despotism": 		0.75,
	"absolute monarchy": 1.0,
	"oligarchy":  1.25
}


class Player(object):

	player_count = 0

	def __init__ (self, _name, _type, number):
		# Basic Attributes
		self.type = _type				# major, old_empire, old_minor
		self.name = _name	
		self.number = number
		self.stability = 0.0
		self.government = ""
		self.culture = ""
		self.accepted_cultures = set()
		self.religion = ""

		self.stability_mod = 0.0
		self.AP = 0.0

		self.provinces = {}
		self.borders = set()

		#General POP Attributes
		self.POP = 5.8
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
			"dyes": 0.0,
			"rubber": 0.0,
			"oil": 0.0
		}

		self.goods = {
			"parts": 0.0,
			"clothing": 0.0,
			"paper": 0.0,
			"cannons": 1.0,
			"furniture": 0.0,
			"chemicals": 0.0,
			"gear": 0.0,
			"radio": 0.0,
			"telephone": 0.0,
			"auto": 0.0,
			"frigates": 0.0,
			"iron_clad": 0.0,
			"battle_ship": 0.0,
			"fighter": 0.0,
			"tank": 0.0
		}

		self.goods_produced = {
			"parts": 0.0,
			"clothing": 0.0,
			"paper": 0.0,
			"cannons": 0.0,
			"furniture": 0.0,
			"chemicals": 0.0,
			"gear": 0.0,
			"radio": 0.0,
			"telephone": 0.0,
			"auto": 0.0,
			"frigates": 0.0,
			"iron_clad": 0.0,
			"battle_ship": 0.0,
			"fighter": 0.0,
			"tank": 0.0
		}

		#Industry
		self.new_development = 0.0
		self.number_developments = 0.0

		self.factories = {
			"ship_yard": 0,
			"parts": 0,
			"clothing": 0,
			"furniture": 0,
			"paper": 0,
			"cannons": 0,
			"chemicals": 0,
			"gear": 0,
			"radio": 0,
			"telephone": 0,
			"fighter": 0,
			"auto": 0,
			"tank": 0
		}

		#self.factories = set()
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

		#culture
		self.culture_points = 0.0
		self.culture_level = 0.0

			#Military
		self.military = {
			"irregulars": 0.0,
			"infantry": 0.0,
			"cavalry": 0.0,
			"artillery": 0.0,
			"frigates": 0.0,
			"iron_clad": 0.0,
			"fighter": 0.0,
			"tank": 0.0,
			"battle_ship": 0.0,
		}

		self.number_units = 4.0
		self.can_train = 1

		self.irregulars = {
			"attack": 0.5,
			"defend": 0.625,
			"manouver": 0.0,
			"ammo_use": 0.025,
			"oil_use": 0.0
			}

		self.infantry = {
			"attack": 1.0,
			"defend": 1.1,
			"manouver": 0.5,
			"ammo_use": 0.1,
			"oil_use": 0.0
			}

		self.artillery = {
			"attack": 1.75,
			"defend": 1.75,
			"manouver": 0.0,
			"ammo_use": 0.2,
			"oil_use": 0.0
			}

		self.cavalry = {
			"attack": 1.5,
			"defend": 1.0,
			"manouver": 2.0,
			"ammo_use": 0.1,
			"oil_use": 0.0
		}

		self.fighter = {
			"attack": 0.6,
			"defend": 1.0,
			"manouver": 6.0,
			"ammo_use": 0.1,
			"oil_use": 0.1
		}

		self.tank = {
			"attack": 3,
			"defend": 2,
			"manouver": 4.0,
			"ammo_use": 0.15,
			"oil_use": 0.1
		}
		
		self.frigates = {
			"attack": 2.0,
			"HP": 1.0,
			"ammo_use": 0.2,
			"oil_use": 0.0
		}

		self.iron_clad = {
			"attack": 2.8,
			"HP": 2,
			"ammo_use": 0.2,
			"oil_use": 0.0,
			}

		self.battle_ship = {
			"attack": 8,
			"HP": 4,
			"ammo_use": 0.6,
			"oil_use": 0.2
		}



		self.colonization = 0.0
		self.num_colonies = 0

		self.fortification = 1.0
		self.max_fortification = 1.1

		self.sprawl = False


	def collect_resources(self):
		print("%s collects resources: \n" % (self.name))
		stab_rounds = round(self.stability * 2) / 2
		for k, p in self.provinces.items():
			#if(self.provinces[i]["worked"] == True):
			if(p.worked == True):
				quality = p.quality
				dev = p.development_level
				c_mod = 1.0
				if p.culture != self.culture:
					if p.culture in self.accepted_cultures:
						c_mod = 0.9
					else:
						c_mod = 0.75
				if p.resource == "rubber" and "electricity" not in self.technologies:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.6
					self.resources["wood"] += gain
					continue 
				if p.resource == "oil" and p.development_level == 0:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.6
					self.resources["food"] += gain
					continue
				if p.powered == True:
					gain = development_map[dev] * stability_map[stab_rounds] * p.quality * c_mod
					print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain == gain * 5
					self.resources[p.resource] += gain
				else:
					if p.resource == "oil":
						continue
					gain = stability_map[stab_rounds] * p.quality * c_mod
					print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain == gain * 5
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
			self.stability -= 0.5
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["food"] = 0.0
			self.midGrowth = False
		else:
			self.resources["food"] -= mFood

		if(self.resources["coal"] < 0.2 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")

		for k, prov in self.provinces.items():
			if self.resources["coal"] >= 0.2 and prov.development_level == 1:
				self.resources["coal"]  -= 0.2
				self.provinces[k].powered = True
			elif self.resources["coal"] >= 0.2 and prov.development_level == 2:
				self.resources["coal"]  -= 0.4
				self.provinces[k].powered = True
		else:
			self.resources["coal"] -= self.number_developments * 0.2
			for k, prov in self.provinces.items():
				self.provinces[k].powered = True
		oil_need = 0
		if self.numMidPOP - 8 > 0:
			oil_need = self.numMidPOP - 8
		if self.resources["oil"] < oil_need:
			penality = self.resources["oil"] - oil_need
			self.stability += penality
			self.resources["oil"] = 0
		else:
			self.resources["oil"] -= oil_need


		#return stab_change

	def turn(self):
		stab_rounds = round(self.stability * 2) / 2
		self.collect_resources()
		self.collect_goods()
		self.payMaintenance()
		for p in self.provinces:
			if p.culture != self.culture and p.culture not in self.accepted_cultures:
				self.stability -= 0.05 

		self.culture_points+= (0.1 + self.midPOP["artists"]["number"] + self.midPOP["bureaucrats"]["number"]/5)
		print("Culture points gained: %s " % (0.1 + self.midPOP["artists"]["number"] + self.midPOP["bureaucrats"]["number"]/5))
		self.can_train = 1 + self.midPOP["officers"]["number"] * 4
		self.AP = int(self.proPOP) * self.production_modifier
		self.reputation += self.midPOP["artists"]["number"] * 0.1
		research_gain = 0.5 + (self.midPOP["researchers"]["number"] * stability_map[stab_rounds] * 2) + self.midPOP["managers"]["number"] * 0.4
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		diplo_gain = 0.15 + (self.midPOP["bureaucrats"]["number"] * self.reputation)
		self.diplo_action += diplo_gain
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  self.military["frigates"]/10 +  self.military["iron_clad"]/5 + self.military["battle_ship"]/2 \
		+ self.midPOP["bureaucrats"]["number"]/5
		self.colonization += col_gain
		print("Colonization point gain: %s" % (col_gain))
		self.POP_increased = 0
