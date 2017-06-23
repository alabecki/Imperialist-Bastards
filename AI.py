
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
	"parts": {"iron": 0.6, "coal": 0.3},
	"cannons": {"iron": 0.6, "coal": 0.3},
	"paper": {"wood": 0.9},
	"clothing": {"cotton": 0.75, "dyes": 0.15},
	"furniture": {"wood": 0.6, "cotton": 0.3},
	"chemicals": {"coal": 0.6}
			}


class AI(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(AI, self).__init__(_name, _type, number, *args, **kwargs)

		self.personality = {
			"militant": 0.0,
			"colonizers": 0.0,
			"industry": 0.0,
			"science_culture": 0.0
		}


		self.mid_class_priority = {
			"researchers": 1.1,
			"officers": 0.9,
			"bureaucrats": 0.9,
			"managers": 0.9,
			"artists": 1.0
		}

		self.pro_need = {
			"food": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"coal": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"spice":{"produces": 0.0, "needs": 0.0, "forecast": 0.0}
		}

		self.build_priority = {
			"frigates": 1,
			"iron_clad": 1,
			"parts_factory": 1,
			"clothing_factory": 0,
			"furniture_factory": 0,
			"paper_factory": 0,
			"cannon_factory": 0.5,
			"chemical_factory": 0,
			"improve_food_provice": 0.5,
			"improve_iron_province": 1,
			"improve_coal_province": 0,
			"improve_wood_province": 0,
			"improve_cotton_province": 0,
			"improve_gold_province": 1,
			"improve_spice_province": 1,
			"improve_dyes_province": 0,
			"improve_fortifications": 1,
			"build_steam_ship_yard": 1,
			"build_infantry": 1,
			"build_cavalry": 1,
			"build_artillery": 1,
			"build_irregulars": 1
		}

		self.objective = 0

		self.build_factory_priority = {
			"parts": 1.0,
			"clothing": 1.0,
			"furniture": 0.9,
			"paper": 0.75,
			"cannons": 1.0,
			"chemicals": 0.2
		}
		#cannon
		self.improve_province_priority = {
			"food": 1.2,
			"iron": 1.0,
			"coal": 0,
			"wood": 0.3,
			"cotton": 0.3,
			"gold": 1,
			"spice": 1,
			"dyes": 0,
			"improve_fortifications": 0.6,
			"build_steam_ship_yard": 1.0,
		}

		self.military_priority = {
			"infantry": 1,
			"cavalry": 1,
			"artillery": 1,
			"irregulars": 0.0,
			"iron_clad": 0.1,
			"frigates": 0.2
		}

		self.technology_priority = {
			"pre_industry_1": 6,
			"pre_industry_2": 6,
			"professional_armies": 5,
			"high_pressure_steam_engine": 8,
			"square_timbering": 4,
			"cotton_gin": 4,
			"steel_plows": 4,
			"saw_mill": 4,
			"cement": 2,
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
			"radio": 2,
			"mechanical_reaper": 2,
		}

		self.resource_priority = {
			"food":	1.2,
			"iron": 1.2,
			"coal": 0.3,
			"cotton": 0.75,
			"wood": 0.5,
			"spice": 2,
			"dyes": 0.75,
			"gold": 1.5
		}

		self.resourse_to_keep = {
			"food":	3,
			"iron": 3,
			"coal": 3,
			"cotton": 2,
			"wood": 2,
			"spice": 2,
			"dyes": 1.0,
			"gold": 2.0
		}

		self.resource_base = {
			"food": 0,
			"iron": 0,
			"coal": 0,
			"cotton": 0,
			"wood": 0,
			"dyes": 0,
			"spice": 0,
			"gold": 0
		}

	def ai_increase_pop(self, market):
		if self.freePOP > 2 or self.proPOP > 5:
			return
		if self.POP_increased >= 2:
			return
		if self.goods["clothing"] < 1 and market.market["clothing"] > 1 and self.resources["gold"] >= market.buy_price("clothing") * 1.5:
			self.ai_buy("clothing", 1, market)
		if self.goods["furniture"] < 1 and market.market["furniture"] > 1 and self.resources["gold"] > market.buy_price("furniture") * 1.5:
			self.ai_buy("furniture", 1, market)
		if self.resources["food"] < 2 and market.market["food"] > 2 and self.resources["gold"] >= market.buy_price("food") * 2.5:
			self.ai_buy("food", 2, market)
		if self.resources["food"] >= 2 and self.goods["clothing"] >= 1 and self.goods["furniture"] >= 1 and self.POP <= ((len(self.provinces) * 2) + self.numMidPOP):
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
					self.goods["furniture"] -= 1.0
					self.POP_increased += 1
					print("POP increase ______________________________________________")

			else:
				self.POP += 1.0
				self.freePOP += 1.0
				self.numLowerPOP += 1
				self.resources["food"] -= 1.0
				self.goods["clothing"] -= 1.0
				self.goods["furniture"] -= 1.0
				self.POP_increased += 1
				print("POP increase ______________________________________________")

	def try_middle_class(self, market):
		if self.midGrowth == False:
			return
		if self.goods["paper"] >= 2 and self.goods["furniture"] >= 1 and self.goods["clothing"] >=1 and self.resources["spice"] >= 1.0 and self.POP < 4:
			if self.freePOP >= 0.5 or self.proPOP >= 2:
				return True
		elif self.freePOP < 0.5 and self.proPOP < 2:
			return False
		flag = True
		if self.goods["paper"] < 2:
			decision = self.ai_decide_on_good("paper", market)
			if decision != "buy":
				flag = False
		elif self.goods["furniture"] < 1:
			decision = self.ai_decide_on_good("furniture", market)
			if decision != "buy":
				flag = False
		elif self.goods["clothing"] < 1:
			decision = self.ai_decide_on_good("clothing", market)
			if decision != "buy":
				flag = False
		elif self.resources["spice"] < 1:
			get = self.ai_buy("spice", 1, market)
			if get == "fail":
				flag = False
		return flag


	def try_middle_class2(self, market):
		stuff = sorted(market.market, key=market.market.get, reverse = True)
		for s in stuff:
			if s =="paper" and self.goods["paper"] < 2 and market.market["paper"] >= 3 and market.buy_price("paper") <= self.resources["gold"] * 1.75:
				self.ai_buy("paper", 2, market)
			if s == "furniture" and self.goods["furniture"] <= 1 and market.market["furniture"] >= 1 and market.buy_price("furniture") <= self.resources["gold"] * 1.75:
				self.ai_buy("furniture", 1, market)
			if s == "clothing" and self.goods["clothing"] <= 1 and market.market["clothing"] >= 1 and market.buy_price("clothing") <= self.resources["gold"] * 1.75:
				self.ai_buy("furniture", 1, market)
			if s == "spice" and self.resources["spice"] <= 1 and market.market["spice"] >= 1 and market.buy_price("spice") <= self.resources["gold"] * 1.75:
				self.ai_buy("spice", 1, market)


	def ai_increase_middle_class(self, market):
		if self.midGrowth == False:
			print("Cannot incrase midPOP becuase did not pay all food last turnS")
			return
		if self.freePOP < 0.25 and self.proPOP < 2:
			print("ProPOP: %s " % (self.proPOP))
			print("Cannot increase middle class at this time (no pop)")
			return
		if self.goods["paper"] < 1 or self.goods["furniture"] < 1 or self.resources["spice"] < 1.0 or self.goods["clothing"] < 1.0:
			self.try_middle_class2(market)
			if self.goods["paper"] < 1 or self.goods["furniture"] < 1 or self.resources["spice"] < 1.0 or self.goods["clothing"] < 1.0 or self.POP < 4:
				print("Cannot increase middle class at this time (tried)")
				return
		if self.freePOP < 0.25:
			self.proPOP -= 1
			self.freePOP +1
		_type = sorted(self.mid_class_priority, key=self.mid_class_priority.get, reverse = True)
		self.resources["spice"] -= 1.0
		self.goods["furniture"] -= 1.0
		self.goods["paper"] -= 2.0
		self.goods["clothing"] -= 1.0
		self.numLowerPOP -= 0.25
		self.numMidPOP += 0.25
		self.midPOP[_type[0]]["number"] += 0.25
		self.freePOP -= 0.25
		self.mid_class_priority[_type[0]] -= 0.1
		self.new_development += 1.0
		print("New middle class pop: %s ________________________" % (_type[0]))


	def early_game(self, turn, market):
			if "clothing" not in self.factories and self.goods["clothing"] <= 2:
				if self.resources["cotton"] >= 1 and market.market["clothing"] <= 3 :
					self.ai_craftman_production("clothing")
			if "paper" not in self.factories and self.goods["paper"] <= 1 and self.AP >= 1:
				if self.resources["wood"] >= 2 and market.market["paper"] <= 3:
					self.ai_craftman_production("paper")
			if "furniture" not in self.factories and self.goods["furniture"] < 1 and self.AP >= 1:
				if self.resources["wood"] >= 1 and market.market["furniture"] <= 3:
					self.ai_craftman_production("furniture")

	def num_army_units(self):
		res = 0
		res += (self.military["irregulars"] + self.military["infantry"] + self.military["cavalry"] + self.military["artillery"])
		return res

	def AI_set_objective(self, turn, market):
		self.objective = 0
		print("Set AI Objective:")
		if self.military["frigates"] < 2 and "professional_armies" in self.technologies and "iron_clad" not in self.technologies:
			self.objective = 1
			return
		army = self.num_army_units()
		print("Army: = %s, Num Low Pop: %s" % (army, self.numLowerPOP))
		if army < self.numLowerPOP/3 and (self.freePOP > 0.2 or self.proPOP >= 2):
			self.objective = 3
			return
		if self.new_development >= 1:
			opt = self.ai_improve_province_options()
			print("Improve Prov Options")
			for o in opt:
				print(o)
			if len(opt) > 1 and "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1 :
				print("Able to develop provice or build factory")
				if len(self.factories) >= self.number_developments and len(self.factories) >= 1:
					self.objective = 4
				else:
					pick = uniform(0, 1)
					if pick >=  0.3:
						self.objective = 2
						return
					else:
						self.objective = 4
						return
			if len(opt) > 1:
				self.objective = 4
				return
			if "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1:
				self.objective = 2
				return
		if self.military["frigates"] < 2 and "iron_clad" not in self.technologies:
			self.objective = 1
			return
		if self.try_middle_class(market) == True:
			self.try_middle_class(market)
			self.ai_increase_middle_class(market)
			self.objecive = 0
			return
		if self.military["frigates"] < 4 and self.num_colonies >= 1:
			if "iron_clad" not in self.technologies or self.steam_ship_yard == False:
				self.objective = 1
				return
			else:
				self.objective = 5
		if self.number_units < self.numLowerPOP:
			self.objective = 3
			return
		if "iron_clad" in self.technologies and self.military["iron_clad"] < self.num_colonies:
			self.objective = 3
		else:
			self.try_middle_class(market)
			self.ai_increase_middle_class(market)
			self.objective = 0
			return


	def attempt_objective(self, market):
		print("Attempting objective: - %s" % (self.objective))
		print("Has %s New Development Points \n" % (self.new_development))
		print("Has %s AP \n" % (str(self.AP)))
		if self.objective == 0:
			return
		if self.AP >= 1:
			if self.objective == 1:
				print("Wants to build frigate")
				flag = True
				if self.goods["cannons"] < 1.5:
					print("Wants cannons")
					decision = self.ai_decide_on_good("cannons", market)
					if decision != "buy":
						flag = False
					self.ai_obtain_good("cannons", decision, market)
				if self.resources["wood"] < 1:
					get = self.ai_buy("wood", 1, market)
					if get == "fail":
						flag = False
				if self.resources["cotton"] < 1:
					get = self.ai_buy("cotton", 1, market)
					if get == "fail":
						flag = False
				if self.freePOP < 0.2 and self.proPOP < 2:
					flag = False
				if self.freePOP < 0.2 and self.proPOP >= 2:
					self.proPOP -= 1
					self.freePOP += 1
				if flag == False:
						print("Cannot produce this this round")
						return
				else:
					self.ai_build_frigates()
					return
			if self.objective == 2:
				print("Wants to build factory")
				flag = True
				if self.goods["parts"] < 1:
					print("Wants machine parts")
					decision = self.ai_decide_on_good("parts", market)
					if decision != "buy":
						flag = False
					self.ai_obtain_good("parts", decision, market)
					print("Flag: %s" % (flag))
				if self.resources["iron"] < 1:
					print("Wants to get iron")
					get = self.ai_buy("iron", 1, market)
					if get == "fail":
						flag = False
						print("Flag: %s" % (flag))
				if flag == False:
					return
				else:
					print("Made it through Factory flags...")
					#priorities = (sorted(self.build_factory_priority.keys(), key=lambda x:x[1], reverse=True ))
					priorities = sorted(self.build_factory_priority, key=self.build_factory_priority.get, reverse = True)
					print("Factory priorities:")
					for p in priorities:
						print(p)

					options = self.ai_factory_options()
					print("Options:")
					for o in options:
						print(o)
					for p in priorities:
						if p in options:
							self.ai_build_build_factory(p, market)
							return
			if self.objective == 4:
				print("Wants to improve province")
				flag = True
				if self.goods["parts"] < 1:
					print("Wants parts")
					decision = self.ai_decide_on_good("parts", market)
					if decision != "buy":
						flag = False
					self.ai_obtain_good("parts", decision, market)
				if self.resources["iron"] < 0.5:
					print("Wants iron")
					get = self.ai_buy("iron", 1, market)
					if get == "fail":
						flag = False
				if self.resources["wood"] < 1:
					print("Wants wood")
					get = self.ai_buy("wood", 1, market)
					if get == "fail":
						flag = False
				if flag == False:
					return
				else:
					print("Past Improve Province Flags")
					#priorities = (sorted(self.improve_province_priority.items(), key=lambda x:x[1], reverse=True ))
					print("priorities")
					priorities = sorted(self.improve_province_priority, key=self.improve_province_priority.get, reverse = True)
					for p in priorities:
						print(p)
					options = self.ai_improve_province_options()
					print("options")
					for o in options:
						print (o)
					for p in priorities:
						if p in options:
							print("Checking for %s province" % (p))
							if p == "improve_fortifications" and self.goods["cannons"] >= 1.5:
								self.ai_improve_fortifications()
								return
							elif p == "food":
								self.ai_develop_province("food")
								return
							if p == "iron":
								self.ai_develop_province("iron")
								return
							if p == "coal":
								self.ai_develop_province("coal")
								return
							if p == "wood":
								self.ai_develop_province("wood")
								return
							if p == "cotton":
								self.ai_develop_province("cotton")
								return
							if p == "gold":
								self.ai_develop_province("gold")
								return
							if p == "spice":
								self.ai_develop_province("spice")
								return
							if p == "dyes":
								self.ai_develop_province("dyes")
								return
							if p == "build_steam_ship_yard":
								self.ai_build_steam_ship_yard()
								return
			if self.objective == 3:
				print("Wants to build army")
				flag = True
				if self.goods["cannons"] < 2:
					print("Wants to get cannons")
					decision = self.ai_decide_on_good("cannons", market)
					if decision != "buy":
						print("Cannot acquire cannons this turn")
						flag == False
						self.ai_obtain_good("cannons", decision, market)
						return
					self.ai_obtain_good("cannons", decision, market)
					if flag  == False:
						print("cannot acquire cannons")
						return
				if self.freePOP < 0.2 and self.proPOP < 2:
					print("No people to raise army")
					return
				if self.freePOP < 0.2:
					self.proPOP -= 1
					self.freePOP += 1
				#priorities = (sorted(self.military_priority(), key=lambda x:x[1], reverse=True ))
				if "professional_armies" not in self.technologies:
					self.ai_build_irregulars()
				else:
					print("About to build army:...")
					priorities = sorted(self.military_priority, key=self.military_priority.get, reverse = True)
					for p in priorities:
						if p == "infantry":
							self.ai_build_infantry()
							return
						if p == "cavalry" and self.resources["food"] > 1:
							self.ai_build_cavalry()
							return
						if p == "artillery" and self.goods["cannons"] > 2:
							self.ai_build_artillery()
							return
						if p == "irregulars":
							self.ai_build_irregulars()
							return
						if p == "iron_clad":
							if "iron_clad" in self.technologies and self.goods["parts"] >= 1 and self.resources["iron"] >= 1 and self.steam_ship_yard == True:
								self.ai_build_ironclad()
								return
						#if p == "frigates":
						#	if(self.resources["wood"] >= 1 and self.resources["cotton"] >= 1 and self.goods["cannons"] >= 1 and "iron_clad" not in self.technologies and self.freePOP >= 0.15):
						#		self.ai_build_frigates()
						#		return
			if self.objective == 5:
				flag = True
				if self.goods["cannons"] < 1.5:
					print("Wants cannons")
					decision = self.ai_decide_on_good("cannons", market)
					if decision != "buy":
						flag = False
					self.ai_obtain_good("cannons", decision, market)
				if self.resources["iron"] < 1:
					get = self.ai_buy("wood", 1, market)
					if get == "fail":
						flag = False
				if self.goods["parts"] < 1:
					decision = self.ai_decide_on_good("parts", market)
					if decision != "buy":
						flag = False
					self.ai_obtain_good("parts", decision, market)
				if self.freePOP < 0.2 and self.proPOP < 2:
					flag = False
				if self.freePOP < 0.2 and self.proPOP >= 2:
					self.proPOP -= 1
					self.freePOP += 1
				if flag == False:
						print("Cannot produce this this round")
						return


	def ai_obtain_good(self, _type, decision, market):
		if decision == "manufacture_prepare":
			for i in manufacture[_type]:
				material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
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
			get = self.ai_buy(craft[_type], 1, market)
			if get == "sucess":
				self.ai_craftman_production(_type)


	def assign_priorities_to_provs(self):
		for p, prov in self.provinces.items():
			kind = prov.resource
			prov.AI_priority = self.resource_priority[kind] * prov.quality
		sorted_provinces = sorted(self.provinces.values(), key = lambda x: (x.AI_priority), reverse = True)
		#sorted_priorities = sorted(self.provinces, key=self.provinces.get, reverse = True)
		#print("Province priorities:")
		#for k, v in self.resource_priority.items():
		#	print(k, v)
		return sorted_provinces

	def update_priorities(self, market):
		for k, v in self.resources.items():
			if k == "gold":
				continue
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




	def AI_reset_POP(self):
		for p, prov in self.provinces.items():
			if prov.worked == True:
				prov.worked = False
				self.freePOP += 1
		while self.proPOP >= 1:
			self.proPOP -= 1
			self.freePOP += 1
		self.freePOP = self.numLowerPOP - self.milPOP
		self.proPOP = 0


	def AI_assign_POP(self):
		#priorities = (sorted(self.resource_priority.items(), key=lambda x:x[1], reverse=True )
		priorities = self.assign_priorities_to_provs()
		desired_producers = int(self.POP / 4)
		#min_producers = int(self.freePOP/3.25)
		#min_producers = 2
		for i in range(desired_producers):
			if self.freePOP >= 2:
				self.proPOP += 1
				self.freePOP -=1
		count = 0
		while self.freePOP >= 1 and count < len(self.provinces):
			for p in priorities:
				temp = p.name
				if temp in self.provinces.keys() and self.provinces[temp].worked == False:
					self.provinces[temp].worked = True
					self.freePOP -= 1
				if self.freePOP < 1:
					break
				count += 1
		while self.freePOP >= 1.5:
			self.proPOP += 1
			self.freePOP -=1


	def AI_sell_surplus(self, market):
		for r, resource in self.resources.items():
			if r == "gold":
				continue
			if resource > self.resourse_to_keep[r]:
				amount = int(resource - self.resourse_to_keep[r])
				if amount >= 1 and market.market[r] < 10:
					if amount > 4:
						amount = 4
					self.ai_sell(r, amount, market)
				if amount >= 1 and market.market[r] < 22 and self.resources["gold"] <= 20:
					if amount > 4:
						amount = 4
					self.ai_sell(r, amount, market)
		if self.goods["parts"] > 3 and market.market["parts"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["parts"] - 3)
			if amount >= 1:
				if amount > 4:
					amount = 4
				self.ai_sell("parts", amount, market)
		if self.goods["parts"] > 3 and market.market["parts"] < 10:
			amount = int(self.goods["parts"] - 3)
			if amount >= 1:
				if amount > 3:
					amount = 3
				self.ai_sell("parts", amount, market)

		if self.goods["clothing"] > 3 and market.market["clothing"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["clothing"] - 3)
			if amount >= 1:
				if amount > 4:
					amount = 4
				self.ai_sell("clothing", amount, market)

		if self.goods["clothing"] > 3 and market.market["clothing"] < 10:
			amount = int(self.goods["clothing"] - 3)
			if amount >= 1:
				if amount > 3:
					amount = 3
				self.ai_sell("clothing", amount, market)

		if self.goods["furniture"] > 3 and market.market["furniture"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["furniture"] - 3)
			if amount >= 1:
				if amount > 4:
					amount = 4
				self.ai_sell("furniture", amount, market)

		if self.goods["furniture"] > 3 and market.market["furniture"] < 10:
			amount = int(self.goods["furniture"] - 3)
			if amount >= 1:
				if amount > 3:
					amount = 3
				self.ai_sell("furniture", amount, market)

		if self.goods["paper"] > 3 and market.market["paper"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["paper"] - 3)
			if amount >= 1:
				if amount > 4:
					amount = 4
				self.ai_sell("paper", amount, market)

		if self.goods["paper"] > 3 and market.market["paper"] < 10:
			amount = int(self.goods["paper"] - 3)
			if amount >= 1:
				if amount > 3:
					amount = 3
				self.ai_sell("paper", amount, market)


		if self.goods["cannons"] > 5 and market.market["cannons"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["cannons"] - 5)
			if amount >= 1:
				if amount > 3:
					amount = 3
				self.ai_sell("cannons", amount, market)

		if self.goods["cannons"] > 4 and market.market["cannons"] < 10:
			amount = int(self.goods["cannons"] - 3)
			if amount >= 1:
				if amount > 2:
					amount = 2
				self.ai_sell("cannons", amount, market)


		if self.goods["chemicals"] > 4 and market.market["chemicals"] < 20 and self.resources["gold"] <= 20:
			amount = int(self.goods["chemicals"] - 4)
			if amount >= 1:
				if amount > 4:
					amount = 4
				self.ai_sell("chemicals", amount, market)

		if self.goods["chemicals"] > 4 and market.market["chemicals"] < 10:
			amount = int(self.goods["chemicals"] - 3)
			if amount >= 1:
				if amount > 2:
					amount = 2
				self.ai_sell("chemicals", amount, market)

	def view_AI_inventory(self):
		print("POP: %s, LowPop: %s, MidPop: %s" % (self.POP, self.numLowerPOP, self.numMidPOP))
		print("freePOP: %s, proPOP: %s " % (self.freePOP, self.proPOP))
		print("Stability: %s, Diplo: %s, Reputation: %s " % (self.stability, self.diplo_action, self.reputation))
		print("Colonize: %s, Num Colonies: %s" % (self.colonization, self.num_colonies))
		print("%s Inventory \n" % (self.name))
		for r, resource in self.resources.items():
			print (r, resource, end= ' ')
		for g, good in self.goods.items():
			print(g, good, end=' ')
		for k, v in self.pro_need.items():
			print(k, v)
		print(" \n number_developments: %s \n" % (self.number_developments))
		for f in self.factories:
			print (f, end=" | ")
		for k, v in self.military.items():
			print(k, v)

	def calculate_resource_production(self):
		stab_rounds = round(self.stability * 2) / 2
		for k, p in self.provinces.items():
			if k == "food" or k == "coal" or k == "spice":
				if p.worked == True:
					if p.powered == True and p.development_level > 0:
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain
					else:
						gain = stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource] += gain
				self.pro_need[p.resource]["produces"] += gain

	def calculate_resource_need(self):
		self.pro_need["food"]["needs"] = ((self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1) + 1
		self.resourse_to_keep["food"] = self.pro_need["food"]["needs"] * 1.25
		#self.pro_need["spice"]["needs"] = self.numMidPOP * 0.3
		self.pro_need["coal"]["needs"] =  0.3 * self.number_developments


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
		print("Price to buy %s" % (price_to_buy))
		price_to_craft = market.buy_price(craft[_type]) * 1
		print("price to craft %s " % (price_to_craft))
		if market.market[_type] > 3 and self.resources["gold"] >= market.buy_price(_type):
			return "buy"
		material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
		price_to_man = 0
		for i in manufacture[_type]:
			price_to_man += market.buy_price(i) * int(manufacture[_type][i] * material_mod)
		if _type in self.factories:
			cap = self.calculate_how_much_can_produce(_type)
			if cap >= 4:
				print("Make w factory")
				return "manufacture_ready"
			else:
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
		elif (price_to_buy < price_to_craft * 1.7 and market.market[_type] >= 1) and self.resources["gold"] >= market.buy_price(_type):
			print("Decide to buy good")
			return "buy"
		elif self.resources[craft[_type]] >= 1.0:
			print("Decide to craft good")
			return "craft_ready"
		elif market.market[craft[_type]] >= 2 and self.resources["gold"] >= market.buy_price(craft[_type]):
			print("Buy materail then craft")
			return "craft_prepare"
		elif market.market[_type] >= 1 and self.resources["gold"] >= market.buy_price(_type):
			print("Decide to buy good")
			return "buy"
		else:
			return "fail"

	def fulfill_needs(self, market):
		for k, v in self.pro_need.items():
			if v["forecast"] < 0.0:
				amount = math.ceil(abs(v["forecast"]))
				print("Amount need " + str(amount))
				self.ai_buy(k, amount, market)
			if self.resources["food"] < 2.5:
				self.ai_buy("food", 1, market)
			if self.resources["food"] < 3 and market.market["food"] > 6 and self.resources["gold"] >= market.buy_price("food") * 2.5:
				self.ai_buy("food", 1, market)
			if self.goods["clothing"] < 1 and market.market["clothing"] > 4 and self.resources["gold"] >= market.buy_price("clothing") * 2:
				self.ai_buy("clothing", 1, market)
			if self.goods["cannons"] <= 2 and market.market["cannons"] > 4 and self.resources["gold"] >= market.buy_price("cannons") * 2:
				self.ai_buy("cannons", 1, market)


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
			self.stability +1
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 3 and self.stability < 1:
			self.resources["spice"] -=2
			self.stability +1
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 4 and self.stability < 2:
			self.resources["spice"] -=2
			self.stability +1
			if self.stability > 3:
				self.stability = 3

	def check_stability(self, market):
		if self.stability < 0 and self.resources["spice"] < 2:
			self.ai_buy("spice", 2, market)
		elif self.stability < 1  and self.resources["spice"] < 2:
			if market.market["spice"] >= 2 and self.resources["gold"] >= market.buy_price("spice") * 4:
				self.ai_buy("spice", 2, market)
		elif self.stability < 2 and self.resources["spice"] < 2:
			if market.market["spice"] >= 4 and self.resources["gold"] >= market.buy_price("spice") * 6:
				self.ai_buy("spice", 2, market)


	def spend_excess_cash(self, market):
		count = 20
		while self.resources["gold"] > 40 and count > 0:
			item = choice(["food", "iron", "cotton", "coal", "dyes", "wood", "spice", "clothing", "parts", "cannons", "paper", "furniture", "chemicals"])
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
		price = market.sell_price(_type)
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
		print(self.stability)
		stab_rounds = round(self.stability * 2) / 2
		print("stab_rounds: %s" % (stab_rounds))
		material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
		material_max = 1000
		for i in manufacture[_type]:
			temp = int(self.resources[i]/(manufacture[_type][i] * material_mod))
			print("man_type_i: %s, material mod: %s self_resource_i %s \n" % (manufacture[_type][i], material_mod, self.resources[i]))
			if temp < material_max:
				material_max = temp
		print("material_max: %s " % (material_max))
		max_amount = self.factory_throughput * stability_map[stab_rounds]
		if(_type == "parts"):
			print("Got to parts...")
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		elif(_type == "cannons"):
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		elif(_type == "paper"):
			if("pulping" in self.technologies):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		elif(_type == "furniture"):
			if("electricity" in self.technologies):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		elif(_type == "clothing"):
			if("power_loom" in self.technologies):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		elif(_type == "chemicals"):
				max_amount = (self.factory_throughput + 3) * stability_map[stab_rounds]
		amount = min([material_max, max_amount])
		#if amount < 2.5:
	#		return False
		for i in manufacture[_type]:
			self.resources[i] -= manufacture[_type][i] * amount * material_mod
		self.goods_produced[_type] += amount
		print("Produced %s %s " % (amount, _type))
		self.AP -= 1
		return True

	def ai_craftman_production(self, _type):
		self.resources[craft[_type]] -= 1.0
		self.goods_produced[_type] += 1.0
		self.AP -= 1
		print("Crafted %s" % (_type))
		print("AP points remaining__: %s \n" % (self.AP))
		return

	def ai_decide_factory_productions(self, market):
		for f in self.factories:
			if self.AP >= 1 and market.market[f] < 14 and self.goods[f] <= 10:
				cap = self.calculate_how_much_can_produce(f)
				if cap < 3.5:
					self.supply_factory_with_material(f, market)
					cap = self.calculate_how_much_can_produce(f)
					if cap < 3:
						return
					else:
						self.ai_factory_production(f)
						return
				else:
					self.ai_factory_production(f)


	def calculate_how_much_can_produce(self, _type):
		cap = 1000
		print("calculate_how_much_can_produce")
		for k, v in manufacture[_type].items():
			print(k, v)
			if self.resources[k] == 0:
				print("%s equals 0" % (k))
				cap = 0
				return cap
			else:
				material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
				temp = self.resources[k]/ (v * material_mod)
				print("%s: %s" % (k, temp))
				print(self.resources[k]/ (v * material_mod))
				if (self.resources[k]/ (v * material_mod)) < cap:
					cap = (self.resources[k]/v * material_mod)
		print("Is able to produce %s \n" % (cap))
		return cap

	def supply_factory_with_material(self, _type, market):
		print("Try to supply %s factory..." % (_type))
		if _type == "parts" or "type" == "cannons":
			if self.resources["iron"] < 4.0:
				amount = ceil(4 - self.resources["iron"])
				amount = min(amount, int(market.market["iron"]))
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
				amount = min(amount, int(market.market[_type]))
				self.ai_buy("coal", amount, market)



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
			self.improve_province_priority["build_steam_ship_yard"] += 0.75
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
			self.build_factory_priority["clothing"] += 0.9
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


	def choose_technology(self):
		available = []
		for k, t in technology_dict.items():
			if(k not in self.technologies and t["requirement"] in self.technologies):
				print(k, t)
				available.append(k)
		options = []
		for t in available:
			if(technology_dict[k]["cost"] <= self.research):
				options.append(t)
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
		if(choice == "muzzle_loaded_arms"):
			self.irregulars["attack"] += 0.1
			self.irregulars["defend"] += 0.06
			self.infantry["attack"] += 0.25
			self.infantry["defend"] += 0.10
			self.cavalry ["attack"] += 0.20
			self.cavalry["defend"] += 0.10
			self.artillery["attack"] += 0.25
			self.artillery["defend"] += 0.10
			self.frigates["attack"] += 0.25
		if(choice == "cement"):
			self.max_fortification += 0.1
			self.improve_province_priority["improve_fortifications"] += 0.25
		if(choice == "breach_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.08
			self.infantry["attack"] += 0.30
			self.infantry["defend"] += 0.15
			self.cavalry["attack"] += 0.25
			self.cavalry["defend"] += 0.12
			self.artillery["attack"] += 0.30
			self.artillery["defend"] += 0.15
			self.frigates["attack"] += 0.30
		if(choice == "machine_guns" ):
			self.irregulars["defend"] += 0.2
			self.infantry["defend"] += 1.0
			self.cavalry["defend"] + 0.15
		if(choice == "indirect_fire"):
			self.artillery["attack"] += 0.1
			self.artillery["defend"] += 0.5
			self.iron_clad["attack"] += 0.25
		if(choice == "electricity"):
			self.production_modifier += 0.1
		if(choice == "medicine"):
			self.POP_growth_mod += 0.10
			self.chemicals.add("medicine")
		if(choice == "synthetic_dyes"):
			self.chemicals.add("dyes")
		if(choice == "fertlizer"):
			self.chemicals.add("fertlizer")
		if(choice == "telegraph"):
			self.production_modifier += 0.1
			self.stability_mod += 0.1
		if(choice == "radio"):
			self.stability_mod += 0.15

	def ai_improve_province_options(self):
		print("Improve province options")
		options = []
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
					print("got to Iron")
					max_dev = 0
					if("square_timbering" in self.technologies):
						max_dev = 1
						print("dev 1")
						print("level: %s " % (prov.development_level))
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
			if self.resources["iron"] >= 1 and self.steam_ship_yard == False and self.new_development > 1.0 and "iron_clad" in self.technologies:
				options.append("build_steam_ship_yard")
			if (self.fortification == 1.0 or (self.fortification == 1.1 and "cement" in self.technologies)) and self.goods["cannons"] >= 1:
				options.append("improve_fortifications")
		return options


	def ai_factory_options(self):
		options = []
		if "high_pressure_steam_engine" in self.technologies and self.new_development >= 1.0:
			if "parts" not in self.factories and self.resource_base["iron"] >= 1:
				options.append("parts")
			if "clothing" not in self.factories and self.resource_base["cotton"] >=1:
				options.append("clothing")
			if "furniture" not in self.factories and self.resource_base["wood"] >=1:
				options.append("furniture")
			if "paper" not in self.factories and self.resource_base["wood"] >= 1:
				options.append("paper")
			if "cannons" not in self.factories and self.resource_base["iron"] >=1 :
				options.append("cannons")
			if "chemicals" not in self.factories and "chemistry" in self.technologies and self.resource_base["coal"] >=1:
				options.append("chemicals")
		return options


	def ai_build_frigates(self):
		self.AP -= 1
		self.goods["cannons"] -= 1.0
		self.resources["cotton"] -= 1.0
		self.resources["wood"] -= 1.0
		self.military["frigates"] += 1.0
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.number_units += 1
		self.military_priority["frigates"] -= 0.5
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("Frigate completed___________________________________________________________________")


	def ai_build_ironclad(self):
		self.AP -= 1
		self.goods["cannons"] -= 1.0
		self.resources["iron"] -= 1.0
		self.goods["parts"]  -= 1.0
		self.military["iron_clad"] += 1
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.number_units += 1
		self.military_priority["iron_clad"]
		self.military_priority["iron_clad"] -= 0.4
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("Ironclad completed___________________________________________________________________________")

	def ai_build_build_factory(self, _type, market):
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
		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories.add(_type)
		market.global_factories[_type] += 1
		self.stability_mod -= 0.05
		self.new_development -= 1

		print("%s Factory Completed ________________________________________________________" % (_type))

	def ai_develop_province(self, _type):
		print("Develop Province")
		for p, province in self.provinces.items():
			if province.resource == _type:
				print("consider - res: %s, dev %s " % (province.resource, province.development_level))
				if self.check_if_prov_can_be_dev(p) == True:
					print("Can a province be developed?")
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

	def build_army(self):
		if self.AP < 1 or self.goods["cannons"] < 2 or self.freePOP < 0.2:
			return
		priorities = sorted(self.military_priority, key=self.military_priority.get, reverse = True)
		for p in priorities:
			if p == "infantry":
				if self.goods["clothing"] >= 0.15 and self.freePOP >= 0.15:
					self.ai_build_infantry()
					return
			if p == "cavalry":
				if self.goods["clothing"] >= 0.1 and self.resources["food"] >= 0.1 and self.freePOP >= 0.15:
					self.ai_build_cavalry()
					return
			if p == "artillery":
				if self.goods["clothing"] >= 0.1 and self.freePOP >= 0.15 and self.goods["cannons"] >= 2:
					self.ai_build_artillery()
					return
	

	def ai_build_infantry(self):
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.goods["cannons"] -= 1.0
			self.military["infantry"] += 1.0
			self.number_units += 1
			self.military_priority["infantry"] -= 0.45
			for k in self.military_priority.keys():
				self.military_priority[k] += 0.1
				print(self.military_priority[k])
			print("Infantry build_____________________________________________________________")

	def ai_build_cavalry(self):
		self.resources["food"] -= 1.0
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
		if(self.provinces[prov].resource == "food"):
			max_dev = 0
			if("steel_plows" in self.technologies):
				print("Is steel plows working?")
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
		if self.provinces[prov].development_level >= max_dev:
			return False
		else:
			return True

	def use_chemicals(self):
		if self.goods["chemicals"] > 4:
			if self.resources["dyes"] < 3:
				self.goods["chemicals"] -= 1
				self.resources["dyes"] += 1
		if self.resources["food"] < 8:
				count = 0
				for p, prov in self.provinces.items():
					if prov.resource == "food":
						count += 1
				while count > 0 and self.goods["chemicals"] > 0:
					self.resources["food"] += 1
					self.goods["chemicals"] -= 1
					count -= 1

	def use_culture(self, players):
		if self.culture >= 1:
			if self.happiness <= -1.0:
				self.culture -= 1
				self.happiness += 1
				print("Increased Happiness")
		other = 0
		for p in self.provinces.values():
			if p.culture != self.name:
				other += 1
		if other >= 1:
			for p in province.values():
				if p.culture != self.name:
					self.culture -= 1
					p.culture = self.name
					print("Assimlated Culture")
					return
		if self.happiness < 1.0:
			self.culture -= 1
			self.happiness += 1
			print("Increased Happiness")
			return
		if self.culture >= 2:
			for p in players.values():
				if p.midPop["artists"] < self.modPop["artists"]:
					if p.numMidPOP >= 0.5:
						for m in p.midPop:
							if p.midPop[m] >= 0.25:
								p.midPop[m] -= 0.25
								p.numMidPOP -= 0.25
								p.POP -= 0.25
								p.resources["gold"] -= 5
								self.midPop[m] += 0.25
								self.numMidPOP += 0.25
								self.POP += 0.25
								self.resources["gold"] += 5
								self.culture -= 2
								return
		if self.resources["gold"] < 35:
			for p in players.values():
				if p.type = "major":
					p.resources["gold"] -= 1
					self.resources[gold] += 1
			print("Cultural Exports")
			return
		if self.happiness < 2.5:
			self.culture -= 1
			self.happiness += 1
			if self.stability > 3.0:
				self.stability = 3.0
			print("Increased Happiness")

