
# AI

from player_class import*
from market import*
from technologies import*
from random import*
from math import*

import math


craft = {
	"parts" : "iron",
	"cannons" : "iron",
	"paper" : "wood",
	"clothing" : "cotton",
	"furniture" : "wood",
	"chemicals" : "coal"
	}

manufacture = {
	"parts": {"iron": 0.6, "coal": 0.4},
	"cannons": {"iron": 0.6, "coal": 0.4},
	"paper": {"wood": 1.0},
	"clothing": {"cotton": 0.8, "dyes": 0.2},
	"furniture": {"wood": 0.65, "cotton": 0.35},
	"chemicals": {"coal": 0.5},
	"gear": {"rubber": 0.4, "iron": 0.3, "coal": 0.3},
	"radio": {"gear": 0.85, "wood": 0.15},
	"telephone": {"gear": 0.85, "wood": 0.15},
	"fighter": {"wood": 0.5, "gear": 0.5, "parts": 0.5, "cannons": 1.0},   # 2.5 
	"auto": {"rubber": 0.5, "gear": 0.5, "parts": 0.5, "iron": 0.5},		#2
	"tank": {"auto": 1.0, "iron": 1.0, "cannons": 1.5},  #4 
	#"frigates": {"cannons": 1.0, "wood": 1.0, "cotton": 1.0},
	#"iron_clad": {"cannons": 1.0, "iron": 1.0, "parts": 1.0},
	#"battle_ship": {"cannons": 3.0, "iron": 3.0, "parts": 1.0, "gear": 1.0 }  #8 
		}



class AI(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(AI, self).__init__(_name, _type, number, *args, **kwargs)

		self.personality = {
			"Army": 1.15,
			"Navy": 0.7,
		}

		self.rival_target = []

		self.allied_target = []

		self.mid_class_priority = {
			"researchers": 1.0,
			"officers": 0.9,
			"bureaucrats": 0.9,
			"managers": 0.9,
			"artists": 1.0
		}

		self.pro_need = {
			"food": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"coal": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"spice":{"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"oil": {"produces": 0.0, "needs": 0.0, "forecast": 0.0}
		}

		
		self.objective = 0

		self.build_factory_priority = {
			"parts": 1.0,
			"clothing": 1.0,
			"furniture": 0.75,
			"paper": 1.0,
			"cannons": 1.0,
			"chemicals": 0.5,
			"gear": 0.95,
			"radio": 0.65,
			"telephone": 0.55,
			"fighter": 0.75,
			"auto": 0.8,
			"tank": 1.0
		}
		#cannon
		self.improve_province_priority = {
			"food": 1.2,
			"iron": 1.0,
			"coal": 0.1,
			"wood": 0.3,
			"cotton": 0.3,
			"gold": 1,
			"spice": 1,
			"dyes": 0.1,
			"rubber": 1.7,
			"oil": 1.7,
			"shipyard": 1.7,
		}

		self.military_priority = {
			"infantry": 1,
			"cavalry": 1,
			"artillery": 1,
			"irregulars": - 1.5,
			"fighter": 0.9,
			"tank": 1.6
		}

		self.technology_priority = {
			"flint_lock": 2.5,
			"basic_civ": 3,
			"pre_modern": 3,
			"pre_industry_1": 5,
			"pre_industry_2": 5,
			"pre_industry_3": 5,
			"professional_armies": 7,
			"high_pressure_steam_engine": 7,
			"square_timbering": 4,
			"cotton_gin": 4,
			"steel_plows": 4.5,
			"saw_mill": 4,
			"cement": 2.5,
			"bessemer_process": 3,
			"muzzle_loaded_arms": 3,
			"breach_loaded_arms": 3,
			"machine_guns": 3,
			"indirect_fire": 3,
			"power_loom": 3,
			"chemistry": 4,
			"pulping": 2,
			"iron_clad": 4,
			"electricity": 3,
			"medicine": 3,
			"synthetic_dyes": 3,
			"fertlizer": 3,
			"dynamite": 3,
			"compound_steam_engine": 4,
			"telegraph": 2,
			"radio": 3.5,
			"mechanical_reaper": 2,
			"oil_drilling": 5,
			"combustion": 4,
			"steel_plate_armor": 2.5,
			"flight": 4.5,
			"automobile": 4,
			"telephone": 3.5,
			"mobile_warfare": 5.5,
			"bombers": 3.5,
			"oil_powered_ships": 5.0,
			"synthetic_oil": 4.0,
			"synthetic_rubber": 4.0,
			"radar": 3.0

		}

		self.resource_priority = {
			"food":	1.0,
			"iron": 1.0,
			"coal": 0.3,
			"cotton": 0.75,
			"wood": 1.0,
			"spice": 2,
			"dyes": 0.75,
			"gold": 1.5,
			"rubber": 1,
			"oil": 1.5
		}

		self.resourse_to_keep = {
			"food":	4,
			"iron": 3,
			"coal": 4,
			"cotton": 2,
			"wood": 2,
			"spice": 2,
			"dyes": 1.0,
			"gold": 2.0,
			"rubber": 2.5,
			"oil": 4
		}

		self.resource_base = {
			"food": 0,
			"iron": 0,
			"coal": 0,
			"cotton": 0,
			"wood": 0,
			"dyes": 0,
			"spice": 0,
			"gold": 0,
			"rubber": 0,
			"oil": 0
		}

	def calculate_resource_base(self):
		for k, v in self.resource_base.items():
			self.resource_base[k] = 0
		for p, prov in self.provinces.items():
			self.resource_base[prov.resource] += (development_map[prov.development_level] * prov.quality)


	def ai_increase_pop(self, market):
		if self.midGrowth == False:
			return
		if self.freePOP > 3 or self.proPOP > 5:
			return
		if self.POP_increased >= 2:
			return
		if self.goods["clothing"] < 1 and market.market["clothing"] > 1 and self.resources["gold"] >= market.buy_price("clothing") * 2:
			self.ai_buy("clothing", 1, market)
		#if self.goods["furniture"] < 1 and market.market["furniture"] > 1 and self.resources["gold"] > market.buy_price("furniture") * 1.5:
		#	self.ai_buy("furniture", 1, market)
		if self.resources["food"] < 2 and market.market["food"] > 2 and self.resources["gold"] >= market.buy_price("food") * 3:
			self.ai_buy("food", 2, market)
		if self.resources["food"] >= 2 and self.goods["clothing"] >= 1 and self.POP <= ((len(self.provinces) * 2.2) + self.numMidPOP):
			if self.POP_increased == 1:
				if self.goods["chemicals"] < 2:
					return
				else: 
					self.goods["chemicals"] -= 1
					self.POP += 1.0
					self.freePOP += 1.0
					self.numLowerPOP += 1
					self.resources["food"] -= 1.0
					self.goods["clothing"] -= 1.0
					#self.goods["furniture"] -= 1.0
					self.POP_increased += 1
					self.stability -= 0.1
					if self.stability < -3.0:
						self.stability = -3.0
					print("POP increase ______________________________________________")

			else:
				self.POP += 1.0
				self.freePOP += 1.0
				self.numLowerPOP += 1
				self.resources["food"] -= 1.0
				self.goods["clothing"] -= 1.0
				#self.goods["furniture"] -= 1.0
				self.POP_increased += 1
				self.stability -= 0.15
				if self.stability < -3.0:
					self.stability = -3.0
				print("POP increase ______________________________________________")

	def determine_middle_class_need(self):
		requirement = ["paper"]
		if self.numMidPOP >= 1 and self.numMidPOP < 2:
			requirement = ["paper", "furniture"]
		if self.numMidPOP >= 2 and self.numMidPOP < 2.5:
			requirement = ["paper", "clothing", "furniture"]
		if self.numMidPOP >= 2.5 and self.numMidPOP < 3:
			requirement = ["paper", "paper", "clothing", "furniture"]
		if self.numMidPOP >= 3 and self.numMidPOP < 3.5:
			requirement = ["paper", "paper", "clothing", "furniture", "chemicals"]
		if self.numMidPOP >= 3.5 and self.numMidPOP < 4:
			requirement = ["paper", "paper", "clothing", "furniture", "radio", "radio"]
		if self.numMidPOP >= 4 and self.numMidPOP < 4.5:
			requirement = ["paper", "paper", "clothing", "furniture", "telephone", "radio", "telephone"]
		if self.numMidPOP > 4.5:
			requirement = ["paper", "paper", "clothing", "furniture", "auto", "radio", "telephone", "auto"]
		print("Mid class requirments:")
		for r in requirement:
			print(r)
		return requirement

	def check_mid_requirement(self, requirement):
		if self.resources["spice"] < 1:
			return False
		for r in requirement:
			if self.goods[r] < 1: 
				return False
		if self.numMidPOP >= 3 and self.goods["paper"] < 2:
			return False
		if self.freePOP < 0.3 and self.proPOP < 2:
			return False
		return True


	def try_middle_class(self, market):
		if self.midGrowth == False:
			return
		requirement = self.determine_middle_class_need()
		per1 = self.check_mid_requirement(requirement)
		if per1 == True:
			return True
		else: 
			for r in requirement:
				if self.goods[r] < 1:
					decision = self.ai_decide_on_good(r, market)
					self.ai_obtain_good(r, decision, market)
			if self.resources["spice"] < 1:
				self.ai_buy("spice", 1, market)
			if self.numMidPOP >= 5 and self.goods["paper"] < 2:
				decision = self.ai_decide_on_good("paper", market)
				self.ai_obtain_good("paper", decision, market)
		per2 = self.check_mid_requirement(requirement)
		if per2 == True:
			return True
		else:
			return False



	def ai_increase_middle_class(self, market):
		if self.midGrowth == False:
			print("Cannot incrase midPOP becuase did not pay all food last turnS")
			return
		check = self.try_middle_class(market)
		if check == False:
			print("Cannot increase middle class at this time (tried)")
			return
		if self.freePOP < 0.2:
			self.proPOP -= 1
			self.freePOP +1
		current = 100
		tries = 0
		allow = False
		_type = sorted(self.mid_class_priority, key=self.mid_class_priority.get, reverse = True)
		while tries < 4 and allow == False:
			#print(type(_type))
			index = _type[tries]
			#print(index)
			#print(type(self.midPOP))
			#print(self.midPOP["researchers"]["number"])
			if self.midPOP[index]["number"] >= 2:
				tries += 1
			else: 
				allow = True
		if allow == False:
			print("Maximum # of Middle Class Achieved!!!")
			return 

		self.resources["spice"] -= 1.0
		requirement = self.determine_middle_class_need()
		for r in requirement:
			self.goods[r] -= 1.0
		self.numLowerPOP -= 0.2
		self.numMidPOP += 0.2
		self.midPOP[_type[tries]]["number"] += 0.2
		self.freePOP -= 0.2
		self.mid_class_priority[_type[tries]] -= 0.1
		self.new_development += 1.0
		print("New middle class pop: %s ________________________" % (_type[tries]))


	def early_game(self, turn, market):
		if turn > 12:
			return
		if self.type != "major":
			return
		if self.resources["cotton"] < 1 and market.buy_price("cotton") < self.resources["gold"] * 1.5:
			self.ai_buy("cotton", 1, market)
		if self.resources["wood"] < 1 and market.buy_price("wood") < self.resources["gold"] * 1.5:
			self.ai_buy("wood", 1, market)
		if self.resources["iron"] < 1 and market.buy_price("iron") < self.resources["gold"] * 1.5:
			self.ai_buy("iron", 1, market)
		if self.factories["cannons"] == 0 and self.goods["cannons"] < 2.5:
			if self.resources["iron"] >= 2 and market.market["cannons"] <= 2:
				self.ai_craftman_production("cannons")
		if self.goods["cannons"] >= 1 and self.resources["wood"] >= 1 and self.shipyard >= 1 and \
			self.resources["cotton"] >= 1 and self.AP >= 1:
				if self.military["frigates"] < 2:
					self.ai_build_frigates()
		if self.factories["clothing"] == 0 and self.goods["clothing"] < 2:
			if self.resources["cotton"] >= 2 and market.market["clothing"] <= 3 :
				self.ai_craftman_production("clothing")
		if self.factories["paper"] == 0 and self.goods["paper"] < 2 and self.AP >= 1:
			if self.resources["wood"] >= 2 and market.market["paper"] <= 3:
				self.ai_craftman_production("paper")
		if self.factories["furniture"] == 0 and self.goods["furniture"] < 1 and self.AP >= 1:
			if self.resources["wood"] >= 2 and market.market["furniture"] <= 3:
				self.ai_craftman_production("furniture")

	def num_army_units(self):
		res = 0
		res += (self.military["irregulars"] + self.military["infantry"] + self.military["cavalry"] + \
			self.military["artillery"] + self.military["tank"] + self.military["fighter"])
		return res

	def num_factories(self):
		count = 0
		for k, v in self.factories.items():
			count += self.factories[k]
		return count


	def try_factory(self, market, globe):
		flag = True
		if self.goods["parts"] < 1:
			print("Wants machine parts")
			decision = self.ai_decide_on_good("parts", market)
			if decision != "buy":
				flag = False
			self.ai_obtain_good("parts", decision, market)
			#print("Flag: %s" % (flag))
		if self.resources["iron"] < 1:
			print("Wants to get iron")
			get = self.ai_buy("iron", 1, market)
			if get == "fail":
				flag = False
		if flag == False:
			return
		else:
			#priorities = (sorted(self.build_factory_priority.keys(), key=lambda x:x[1], reverse=True ))
			priorities = sorted(self.build_factory_priority, key=self.build_factory_priority.get, reverse = True)
			options = self.ai_factory_options()
			for o in options:
				for p in priorities:
					if p in options:
						self.ai_build_factory(p, market, globe)
						return	


	def try_development(self, market):
		flag = True
		if self.goods["parts"] < 1:
			print("Wants parts")
			decision = self.ai_decide_on_good("parts", market)
			if decision != "buy":
				flag = False
			self.ai_obtain_good("parts", decision, market)
		if self.resources["wood"] < 1:
			print("Wants wood")
			get = self.ai_buy("wood", 1, market)
			if get == "fail":
				flag = False
		if self.sprawl == True:
			if self.goods["parts"] < 1.5:
				print("Wants parts")
				decision = self.ai_decide_on_good("parts", market)
				if decision != "buy":
					flag = False
			if self.resources["wood"] < 1.5:
				print("Wants wood")
				get = self.ai_buy("wood", 1, market)
				if get == "fail":
					flag = False


		if flag == False:
			return
		else:
			print("Development Check")
			priorities = sorted(self.improve_province_priority, key=self.improve_province_priority.get, reverse = True)
			options = self.ai_improve_province_options()
			for p in priorities:
				if p in options:
				#	print("Checking for %s province" % (p))
					self.ai_develop_province(p)
					return

	def develop_industry(self, market, globe):
		print("Develop Industry:")
		print(self.type)
		if self.type != "major" and self.type != "old_empire":
			return
		print("Development Points: %s" % (self.new_development))
		if self.new_development < 1:
			return
		opt = self.ai_improve_province_options()
		print("Development options_________________")
		for o in opt:
			print(o)
		print("Resource Base")
		for k, v in self.resource_base.items():
			print(k, v)

		fact = self.ai_factory_options()
		print("Factory options:_________________")
		for f in fact:
			print(f)
		if len(opt) >= 1 and len(self.ai_factory_options()) >= 1:
			print("Able to develop provice or build factory")
			number_factories =  self.num_factories()
			if number_factories == 0:
				print("Wants to build factory")
				self.try_factory(market, globe)
			if number_factories >= self.number_developments and len(self.factories) >= 2:
				print("Wants to develop province")
				self.try_development(market)
			else:
				pick = uniform(0, 1)
				if pick <=  0.38:
					print("Wants to build factory")
					self.try_factory(market, globe)
				else:
					print("Wants to improve province")
					self.try_development(market)
		elif len(opt) > 0:
			print("Try to develop province...")
			self.try_development(market)
		elif "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1:
			self.try_factory(market, globe)
			
				

	def ai_obtain_good(self, _type, decision, market):
		get = ""
		if decision == "manufacture_prepare":
			for i in manufacture[_type]:
				material_mod = 1 - (self.midPOP["managers"]["number"] / 3)
				material_max = 1000
				for i in manufacture[_type]:
					temp = int((manufacture[_type][i] * material_mod)/(self.resources[i] + 0.1))
					if temp < material_max:
						material_max = temp
				need = int(5 - material_max)
				for i in manufacture[_type]:
					get = self.ai_buy(i, need, market)
					if get == "fail":
						break
				self.ai_factory_production(_type)
		elif decision == "manufacture_ready":
			self.ai_factory_production(_type)
		elif decision == "buy":
			self.ai_buy(_type, 1, market)
		elif decision == "craft_ready":
			self.ai_craftman_production(_type)
		else:
			if _type in craft.keys():
				get = self.ai_buy(craft[_type], 1, market)
			if get == "sucess":
				self.ai_craftman_production(_type)


	def assign_priorities_to_provs(self):
		for p, prov in self.provinces.items():
			#print(p, prov.resource)
			kind = prov.resource
			prov.AI_priority = self.resource_priority[kind] * prov.quality
		sorted_provinces = sorted(self.provinces.values(), key = lambda x: (x.AI_priority), reverse = True)
		#sorted_priorities = sorted(self.provinces, key=self.provinces.get, reverse = True)
		#print("Province priorities:")
		#for k, v in self.resource_priority.items():
		#	print(k, v)
		return sorted_provinces

	def update_priorities(self, market):
		if self.stability > 3.0:
			self.stability = 3.0
		for k, v in self.resources.items():
			if k == "gold":
				continue
			if market.market[k] < 1:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if market.market[k] < 5:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if self.resources[k] < 1:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if market.market[k] > 21:
				self.resource_priority[k] -= 0.1
				self.improve_province_priority[k] -= 0.1
			if self.resources[k] > 14:
				self.resource_priority[k] -= 0.1
				self.improve_province_priority[k] -= 0.1
		#for k, v in self.goods.items():
		#	if market.market[k] < 3:
		#		self.build_factory_priority[k] + 0.1


	def AI_reset_POP(self):
		for p, prov in self.provinces.items():
			prov.worked = False
		self.proPOP = 0
		self.freePOP = self.numLowerPOP - self.milPOP
	

	def AI_assign_POP(self):
		#priorities = (sorted(self.resource_priority.items(), key=lambda x:x[1], reverse=True )
		priorities = self.assign_priorities_to_provs()
		for p in priorities:
				print(p.name)
		#desired_producers = int(self.POP / 4)
		#print(desired_producers)
		#min_producers = int(self.freePOP/3.25)
		#min_producers = 2
		#for i in range(desired_producers):
		#	if self.freePOP >= 2:
		#		self.proPOP += 1
		#		self.freePOP -=1
		if self.type == "major" or self.type == "old_empire":
			self.proPOP += 1
			self.freePOP -= 1
		count = 0
		for p in priorities:
			if self.freePOP > 1.4 and count <= 10:

				#print("Number free pop: %s" % self.freePOP)
				if self.provinces[p.name].worked == False:
					self.provinces[p.name].worked = True
					self.freePOP -= 1
					count += 1
		while self.freePOP >= 1.4:
			self.proPOP += 1
			self.freePOP -=1


	def AI_sell_surplus(self, market):
		for r, resource in self.resources.items():
			if r == "gold":
				continue
			if resource > self.resourse_to_keep[r]:
				amount = int(resource - self.resourse_to_keep[r])
				if amount > 4:
						amount = 4
				if amount >= 1 and market.market[r] < 12:
					self.ai_sell(r, amount, market)
				if amount >= 1 and market.market[r] < 22 and self.resources["gold"] <= 25:
					self.ai_sell(r, amount, market)

				if amount >= 1 and market.market[r] < 32 and self.resources["gold"] <= 10:
					self.ai_sell(r, amount, market)


		for g, good in self.goods.items():
			if self.goods[g]  > 2 and g != "cannons"  and market.market[g] < 30 and self.resources["gold"] <= 10:
				amount = int(self.goods[g] - 2)
				if amount >= 1:
					if amount > 5:
						amount = 5
					self.ai_sell(g, amount, market)
			if self.goods[g]  > 3 and g != "cannons"  and market.market[g] < 20 and self.resources["gold"] <= 25:
				amount = int(self.goods[g] - 3)
				if amount >= 1:
					if amount > 5:
						amount = 5
					self.ai_sell(g, amount, market)
			if self.goods[g] > 3 and market.market[g] < 12 and g != "cannons":
				amount = int(self.goods[g] - 3)
				if amount >= 1:
					if amount > 5:
						amount = 5

					self.ai_sell(g, amount, market)
			ammo_needed = self.calculate_ammo_needed() + 2
			if self.goods[g] > ammo_needed + 1 and g == "cannons":
				amount = self.goods["cannons"] - ammo_needed
				if amount > 4:
					amount = 4
				self.ai_sell("cannons", amount, market)
			


	def view_AI_inventory(self):
		print("POP: %s, LowPop: %s, MidPop: %s" % (self.POP, self.numLowerPOP, self.numMidPOP))
		print("freePOP: %s, proPOP: %s " % (self.freePOP, self.proPOP))
		print("Stability: %s, Diplo: %s, Reputation: %s " % (self.stability, self.diplo_action, self.reputation))
		print("Colonize: %s, Num Colonies: %s" % (self.colonization, self.num_colonies))
			
		for m, mid in self.midPOP.items():
			print(m, mid)
			print(m, mid["number"])
		print("\n")
		print("%s Inventory \n" % (self.name))
		for r, resource in self.resources.items():
			print (r, resource, end= ' ')
		for g, good in self.goods.items():
			print(g, good, end=' ')
		for k, v in self.pro_need.items():
			print(k, v)
		print(" \n number_developments: %s \n" % (self.number_developments))
		for k, v in self.factories.items():
			print(k, v, end = " | ")
		for k, v in self.military.items():
			print(k, v)

	def calculate_resource_production(self):
		stab_rounds = round(self.stability * 2) / 2
		stab_mod = stability_map[stab_rounds]
		for p in self.pro_need:
			self.pro_need[p]["produces"] = 0
		for k, p in self.provinces.items():
			gain = 0
			if p.resource == "oil" and p.development_level == 0:
				continue
			if p.resource == "food" or p.resource == "coal" or p.resource == "spice" or p.resource == "oil":
				if p.worked == True:
					if p.powered == True and p.development_level > 0:
						dev = p.development_level
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality
					else:
						if p.resource == "oil":
							continue
						gain = stability_map[stab_rounds] * p.quality
				self.pro_need[p.resource]["produces"] += gain

	def calculate_resource_need(self):
		self.pro_need["food"]["needs"] = ((self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1) + 1
		self.resourse_to_keep["food"] = self.pro_need["food"]["needs"] * 1.25
		#self.pro_need["spice"]["needs"] = self.numMidPOP * 0.3
		self.pro_need["coal"]["needs"] =  0.1 * self.number_developments
		if self.numMidPOP - 8 > 0:
			self.pro_need["oil"]["needs"] = self.numMidPOP - 8

	def calculate_resource_forecast(self):
		for k, v in self.pro_need.items():
			v["forecast"] = (self.resources[k] + v["produces"]) - v["needs"]
			if v["produces"] < v["needs"]:
				self.resource_priority[k] += 0.25
			if self.resources[k] > self.numLowerPOP * 1.25:
				self.resource_priority[k] -= 0.2
		for k, v in self.resources.items():
			if self.resources[k] < 1:
				self.resource_priority[k] += 0.1
			if self.resources[k] > 16:
				self.resource_priority[k] -= 0.1
 

	def ai_decide_on_good(self, _type, market):
		print("Wants to  get %s \n" % (_type))
		price_to_buy = market.buy_price(_type)
		#print("Price to buy %s" % (price_to_buy))
		price_to_craft = 100
		if _type in craft.keys():
			price_to_craft = market.buy_price(craft[_type])
	#	print("price to craft %s " % (price_to_craft))
		if market.market[_type] > 3 and self.resources["gold"] >= market.buy_price(_type):
			return "buy"
		material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
		price_to_man = 0
		for i in manufacture[_type]:
			price_to_man += market.buy_price(i) * int(manufacture[_type][i] * material_mod)
		if self.factories[_type] >= 1:
			cap = self.calculate_how_much_can_produce(_type)
			if cap >= 4:
				print("Make w factory")
				return "manufacture_ready"
			else:
				print("Try to suppy factory....")
				self.supply_factory_with_material(_type, market)
				cap = self.calculate_how_much_can_produce(_type)
				if cap >=4:
					return "manufacture_ready"
				if market.market[_type] >= 1:
					return "buy"
				else:
					return "fail"
				#material_on_market = 0
			#	for k, v in manufacture[_type].items():
				#	material_on_market += manufacture[_type][i] * market.market[k]
				#if (price_to_man * 1.3) < price_to_buy and material_on_market >= 3:
					#return "manufacture_prepare"
		elif market.market[_type] >= 1 and self.resources["gold"] >= market.buy_price(_type):
			print("Decide to buy " + _type)
			return "buy"

		elif _type in ["gear", "telephone", "radio", "auto", "fighter", "tank"]:
			return "fail" 
		elif _type in craft.keys():
			if self.resources[craft[_type]] >= 1.0:
				print("Decide to craft good" + _type)
				return "craft_ready"
		elif market.market[craft[_type]] >= 3 and self.resources["gold"] >= market.buy_price(craft[_type]) and \
		_type in craft.keys():
			print("Buy materail then craft")
			return "craft_prepare"
		else:
			return "fail"


	def calculate_oil_needed(self):
		oil_needed = 0.0
		oil_needed += self.military["tank"] * self.tank["oil_use"]
		oil_needed += self.military["fighter"] * self.fighter["oil_use"]
		oil_needed = self.military["battle_ship"] * self.battle_ship["oil_use"]
		return oil_needed

		

	def calculate_ammo_needed(self):
		ammo_needed = 0.0
		ammo_needed += self.military["frigates"] * self.frigates["ammo_use"]
		ammo_needed += self.military["iron_clad"] * self.iron_clad["ammo_use"]
		ammo_needed += self.military["battle_ship"] * self.battle_ship["ammo_use"]
		ammo_needed += self.military["infantry"] * self.infantry["ammo_use"]
		ammo_needed += self.military["cavalry"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["artillery"] * self.artillery["ammo_use"]
		ammo_needed += self.military["tank"] * self.cavalry["ammo_use"]
		ammo_needed += self.military["fighter"] * self.artillery["ammo_use"]
		return ammo_needed

	def fulfill_needs(self, market):
		food_need = self.numLowerPOP * 0.2 + self.numMidPOP * 0.3 + self.military["cavalry"] * 0.1 + 1
		if self.resources["food"] < food_need:
			while self.resources["food"] < food_need and market.market["food"] >= 1 and self.resources["gold"] >= market.buy_price("food"):
				self.ai_buy("food", 1, market)
		coal_need = (self.number_developments * 0.1) + 1
		if self.resources["coal"] < coal_need:
			while self.resources["coal"] < coal_need and market.market["coal"] >= 2 and self.resources["gold"] >= market.buy_price("coal") * 2:
				self.ai_buy("coal", 1, market)

	
		ammo_needed = self.calculate_ammo_needed()
		if self.goods["cannons"] < (ammo_needed + 2):
			while self.goods["cannons"] < (ammo_needed + 2) and market.market["cannons"] >= 1 and self.resources["gold"] >= market.buy_price("cannons") * 2:
				self.ai_buy("cannons", 1, market)
		oil_needed = self.calculate_oil_needed()
		if self.resources["oil"] < (oil_needed + 1):
			while self.resources["oil"] < (oil_needed + 1) and market.market["oil"] >= 1 and self.resources["gold"] >= market.buy_price("oil") * 2:
				self.ai_buy("oil", 1, market)

		if self.goods["clothing"] < 1 and market.market["clothing"] > 3 and self.resources["gold"] >= market.buy_price("clothing") * 2:
			self.ai_buy("clothing", 1, market)
		if self.goods["chemicals"] <= 2 and market.market["chemicals"] > 4 and self.resources["gold"] >= market.buy_price("chemicals") * 3.:
			self.ai_buy("chemicals", 2, market)
		if self.resources["food"] < 5 and self.POP > 14 and market.market["food"] >= 8 and self.resources["gold"] >= market.buy_price("food") * 4:
			self.ai_buy("food", 3, market)
		if self.resources["rubber"] < 2 and market.market["rubber"] > 3 and  market.buy_price("rubber") * 2.5:
			self.ai_buy("rubber", 1, market)
		if self.goods["gear"] < 2 and market.market["gear"] > 2 and self.resources["gold"] > market.buy_price("gear") * 2:
			self.ai_buy("gear", 1, market)
		if self.goods["gear"] < 4 and market.market["gear"] > 6 and self.resources["gold"] > market.buy_price("gear") * 2.5:
			self.ai_buy("gear", 1, market)
		if self.goods["parts"] < 2 and market.market["parts"] > 3 and self.resources["gold"] > market.buy_price("parts") * 2:
			self.ai_buy("parts", 1, market)

	def ai_buy(self, _type, _amount, market):
		print("Wants to buy %s " % (_type))
		price = market.buy_price(_type)
		while self.resources["gold"] >= price and _amount >= 1 and market.market[_type] >= 1:
			self.resources["gold"] -= price
			market.gold += price
			market.market[_type] -= 1
			if _type in market.resources:
				self.resources[_type]  += 1
			elif(_type == "chemicals"):
				self.goods["chemicals"] += 2
			else:
				self.goods[_type] += 1
			_amount -= 1
			price = market.buy_price(_type) 
			print("Buys 1 %s" % (_type))

		if _amount < 1:
			return "sucess"
		else:
			return "fail"


	def use_spice_stability(self):
		if self.resources["spice"] >= 2 and self.stability < 0:
			self.resources["spice"] -=2
			self.stability += 0.5
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 3 and self.stability < 1:
			self.resources["spice"] -=2
			self.stability += 0.5
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 4 and self.stability < 2:
			self.resources["spice"] -=2
			self.stability += 0.5
			if self.stability > 3:
				self.stability = 3

	def check_stability(self, market):
		if self.stability < 0 and self.resources["spice"] < 2:
			self.ai_buy("spice", 2, market)
		elif self.stability < 1  and self.resources["spice"] < 2:
			if market.market["spice"] >= 2 and self.resources["gold"] >= market.buy_price("spice") * 4:
				self.ai_buy("spice", 2, market)
		elif self.stability < 2 and self.resources["spice"] < 2:
			if market.market["spice"] >= 4 and self.resources["gold"] >= market.buy_price("spice")  *6:
				self.ai_buy("spice", 2, market)


	def spend_excess_cash(self, market):
		count = 20
		while self.resources["gold"] > 50 and count > 0:
			item = choice(["food", "iron", "cotton", "coal", "dyes", "wood", "spice", "clothing", \
			"parts", "cannons", "paper", "furniture", "chemicals", "radio", "telephone", "tank", "auto", "fighter"])
			if item in market.resources:
				if market.market[item] > 8:
					if self.resources[item] < 4:
						self.ai_buy(item, 1, market)
			if item in market.goods:
				if market.market[item] > 4:
					if self.goods[item] < 2:
						self.ai_buy(item, 1, market)
			count -= 1

	def ai_sell(self, _type, amount, market):
		print("Try to sell type %s, amount %s" % (_type, amount))
		if market.market[_type] > 30:
			print("The market cannot buy any more of that resource (over 30) \n")
			return
		price = market.sell_price(_type)
		if price == 0:
			print("The market cannot buy any more of that resource (price 0) \n")
			return
		while market.gold >= price and market.market[_type] <= 30 and amount >= 1:
			print("Sold %s" % (_type))
			market.gold -= price
			market.market[_type] += 1
			self.resources["gold"] += price
			if _type in market.resources:
				self.resources[_type] -= 1
			elif _type in market.goods:
				self.new_development +=  0.25
				if _type == "chemicals":
					self.goods["chemicals"] -= 2
			else:
				self.goods[_type] -= 1
			price = market.sell_price(_type)
			amount -= 1


	def ai_factory_production(self, _type):
		print('Factory Production++++++++++++++++++++++++++++++++++++++++++++++++++')
		stab_rounds = round(self.stability* 2) / 2
		stab_mod = stability_map[stab_rounds]
		material_mod = 1 - (self.midPOP["managers"]["number"] / 4)
		material_max = 1000

		max_amount = self.factories[_type] * stab_mod * 4
		print("MAX amount %s" % (max_amount))

			
		for i in manufacture[_type]:
			if i in self.resources.keys():
				temp = int(self.resources[i]/(manufacture[_type][i] * material_mod))
				print("man_type_i: %s, material mod: %s self_resource_i %s \n" % (manufacture[_type][i], material_mod, self.resources[i]))
				if temp < material_max:
					material_max = temp
			if i in self.goods.keys():
				temp = int(self.goods[i]/(manufacture[_type][i] * material_mod))
				if temp < material_max:
					material_max = temp
		print("material_max: %s " % (material_max))
		amount = min([material_max, max_amount])
		print("AMOUNT FACT %s ^^^^^^^^^^^^^^^^^^^^^^^^^^^^" % (amount))
		if amount < 1:
			return False
		if amount < 2.5 and _type != "tank" and _type != "fighter": 
			return False
	
		for i in manufacture[_type]:
			if i in self.resources.keys():
				self.resources[i] -= manufacture[_type][i] * amount * material_mod
			else:
				self.goods[i] -= manufacture[_type][i] * amount * material_mod
		self.goods_produced[_type] += amount
		print("Produced %s %s " % (amount, _type))
		self.AP -= 1
		return True

	def ai_craftman_production(self, _type):
		if _type not in craft.keys():
			return False
		self.resources[craft[_type]] -= 1.0
		self.goods_produced[_type] += 1.0
		self.AP -= 1
		print("Crafted %s" % (_type))
		#print("AP points remaining__: %s \n" % (self.AP))
		return

	def ai_decide_factory_productions(self, market):
		number_units = self.num_army_units()
		for k, v in self.factories.items():
			print(k, v)
			if v >= 1:
				print("Factory owned: %s" % (k))

				if self.AP >= 1 and market.market[k] < 15 and self.goods[k] <= 10:
					cap = self.calculate_how_much_can_produce(k)
					if cap < 3:
						self.supply_factory_with_material(k, market)
						cap = self.calculate_how_much_can_produce(k)
						if cap < 3:
							continue
						else:
							self.ai_factory_production(k)
							continue
					else:
						self.ai_factory_production(k)
			


	def calculate_how_much_can_produce(self, _type):
		cap = 1000
		print("calculate_how_much_can_produce: %s" % (_type))

		for k, v in manufacture[_type].items():
			print(k, v)
			if (k in self.resources.keys() and self.resources[k] == 0) or (k in self.goods.keys() and self.goods[k] == 0):
				print("%s equals 0" % (k))
				cap = 0

				return cap
			else:
				material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
				if k in self.resources.keys():
					temp = self.resources[k]/ (v * material_mod)
					if (self.resources[k]/ (v * material_mod)) < cap:
						cap = (self.resources[k]/v * material_mod)
				if k in self.goods.keys():
					temp = self.goods[k]/ (v * material_mod)
					if (self.goods[k]/ (v * material_mod)) < cap:
						cap = (self.goods[k]/v * material_mod)
		print("Is able to produce %s \n" % (cap))
		return cap

	def supply_factory_with_material(self, _type, market):
		print("Try to supply %s factory..." % (_type))
		if _type == "parts" or "type" == "cannons":
			if self.resources["iron"] < 4.0:
				amount = ceil(5 - self.resources["iron"])
				amount = min (amount, int(market.market["iron"]))
				self.ai_buy("iron", amount, market)
			if self.resources["coal"] < 2.0:
				amount = ceil(2 - self.resources["coal"])
				amount = min(amount, int(market.market["coal"]))
				self.ai_buy("coal", amount, market)
		elif _type == "clothing":
			if self.resources["cotton"] < 5:
				amount = ceil(5 - self.resources["cotton"])
				amount = min(amount, int(market.market["cotton"]))
				self.ai_buy("cotton", amount, market)
			if self.resources["dyes"] < 1:
				amount = ceil(2 - self.resources["dyes"])
				amount = min(amount, int(market.market["dyes"]))
				self.ai_buy("dyes", amount, market)
		elif _type == "furniture":
			if self.resources["wood"] < 4:
				amount = ceil(4 - self.resources["wood"])
				amount = min(amount, int(market.market["wood"]))
				self.ai_buy("wood", amount, market)
			if self.resources["cotton"] < 2.0:
				amount = ceil(2 - self.resources["cotton"])
				amount = min(amount, int(market.market["cotton"]))
				self.ai_buy("cotton", amount, market)
		elif _type == "paper":
			if self.resources["wood"] < 5:
				amount = ceil(5 - self.resources["wood"])
				amount = min(amount, int(market.market["wood"]))
				self.ai_buy("wood", amount, market)
		elif _type == "chemicals":
			if self.resources["coal"] < 4:
				amount = ceil(5 - self.resources["coal"])
				amount = min(amount, int(market.market["coal"]))
				self.ai_buy("coal", amount, market)
		elif _type == "gear":
			if self.resources["rubber"] < 3:
				amount = ceil(5 - self.resources["rubber"])
				amount = min(amount, int(market.market["rubber"]))
				self.ai_buy("rubber", amount, market)
			if self.resources["iron"] < 2:
				amount = ceil(4 - self.resources["iron"])
				amount = min(amount, int(market.market["iron"]))
				self.ai_buy("iron", amount, market)
			if self.resources["coal"] < 2.5:
				amount = ceil(4 - self.resources["coal"])
				amount = min(amount, int(market.market["coal"]))
				self.ai_buy("coal", amount, market)
		elif _type == "radio" or _type == "telephone":
			if self.goods["gear"] < 3:
				decision = self.ai_decide_on_good("gear", market)
				self.ai_obtain_good("gear", decision, market)
				amount = ceil(5 - self.goods["gear"])
				amount = min(amount, int(market.market["gear"]))
				self.ai_buy("gear", amount, market)
		elif _type == "auto":
			if self.goods["gear"] < 4:
				decision = self.ai_decide_on_good("gear", market)
				self.ai_obtain_good("gear", decision, market)
				amount = ceil(4 - self.goods["gear"])
				amount = min(amount, int(market.market["gear"]))
				self.ai_buy("gear", amount, market)
			if self.goods["parts"] < 4:
				decision = self.ai_decide_on_good("parts", market)
				self.ai_obtain_good("parts", decision, market)
				amount = ceil(4 - self.goods["parts"])
				amount = min(amount, int(market.market["parts"]))
				self.ai_buy("parts", amount, market)
			if self.resources["rubber"] < 3:
				amount = ceil(4 - self.resources["rubber"])
				amount = min(amount, int(market.market["rubber"]))
				self.ai_buy("rubber", amount, market)
			if self.resources["iron"] < 2.0:
				amount = ceil(4 - self.resources["iron"])
				amount = min(amount, int(market.market["iron"]))
		elif _type == "fighter":
			if self.goods["gear"] < 3:
				decision = self.ai_decide_on_good("gear", market)
				self.ai_obtain_good("gear", decision, market)
				amount = ceil(4 - self.goods["gear"])
				amount = min(amount, int(market.market["gear"]))
				self.ai_buy("gear", amount, market)
			if self.goods["parts"] < 3:
				decision = self.ai_decide_on_good("parts", market)
				self.ai_obtain_good("parts", decision, market)
				amount = ceil(4 - self.goods["parts"])
				amount = min(amount, int(market.market["parts"]))
				self.ai_buy("parts", amount, market)
			if self.resources["wood"] < 3:
				amount = ceil(4 - self.resources["wood"])
				amount = min(amount, int(market.market["wood"]))
				self.ai_buy("wood", amount, market)
			if self.goods["cannons"] < 6:
				decision = self.ai_decide_on_good("cannons", market)
				self.ai_obtain_good("cannons", decision, market)
				amount = ceil(7 - self.goods["cannons"])
				amount = min(amount, int(market.market["cannons"]))
				self.ai_buy("cannons", amount, market)
		elif _type == "tank":
			if self.goods["gear"] < 3:
				decision = self.ai_decide_on_good("gear", market)
				self.ai_obtain_good("gear", decision, market)
				amount = ceil(5 - self.goods["gear"])
				amount = min(amount, int(market.market["gear"]))
				self.ai_buy("gear", amount, market)
			if self.goods["parts"] < 3:
				decision = self.ai_decide_on_good("parts", market)
				self.ai_obtain_good("parts", decision, market)
				amount = ceil(5 - self.goods["parts"])
				amount = min(amount, int(market.market["parts"]))
				self.ai_buy("parts", amount, market)
			if self.resources["iron"] < 5:
				amount = ceil(6 - self.resources["iron"])
				amount = min(amount, int(market.market["iron"]))
				self.ai_buy("iron", amount, market)
			if self.goods["cannons"] < 7:
				decision = self.ai_decide_on_good("cannons", market)
				self.ai_obtain_good("cannons", decision, market)
				amount = ceil(8 - self.goods["cannons"])
				amount = min(amount, int(market.market["cannons"]))
				self.ai_buy("cannons", amount, market)


	def ai_modify_priorities_from_province(self, resource):
		if resource == "food":
			self.technology_priority["steel_plows"] += 1
			self.technology_priority["mechanical_reaper"] += 1
			self.technology_priority["fertlizer"] += 1
			self.improve_province_priority["food"] + 0.6
		if resource == "iron":
			self.technology_priority["square_timbering"] += 1
			self.technology_priority["dynamite"] += 1
			self.technology_priority["bessemer_process"] += 1
			self.technology_priority["iron_clad"] += 0.5
			self.technology_priority["muzzle_loaded_arms"] += 1
			self.technology_priority["breach_loaded_arms"] += 1
			self.technology_priority["machine_guns"] += 1
			self.technology_priority["indirect_fire"] += 1
			self.improve_province_priority["iron"] += 0.75
			self.build_factory_priority["parts"] += 0.8
			self.improve_province_priority["coal"] += 0.5
			self.build_factory_priority["cannons"] + 0.8
			self.build_factory_priority["tank"] += 0.6
			#self.military_priority["iron_clad"] += 1
			#self.military_priority["frigates"] + 0.1
		if resource == "coal":
			self.technology_priority["square_timbering"] += 1
			self.technology_priority["dynamite"] += 0.5
			self.technology_priority["bessemer_process"] += 0.5
			self.technology_priority["chemistry"] += 1
			self.technology_priority["synthetic_dyes"] + 0.5
			self.technology_priority["fertlizer"] + 1
			self.technology_priority["medicine"] + 1
			self.improve_province_priority["coal"] += 0.5
			self.build_factory_priority["parts"] += 0.4
			self.build_factory_priority["cannons"] += 0.4
			self.build_factory_priority["chemicals"] += 0.75
		if resource == "wood":
			self.technology_priority["saw_mill"] += 1
			self.technology_priority["pulping"] += 1
			self.technology_priority["compound_steam_engine"] += 1
			self.build_factory_priority["paper"] += 1
			self.build_factory_priority["furniture"] += 0.8
			self.improve_province_priority["wood"] += 0.75
			#self.military_priority["frigates"] + 0.4
		if resource == "cotton":
			self.technology_priority["cotton_gin"] += 1
			self.technology_priority["power_loom"] += 1
			self.technology_priority["compound_steam_engine"] += 1
			self.technology_priority["synthetic_dyes"] + 2
			self.technology_priority["chemistry"] += 1
			self.build_factory_priority["clothing"] += 0.8
			self.build_factory_priority["furniture"] += 0.4
			self.build_factory_priority["chemicals"] += 0.3
			self.improve_province_priority["cotton"] += 0.8
			#self.military_priority["frigates"] + 0.4
		if resource == "dyes":
			self.technology_priority["synthetic_dyes"] -= 1
			self.technology_priority["compound_steam_engine"] += 1
			self.improve_province_priority["dyes"] += 1
			self.build_factory_priority["clothing"] += 0.25
		if resource == "spice":
			self.technology_priority["steel_plows"] += 1
			self.improve_province_priority["spice"] += 2.5
		if resource == "gold":
			self.technology_priority["dynamite"] += 1
			self.improve_province_priority["gold"] += 2.5

		if resource == "rubber":
			self.build_factory_priority["gear"] += 0.8
			self.build_factory_priority["telephone"] + 0.7
			self.build_factory_priority["radio"] + 0.7
			self.build_factory_priority["auto"] + 0.5
			self.build_factory_priority["tank"] + 0.5
			self.build_factory_priority["auto"] + 0.5
			self.build_factory_priority["fighter"] + 0.5
			self.improve_province_priority["rubber"] += 0.8

		if resource == "oil":
			self.improve_province_priority["oil"] + 0.4
			self.build_factory_priority["tank"] + 0.3
			self.build_factory_priority["fighter"] + 0.5


	def choose_technology(self):
		options = []
		print("Current Techs:")
		for t in self.technologies:
			print(t)
		
		for k, t in technology_dict.items():
			if k not in self.technologies and t["requirement"] <= self.technologies  \
			 and self.numMidPOP >= t["min_mid"] and t["cost"] <= self.research:
				print(k, t)
				options.append(k)
		print("Options: %s \n" % (options))
		if len(options) == 0:
			return None
		#priorities = sorted([self.technology_priority(v,k) for (k,v) in self.technology_priority], reverse=True)
		#priorities = (sorted(self.technology_priority.keys(), key=lambda x:x[1]))
		priorities = sorted(self.technology_priority, key=self.technology_priority.get, reverse = True)
		for p in priorities:
			if p in options:
		#priorities = sorted(self.technology_priority, key=my_dict.get)
				self.ai_research_tech(p)
				return


	def ai_research_tech(self, choice):
		print("Researched  %s ______________________________________________________ \n" % (choice))
		self.research -= technology_dict[choice]["cost"]
		self.technologies.add(choice)
		if choice == "flint_lock":
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.3
			self.infantry["defend"] += 0.10
			self.cavalry["attack"] += 0.20
			self.cavalry["defend"] += 0.08
			self.artillery["attack"] += 0.3
			self.artillery["defend"] += 0.10
			self.frigates["attack"] += 0.25

		if(choice == "muzzle_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.3
			self.infantry["defend"] += 0.10
			self.cavalry["attack"] += 0.20
			self.cavalry["defend"] += 0.08
			self.artillery["attack"] += 0.3
			self.artillery["defend"] += 0.10
			self.frigates["attack"] += 0.25
		if(choice == "cement"):
			self.max_fortification += 0.1
		if(choice == "breach_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.35
			self.infantry["defend"] += 0.2
			self.cavalry["attack"] += 0.25
			self.cavalry["defend"] += 0.10
			self.artillery["attack"] += 0.35
			self.artillery["defend"] += 0.2
			self.frigates["attack"] += 0.35
			self.frigates["attack"] += 0.35
		if(choice == "machine_guns" ):
			self.irregulars["defend"] += 0.2
			self.infantry["defend"] += 1.0
			self.infantry["attack"] += 0.1
			self.cavalry["defend"] + 0.15
		if(choice == "indirect_fire"):
			self.artillery["attack"] += 0.1
			self.artillery["defend"] += 0.4
			self.artillery["ammo_use"] += 0.05
			self.iron_clad["attack"] += 0.25
		if(choice == "bombers"):
			self.fighter["attack"] += 1
			self.fighter["ammo"] += 0.1
		if(choice == "radar"):
			self.fighter["defend"] += 0.5
			self.battle_ship["attack"] += 1

	def ai_improve_province_options(self):
		#print("Improve province options")
		options = []
		if "high_pressure_steam_engine" not in self.technologies:
			print("Does not have high preassure steam engine")
			return options
		if self.new_development >= 1.0:
			for p, prov in self.provinces.items():
				if prov.resource == "food":
					max_dev = 0
					if("steel_plows" in self.technologies):
						max_dev = 1
					if("mechanical_reaper" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("food")
				elif prov.resource == "iron":
					#print("got to Iron")
					max_dev = 0
					if("square_timbering" in self.technologies):
						max_dev = 1
						#print("dev 1")
						#print("level: %s " % (prov.development_level))
					if("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("iron")
				elif prov.resource == "coal":
					max_dev = 0
					if("square_timbering" in self.technologies):
						max_dev = 1
					if("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("coal")
				elif prov.resource == "cotton":
					max_dev = 0
					if("cotton_gin" in self.technologies):
						max_dev = 1
					if("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("cotton")

				elif prov.resource == "wood":
					max_dev = 0
					if("saw_mill" in self.technologies):
						max_dev = 1
					if("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("wood")
				elif prov.resource == "spice":
					max_dev = 0
					if("steel_plows" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("spice")
				elif prov.resource == "gold":
					max_dev = 0
					if("dynamite" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("gold")
				elif prov.resource == "dyes":
					max_dev = 0
					if("compound_steam_engine" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("dyes")
				elif prov.resource == "rubber":
					max_dev = 0
					if "electricity" in self.technologies:
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("rubber")
				elif prov.resource == "oil":
					max_dev = 0
					if "oil_drilling" in self.technologies:
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("oil") 

			if self.shipyard == 0:
				options.append("shipyard")
			if self.shipyard < 2 and "iron_clad" in self.technologies:
				options.append("shipyard")
			if self.shipyard < 3 and "oil_powered_ships" in self.technologies:
				options.append("shipyard")
		return options


	def ai_factory_options(self):
		options = []
		if "high_pressure_steam_engine" in self.technologies and self.new_development >= 1.0:
		
			if self.factories["parts"] == 0 and self.resource_base["iron"] >= 1:
				options.append("parts")
			if self.factories["parts"] == 1 and "bessemer_process" in self.technologies and self.resource_base["iron"] >= 1.8 and self.resource_base["coal"] >= 1.0: 
				options.append("parts")
			if self.factories["clothing"] == 0 and self.resource_base["cotton"] >= 1:
				options.append("clothing")
			if self.factories["clothing"] == 1 and "power_loom" in self.technologies and self.resource_base["cotton"] >= 1.8:
				options.append("clothing")
			if self.factories["furniture"] == 0 and self.resource_base["wood"] >= 1:
				options.append("furniture")
			if self.factories["furniture"] == 1 and "electricity" in self.technologies and self.resource_base["wood"] >= 1.4 and self.resource_base["cotton"] >= 0.9:
				options.append("furniture")
			if self.factories["paper"] == 0 and self.resource_base["wood"] >= 1:
				options.append("paper")
			if self.factories["paper"] == 1 and "pulping" in self.technologies and self.resource_base["wood"] >= 1.8:
				options.append("paper")
			if self.factories["cannons"] == 0:
				options.append("cannons")
			if self.factories["cannons"] == 1 and "bessemer_process" in self.technologies and self.resource_base["iron"] >= 1.6:
				options.append("cannons")
			if self.factories["chemicals"] == 0 and "chemistry" in self.technologies and self.resource_base["coal"] > 1.2:
				options.append("chemicals")
			if self.factories["chemicals"] == 1 and "dyes" in self.technologies and self.resource_base["coal"] > 2:
				options.append("chemicals") 
			if self.factories["gear"] < 2 and "electricity" in self.technologies:
				options.append("gear")
			if self.factories["radio"] < 2 and "radio" in self.technologies:
				options.append("radio")
			if self.factories["telephone"] < 2 and "telephone" in self.technologies:
				options.append("telephone")
			if self.factories["fighter"] < 2 and "flight" in self.technologies:
				options.append("fighter")
			if self.factories["auto"] < 2 and "automobile" in self.technologies:
				options.append("auto")
			if self.factories["tank"] < 2 and "mobile_warfare" in self.technologies:
				options.append("tank") 
		return options


	def ai_build_frigates(self):
		self.resources["wood"] -= 1
		self.resources["cotton"] -= 1 
		self.goods["cannons"] -= 1
		self.military["frigates"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("Frigate completed___________________________________________________________________")

	def ai_build_iron_clad(self):
		self.goods["cannons"] -= 1
		self.resources["iron"] -= 1
		self.goods["parts"] -= 1
		self.military["iron_clad"] += 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("Ironclad completed___________________________________________________________________")
 

	def ai_build_battle_ship(self):
		self.goods["cannons"] -= 3
		self.resources["iron"] -= 3
		self.goods["parts"] -= 1
		self.goods["gear"] -= 1
		self.military["battle_ship"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("Battle_ship completed___________________________________________________________________")


	def decide_build_navy(self, market):
		print("Decide on navy__###############################################################")
		transport_limit = 0
		transport_limit += self.military["frigates"] * 2
		transport_limit += self.military["iron_clad"] * 2
		transport_limit += self.military["battle_ship"] * 3
		num_units = self.num_army_units()
		if transport_limit < num_units * self.personality["Navy"]:
			if self.goods["cannons"] >= 5 and self.resources["iron"] >= 3 and self.goods["parts"] >=1 and \
			self.goods["gear"] >= 1 and self.AP >= 2 and "oil_powered_ships" in self.technologies and self.shipyard == 3:
				self.ai_build_battle_ship()
			elif self.goods["cannons"] >= 2 and self.goods["parts"] >= 1 and self.resources["iron"] >= 1 \
				and self.AP >= 1 and "oil_powered_ships" not in self.technologies and "iron_clad" in self.technologies and self.shipyard >= 2:
				self.ai_build_iron_clad()
			elif self.goods["cannons"] >= 2 and self.resources["wood"] >= 1 and self.shipyard >= 1 and \
			self.resources["cotton"] >= 1 and self.AP >=1 and "iron_clad" not in self.technologies:
				self.ai_build_frigates()
		


	def ai_build_factory(self, _type, market, globe):
		if _type == "parts" or _type == "cannons":
			self.resource_priority["coal"] += 0.3
			self.resource_priority["iron"] += 0.3
			self.resourse_to_keep["coal"] += 2
			self.resourse_to_keep["iron"] += 3
		if _type == "clothing":
			self.resource_priority["cotton"] += 0.5
			self.resource_priority["dyes"] += 0.5
			self.resourse_to_keep["cotton"] += 3
			self.resourse_to_keep["dyes"] += 0.5
		if _type == "paper":
			self.resource_priority["wood"] += 0.5
			self.resourse_to_keep["wood"] += 4
		if _type == "furniture":
			self.resource_priority["wood"] += 0.3
			self.resource_priority["cotton"] += 0.2
			self.resourse_to_keep["wood"] += 3
			self.resourse_to_keep["cotton"] += 2
		if _type == "chemicals":
			self.resource_priority["coal"] += 0.5
			self.resourse_to_keep["coal"] += 3.5
		if _type == "gear":
			self.resource_priority["rubber"] += 1
			self.resource_priority["iron"] +=  0.15
		if _type == "tank" or _type == "fighter":
			self.resource_priority["oil"] += 0.5
			self.resource_priority["iron"] += 0.25
		if _type == "auto":
			self.resource_priority["oil"] += 0.4
			self.resource_priority["rubber"] += 0.4
			self.resource_priority["iron"] += 0.3

		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories[_type] += 1
		#globe.factories[_type] += 1
		self.build_factory_priority[_type] -= 0.2
		self.stability -= 0.33
		if self.stability <  -3.0:
			self.stability = -3.0
		self.new_development -= 1

		print("%s Factory Completed ________________________________________________________" % (_type))

	def ai_develop_province(self, _type):
		print("Develop Province")
		if _type == "shipyard":
			self.shipyard += 1
			self.goods["parts"] -= 1.0
			self.resources["wood"] -= 1.0
			self.AP -= 1
			self.new_development -= 1
			self.number_developments += 1
			print("Developed shipyard to %s" % (self.shipyard))
			return
		for p, province in self.provinces.items():
			if province.resource == _type:
				#print("consider - res: %s, dev %s " % (province.resource, province.development_level))
				if self.check_if_prov_can_be_dev(p) == True:
					#print("Can a province be developed?")
					if _type == "iron":
						self.build_factory_priority["parts"] += 0.2
						self.build_factory_priority["cannons"] += 0.2
					if _type == "coal":
						self.build_factory_priority["parts"] += 0.1
						self.build_factory_priority["cannons"] += 0.1
						self.build_factory_priority["chemicals"] += 0.3
					if _type == "wood":
						self.build_factory_priority["paper"] += 0.3
						self.build_factory_priority["furniture"] += 0.2
					if _type == "cotton":
						self.build_factory_priority["clothing"] += 0.25
						self.build_factory_priority["furniture"] += 0.1
					if _type == "dyes":
						self.build_factory_priority["clothing"] += 0.1

					self.goods["parts"] -= 1.0
					self.resources["wood"] -= 1.0
					if self.sprawl == True:
						self.goods["parts"] -= 0.5
						self.resources["wood"] -= 0.5
					self.AP -= 1
					self.new_development -= 1
					self.provinces[p].development_level += 1
					self.resource_priority["coal"] += 0.25
					self.number_developments += 1
					print("Developed %s province ____________________________" % (_type))
					return

	def ai_improve_fortifications(self):
		self.AP -= 1
		self.goods["cannons"] -= 1
		self.fortification += 0.1
		print("Fortification improved____________________________________________")

	def ai_build_steam_ship_yard(self):
		self.goods["parts"] -= 1
		self.resources["iron"] -= 1
		self.resources["wood"] -= 1
		self.AP -1
		self.new_development -=1
		self.steam_ship_yard = True
		print("steam_ship_yard completed!____________________________________________________")

	def build_army(self, market):
		if self.proPOP > 4 and self.freePOP < 0.3:
			self.proPOP -= 1
			self.freePOP += 1
		num_units = self.num_army_units()
		if num_units > self.POP * self.personality["Army"]:
			return
		if self.AP < 1 or self.goods["cannons"] < 2 or self.can_train < 1:
			return
		tries = 0
		while self.goods["cannons"] > 2 and self.freePOP > 0.2 and self.can_train >= 1:
			priorities = sorted(self.military_priority, key=self.military_priority.get, reverse = True)
			for p in priorities:
				if p == "infantry" and self.military["infantry"] < self.POP/3:
					self.ai_build_infantry()
				elif p == "cavalry" and "mobile_warfare" not in self.technologies and self.goods["tank"] == 0 and self.military["cavalry"] <= self.POP/4:
					self.ai_build_cavalry()
				elif p == "artillery" and self.military["artillery"] <= self.POP/4:
					if self.goods["cannons"] >= 3:
						self.ai_build_artillery()
				elif p == "tank": 
					if self.goods["tank"] >= 1 and self.military["tank"] <= self.POP/4:
						self.ai_build_tank()
					else:
						if market.market["tank"] > 2 and self.resources["gold"] > market.buy_price("tank") * 2:
							self.ai_buy("tank", 1, market)
							self.ai_build_tank()
				elif p == "fighter" and self.military["fighter"] <= self.POP/4:
					if self.goods["fighter"] >= 1:
						self.ai_build_fighter()
					else:
						if market.market["fighter"] > 2 and self.resources["gold"] > market.buy_price("fighter") * 2:
							self.ai_buy("fighter", 1, market)
							self.ai_build_fighter()
				tries += 1
			if tries > 16:
				return

	def ai_build_tank(self):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.can_train -= 1
		self.military["tank"] += 1.0
		self.goods["tank"] -= 1
		self.number_units += 1
		self.military_priority["tank"] -= 0.3
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
			#print(self.military_priority[k])
		print("Tank build_____________________________________________________________")

	def ai_build_fighter(self):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.can_train -= 1
		self.military["fighter"] += 1.0
		self.goods["fighter"] -= 1
		self.number_units += 1
		self.military_priority["fighter"] -= 0.33
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
			#print(self.military_priority[k])
		print("Fighter build_____________________________________________________________")


	def ai_build_infantry(self):
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.can_train -= 1
			self.goods["cannons"] -= 1.0
			self.military["infantry"] += 1.0
			self.number_units += 1
			self.military_priority["infantry"] -= 0.45
			for k in self.military_priority.keys():
				self.military_priority[k] += 0.1
				#print(self.military_priority[k])
			print("Infantry build_____________________________________________________________")

	def ai_build_cavalry(self):
		self.resources["food"] -= 1.0
		self.can_train -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.goods["clothing"] -= 0.1
		self.number_units += 1
		self.military["cavalry"] += 1.0
		self.military_priority["cavalry"] -= 0.5
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1

		print("Cavalry build_________________________________________________________________")

	def ai_build_artillery(self):
		self.goods["cannons"] -= 2.0
		self.can_train -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		self.military["artillery"] += 1.0
		self.military_priority["artillery"] -= 0.4
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("Artillary built_______________________________________________________________")

	def ai_build_irregulars(self):
		self.goods["cannons"] -= 0.5
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		self.military["irregulars"] += 1.0
		self.military_priority["irregulars"] -= 0.7
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("Irregulars build _________________________________________________________________")

	def check_if_prov_can_be_dev(self, prov):
		print("Check if %s can be developed..." % (prov))
		if self.provinces[prov].development_level >= 2:
			return
		max_dev = 0
		if(self.provinces[prov].resource == "food"):
			max_dev = 0
			if("steel_plows" in self.technologies):
			#	print("Is steel plows working?")
				max_dev = 1
			if("mechanical_reaper" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "iron" or self.provinces[prov].resource == "coal"):
			max_dev = 0
			if("square_timbering" in self.technologies):
				max_dev = 1
			if("dynamite" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "cotton"):
			max_dev = 0
			if("cotton_gin" in self.technologies):
				max_dev = 1
			if("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "wood"):
			max_dev = 0
			if("saw_mill" in self.technologies):
				max_dev = 1
			if("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "spice"):
			max_dev = 0
			if("steel_plows" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "gold"):
			max_dev = 0
			if("dynamite" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "dyes"):
			max_dev = 0
			if("compound_steam_engine" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "oil"):
			max_dev = 0
			if("oil_drilling" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "rubber"):
			max_dev = 0
			if("electricity" in self.technologies):
				max_dev = 1
		if self.provinces[prov].development_level >= max_dev:
			return False
		else:
			return True

	def use_chemicals(self):
		if self.goods["chemicals"] > 4:
			if self.resources["dyes"] < 3:
				self.goods["chemicals"] -= 1
				self.resources["dyes"] += 1
				print("Turned Chemicals to dyes")
		if self.resources["food"] < 8:
				count = 0
				for p, prov in self.provinces.items():
					if prov.resource == "food":
						count += 1
				while count > 0 and self.goods["chemicals"] > 0:
					self.resources["food"] += 0.5
					self.goods["chemicals"] -= 1
					count -= 1
					print("Turn chemicals to food")
		if "electricity" in self.technologies and self.resources["rubber"] < 2 and self.goods["chemicals"] >= 5:
			self.resources["rubber"] += 1
			self.goods["chemicals"] -= 5
		if "auto" in self.technologies and self.resources["oil"] < 2 and self.goods["chemicals"] >= 5:
			self.resources["oil"] += 1
			self.goods["chemicals"] -= 5


	def use_culture(self, players):
		if self.culture_points < 1:
			return
		if self.stability <= 0.0:
			self.culture_points -= 1
			self.stability += 0.5
			print("Increased Stability_______________________________________________")
			return
		other = 0
		for p in self.provinces.values():
			if p.culture != self.culture:
				other += 1
		if other >= 1:
			for p in self.provinces.values():
				if p.culture != self.culture:
					self.culture_points -= 1
					chance = uniform(0, 1)
					if p.type == "uncivilized":
						if chance < 0.4:
							self.accepted_cultures.add(p.culture)
							print("Assimlated Culture")
					if p.type == "old":
						if chance < 0.2:
							self.accepted_cultures.add(p.culture)
							print("Assimlated Culture") 
					if p.type == "civilized":
						if chance < 0.11:
							self.accepted_cultures.add(p.culture)
							print("Assimlated Culture")
					return
		if self.stability < 1.0:
			self.culture_points -= 1
			self.stability += 0.5
			print("Increased Stability______________________________________________________________")
			return
	#	if self.culture >= 3:
	#		for p in players.values():
	#			if p.midPOP["artists"]["number"] < self.midPOP["artists"]["number"] and p.type == "major":
	#				if p.numMidPOP >= 0.75:
	#					for m in p.midPOP:
	#						if p.midPOP[m]["number"] >= 0.25:
	#							p.midPOP[m]["number"] -= 0.25
	#							p.numMidPOP -= 0.25
	#							p.POP -= 0.25
	#							p.resources["gold"] -= 5
	#							self.midPOP[m]["number"] += 0.25
	#							self.numMidPOP += 0.25
	#							self.POP += 0.25
	#							self.resources["gold"] += 5
	#							self.culture -= 3
	#							print("%s has stolen a %s POP from %s !" % (self.name, m, p.name))
	#							return
		if self.resources["gold"] < 40:
			for p in players.values():
				if p.type == "major":
					p.resources["gold"] -= 1
					self.resources["gold"] += 1
			print("Cultural Exports")
			return
		if self.stability < 2.5:
			self.culture_points -= 1
			self.stability += 0.5
			if self.stability > 3.0:
				self.stability = 3.0
			print("Increased Stability")

	def check_obsolete(self):
		if self.military["iron_clad"] >= 2 or self.military["battle_ship"] > 0:
			if self.military["frigates"] > 0:
				self.resources["iron"] += self.military["frigates"]
				self.milPOP -= self.military["frigates"] * 0.2
				self.freePOP += self.military["frigates"] * 0.2
				self.number_units -= self.military["frigates"]
				self.military["frigates"] = 0
		if self.military["tank"] >= 2:
			if self.military["cavalry"] > 0:
				self.resources["iron"] += self.military["cavalry"]
				self.milPOP -= self.military["cavalry"] * 0.2
				self.freePOP += self.military["cavalry"] * 0.2
				self.number_units -= self.military["cavalry"]
				self.military["cavalry"] = 0
		if self.military["battle_ship"] >= 3:
			if self.military["iron_clad"] > 0:
				self.resources["iron"] += self.military["iron_clad"] * 3
				self.milPOP -= self.military["iron_clad"] * 0.2
				self.freePOP += self.military["iron_clad"] * 0.2
				self.number_units -= self.military["iron_clad"]
				self.military["iron_clad"] = 0

		if "mobile_warfare" in self.technologies and self.military["cavalry"] >= 1:
			self.resources["iron"] += 1
			self.milPOP -= 0.2
			self.freePOP += 0.2
			self.number_units -= 1
			self.military["cavalry"] -= 1

		if "fight" in self.technologies and self.military["cavalry"] >= 1:
			self.resources["iron"] += 1
			self.milPOP -= 0.2
			self.freePOP += 0.2
			self.number_units -= 1
			self.military["cavalry"] -= 1

		if "oil_powered_ships" in self.technologies and self.military["iron_clad"] >= 3:
			self.resources["iron"] += 3
			self.milPOP -= 0.2
			self.freePOP += 0.2
			self.number_units -= 1
			self.military["iron_clad"] -= 1

		if self.military["irregulars"] > 0:
			if self.military["infantry"] >= 3 or self.military["cavalry"] >= 3:
				self.military["irregulars"] -= 1
				self.milPOP -= 0.2
				self.freePOP -= 0.2
				self.number_units -= 1