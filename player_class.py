

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

military_doctrines = ["Infantry_Offense", "Infantry_Defense", "Mobile_Offense", "Mobile_Defense", "Artillery_Offense",
"Artillery_Defense", "Fighter_Offense", "Fighter_Defense", "Sea_Doctrine1", "Sea_Doctrine2", "Enhanced_Mobility"]


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
		self.VP = 0.0
		self.defeated = False

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
			"food": 1.0,
			"iron": 0.0,
			"wood": 0.0,
			"coal": 0.0,
			"cotton": 0.0,
			"spice": 0.0,
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
		self.number_developments = 0.0

		self.factories = {
			"tank": 0,
			"fighter": 0,
			"auto": 0,
			"parts": 0,
			"clothing": 0,
			"cannons": 0,
			"paper": 0,
			"furniture": 0,
			"chemicals": 0,
			"gear": 0,
			"telephone": 0,
			"radio": 0,
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
			"attack": 0.8,
			"defend": 1.2,
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
			"attack": 7,
			"HP": 4,
			"ammo_use": 0.6,
			"oil_use": 0.2
		}

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


	def determine_middle_class_need(self):
		requirement = ["paper"]
		if self.numMidPOP >= 1 and self.numMidPOP < 2:
			requirement = ["paper", "furniture"]
		if self.numMidPOP >= 2 and self.numMidPOP < 2.5:
			requirement = ["paper", "clothing", "furniture"]
		if self.numMidPOP >= 2.5 and self.numMidPOP < 3:
			requirement = ["paper", "clothing", "furniture"]
		if self.numMidPOP >= 3 and self.numMidPOP < 3.5:
			requirement = ["paper", "clothing", "furniture", "chemicals"]
		if self.numMidPOP >= 3.5 and self.numMidPOP < 4:
			requirement = ["paper", "clothing", "furniture", "radio", "radio"]
		if self.numMidPOP >= 4 and self.numMidPOP < 4.5:
			requirement = ["paper", "clothing", "furniture", "telephone", "radio", "telephone"]
		if self.numMidPOP > 4.5:
			requirement = ["paper", "clothing", "furniture", "auto", "radio", "telephone", "auto"]
		#print("Mid class requirments:")
		#for r in requirement:
		#	print(r)
		return requirement


	def check_mid_requirement(self, requirement):
		if self.resources["spice"] < 1 and self.numMidPOP < 4.5:
			return False
		for r in requirement:
			if self.goods[r] < 1: 
				return False
		#if self.numMidPOP >= 3 and self.goods["paper"] < 2:
		#	return False
		if self.freePOP < 0.3 and self.proPOP < 2:
			return False
		return True


	def collect_resources(self, market):
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
						c_mod = 0.85
					else:
						c_mod = 0.70
				if p.resource == "rubber" and "chemistry" not in self.technologies:
					gain = stability_map[stab_rounds] * p.quality * c_mod * 0.75
					res_dict["food"] += gain
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
					print(p.resource)
					res_dict[p.resource] += gain
		for r, res in res_dict.items():
			
			print(r, res)
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
		if self.numMidPOP - 4.4 > 0:
			oil_need = (self.numMidPOP - 4.4)/2
		if self.resources["oil"] < oil_need:
			penality = self.resources["oil"] - oil_need
			self.stability += penality
			if self.stability < -3:
				self.stability = -3
			self.resources["oil"] = 0
		else:
			self.resources["oil"] -= oil_need


		#return stab_change


	def calculate_access_to_goods(self, market):
		for k, v in self.supply.items():
			self.supply[k] = 0
		for k, v in self.supply.items():
			for i in market.market[k]:
				if i.owner in self.embargo:
					continue
				else:
					self.supply[k] += 1

	def turn(self, market):
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
		culture_gain = 0.2 + self.midPOP["artists"]["number"]
		self.culture_points+= culture_gain
		##for g in globe.culture:
			#print(g)
		#globe.culture.append([self.name, cps])
		print("Culture points gained: %s " % (culture_gain))
		self.can_train = 1 + self.midPOP["officers"]["number"] * 5
		self.AP = int(self.proPOP) * self.production_modifier
		research_gain = (0.25 + (self.midPOP["researchers"]["number"] * stability_map[stab_rounds]) * 2 + \
		(self.midPOP["managers"]["number"] * stability_map[stab_rounds] * 0.33)) * government_map[self.government]
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		#globe.research.append([self.name, research_gain])
		diplo_gain = 0.2 + (self.midPOP["bureaucrats"]["number"] * self.reputation * 2)
		self.diplo_action += diplo_gain
		#globe.diplomacy.append([self.name, diplo_gain])
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  self.military["frigates"]/10 +  self.military["iron_clad"]/6 + self.military["battle_ship"]/3 \
		+ self.midPOP["bureaucrats"]["number"]/4
		self.colonization += col_gain
		#globe.colonization.append([self.name, col_gain])
		print("Colonization point gain: %s" % (col_gain))
		self.POP_increased = 0
		self.just_attacked -= 1
		


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
		#print("%s cores:" % (self.name))
		#for c in core:
		#	print(c.name)
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
		#strength = strength * (1 + (self.midPOP["officers"]["number"]/2))
		
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
		if self.sprawl == True:
			strength = strength * (self.fortification + 1)
		else:
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
				_type = choice(["infantry", "cavalry", "artillery", "tank", "fighter"])
				if self.military[_type] - forces[_type] >= 1:
					forces[_type] += 1
					break
				tries += 1
		return forces


	def calculate_naval_strength(self):
		count = 0
		
		count += self.military["frigates"] * self.frigates["attack"]
		count +=  self.military["iron_clad"] * self.iron_clad["attack"] * 2
		count +=  self.military["battle_ship"] * self.battle_ship["attack"] * 4
		return count


	def war_after_math(self, target, players, relations, prov):


		if self.culture == prov.culture:
			self.reputation += 0.15
			self.stability += 0.2
	
		#if target in self.CB:
		#	self.CB.remove(target)
		if target.type == "old_minor":
			self.reputation -= 0.1
			self.stability += 0.1
		if target.type == "old_empire":
			self.reputation -= 0.15
			self.stability += 0.1
		if (target.type == "minor" or target.type == "major") and self.military["tank"] == 0:
			self.reputation -= 0.3
			for pl, play in players.items():
				if play.type == "major" and self.name != pl:
					relations[frozenset([self.name, pl])].relationship -= 0.2

		for p, pl in players.items():
			if len(set([self.name, p])) == 1 or len(set([target.name, p])) == 1:
				continue
			if relations[frozenset([self.name, p])].relationship < -1.5:
				relations[frozenset([self.name, p])].relationship -= 0.1
			if relations[frozenset([target.name, p])].relationship >= 0 and relations[frozenset([self.name, p])].relationship < 1.5:
				relations[frozenset([self.name, p])].relationship -= 0.1
			if relations[frozenset([target.name, p])].relationship >= 1:
				relations[frozenset([self.name, p])].relationship -= 0.15 
			if relations[frozenset([target.name, p])].relationship >= 2:
				relations[frozenset([self.name, p])].relationship -= 0.15
			if relations[frozenset([target.name, p])].relationship >= 2.7:
				if pl.type == "major" or pl.type == "minor":
					new = CB(p, self.name, "annex", prov.name, 5)
					pl.CB.add(new)

			if pl.type == "AI":
				if pl.rival_target != []:
					if target == pl.rival_target[0]: 
						relations[frozenset([self.name, p])].relationship -= 0.15
				if target in pl.allied_target:
					relations[frozenset([self.name, p])].relationship -= 0.2



	def check_for_sea_invasion(self):
		res = False
		for prov in self.provinces.values():
			if prov.ocean == True:
				res = True
		return res


	def calculate_number_of_units(player):
		count = 0
		count += self.military["infantry"] + self.military["cavalry"] + self.military["artillery"] + \
		 self.military["irregulars"] + self.military["tank"] + self.military["fighter"]
		return count



	def calculate_army_ammo_needed(self):
		ammo_needed = 0.0
		ammo_needed += self.military["infantry"] * self.infantry["ammo_use"]
		ammo_needed += self.military["cavalry"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["artillery"] * self.artillery["ammo_use"]
		ammo_needed += self.military["tank"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["fighter"] * self.artillery["ammo_use"]
		print("Ammo Needed for %s: %s" % (self.name, ammo_needed))

		return ammo_needed

	def calculate_army_oil_needed(self):
		oil_needed = 0.0
		oil_needed += self.military["tank"] * self.tank["oil_use"]
		oil_needed += self.military["fighter"] * self.fighter["oil_use"]
		print("Oil Needed for %s: %s" % (self.name, oil_needed))
		return oil_needed