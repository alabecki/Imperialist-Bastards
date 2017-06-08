

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
		self.stability_mod = 1.0
		self.AP = 2.0

		self.provinces = {}
		self.borders = set()

		#General POP Attributes
		self.POP = 6.1
		self.POP_growth_mod = 1.0
		self.freePOP = 5.0
		self.proPOP = 0.0
		self.production_modifier = 1.0
		self.milPOP = 0.6

		self.midPOP = {
		"researchers": {"number": 0.0, "priority": 0.2},
		"officers": {"number": 0.0, "priority": 0.2},
		"bureaucrats": {"number": 0.0, "priority": 0.2},
		"artists": {"number": 0.0, "priority": 0.2},
		"managers": {"number": 0.0, "priority": 0.2}
		}

		self.midGrowth = True
		self.numMidPOP = 0.5
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
			"clothing": 1.0,
			"paper": 1.0,
			"cannons": 0.5,
			"furniture": 0.5,
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

		self.colonization = 0.5
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
		for k in goods_produced.keys():
			self.goods_produced[k] = 0
		#self.goods_produced = dict.fromkeys(self.goods_produced, 0)


	def calMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
		mClothing = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
		mFurniture = (self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2)
		mPaper = (self.numMidPOP * 0.4)
		mSpice = (self.numMidPOP * 0.3)
		mArms = (self.midPOP["officers"]["number"] * 0.3)
		return [mFood, mClothing, mFurniture, mPaper, mSpice, mArms]

	def payMaintenance(self):
		temp = self.calMaintenance()
		stab_change = 0
		if(self.resources["food"] < temp[0]):
			self.freePOP -= (self.resources["food"] - temp[0])
			self.stability -= 0.1
			stab_change -= 0.1
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["food"] = 0.0
			self.midGrowth = False
		else:
			self.resources["food"] -= temp[0]
		if(self.goods["clothing"] < temp[1]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.goods["clothing"] = 0.0
			self.midGrowth = False
		else:
			self.goods["clothing"] -= temp[1]
			self.new_development += temp[1] * 0.1
		if(self.goods["furniture"] < temp[2]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.midGrowth = False
			self.goods["furniture"] = 0.0
		else:
			self.goods["furniture"] -= temp[2]
			self.new_development += temp[2] * 0.1
		if(self.goods["paper"] < temp[3]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.goods["paper"] = 0.0
			self.midGrowth = False
		else:
			self.goods["paper"] -= temp[3]
			self.new_development += temp[3] * 0.1
		if(self.resources["spice"] < temp[4]):
			stability -= 0.075
			stab_change -= 0.075
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["spice"] = 0.0
			self.midGrowth = False
		else:
			self.resources["spice"] -= temp[4]
			self.new_development += temp[4] * 0.1
		if(self.goods["cannons"] < temp[5]):
			temp = self.numMidPOP["officers"]["number"] * 0.9
			self.numMidPOP["officers"]["number"] -= temp
			self.numMidPOP -= temp
			self.freePOP += temp
		else:
			self.goods["cannons"] -= temp[5]
			self.new_development += temp[5] * 0.1
		if(self.resources["coal"] < 0.25 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")
			while(self.resources["coal"] >= 0.3 ):
				for k, prov in self.provinces.items():
					if(prov.development_level == 1):
						self.resources["coal"] -= 0.25
						self.provinces[prov].powered = True
					elif(prov.development_level == 2):
						self.resources["coal"] -= 0.5
						self.provinces(prov).powered = True
		else:
			self.resources["coal"] -= self.number_developments * 0.25
			for k, prov in self.provinces.items():
				prov.powered = True
		#return stab_change


	def popChange(self):
		if(self.resources["food"] > 0.5):
			change =  self.POP * 0.02
			if(self.stability > 0):
				stab_rounds = round(self.stability * 2) / 2
				change += (self.POP * 0.02) * (stability_map[stab_rounds] * self.POP_growth_mod)
			mChemicals = (self.numMidPOP * 0.15)
			if(self.goods["chemicals"] >= mChemicals):
				self.goods["chemicals"] -= mChemicals
				change += 0.1 * self.numMidPOP
			self.freePOP += change
			self.numLowerPOP += change
			self.POP += change
			print("Population changed by %s " % (change))

	def popMidChange(self):
		if(self.stability < -2):
			return
		if(self.midGrowth == False):
			return
		else:
			stab_rounds = round(self.stability * 2) / 2
			change = 0.1 + ((self.midPOP["bureaucrats"]["number"]/3) + (self.midPOP["researchers"]["number"]/5))* stability_map[stab_rounds]
			self.numMidPOP += change
			self.POP += change
			print("Middle Class population change: %s \n" % (change))
			for key, value in self.midPOP.items():
				value["number"] += change * value["priority"]
				print("%s increased by %s" % (key, change * value["priority"]))




	def turn(self):
		self.collect_resources()
		self.collect_goods()
		self.payMaintenance()
		stab_change1 = (self.numLowerPOP * 0.01) + (self.numMidPOP * 0.02)
		print("Stab change 1 " + str(stab_change1))
		self.stability -= (stab_change1)
		print("Stab modifier: " + str(self.stability_mod))
		stab_change2 = ((self.midPOP["bureaucrats"]["number"]/6) + (self.midPOP["artists"]["number"]/3)) * self.stability_mod
		print("Stab change 2 " + str(stab_change2))
		stab_rounds = round(self.stability * 2) / 2
		self.stability += stab_change2
		if self.stability < -3.0:
			self.stability = -3.0
		if self.stability > 3.0:
			self.stability = 3.0
		#total_stab_change = stab_change2 - (stab_change1 + stab_change0)
		#print("Stability changes by: %s" % (total_stab_change))
		self.popChange()
		self.popMidChange()
		self.AP = int(self.proPOP) * self.production_modifier
		research_gain = ((0.2 + (self.midPOP["researchers"]["number"] * 1.0) + (self.midPOP["managers"]["number"] * 0.25))) * stability_map[stab_rounds]
		research_gain = research_gain * self.techModifier
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		diplo_gain = 0.2 + (self.midPOP["bureaucrats"]["number"]) * self.reputation
		self.diplo_action += diplo_gain
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  ((self.military["frigates"] + self.military["iron_clad"])/5 + self.midPOP["bureaucrats"]["number"]/2)
		self.colonization += col_gain
		print("Colonization point gain: %s" % (col_gain))
