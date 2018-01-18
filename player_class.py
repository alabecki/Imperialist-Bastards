

from random import*
from minor_classes import*
from technologies import technology_dict
from globe import*
from queue import*
from copy import deepcopy



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
	"oligarchy":  1.1
}

military_doctrines = ["Discipline", "Recon", "ManouverI", "ManouverII", "Entrenchment", "CombinedArms", \
"SeaI", "SeaII", "AcePilots", "FirePower"]


manufacture = {
	"parts": {"iron": 0.67, "coal": 0.33},
	"cannons": {"iron": 0.67, "coal": 0.33},
	"paper": {"wood": 1.0},
	"clothing": {"cotton": 0.9, "dyes": 0.3},
	"furniture": {"wood": 0.67, "cotton": 0.33},
	"chemicals": {"coal": 1},
	"gear": {"rubber": 0.6, "iron": 0.2, "coal": 0.2},
	"radio": {"gear": 0.85, "wood": 0.15},
	"telephone": {"gear": 0.85, "wood": 0.15},
	"fighter": {"wood": 1, "gear": 1, "parts": 1, "cannons": 1.0},   # 2.5 
	"auto": {"rubber": 0.5, "gear": 1.0, "parts": 1.0, "iron": 0.5},		#2
	"tank": {"iron": 1.5, "cannons": 1.5, "rubber": 0.5, "gear": 1, "parts": 1},  #4 
	#"frigates": {"cannons": 1.0, "wood": 1.0, "cotton": 1.0},
	#"iron_clad": {"cannons": 1.0, "iron": 1.0, "parts": 1.0},
	#"battle_ship": {"cannons": 3.0, "iron": 3.0, "parts": 1.0, "gear": 1.0 }  #8 
		}

craft = {
	"parts": {"iron": 0.67, "coal": 0.33},
	"cannons": {"iron": 0.67, "coal": 0.33},
	"paper": {"wood": 1.0},
	"clothing": {"cotton": 0.9, "dyes": 0.3},
	"furniture": {"wood": 0.67, "cotton": 0.33},
			}


class Player(object):

	#player_count = 0
	def __init__(self, name, kind, number, *args, **kwargs):
	#def __init__ (self, _name, _type, number):
		# Basic Attributes
		self.colour = "white"
		self.type = kind				# major, old_empire, old_minor, civ_minor
		self.name = name	
		self.number = number
		self.stability = 0.0
		self.government = ""
		self.culture = ""
		self.accepted_cultures = set()
		self.religion = ""
		self.capital = set()
		self.VP = 0.0
		self.defeated = False
		self.development_level = 0


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

		self.developments = {
			"research": 0,
			"military": 0,
			"government": 0,
			"culture": 0,
			"management": 0
		}

		'''self.midPOP = {
		"researchers": {"number": 0.0, "priority": 0.2},
		"officers": {"number": 0.0, "priority": 0.2},
		"bureaucrats": {"number": 0.0, "priority": 0.2},
		"artists": {"number": 0.0, "priority": 0.2},
		"managers": {"number": 0.0, "priority": 0.2}
		}'''

		self.midGrowth = True
		self.numMidPOP = 0.0
		self.numLowerPOP = 5.0

		#Good and Resources
		self.resources = {
			"gold": 10.0,
			"food": 1.0,
			"iron": 0.0,
			"wood": 0.0,
			"coal": 0.0,
			"cotton": 0.0,
			"spice": 0.0,
			"dyes": 0.0,
			"rubber": 0.0,
			"oil": 0.0,
			"/": 0.0,
			"//": 0.0,
			#"///": 0.0
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
			"tank": 0.0,
			"auto": 0.0,
			"fighter": 0.0,
		}


		self.supply = {
			"gold": 0.0,
			"food": 0.0,
			"iron": 0.0,
			"wood": 0.0,
			"coal": 0.0,
			"cotton": 0.0,
			"spice": 0.0,
			"dyes": 0.0,
			"rubber": 0.0,
			"oil": 0.0,
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
			"fighter": 0.0,
			"tank": 0.0,
			"/": 0.0,
			"//": 0.0,
			"///": 0.0
		}

		self.embargo = set()

		self.sphere = set()

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
			#"frigates": 0.0,
			#"iron_clad": 0.0,
			#"battle_ship": 0.0,
			"fighter": 0.0,
			"tank": 0.0
		}

		#Industry
		self.new_development = 0.0
		self.number_developments = 0

		self.factories = {
			"tank": {"number":0, "used": False},
			"fighter": {"number":0, "used": False},
			"auto": {"number":0, "used": False},
			"parts": {"number":0, "used": False},
			"clothing": {"number":0, "used": False},
			"cannons": {"number":0, "used": False},
			"paper": {"number":0, "used": False},
			"furniture": {"number":0, "used": False},
			"chemicals": {"number":0, "used": False},
			"gear": {"number":0, "used": False},
			"telephone": {"number":0, "used": False},
			"radio": {"number":0, "used": False},
		}

		self.crafted = False 

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
		self.CB = {}
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
			"manouver": 0.1,
			"recon": 0.0,
			"ammo_use": 0.02,
			"oil_use": 0.0
			}

		self.infantry = {
			"attack": 1.0,
			"defend": 1.2,
			"manouver": 0.5,
			"recon": 0.2,
			"ammo_use": 0.05,
			"oil_use": 0.0,
			"weight:": 1
			}

		self.artillery = {
			"attack": 1.0,
			"defend": 1.8,
			"manouver": 0.0,
			"recon": 0.0,
			"ammo_use": 0.1,
			"oil_use": 0.0,
			"weight": 2
			}

		self.cavalry = {
			"attack": 1.5,
			"defend": 1.0,
			"manouver": 1.0,
			"recon": 1.0,
			"ammo_use": 0.05,
			"oil_use": 0.0,
			"weight": 2
		}

		self.fighter = {
			"attack": 1.0,
			"defend": 1.5,
			"manouver": 1.0,
			"recon": 2.0,
			"ammo_use": 0.75,
			"oil_use": 0.1,
			"weight": 3
		}

		self.tank = {
			"attack": 3.0,
			"defend": 2.0,
			"manouver": 1.0,
			"recon": 0.2,
			"ammo_use": 0.75,
			"oil_use": 0.1,
			"weight": 3
		}
		
		self.frigates = {
			"attack": 1.0,
			"HP": 1.0,
			"ammo_use": 0.1,
			"oil_use": 0.0,
			"capacity": 2
		}

		self.iron_clad = {
			"attack": 1.5,
			"HP": 2.0,
			"ammo_use": 0.1,
			"oil_use": 0.0,
			"capacity": 3
			}

		self.battle_ship = {
			"attack": 4.0,
			"HP": 4.0,
			"ammo_use": 0.3,
			"oil_use": 0.2,
			"capacity": 6
		}

		self.military_produced = {
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


		self.org_factor = 1

		self.doctrines = set()

		self.claims = set()

		self.objectives = set()

		self.just_attacked = -1

		self.colonization = 0.0
		self.num_colonies = 0

		self.fortification = 1.0
		self.max_fortification = 1.1

		self.shipyard = 0

		self.sprawl = False

		self.ideas = set()


	def determine_middle_class_need(self):
		requirement = ["paper"]
		if self.development_level > 0:
			requirement.append("spice")
		if self.development_level > 1:
			requirement.append("furniture")
		if self.development_level > 2:
			requirement.append("paper")
		if self.development_level > 3:
			requirement.append("clothing")
		if self.development_level > 4:
			requirement.append("spice")
		if self.development_level > 5:
			requirement.append("furniture")
		if self.development_level > 6:
			requirement.append("paper")
		if self.development_level > 7:
			requirement.append("clothing")
		if self.development_level > 9:
			requirement.append("telephone")
			requirement.append("telephone")
			requirement.append("telephone")
			requirement.remove("paper")
			requirement.remove("clothing")
		if self.development_level > 10:
			requirement.remove("telephone")
			requirement.append("paper")
			requirement.append("clothing")
			requirement.remove("furniture")
		if self.development_level > 11:
			requirement.append("furniture")
		if self.development_level > 12:
			requirement.append("radio")
			requirement.append("radio")
			requirement.append("radio")
			requirement.remove("paper")
			requirement.remove("clothing")
		if self.development_level > 13:
			requirement.remove("radio")
			requirement.append("paper")
			requirement.append("clothing")
			requirement.remove("furniture")
		if self.development_level > 14:
			requirement.append("furniture")
		if self.development_level > 15:
			requirement.append("auto")
			requirement.append("auto")
			requirement.append("auto")
			requirement.remove("paper")
			requirement.remove("clothing")
			requirement.remove("furniture")
		if self.development_level > 16:
			requirement.append("paper")
		if self.development_level > 17:
			requirement.append("furniture")
			requirement.append("clothing")
		return requirement

	#	requirement = ["paper"]
	#	if self.numMidPOP >= 1 and self.numMidPOP < 2:
	#		requirement = ["paper", "furniture"]
	#	if self.numMidPOP >= 2 and self.numMidPOP < 2.5:
	#		requirement = ["paper", "clothing", "furniture"]
	#	if self.numMidPOP >= 2.5 and self.numMidPOP < 3:
	#		requirement = ["paper", "clothing", "furniture"]
	#	if self.numMidPOP >= 3 and self.numMidPOP < 3.5:
	#		requirement = ["paper", "clothing", "furniture", "chemicals"]
	#	if self.numMidPOP >= 3.5 and self.numMidPOP < 4:
	#		requirement = ["paper", "clothing", "furniture", "telephone", "telephone"]
	#	if self.numMidPOP >= 4 and self.numMidPOP < 4.5:
	#		requirement = ["paper", "clothing", "furniture", "telephone", "radio", "radio"]
	#	if self.numMidPOP > 4.5:
	#		requirement = ["paper", "clothing", "furniture", "auto", "radio", "telephone", "auto"]
		#print("Mid class requirments:")
		#for r in requirement:
		#	print(r)
	#	return requirement


	def check_mid_requirement(self, requirement):
		check_list = {
			"paper": 0,
			"spice": 0,
			"furniture": 0,
			"clothing": 0,
			"telephone": 0,
			"radio": 0,
			"auto": 0
		}
		for i in requirement:
			check_list[i] += 1
		for k, v in check_list.items():
			if k == "spice":
				if self.resources["spice"] < v:
					return False
			else:
				if self.goods[k] < v:
					return False 

		#if self.resources["spice"] < 1 and self.numMidPOP < 4.5:
		#	return False
		#for r in requirement:
		#	if self.goods[r] < 1: 
		#		return False
		#if self.numMidPOP >= 3 and self.goods["paper"] < 2:
		#	return False
		if self.freePOP < 0.2 and self.proPOP < 2:
			return False
		return True

	def check_development(self):
		requirement = self.determine_middle_class_need()
		if self.check_mid_requirement(requirement) == True and self.freePOP >= 0.2:
			return True
		else:
			return False

			
	def collect_resources(self, market):
		stab_rounds = round(self.stability * 2) / 2
		res_dict = {
			"gold": 0,
			"food": 0,
			"iron": 0,
			"wood": 0,
			"cotton": 0,
			"coal": 0,
			"dyes": 0,
			"spice": 0,
			"rubber": 0,
			"oil": 0,
		}

		for k, p in self.provinces.items():
			#if(self.provinces[i]["worked"] == True):
			if(p.worked == True):
				quality = p.quality
				dev = p.development_level
				c_mod = 1.0
				if p.culture != self.culture:
					if p.culture in self.accepted_cultures:
						c_mod = 0.85
					else:
						c_mod = 0.70
				if p.resource == "rubber" and "chemistry" not in self.technologies:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.75
					res_dict["wood"] += gain
					#self.resources["wood"] += gain
					continue 
				if p.resource == "oil" and p.development_level == 0:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.75
					res_dict["food"] += gain
					#self.resources["food"] += gain
					continue
				if p.powered == True:
					gain = development_map[dev] * stability_map[stab_rounds] * p.quality * c_mod
					#print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain = gain * 5
					res_dict[p.resource] += gain
					#self.resources[p.resource] += gain
				else:
					if p.resource == "oil":
						continue
					gain = stability_map[stab_rounds] * p.quality * c_mod
					#print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain = gain * 5
					#self.resources[p.resource] += gain
					#print(p.resource)
					res_dict[p.resource] += gain
		for r, res in res_dict.items():
			#print(r, res)
			self.resources[r] += res
			
			if r == "food":
				market.food_production[self.name] = res
			if r == "iron":
				market.iron_production[self.name] = res
			if r == "wood":
				market.wood_production[self.name] = res 
			if r == "cotton":
				market.cotton_production[self.name] = res 
			if r == "coal":
				market.coal_production[self.name] = res
			if r == "gold":
				market.gold_production[self.name] = res 
			if r == "spice":
				market.spice_production[self.name] = res 
			if r == "rubber":
				market.rubber_production[self.name] = res
			if r == "oil":
				market.oil_production[self.name] = res

		return res_dict


	def collect_goods(self):

		for k, p in self.goods_produced.items():
			print("Has produced %d %s" % (p, k))
			self.goods[k] += p
		
		for k, v in self.military_produced.items():
			self.military[k] += v

		for k in self.military_produced.keys():
			self.military_produced[k] = 0	
		#self.goods_produced = dict.fromkeys(self.goods_produced, 0)


	def payMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
		if(self.resources["food"] < mFood ):
			self.freePOP += (self.resources["food"] - mFood)
			self.stability -= 0.5
			if self.freePOP < 0:
				self.freePOP = 0
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["food"] = 0.0
			self.midGrowth = False
		else:
			self.resources["food"] -= mFood
			self.midGrowth = True


		if(self.resources["coal"] < 0.1 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")

			for k, prov in self.provinces.items():
				if self.resources["coal"] >= 0.1 and prov.development_level == 1:
					self.resources["coal"]  -= 0.1
					self.provinces[k].powered = True
				elif self.resources["coal"] >= 0.2 and prov.development_level == 2:
					self.resources["coal"]  -= 0.2
					self.provinces[k].powered = True
		else:
			self.resources["coal"] -= self.number_developments * 0.1
			for k, prov in self.provinces.items():
				self.provinces[k].powered = True
		oil_need = 0
		if self.development_level > 14:
			oil_need = (self.development_level - 15) * 0.2
		if self.resources["oil"] < oil_need:
			penality = self.resources["oil"] - oil_need
			self.stability += penality
			if self.stability < -3:
				self.stability = -3
			self.resources["oil"] = 0
			self.midGrowth = False

		else:
			self.resources["oil"] -= oil_need


		#return stab_change


	def calculate_access_to_goods(self, market):
		#for i in self.embargo:
			#print("Embargo by: %s" %  (i))
		for k, v in self.supply.items():
			self.supply[k] = 0
		for k, v in self.supply.items():
			#print("Market Supply: %s" % (len(market.market[k])))
			for i in market.market[k]:
				#print(i.owner)
				if i.owner in self.embargo:
			#		print("Blocked by %s" % (i))
					continue
				self.supply[k] += 1
			#print("Your supply: %s" % (self.supply[k]))

	def turn(self, market):
		self.crafted = False
		for fact in self.factories.keys():
			self.factories[fact]["used"] = False
		self.POP_increased = 0
		if self.stability < -3: 
			self.stability = - 3
		if self.stability > 3:
			self.stability = 3
		stab_rounds = round(self.stability * 2) / 2
		self.collect_resources(market)
		self.collect_goods()
		self.payMaintenance()
		if market.turn >= 20:
			for p in self.provinces.values():
				if p.culture != self.culture and p.type == "civilized":
					if p.culture not in self.accepted_cultures:
						self.stability -= 0.05
					else:
						self.stability -= 0.025 

		if self.stability < -3.0:
			self.stability = -3.0
		culture_gain = 0.2 + self.developments["culture"]/3
		#culture_gain = 0.2 + self.midPOP["artists"]["number"]
		self.culture_points+= culture_gain
		##for g in globe.culture:
			#print(g)
		#globe.culture.append([self.name, cps])
		print("Culture points gained: %s " % (culture_gain))
		#self.can_train = 1 + self.midPOP["officers"]["number"] * 5
		self.can_train = 1 + self.developments["military"]
		self.AP = int(self.proPOP) * self.production_modifier
		#research_gain = (0.25 + (self.midPOP["researchers"]["number"] * stability_map[stab_rounds]) * 2 + \
		#(self.midPOP["managers"]["number"] * stability_map[stab_rounds] * 0.33)) * government_map[self.government]
		research_gain = 0.24 + ((self.developments["research"] + self.developments["management"]/6) * \
		government_map[self.government] * stability_map[stab_rounds])
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		#globe.research.append([self.name, research_gain])
		#diplo_gain = 0.2 + (self.midPOP["bureaucrats"]["number"] * self.reputation * 2)
		diplo_gain = 0.2 + (self.developments["government"] * self.reputation * 0.75)
		self.diplo_action += diplo_gain
		#globe.diplomacy.append([self.name, diplo_gain])
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  self.military["frigates"]/10 +  self.military["iron_clad"]/6 + self.military["battle_ship"]/3 \
		+  self.developments["government"]/6
		self.colonization += col_gain
		#globe.colonization.append([self.name, col_gain])
		print("Colonization point gain: %s" % (col_gain))
		self.POP_increased = 0
		self.just_attacked -= 1

		for v in self.factories.values():
			v["used"] = False

		cb_keys = []
		for k, v in self.CB.items():
			cb_keys.append(v.opponent)
		for cb in cb_keys:
			if cb in self.CB.keys():
				self.CB[cb].time -= 1
				if self.CB[cb].time < 0:
					del self.CB[cb]
		return [research_gain, culture_gain, col_gain, diplo_gain]
	

	def b_borders_a(self, p2):
		bBa = set()
		p1c = self()
		for v1 in self.provinces.values():
			for v2 in p2.provinces.values():
				if abs(v1.x - v2.x) <= 1 and abs(v1.y - v2.y) <= 1:
					bBa.add(v2)
		return bBa

	def check_for_border(self, p2, players):
		self_core = self.core_provinces()
		#print("Core Provs %s:" % (self.name))
		#for p in self_core:
		#	print(p.name)

		if len(p2.provinces.keys()) < 1:
			return False
		other_core = p2.core_provinces()
		#print("Core Provs " + p2.name)
		#for o in other_core:
		#	print (o.name)
		for c1 in self_core:
			for c2 in other_core:
				#print(abs(c1.x - c2.x), abs(c1.y - c2.y))
				if abs(c1.x - c2.x) <= 1 and abs(c1.y - c2.y) <= 1:
					#print("True")
					return True
		#print("false")
		return False

	
	def core_provinces(self):
		#print("Current Provinces")
		#for k, v in self.provinces.items():
		#	print(k, v)
		core = set()
		consider = Queue(100)
		if len(self.capital) == 0:
			#print("No capital?")
			return core
		else:
			for c in self.capital:
			#	print(self.name)
			#	print("Capital: %s" %(c))
				first = self.provinces[c]
				consider.put(first)
				while consider.qsize() >= 1:
					thing = consider.get()
					if type(thing) != Province:
						continue
					for p in self.provinces.values():
						if p != thing:
							if abs(thing.x - p.x) <= 1 and abs(thing.y - p.y) <= 1:
								#print("Yes")
								if p not in core and p != thing:
									consider.put(p)
						
					if thing not in core:
						core.add(thing)
		#print("%s cores:" % (self.name))
		#for c in core:
		#	print(c.name)
		return core

	def check_for_ground_invasion(self, prov, provinces):
		core = self.core_provinces()
		prov = provinces[prov]
		for c in core:
			#c = provinces[c] 
			if abs(c.x - prov.x) <= 1 and abs(c.y - prov.y) <= 1:
				return True
		return False


	def calculate_base_attack_strength(self):
		strength = 0.0
		strength += self.military["infantry"] * self.infantry["attack"]
		strength += self.military["cavalry"] * self.cavalry["attack"]
		strength += self.military["artillery"] * self.artillery["attack"]
		strength += self.military["tank"] * self.tank["attack"]
		strength += self.military["fighter"] * self.fighter["attack"]
		#strength = strength * (1 + (self.midPOP["officers"]["number"]/2))
		
		return strength


	def calculate_amphib_strength(self, forces):
		strength = 0
		for k, v in forces.items():
			if k == "infantry":
				strength += forces[k] * self.infantry["attack"]
			if k == "cavalry":
				strength += forces[k] * self.cavalry["attack"]
			if k == "artillery":
				strength += forces[k] * self.artillery["attack"]
			if k == "tank":
				strength += forces[k] * self.tank["attack"]
			if k == "fighter":
				strength += forces[k] * self.fighter["attack"]
		return strength


	def calculate_base_defense_strength(self):
		strength = 0.0
		strength += self.military["irregulars"] * self.irregulars["defend"]
		strength += self.military["infantry"] * self.infantry["defend"]
		strength += self.military["cavalry"] * self.cavalry["defend"]
		strength += self.military["artillery"] * self.artillery["defend"]
		strength += self.military["tank"] * self.tank["defend"]
		strength += self.military["fighter"] * self.fighter["defend"]
		#strength = strength * (1 + (self.midPOP["officers"]["number"]/2))
		strength = strength * self.fortification
		return strength


	def ai_naval_projection(self, target):
		forces = self.ai_transport_units(target)
		strength = 0
		for k, v in forces.items():
			att = 0
			if k == "infantry":
				strength += forces[k] * self.infantry["attack"]
			if k == "cavalry":
				strength += forces[k] * self.cavalry["attack"]
			if k == "artillery":
				strength += forces[k] * self.artillery["attack"]
			if k == "tank":
				strength += forces[k] * self.tank["attack"]
			if k == "fighter":
				strength += forces[k] * self.fighter["attack"]
		return strength

	def num_army_units(self):
		res = (self.military["irregulars"] + self.military["infantry"] + self.military["cavalry"] + self.military["artillery"] + self.military["tank"] + self.military["fighter"])
		return res


	def ai_transport_units(self, target):
		tries = 0
		target_strength = target.calculate_base_defense_strength()
		#print("Target strength: %s" % (target_strength))
		self_strength = 0
		number_units = self.num_army_units()
		transport_limit = ((self.military["frigates"] + self.military["iron_clad"]) * 2 + self.military["battle_ship"] * 3) 
		forces = {
			"infantry": 0,
			"cavalry": 0,
			"artillery": 0,
			"tank": 0,
			"fighter": 0
		}
		number = 0
		if transport_limit == 0:
			return forces

		while (self_strength < (target_strength * 2) and number_units >= 1 and tries < 160 and number <= transport_limit):
			pick = choice(["infantry", "artillery", "cavalry", "fighter", "tank"])
			if (self.military[pick] - forces[pick]) >= 1:
			#	print("Adds %s " % (pick))
				forces[pick] += 1
				if pick == "infantry":
					self_strength += self.infantry["attack"]
				elif pick == "cavalry":
					self_strength += self.cavalry["attack"]
				elif pick == "artillery":
					self_strength += self.artillery["attack"]
				elif pick == "tank":
					self_strength += self.tank["attack"]
				elif pick == "fighter":
					self_strength += self.fighter["attack"]
				tries += 1
				number_units -= 1
				#print("Tries: %s" % (tries))
				number += 1
			else:
				tries += 1

		return forces


	def check_for_sea_invasion(self):
		res = False
		for prov in self.provinces.values():
			if prov.ocean == True:
				res = True
		return res


	def calculate_number_of_units(self):
		count = 0
		count += self.military["infantry"] + self.military["cavalry"] + self.military["artillery"] + \
		 self.military["irregulars"] + self.military["tank"] + self.military["fighter"]
		return count


	def amount_can_manif(self, _type):
		if self.stability < -3.0:
			self.stability = -3.0
		if self.stability > 3.0:
			self.stability = 3.0
		if self.AP < 1:
			return 0
		if self.factories[_type]["number"] == 0:
			if _type in craft.keys():
				for i in craft[_type]:
					if i in self.resources.keys():
						if(craft[_type][i] > self.resources[i]):
							return 0
				return 1
			else: 
				return 0
			
		else:
			stab_rounds = round(self.stability* 2) / 2
			stab_mod = stability_map[stab_rounds]
			max_amount = self.factories[_type]["number"] * stab_mod * self.factory_throughput
			material_mod = 1 - (self.developments["management"]/10)
			#max_amount = max_amount/(material_mod + 0.0001)
			material_max = 1000
			for i in manufacture[_type]:
				if i in self.resources.keys():
					temp = int(self.resources[i] / (manufacture[_type][i] * material_mod))
					if temp < material_max:
						material_max = temp
				if i in self.goods.keys():
					temp = int(self.goods[i] / (manufacture[_type][i] * material_mod))
					if temp < material_max:
						material_max = temp
		amount = min([material_max, max_amount])
		print("Can currently produce %d %s" % (amount, _type))
		return amount


	def factory_optons(self):
		options = []
		if(self.new_development < 1):
			return options
		if("high_pressure_steam_engine" not in self.technologies):
			return options
		if(self.AP < 1):
			return options
		if(self.resources["iron"] < 1.0):
			return options
		elif(self.goods["parts"] < 1.0):
			return options

		if self.factories["parts"]["number"] == 0:
			options.append("parts")
		if self.factories["parts"]["number"] == 1 and "bessemer_process" in self.technologies: 
			options.append("parts")
		if self.factories["clothing"]["number"] == 0:
			options.append("clothing")
		if self.factories["clothing"]["number"] == 1 and "power_loom" in self.technologies:
			options.append("clothing")
		if self.factories["furniture"]["number"] == 0:
			options.append("furniture")
		if self.factories["furniture"]["number"] == 1 and "electricity" in self.technologies:
			options.append("furniture")
		if self.factories["paper"]["number"] == 0:
			options.append("paper")
		if self.factories["paper"]["number"] == 1 and "pulping" in self.technologies:
			options.append("paper")
		if self.factories["cannons"]["number"] == 0:
			options.append("cannons")
		if self.factories["cannons"]["number"] == 1 and "bessemer_process" in self.technologies:
			options.append("cannons")
		if self.factories["chemicals"]["number"] == 0 and "chemistry" in self.technologies:
			options.append("chemicals")
		if self.factories["chemicals"]["number"] == 1 and "synthetic_dyes" in self.technologies:
			options.append("chemicals")
		if self.factories["gear"]["number"] < 2 and "electricity" in self.technologies:
			options.append("gear")
		if self.factories["radio"]["number"] < 2 and "radio" in self.technologies:
			options.append("radio")
		if self.factories["telephone"]["number"] < 2 and "telephone" in self.technologies:
			options.append("telephone")
		if self.factories["fighter"]["number"] < 2 and "flight" in self.technologies:
			options.append("fighter")
		if self.factories["auto"]["number"] < 2 and "automobile" in self.technologies:
			options.append("auto")
		if self.factories["tank"]["number"] < 2 and "mobile_warfare" in self.technologies:
			options.append("tank")
		return options


	def build_factory(self, _type, market):
		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories[_type]["number"] += 1
		market.global_factories[_type] += 1
		self.stability -= 0.3
		self.new_development -= 1
		return


	def manifacture_good(self, _type, amount):
		
		self.AP -= 1
		if self.factories[_type]["number"] == 0:
			for i in craft[_type]:
				self.resources[i] -= craft[_type][i]
			self.goods_produced[_type] += amount
			return

		else:
			material_mod = 1 - (self.developments["management"]/10)
			for i in manufacture[_type]:
				if i in self.resources.keys():
					self.resources[i] -= manufacture[_type][i] * amount * material_mod
				else:
					self.goods[i] -= manufacture[_type][i] * amount * material_mod
			self.goods_produced[_type] += amount
			
			self.factories[_type]["used"] = True
			return

	def pro_POP_add(self):
		self.proPOP += 1
		self.freePOP -= 1


	def pro_POP_subtract(self):
		self.proPOP -= 1
		self.freePOP += 1

	def check_if_prov_can_be_dev(self, prov):
		if self.provinces[prov].development_level >= 2:
			return
		max_dev = 0
		if (self.provinces[prov].resource == "food"):
			max_dev = 0
			if ("steel_plows" in self.technologies):
				max_dev = 1
			if ("mechanical_reaper" in self.technologies):
				max_dev = 2
		elif (self.provinces[prov].resource == "iron" or self.provinces[prov].resource == "coal"):
			max_dev = 0
			if ("square_timbering" in self.technologies):
				max_dev = 1
			if ("dynamite" in self.technologies):
				max_dev = 2
		elif (self.provinces[prov].resource == "cotton"):
			max_dev = 0
			if ("cotton_gin" in self.technologies):
				max_dev = 1
			if ("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif (self.provinces[prov].resource == "wood"):
			max_dev = 0
			if ("saw_mill" in self.technologies):
				max_dev = 1
			if ("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif (self.provinces[prov].resource == "spice"):
			max_dev = 0
			if ("steel_plows" in self.technologies):
				max_dev = 1
		elif (self.provinces[prov].resource == "gold"):
			max_dev = 0
			if ("dynamite" in self.technologies):
				max_dev = 1
		elif (self.provinces[prov].resource == "dyes"):
			max_dev = 0
			if ("compound_steam_engine" in self.technologies):
				max_dev = 1
		elif (self.provinces[prov].resource == "oil"):
			max_dev = 0
			if ("oil_drilling" in self.technologies):
				max_dev = 1
		elif (self.provinces[prov].resource == "rubber"):
			max_dev = 0
			if ("chemistry" in self.technologies):
				max_dev = 1
		if self.provinces[prov].development_level >= max_dev:
			return False
		else:
			return True


	def get_fact_level(self):
		value = 0
		for k, v in self.factories.items():
			value += v["number"]
		return value

	def everyone_but_self(self, players):
		all_others = []
		for k in players.keys():
			if self.name != k:
				all_others.append(k)
		return all_others


	def choose_doctrine(self, choice):	
		self.doctrines.add(choice)
		if choice == "AcePilots":
			self.fighter["manouver"] += 0.5
			self.fighter["attack"] += 0.1
			self.fighter["defend"] += 0.1
			self.fighter["recon"] += 0.1

		if choice == "Discipline":
			self.infantry["attack"] += 0.15
			self.infantry["defend"] += 0.15
			self.artillery["attack"] += 0.1
			self.artillery["defend"] += 0.1
			self.tank["attack"] += 0.2
			self.tank["defend"] += 0.2
			self.cavalry["attack"] += 0.1
			self.cavalry["defend"] += 0.1

		if choice == "Recon":
			self.infantry["recon"] += 0.15
			self.cavalry["recon"] += 0.3
			self.fighter["recon"] += 0.45
			self.tank["recon"] += 0.2

		if choice == "ManouverI":
			self.infantry["manouver"] += 0.2
			self.cavalry["manouver"] += 0.3
			self.tank["manouver"] += 0.3

		if choice == "ManouverII":
			self.infantry["manouver"] += 0.3
			self.cavalry["manouver"] += 0.4
			self.tank["manouver"] += 0.4

		if choice == "Entrenchment":
			self.infantry["defend"] += 0.3
			self.artillery["defend"] += 0.3
			self.tank["defend"] += 0.1

		if choice == "CombinedArms":
			self.fighter["attack"] += 0.1
			self.fighter["recon"] += 0.2
			self.tank["manouver"] += 0.15
			self.tank["attack"] += 0.1
			self.artillery["attack"] += 0.1
			self.infantry["attack"] += 0.1

		if choice == "FirePower":
			self.artillery["attack"] += 0.25
			self.artillery["attack"] += 0.25
			self.tank["attack"] += 0.1
			self.tank["defend"] += 0.1
			self.fighter["attack"] += 0.1

		if choice == "SeaI":
			self.frigates["attack"] += 0.2
			self.iron_clad["attack"] += 0.3
			self.battle_ship["attack"] += 0.8

		if choice == "SeaII":
			self.frigates["attack"] += 0.3
			self.iron_clad["attack"] += 0.4
			self.battle_ship["attack"] += 1.0


	def recon(self):
		recon = 0
		recon += self.military["infantry"] * self.infantry["recon"]
		recon += self.military["cavalry"] * self.cavalry["recon"]
		recon += self.military["tank"] * self.tank["recon"]
		recon += self.military["fighter"] * self.fighter["recon"]
		return recon

	def ammo_penalty(self, ammo_needed):
		if ammo_needed > self.goods["cannons"]:
			AmmoPenalty = self.goods["cannons"]/(ammo_needed + 0.001)
			AmmoPenalty = AmmoPenalty + (1 - AmmoPenalty)/2
			self.goods["cannons"] = 0
		else:
			self.goods["cannons"] -= ammo_needed
			AmmoPenalty = 1
		return AmmoPenalty


	def oil_penalty(self, oil_needed):
		if oil_needed > self.resources["oil"]:
			OilPenalty = self.resources["oil"]/(oil_needed + 0.001)
			self.resources["oil"] = 0
		else:
			self.resources["oil"] -= oil_needed
			OilPenalty = 1
		return OilPenalty


	def calculate_number_of_ships(self):
		count = 0
		count += self.military["frigates"] + self.military["iron_clad"] + self.military["battle_ship"]
		return count

	def calculate_naval_strength(self):
		count = 0
		count += self.military["frigates"] * self.frigates["attack"]
		count +=  self.military["iron_clad"] * self.iron_clad["attack"] * 1.6
		count +=  self.military["battle_ship"] * self.battle_ship["attack"] * 3.2
		return count


	def calculate_ammo_needed_navy(self):
		amount = 0
		amount += self.military["frigates"] * self.frigates["ammo_use"]
		amount += self.military["iron_clad"] * self.iron_clad["ammo_use"]
		amount += self.military["battle_ship"] * self.battle_ship["ammo_use"]
		return amount

	def calculate_oil_needed_navy(self):
		amount = self.military["battle_ship"] * self.battle_ship["oil_use"]
		#print("Oil Needed for %s: %s" % (self.name, amount))
		return amount


	def calculate_land_ammo_needed(self):
		ammo_needed = 0.0
		ammo_needed += self.military["infantry"] * self.infantry["ammo_use"]
		ammo_needed += self.military["cavalry"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["artillery"] * self.artillery["ammo_use"]
		ammo_needed += self.military["tank"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["fighter"] * self.artillery["ammo_use"]
		return ammo_needed

	def calculate_oil_needed(self):
		oil_needed = 0.0
		oil_needed += self.military["tank"] * self.tank["oil_use"]
		oil_needed += self.military["fighter"] * self.fighter["oil_use"]
		#print("Oil Needed for %s: %s" % (self.name, oil_needed))
		return oil_needed

	def calculate_amphib_oil(self, current_makeup):
		oil = 0
		for k, v in current_makeup.items():
			if k == "tank":
				oil += current_makeup[k] * self.tank["oil_use"]
			if k == "fighter":
				oil += current_makeup[k] * self.fighter["oil_use"]
		return oil


	def calculate_amphib_ammo(self, current_makeup):
		ammo = 0
		for k, v in current_makeup.items():
			if k == "infantry":
				ammo += current_makeup[k] * self.infantry["ammo_use"]
			if k == "cavalry":
				ammo += current_makeup[k] * self.cavalry["ammo_use"]
			if k == "artillery":
				ammo += current_makeup[k] * self.artillery["ammo_use"]
			if k == "tank":
				ammo += current_makeup[k] * self.tank["ammo_use"]
			if k == "fighter":
				ammo += current_makeup[k] * self.fighter["ammo_use"]
		return ammo


	def calculate_transport_limit(self):
		transport_limit = 0
		transport_limit += self.military["frigates"] * 2
		transport_limit += (self.military["iron_clad"] * 3)
		transport_limit += (self.military["battle_ship"] * 6)
		return transport_limit 

	def calculate_army_weight(self, forces):
		weight = 0
		weight += forces["infantry"]
		weight += (forces["cavalry"] * 2)
		weight += (forces["artillery"] * 2)
		weight += (forces["tank"] * 3)
		weight += (forces["fighter"] * 3)
		print("weight %s" % weight)
		return weight

