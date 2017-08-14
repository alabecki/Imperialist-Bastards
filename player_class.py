

import random
import minor_classes
from technologies import technology_dict
from globe import*
from queue import*


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
		self.type = _type				# major, old_empire, old_minor, civ_minor
		self.name = _name	
		self.number = number
		self.stability = 0.0
		self.government = ""
		self.culture = ""
		self.accepted_cultures = set()
		self.religion = ""
		self.capital = ""

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
			"oil": 0.0,
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
			"tank": 0.0,
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

		self.shipyard = 0

		self.sprawl = False


	def collect_resources(self, globe):
		print("%s collects resources: \n" % (self.name))
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
						c_mod = 0.9
					else:
						c_mod = 0.75
				if p.resource == "rubber" and "electricity" not in self.technologies:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.6
					res_dict["food"] += gain
					#self.resources["wood"] += gain
					continue 
				if p.resource == "oil" and p.development_level == 0:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.6
					res_dict["food"] += gain
					#self.resources["food"] += gain
					continue
				if p.powered == True:
					gain = development_map[dev] * stability_map[stab_rounds] * p.quality * c_mod
					print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain == gain * 5
					res_dict[p.resource] += gain
					#self.resources[p.resource] += gain
				else:
					if p.resource == "oil":
						continue
					gain = stability_map[stab_rounds] * p.quality * c_mod
					print("%s gains %s %s" % (self.name, gain, p.resource))
					if p.resource == "gold":
						gain == gain * 5
					#self.resources[p.resource] += gain
					print(p.resource)
					res_dict[p.resource] += gain
		for r, res in res_dict.items():
			
			print(r)
			self.resources[r] += res
			#if globe.resources[r]:
			#	globe.resources[r].append([self.name, res])
			#else:
			#	globe.resources[r] = [(self.name, res)]


	def collect_goods(self):
		print("%s collects: " % (self.name))
		for k, p in self.goods_produced.items():
			print("%s: %s " % (k, p))
			self.goods[k] += p
		for k in self.goods_produced.keys():
			self.goods_produced[k] = 0
		#self.goods_produced = dict.fromkeys(self.goods_produced, 0)


	def payMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
		if(self.resources["food"] < mFood ):
			self.freePOP -= (self.resources["food"] - mFood)
			self.stability -= 0.5
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
		if self.numMidPOP - 6 > 0:
			oil_need = self.numMidPOP - 6
		if self.resources["oil"] < oil_need:
			penality = self.resources["oil"] - oil_need
			self.stability += penality
			if self.stability < -3:
				self.stability = -3
			self.resources["oil"] = 0
		else:
			self.resources["oil"] -= oil_need


		#return stab_change

	def turn(self, globe):
		stab_rounds = round(self.stability * 2) / 2
		self.collect_resources(globe)
		self.collect_goods()
		self.payMaintenance()
		for p in self.provinces.values():
			if p.culture != self.culture and p.culture not in self.accepted_cultures:
				self.stability -= 0.05 
		if self.stability < -3.0:
			self.stability = -3.0
		cps = 0.1 + self.midPOP["artists"]["number"] + self.midPOP["bureaucrats"]["number"]/5
		self.culture_points+= cps
		##for g in globe.culture:
			#print(g)
		#globe.culture.append([self.name, cps])
		print("Culture points gained: %s " % (0.2 + self.midPOP["artists"]["number"] * 2 + self.midPOP["bureaucrats"]["number"]/2))
		self.can_train = 1 + self.midPOP["officers"]["number"] * 5
		self.AP = int(self.proPOP) * self.production_modifier
		self.reputation += self.midPOP["artists"]["number"] * 0.1
		research_gain = 0.25 + (self.midPOP["researchers"]["number"] * stability_map[stab_rounds]) * 2 + \
		(self.midPOP["managers"]["number"] * stability_map[stab_rounds] * 0.4)
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		#globe.research.append([self.name, research_gain])
		diplo_gain = 0.15 + (self.midPOP["bureaucrats"]["number"] * self.reputation)
		self.diplo_action += diplo_gain
		#globe.diplomacy.append([self.name, diplo_gain])
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  self.military["frigates"]/10 +  self.military["iron_clad"]/5 + self.military["battle_ship"]/2 \
		+ self.midPOP["bureaucrats"]["number"]/5
		self.colonization += col_gain
		#globe.colonization.append([self.name, col_gain])
		print("Colonization point gain: %s" % (col_gain))
		self.POP_increased = 0
		


	def b_borders_a(self, p2):
		bBa = set()
		p1c = self()
		for v1 in self.provinces.values():
			for v2 in p2.provinces.values():
				if abs(v1.x - v2.x) <= 1 and abs(v1.y - v2.y) <= 1:
					bBa.add(v2)
		return bBa

	def check_for_border(self, p2):
		self_core = self.core_provinces()
		#print("Core Provs Self:")
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
		core = set()
		consider = Queue(100)
		if self.capital == "":
			return core
		else:
			first = self.provinces[self.capital]
			consider.put(first)
			while consider.qsize() >= 1:
				thing = consider.get()
				for p in self.provinces.values():
					if p != thing:
						if abs(thing.x - p.x) <= 1 and abs(thing.y - p.y) <= 1:
							#print("Yes")
							if p not in core and p != thing:
								consider.put(p)
					
				if thing not in core:
					core.add(thing)
			return core

	def check_for_ground_invasion(self, prov, provinces):
		core = self.core_provinces()
		for c in core: 
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
		
		return strength


	def calculate_base_defense_strength(self):
		strength = 0.0
		strength += self.military["irregulars"] * self.irregulars["defend"]
		strength += self.military["infantry"] * self.infantry["defend"]
		strength += self.military["cavalry"] * self.cavalry["defend"]
		strength += self.military["artillery"] * self.artillery["defend"]
		strength += self.military["tank"] * self.tank["defend"]
		strength += self.military["fighter"] * self.fighter["defend"]
		strength = strength * self.fortification
		return strength


	def ai_naval_projection(self):
		forces = self.ai_transport_units()
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


	def ai_transport_units(self):
		transport_limit = (self.military["frigates"] + self.military["iron_clad"] + self.military["battle_ship"]) * 2 
		forces = {
			"infantry": 0,
			"cavalry": 0,
			"artillery": 0,
			"tank": 0,
			"fighter": 0
		}
		number = 0
		for v in range(int(transport_limit)):
			tries = 0
			while tries < 32:
				_type = random.choice(["infantry", "cavalry", "artillery", "tank", "fighter"])
				if self.military[_type] - forces[_type] >= 1:
					forces[_type] += 1
					break
				tries += 1
		return forces


	def calculate_naval_strength(self):
		count = 0
		
		count += self.military["frigates"] * self.frigates["attack"]
		count +=  self.military["iron_clad"] * self.iron_clad["attack"]
		count +=  self.military["battle_ship"] * self.battle_ship["attack"]
		return count
