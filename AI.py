# AI

from player_class import *
from market import *
from technologies import *
from minor_classes import *

from random import *
from math import *

import datetime

import math

craft = {
	"parts": {"iron": 0.67, "coal": 0.33},
	"cannons": {"iron": 0.67, "coal": 0.33},
	"paper": {"wood": 1.0},
	"clothing": {"cotton": 0.9, "dyes": 0.3},
	"furniture": {"wood": 0.67, "cotton": 0.33},
}

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
	"fighter": {"wood": 1, "gear": 1, "parts": 1, "cannons": 1.0},  # 2.5
	"auto": {"rubber": 0.5, "gear": 1.0, "parts": 1.0, "iron": 0.5},  # 2
	"tank": {"iron": 1.5, "cannons": 1.5, "rubber": 0.5, "gear": 1, "parts": 1},  # 4
	# "frigates": {"cannons": 1.0, "wood": 1.0, "cotton": 1.0},
	# "iron_clad": {"cannons": 1.0, "iron": 1.0, "parts": 1.0},
	# "battle_ship": {"cannons": 3.0, "iron": 3.0, "parts": 1.0, "gear": 1.0 }  #8
}


class AI(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(AI, self).__init__(_name, _type, number, *args, **kwargs)

		self.personality = {
			"Army": 1.15,
			"Navy": 0.7,
			"Offensive": 0.5
		}

		self.general_priority = ""

		self.rival_target = []

		self.allied_target = []

		self.sphere_targets = set()

		self.mid_class_priority = {
			"research": 1.0,
			"military": 0.9,
			"government": 0.9,
			"management": 0.9,
			"culture": 1.0
		}

		self.pro_need = {
			"food": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"coal": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"spice": {"produces": 0.0, "needs": 0.0, "forecast": 0.0},
			"oil": {"produces": 0.0, "needs": 0.0, "forecast": 0.0}
		}

		self.objective = 0

		self.build_factory_priority = {
			"parts": 1.0,
			"clothing": 1.1,
			"furniture": 0.9,
			"paper": 1.0,
			"cannons": 0.95,
			"chemicals": 0.55,
			"gear": 0.95,
			"radio": 0.65,
			"telephone": 0.65,
			"fighter": 0.9,
			"auto": 0.8,
			"tank": 2
		}

		self.production_priority = {
			"parts": 1.0,
			"clothing": 1.1,
			"furniture": 0.9,
			"paper": 1.0,
			"cannons": 0.95,
			"chemicals": 0.55,
			"gear": 0.95,
			"radio": 0.65,
			"telephone": 0.65,
			"fighter": 1.5,
			"auto": 0.8,
			"tank": 2
		}
		# cannon
		self.improve_province_priority = {
			"food": 1.1,
			"iron": 1.0,
			"coal": 0.4,
			"wood": 0.8,
			"cotton": 0.65,
			"gold": 1.5,
			"spice": 2,
			"dyes": 0.65,
			"rubber": 0.2,
			"oil": 0.2,
			"shipyard": 14,
			"fortification": 0.9,
			"/": 0,
			"//": 0,
			"///": 0
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
			"pre_industry": 5,
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
			"ironclad": 4,
			"electricity": 3.5,
			"medicine": 3,
			"synthetic_dyes": 3,
			"fertlizer": 3,
			"dynamite": 3,
			"compound_steam_engine": 4,
			"telegraph": 3.25,
			"radio": 3.85,
			"mechanical_reaper": 2,
			"oil_drilling": 5,
			"combustion": 4,
			"steel_plate_armor": 2.5,
			"flight": 4.5,
			"automobile": 3.75,
			"telephone": 3.5,
			"rotary_drilling": 4,
			"mobile_warfare": 5.5,
			"bombers": 3.5,
			"oil_powered_ships": 5.0,
			"synthetic_oil": 4.0,
			"synthetic_rubber": 4.0,
			"radar": 3.0,
			"rockets": 1,
			"early_computers": 2.3,
			"atomic_bomb": 5

		}

		self.resource_priority = {
			"food": 1.0,
			"iron": 1.1,
			"coal": 0.4,
			"cotton": 0.8,
			"wood": 1.0,
			"spice": 1.6,
			"dyes": 0.8,
			"gold": 1.5,
			"rubber": 0.1,
			"oil": 0.1,
			"/": -1000.0,
			"//": -1000,
			"///": -1000

		}

		self.resourse_to_keep = {
			"food": 4,
			"iron": 2,
			"coal": 2,
			"cotton": 2,
			"wood": 2,
			"spice": 1,
			"dyes": 2.0,
			"gold": 2.0,
			"rubber": 2,
			"oil": 2,
			"/": 0,
			"//": 0,
			"///": 0
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
			"oil": 0,
			"/": 0,
			"//": 0,
			"///": 0
		}

	def calculate_production_priority(self, market):
		for k, v in self.production_priority.items():
			self.production_priority[k] = 0
		for g, good in self.goods.items():
			if self.supply[g] < 12 and self.goods[g] < 8:
				self.production_priority[g] += 1
			if self.supply[g] < 8 and self.goods[g] < 5:
				self.production_priority[g] += 1
			if self.supply[g] < 4 and self.goods[g] < 3:
				self.production_priority[g] += 1
			if self.supply[g] < 1:
				self.production_priority[g] += 1
			if g == "tank" and self.military["tank"] < 5:
				self.production_priority["tank"] += 2
			if g == "fighter" and self.military["fighter"] < 5:
				self.production_priority["fighter"] += 2
			if "mobile_warfare" in self.technologies:
				self.production_priority["cannons"] += 1

	def calculate_resource_base(self):
		for k, v in self.resource_base.items():
			self.resource_base[k] = 0
		for p, prov in self.provinces.items():
			self.resource_base[prov.resource] += (development_map[prov.development_level] * prov.quality)

	def ai_increase_pop(self, market, relations, players):
		if self.midGrowth == False:
			return
		if self.freePOP > 3 or self.proPOP > 5:
			return
		if self.POP_increased >= 2:
			return
		if self.goods["clothing"] < 1 and self.supply["clothing"] > 1 and self.resources["gold"] >= market.buy_price(
				"clothing", self.supply["clothing"]) * 2:
			self.ai_buy("clothing", 1, market, relations, players)
		# if self.goods["furniture"] < 1 and market.market["furniture"] > 1 and self.resources["gold"] > market.buy_price("furniture") * 1.5:
		#	self.ai_buy("furniture", 1, market)
		if self.resources["food"] < 2 and self.supply["food"] > 2 and self.resources["gold"] >= market.buy_price("food",
																												 self.supply[
																													 "food"]) * 3:
			self.ai_buy("food", 2, market, relations, players)
		if self.resources["food"] >= 2 and self.goods["clothing"] >= 1 and self.POP <= (
					(len(self.provinces) * 2.2) + self.numMidPOP):
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
					# self.goods["furniture"] -= 1.0
					self.POP_increased += 1
					self.stability -= 0.1
					if self.stability < -3.0:
						self.stability = -3.0
				   # print("POP increase ______________________________________________")

			else:
				self.POP += 1.0
				self.freePOP += 1.0
				self.numLowerPOP += 1
				self.resources["food"] -= 1.0
				self.goods["clothing"] -= 1.0
				# self.goods["furniture"] -= 1.0
				self.POP_increased += 1
				self.stability -= 0.15
				if self.stability < -3.0:
					self.stability = -3.0
			   # print("POP increase ______________________________________________")

	def try_middle_class(self, market, relations, players):
		if self.midGrowth == False:
			return
		requirement = self.determine_middle_class_need()
		per1 = self.check_mid_requirement(requirement)
		if per1 == True:
			return True
		else:
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
			# print("Check for %s" % (k))
			if k == "spice":
				if self.resources["spice"] < v:
					self.ai_buy("spice", v - self.resources["spice"], market, relations, players)
			elif self.goods[k] < v:
				for i in range(int((v - self.goods[k]) + 1)):
					decision = self.ai_decide_on_good(k, market, relations, players)
					self.ai_obtain_good(k, decision, market, relations, players)
		per2 = self.check_mid_requirement(requirement)
		if per2 == True:
			return True
		else:
			return False

	def ai_increase_middle_class(self, market, relations, players):
		print("Try to increase middle class____________________")
		if "pre_industry" not in self.technologies:
			return
		if self.type != "major" and self.POP <= 6:
			if self.POP <= self.numMidPOP * 8:
				return
		if self.midGrowth == False:
			print("Cannot increase development because did not pay all food last turn")
			return
		print("Trying to increase middle class.........")
		check = self.try_middle_class(market, relations, players)
		if check == False:
			return
		if self.freePOP < 0.5:
			self.proPOP -= 1
			self.freePOP + 1
		least_dev = 100
		for d, dev in self.developments.items():
			if self.developments[d] < least_dev:
				least_dev = self.developments[d]
		least_dev = max(1, least_dev)
		d_options = []
		for d, dev in self.developments.items():
			if self.developments[d] > 4:
				continue
			if self.developments[d] < least_dev * 2:
				d_options.append(d)
		
		d_selection = ""
		if self.stability < -1.2 and "culture" in d_options:
			# print("pick culture")
			d_selection = "culture"
		elif self.new_development < 1 and "management" in d_options and "government" in d_options:
			if self.developments["government"] < self.developments["management"]:
				d_selection = "government"
			# print("pick gov")
			elif self.new_development < 1 and "management" in d_options:
				d_selection = "management"
				# print("pick man")

		elif self.new_development < 1 and "government" in d_options:
			d_selection = "government"
		# print("pick gov")
		else:
			d_preferences = sorted(self.mid_class_priority, key=self.mid_class_priority.get, reverse=True)
			for do in d_preferences:
				if do in d_options:
					d_selection = do
					break
		if self.development_level > 19:
		   # print("It seems that maximal mid class has been achieved by %s" % (self.name))
			stop = input()
			return
		spice_required = 0
		if self.development_level > 1:
			spice_required = 1
		if self.development_level > 6:
			spice_required = 2
		if self.resources["spice"] < spice_required:
			return
		requirement = self.determine_middle_class_need()
		for r in requirement:
			if r == "spice":
				self.resources["spice"] -= 1
			# print("Pays 1 Spice")
			else:
				self.goods[r] -= 1.0
				# print("Pays 1 %s" % (r))
		self.numLowerPOP -= 0.5
		self.numMidPOP += 0.5
		self.development_level += 1
		# self.midPOP[m_selection]["number"] += 0.2
		self.developments[d_selection] += 1
		self.freePOP -= 0.5
		self.mid_class_priority[d_selection] -= 0.1
		self.new_development += 1
		if d_selection == "management" or d_selection == "government":
			self.new_development += 1
		if d_selection == "military":
			self.milPOP -= 0.4
			self.freePOP += 0.4
			self.ai_choose_doctrine()
		print("New middle class pop: %s ________________________" % (d_selection))
		market.report.append("%s has increased %s development to %s" % (self.name,  d_selection, self.developments[d_selection]))
		market.report.append("%s's development level is now %s" % (self.name, self.development_level))

	def ai_choose_doctrine(self):
		while (len(self.doctrines) <= 10):
			if "SeaI" not in self.doctrines:
				if self.personality["Navy"] > 0.75:
					self.doctrines.add("SeaI")
					self.frigates["attack"] += 0.2
					self.iron_clad["attack"] += 0.3
					self.battle_ship["attack"] += 0.8
					return

			elif "SeaI" in self.doctrines and "SeaII" not in self.doctrines:
				roll = random()
				if self.personality["Navy"] > 0.75:
					if roll < 0.5:
						self.doctrines.add("SeaII")
						self.frigates["attack"] += 0.3
						self.iron_clad["attack"] += 0.4
						self.battle_ship["attack"] += 1.0
						return
		

			options = []
			for md in military_doctrines:
				if md == "SeaI" not in self.doctrines and md == "SeaII":
					continue
				if "mobile_warfare" not in self.technologies and md == "CombinedArms":
					continue 
				if "flight" not in self.technologies and md == "CombinedArms":
					continue
				if "machine_guns" not in self.technologies and md == "Entrenchment":
					continue
				if "ManouverI" not in self.doctrines and md == "ManouverII":
					continue
				if "SeaI" not in self.doctrines and md == "SeaII":
					continue
				if md not in self.doctrines:
					options.append(md)
					print("Adding %s" % md)
					print(md)
				if len(options) == 0:
					print("No doctrine options left!")
					return
			doct = choice(options)
			self.choose_doctrine(doct)

	def early_game_expansion(self, market, relations, players):
		if market.turn > 8:
			return
		if self.resources["wood"] < 1 and market.buy_price("wood", self.supply["wood"]) < self.resources["gold"] * 1.5:
			self.ai_buy("wood", 1, market, relations, players)
		if self.resources["iron"] < 1 and market.buy_price("iron", self.supply["iron"]) < self.resources["gold"] * 1.5:
			self.ai_buy("iron", 1, market, relations, players)
		if self.factories["cannons"]["number"] == 0 and self.goods["cannons"] < 2.5:
			if self.resources["iron"] >= 2 and self.supply["cannons"] <= 2 and self.crafted == False:
				self.ai_craftman_production("cannons", market)
		if self.resources["cotton"] < 1 and market.buy_price("cotton", self.supply["cotton"]) < self.resources[
			"gold"] * 1.5:
			self.ai_buy("cotton", 1, market, relations, players)
		if self.factories["clothing"]["number"] == 0 and self.goods["clothing"] < 2:
			if self.resources["cotton"] >= 2 and self.supply["clothing"] <= 3 and self.crafted == False:
				self.ai_craftman_production("clothing", market)

	def early_game_army(self, market, relations, players):
		if market.turn > 8:
			return
		if self.resources["iron"] < 1 and market.buy_price("iron", self.supply["iron"]) < self.resources["gold"] * 1.5:
			self.ai_buy("iron", 1, market, relations, players)
		if self.factories["cannons"]["number"] == 0 and self.goods["cannons"] < 2.5:
			if self.resources["iron"] >= 2 and self.supply["cannons"] <= 2 and self.crafted == False:
				self.ai_craftman_production("cannons", market)
		if self.resources["cotton"] < 1 and market.buy_price("cotton", self.supply["cotton"]) < self.resources[
			"gold"] * 1.5:
			self.ai_buy("cotton", 1, market, relations, players)
		if self.factories["clothing"]["number"] == 0 and self.goods["clothing"] < 2:
			if self.resources["cotton"] >= 2 and self.supply["clothing"] <= 3 and self.crafted == False:
				self.ai_craftman_production("clothing", market)

	def early_game_development(self, market, relations, players):
		if market.turn > 8:
			return
		if self.resources["cotton"] < 1 and market.buy_price("cotton", self.supply["cotton"]) < self.resources[
			"gold"] * 1.5:
			self.ai_buy("cotton", 1, market, relations, players)
		if self.factories["clothing"]["number"] == 0 and self.goods["clothing"] < 2:
			if self.resources["cotton"] >= 2 and self.supply["clothing"] <= 3 and self.crafted == False:
				self.ai_craftman_production("clothing", market)
		if self.factories["paper"]["number"] == 0 and self.goods["paper"] < 2 and self.AP >= 1:
			if self.resources["wood"] >= 2 and self.supply["paper"] <= 3 and self.crafted == False:
				self.ai_craftman_production("paper", market)
		if self.factories["furniture"]["number"] == 0 and self.goods["furniture"] < 1 and self.AP >= 1:
			if self.resources["wood"] >= 2 and self.supply["furniture"] <= 3 and self.crafted == False:
				self.ai_craftman_production("furniture", market)

	def early_game(self, market, relations, players):
		if market.turn > 8:
			return
		if self.type != "major":
			return
		if self.resources["cotton"] < 1 and market.buy_price("cotton", self.supply["cotton"]) < self.resources[
			"gold"] * 1.5:
			self.ai_buy("cotton", 1, market, relations, players)
		if self.resources["wood"] < 1 and market.buy_price("wood", self.supply["wood"]) < self.resources["gold"] * 1.5:
			self.ai_buy("wood", 1, market, relations, players)
		if self.resources["iron"] < 1 and market.buy_price("iron", self.supply["iron"]) < self.resources["gold"] * 1.5:
			self.ai_buy("iron", 1, market, relations, players)
		if self.factories["cannons"]["number"] == 0 and self.goods["cannons"] < 2.5:
			if self.resources["iron"] >= 2 and self.supply["cannons"] <= 2 and self.crafted == False:
				self.ai_craftman_production("cannons", market)
		# if self.goods["cannons"] >= 1 and self.resources["wood"] >= 1 and self.shipyard >= 1 and \
		#	self.resources["cotton"] >= 1 and self.AP >= 1:
		#		if self.military["frigates"] < 2:
		#			self.ai_build_frigates()
		if self.factories["clothing"]["number"] == 0 and self.goods["clothing"] < 2 and self.crafted == False:
			if self.resources["cotton"] >= 2 and self.supply["clothing"] <= 3:
				self.ai_craftman_production("clothing", market)
		if self.factories["paper"]["number"] == 0 and self.goods["paper"] < 2 and self.AP >= 1 and self.crafted == False:
			if self.resources["wood"] >= 2 and self.supply["paper"] <= 3:
				self.ai_craftman_production("paper")
		if self.factories["furniture"]["number"] == 0 and self.goods["furniture"] < 1 and self.AP >= 1:
			if self.resources["wood"] >= 2 and self.supply["furniture"] <= 3 and self.crafted == False:
				self.ai_craftman_production("furniture", market)

	def num_army_units(self):
		res = (self.military["irregulars"] + self.military["infantry"] + self.military["cavalry"] + self.military[
			"artillery"] + self.military["tank"] + self.military["fighter"])
		return res

	def num_factories(self):
		count = 0
		for k, v in self.factories.items():
			count += self.factories[k]["number"]
		return count

	def try_factory(self, market, relations, players):
		flag = True
		if self.goods["parts"] < 1:
			print("Wants machine parts")
			decision = self.ai_decide_on_good("parts", market, relations, players)
			if decision != "buy":
				flag = False
			self.ai_obtain_good("parts", decision, market, relations, players)
		# print("Flag: %s" % (flag))
		if self.resources["iron"] < 1:
			print("Wants to get iron")
			get = self.ai_buy("iron", 1, market, relations, players)
			if get == "fail":
				flag = False
		if flag == False:
			return
		else:
			# priorities = (sorted(self.build_factory_priority.keys(), key=lambda x:x[1], reverse=True ))
			priorities = sorted(self.build_factory_priority, key=self.build_factory_priority.get, reverse=True)
			# print("Factory Priorities:")
			# for p in priorities:
			#	print(p)
			options = self.ai_factory_options()
			for p in priorities:
				for o in options:
					if p in options:
						self.ai_build_factory(p, market, players)
						return

	def try_development(self, market, relations, players):
		flag = True
		if self.goods["parts"] < 1:
			# print("Wants parts")
			decision = self.ai_decide_on_good("parts", market, relations, players)
			if decision != "buy":
				flag = False
			self.ai_obtain_good("parts", decision, market, relations, players)
		if self.resources["wood"] < 1:
			# print("Wants iron")
			get = self.ai_buy("wood", 1, market, relations, players)
			if get == "fail":
				flag = False
		if self.sprawl == True:
			if self.goods["parts"] < 1.5:
				#	print("Wants parts")
				decision = self.ai_decide_on_good("parts", market, relations, players)
				if decision != "buy":
					flag = False
			if self.resources["wood"] < 1.5:
				#	print("Wants iron")
				get = self.ai_buy("wood", 1, market, relations, players)
				if get == "fail":
					flag = False

		if flag == False:
			return
		else:
			# print("Development Check")
			priorities = sorted(self.improve_province_priority, key=self.improve_province_priority.get, reverse=True)
			options = self.ai_improve_province_options()
			for p in priorities:
				if p in options:
					#	print("Checking for %s province" % (p))
					self.ai_develop_province(p, market)
					return

	def develop_industry(self, market, relations, players):
		print("Develop Industry:")
		if self.AP < 1:
			print("No AP left")
			return
		print(self.type)
		if self.type == "old_minor":
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
			print("Able to develop province or build factory")
			number_factories = self.num_factories()
			if self.type == "major":
				if number_factories < 2:
					self.try_factory(market, relations, players)
				elif number_factories >= self.number_developments and len(self.factories) >= 2:
					print("Wants to develop province")
					self.try_development(market, relations, players)
				else:
					pick = uniform(0, 1)
					if pick <= 0.38:
						print("Wants to build factory")
						self.try_factory(market, relations, players)
					else:
						print("Wants to improve province")
						self.try_development(market, relations, players)
			else:
				pick = uniform(0, 1)
				if pick <= 0.36:
					print("Wants to build factory")
					self.try_factory(market, relations, players)
				else:
					print("Wants to improve province")
					self.try_development(market, relations, players)
		elif len(opt) > 0:
			print("Try to develop province...")
			self.try_development(market, relations, players)
		elif "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1:
			self.try_factory(market, relations, players)

	def ai_obtain_good(self, _type, decision, market, relations, players):
		get = ""
		if decision == "manufacture_prepare":
			for i in manufacture[_type]:
				# material_mod = 1 - (self.midPOP["managers"]["number"] / 3)
				material_mod = 1 - (self.developments["management"] / 10)
				material_max = 1000
				for i in manufacture[_type]:
					temp = int((manufacture[_type][i] * material_mod) / (self.resources[i] + 0.1))
					if temp < material_max:
						material_max = temp
				need = int(5 - material_max)
				for i in manufacture[_type]:
					get = self.ai_buy(i, need, market, relations, players)
					if get == "fail":
						break
				self.ai_factory_production(_type, market)
		elif decision == "manufacture_ready":
			self.ai_factory_production(_type, market)
		elif decision == "buy":
			self.ai_buy(_type, 1, market, relations, players)
		elif decision == "craft_ready" and self.crafted == False:
			self.ai_craftman_production(_type, market)
		else:
			if _type in craft.keys():
				check = True
				for i in craft[_type]:
					get = self.ai_buy(i, craft[_type][i], market, relations, players)
					if get == "fail":
						check = False
				if check == True and self.crafted == False:
					self.ai_craftman_production(_type, market)

	def assign_priorities_to_provs(self):
		for p, prov in self.provinces.items():
			# print(p, prov.resource)
			kind = prov.resource
			prov.AI_priority = self.resource_priority[kind] * prov.quality
		sorted_provinces = sorted(self.provinces.values(), key=lambda x: (x.AI_priority), reverse=True)
		# sorted_priorities = sorted(self.provinces, key=self.provinces.get, reverse = True)
		# print("Province priorities:")
		# for p in sorted_provinces:
		#	print(p.name, p.resource, p.quality)
		return sorted_provinces

	def update_priorities(self, market):
		if self.stability > 3.0:
			self.stability = 3.0
		for k, v in self.resources.items():
			if k == "gold":
				continue
			if k == "oil" and "oil_drilling" not in self.technologies:
				continue
			if k == "rubber" and "chemistry" not in self.technologies:
				continue
			if self.supply[k] < 1:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if self.supply[k] < 5:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if self.resources[k] < 1:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1
			if len(market.market[k]) > 21:
				self.resource_priority[k] -= 0.1
				self.improve_province_priority[k] -= 0.1
			if self.resources[k] > 14:
				self.resource_priority[k] -= 0.1
				self.improve_province_priority[k] -= 0.1
			if len(market.market[k]) < 3:
				self.resource_priority[k] += 0.1
				self.improve_province_priority[k] += 0.1

	def AI_reset_POP(self):
		for p, prov in self.provinces.items():
			prov.worked = False
		self.proPOP = 0
		self.freePOP = self.numLowerPOP - self.milPOP

	def AI_assign_POP(self):
		# priorities = (sorted(self.resource_priority.items(), key=lambda x:x[1], reverse=True )
		priorities = self.assign_priorities_to_provs()
		# for p in priorities:
		#		print(p.name)
		if self.type == "major" or self.type == "old_empire":
			self.proPOP += 1
			self.freePOP -= 1
		if self.POP > 11:
			self.freePOP -= 1
			self.proPOP += 1
		if self.POP > 17:
			self.proPOP += 1
			self.freePOP -= 1
		if self.POP > 23:
			self.proPOP += 1
			self.freePOP -= 1
		if self.POP > 30:
			self.proPOP += 1
			self.freePOP -= 1

		count = 0
		for p in priorities:
			if self.freePOP > 1 and count <= 16:
				# print("Number free pop: %s" % self.freePOP)
				if self.provinces[p.name].worked == False:
					self.provinces[p.name].worked = True
					self.freePOP -= 1
					count += 1
		while self.freePOP >= 1.2:
			self.proPOP += 1
			self.freePOP -= 1

	def AI_sell_surplus(self, market, players):
		for r, resource in self.resources.items():
			if r == "gold":
				continue
			if resource > self.resourse_to_keep[r]:
				# print("Resource Amount:%s: %s" % (r, resource))
				amount = int(resource - self.resourse_to_keep[r])
				# print("Amount after need: %s" % (amount))
				if amount > 4:
					amount = 4
				if amount >= 1 and len(market.market[r]) < 12:
					self.ai_sell(r, amount, market, players)
				elif amount >= 1 and len(market.market[r]) < 20 and self.resources["gold"] <= 20:
					self.ai_sell(r, amount, market, players)

				elif amount >= 1 and len(market.market[r]) < 32 and self.resources["gold"] <= 3:
					self.ai_sell(r, amount, market, players)

		for g, good in self.goods.items():
			if self.goods[g] > 2 and g != "cannons" and len(market.market[g]) < 30 and self.resources["gold"] <= 4:
				amount = int(self.goods[g] - 2)
				if amount >= 1:
					if amount > 5:
						amount = 5
					self.ai_sell(g, amount, market, players)
			if self.goods[g] > 3 and g != "cannons" and len(market.market[g]) < 18 and self.resources["gold"] <= 20:
				amount = int(self.goods[g] - 3)
				if amount >= 1:
					if amount > 5:
						amount = 5
					self.ai_sell(g, amount, market, players)
			if self.goods[g] > 3 and len(market.market[g]) < 12 and g != "cannons":
				amount = int(self.goods[g] - 3)
				if amount >= 1:
					if amount > 5:
						amount = 5

					self.ai_sell(g, amount, market, players)
			ammo_needed = self.calculate_ammo_needed() + 2
			if self.goods[g] > ammo_needed + 1 and g == "cannons":
				amount = self.goods["cannons"] - (ammo_needed + 1)
				if amount > 5:
					amount = 5
				self.ai_sell("cannons", amount, market, players)

   # def view_AI_inventory(self):
	 #   print("POP: %s, LowPop: %s, Development Level: %s" % (self.POP, self.numLowerPOP, self.development_level))
	  #  print("freePOP: %s, proPOP: %s " % (self.freePOP, self.proPOP))
	   # print("Stability: %s, Diplo: %s, Reputation: %s " % (self.stability, self.diplo_action, self.reputation))
		#print("Colonize: %s, Num Colonies: %s" % (self.colonization, self.num_colonies))
	   # print("New Development %s, Research Points %s, Culture Points %s" % (
			#self.new_development, self.research, self.culture_points))
		# for m, mid in self.midPOP.items():
		#	print(m, mid)
	#    for d, dev in self.developments.items():
		#    print(d, dev)
		#print("\n")
		#print("%s Inventory \n" % (self.name))
	 #   for r, resource in self.resources.items():
		 #   print(r, resource, end=' ')
	  #  for g, good in self.goods.items():
	   #     print(g, good, end=' ')
		#for k, v in self.pro_need.items():
		 #   print(k, v)
	 #   print(" \n number_developments: %s \n" % (self.number_developments))
	  #  print("Fortifiction Level: %s " % (self.fortification))
	   # print("Shipyard Level: %s" % (self.shipyard))
		#for k, v in self.factories.items():
		#    print(k, v["number"], end=" | ")
	   # for k, v in self.military.items():
		#    print(k, v)
		#if self.rival_target != []:
		 #   print("Rival Target:")
		  #  print(self.rival_target[0].name, self.rival_target[1].name)
		#print("CBs:")
	   # for cb in self.CB:
		 #   print("Opponent: %s, Province: %s, Action: %s, Time: %s" % (cb.opponent, cb.province, cb.action, cb.time))

		#print("Embargoed by:")
		#for e in self.embargo:
		 #   print(e, end=" ")
		#print("\n")

	   # self_naval_projection_strength = self.ai_naval_projection(self)
	  #  print("Naval Projection: %s" % (self_naval_projection_strength))
	 #   attack = self.calculate_base_attack_strength()
	 #   print("Attack Strength (Land: %s" % (attack))
	 #   defend = self.calculate_base_defense_strength()
	 #   print("Defense Strength: %s " % (defend))

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
		self.pro_need["food"]["needs"] = (
			(self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1)
		self.resourse_to_keep["food"] = self.pro_need["food"]["needs"] * 1.25
		# self.pro_need["spice"]["needs"] = self.numMidPOP * 0.3
		self.pro_need["coal"]["needs"] = 0.1 * self.number_developments
		if self.numMidPOP > 4.5:
			self.pro_need["oil"]["needs"] = 0
			if self.development_level > 14:
				self.pro_need["oil"]["needs"] = (self.development_level - 15) * 0.2

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

	def ai_decide_on_good(self, _type, market, relations, players):
		# print("Wants to  get %s \n" % (_type))
		price_to_buy = market.buy_price(_type, self.supply[_type])
		# print("Price to buy %s" % (price_to_buy))
		price_to_craft = 100
		if _type in craft.keys():
			price_to_craft = 0
			for i in craft[_type]:
				price_to_craft += market.buy_price(i, self.supply[i]) * craft[_type][i]
				#	print("price to craft %s " % (price_to_craft))
		if self.supply[_type] > 3 and self.resources["gold"] >= market.buy_price(_type, self.supply[_type]):
			return "buy"
		# material_mod = 1 - (self.midPOP["managers"]["number"] / 5)
		material_mod = 1 - (self.developments["management"] / 10)
		price_to_man = 0
		for i in manufacture[_type]:
			price_to_man += market.buy_price(i, self.supply[_type]) * int(manufacture[_type][i] * material_mod)
		if self.factories[_type]["number"] >= 1:
			cap = self.calculate_how_much_can_produce(_type)
			if cap >= 4:
				# print("Make w factory")
				return "manufacture_ready"
			else:
			  #  print("Try to supply factory....")
				self.supply_factory_with_material(_type, market, relations, players)
				cap = self.calculate_how_much_can_produce(_type)
				if cap >= 4:
					return "manufacture_ready"
				if self.supply[_type] >= 1:
					return "buy"
				else:
					return "fail"
					# material_on_market = 0
					#	for k, v in manufacture[_type].items():
					#	material_on_market += manufacture[_type][i] * market.market[k]
					# if (price_to_man * 1.3) < price_to_buy and material_on_market >= 3:
					# return "manufacture_prepare"
		elif self.supply[_type] >= 1 and self.resources["gold"] >= market.buy_price(_type, self.supply[_type]):
			# print("Decide to buy " + _type)
			return "buy"

		elif _type in ["gear", "telephone", "radio", "auto", "fighter", "tank"]:
			return "fail"
		elif _type in craft.keys():
			check = True
			for i in craft[_type]:
				if self.resources[i] < craft[_type][i]:
					check = False
			if check == True:
				return "craft_ready"
			else:
				check = True
				if _type not in craft.keys():
					check = False
				for i in craft[_type]:
					check = False
					if self.supply[i] < 2:
						check = False
					elif self.resources["gold"] <= (market.buy_price(i, self.supply[i])) * 2:
						check = False
				if check == True:
					return "craft_prepare"
		else:
			return "fail"

	def calculate_oil_needed(self):
		oil_needed = 0.0
		oil_needed += self.military["tank"] * self.tank["oil_use"]
		oil_needed += self.military["fighter"] * self.fighter["oil_use"]
		oil_needed = self.military["battle_ship"] * self.battle_ship["oil_use"]
		oil_needed = oil_needed * 2
		if self.numMidPOP > 4.5:
			oil_needed += (self.numMidPOP - 4.5) / 2
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
		ammo_needed = ammo_needed * 2
		return ammo_needed

	def fulfill_needs(self, market, relations, players):
		food_need = self.numLowerPOP * 0.2 + self.numMidPOP * 0.3 + self.military["cavalry"] * 0.1 + 1
		if self.resources["food"] < food_need:
			while self.resources["food"] < food_need and self.supply["food"] >= 1 and self.resources[
				"gold"] >= market.buy_price("food", self.supply["food"]):
				#	print("Food: %s, Need %s, Supply %s, Gold %s, Price %s" % (self.resources["food"], food_need, self.supply["food"], self.resources["gold"], market.buy_price("food", self.supply["food"])))
				possible = self.ai_buy("food", 1, market, relations, players)
				if possible == "fail":
					break
		coal_need = (self.number_developments * 0.1) + 1
		if self.resources["coal"] < coal_need:
			while self.resources["coal"] < (coal_need + 2) and self.supply["coal"] >= 2 and self.resources[
				"gold"] >= market.buy_price("coal", self.supply["coal"]) * 2:
				possible = self.ai_buy("coal", 1, market, relations, players)
				if possible == "fail":
					break
		ammo_needed = self.calculate_ammo_needed()
		if self.goods["cannons"] < (ammo_needed + 2):
			while self.goods["cannons"] < (ammo_needed + 2) and self.supply["cannons"] >= 1 and self.resources[
				"gold"] >= market.buy_price("cannons", self.supply["cannons"]) * 2:
				possible = self.ai_buy("cannons", 1, market, relations, players)
				if possible == "fail":
					break
		oil_needed = self.calculate_oil_needed()
		if self.resources["oil"] < (oil_needed + 1):
			while self.resources["oil"] < (oil_needed + 1) and self.supply["oil"] >= 1 and self.resources[
				"gold"] >= market.buy_price("oil", self.supply["oil"]) * 1.5:
				possible = self.ai_buy("oil", 1, market, relations, players)
				if possible == "fail":
					break
		if self.goods["clothing"] < 1 and self.supply["clothing"] > 3 and self.resources["gold"] >= market.buy_price(
				"clothing", self.supply["clothing"]) * 2:
			self.ai_buy("clothing", 1, market, relations, players)
		if self.goods["chemicals"] <= 2 and self.supply["chemicals"] > 4 and self.resources["gold"] >= market.buy_price(
				"chemicals", self.supply["chemicals"]) * 3.:
			self.ai_buy("chemicals", 2, market, relations, players)
		if self.resources["food"] < 5 and self.POP > 14 and self.supply["food"] >= 8 and self.resources[
			"gold"] >= market.buy_price("food", self.supply["food"]) * 4:
			self.ai_buy("food", 3, market, relations, players)
		# if self.factories["gear"] > 0:
		#	if self.resources["rubber"] < 2 and self.supply["rubber"] > 3 and  market.buy_price("rubber", self.supply["rubber"]) * 2.5:
		#	self.ai_buy("rubber", 1, market, relations, players)
		if self.goods["gear"] < 2 and self.supply["gear"] > 2 and self.resources["gold"] > market.buy_price("gear",
																											self.supply[
																												"gear"]) * 2:
			self.ai_buy("gear", 1, market, relations, players)
		if self.goods["gear"] < 4 and self.supply["gear"] > 6 and self.resources["gold"] > market.buy_price("gear",
																											self.supply[
																												"gear"]) * 2.5:
			self.ai_buy("gear", 1, market, relations, players)
		if self.goods["parts"] < 2 and self.supply["parts"] > 3 and self.resources["gold"] > market.buy_price("parts",
																											  self.supply[
																												  "parts"]) * 2:
			self.ai_buy("parts", 1, market, relations, players)
		cans = self.goods["cannons"] - ammo_needed
		if cans < 2:
			possible = self.ai_buy("cannons", 2, market, relations, players)

	def ai_buy(self, kind, amount, market, relations, players):
	 #   print("Wants to buy %s" % (kind))
		# if len(market.market[kind]) < 1:
		#	return
		price = market.buy_price(kind, self.supply[kind])
	  #  print("Price: %s" % (price))
		p_relations = [r for r in relations.values() if self.name in r.relata]
		p_relations = deepcopy(p_relations)
		for pr in p_relations:
			pair = list(pr.relata)
			if pair[0] == self.name:
				other = pair[1]
			else:
				other = pair[0]
			other = players[other]
			#	if other.midPOP["managers"]["number"] > 0:
			#	pr.relationship += other.midPOP["managers"]["number"]/4
			if other.developments["management"] > 0:
				pr.relationship += other.developments["management"] / 8
				# if "quality control" in other.ideas:
				#	pr.relata += 0.15
		if kind == "clothing" or kind == "furniture":
			for pr in p_relations:
				pair = list(pr.relata)
				if pair[0] == self.name:
					other = pair[1]
				else:
					other = pair[0]
				other = players[other]
				# if other.midPOP["artists"]["number"] > 0:
				#	pr.relationship += other.midPOP["artists"]["number"]/2
				# if "brand name clothing" in other.ideas:
				#	pr.relata += 0.5
				if other.developments["culture"] > 0:
					pr.relationship += other.developments["culture"] / 4

		if kind == "radio" or kind == "telephone" or kind == "auto":
			for pr in p_relations:
				pair = list(pr.relata)
				if pair[0] == self.name:
					other = pair[1]
				else:
					other = pair[0]
				other = players[other]
				# if other.midPOP["artists"]["number"] > 0:
				#	pr.relationship += other.midPOP["artists"]["number"]/4
				if other.developments["culture"] > 0:
					pr.relationship += other.developments["culture"] / 8

		# print("Are we still there?")
		p_relations.sort(key=lambda x: x.relationship, reverse=True)
		# print("P_relations:_____________________________________________________________________________")
		# for pr in p_relations:
		#	print("pr: %s" % (pr.relata))
		stock = []
		for s in market.market[kind]:
			if s.owner not in self.embargo:
				stock.append(s)
		# print("STOCK_____________")
		# for s in stock:
		#	print(s.owner)
		# print("Stock amount %s" % (len(stock)))
		if len(stock) < 1:
			return "fail"
		# while self.resources["gold"] > price and amount >= 1 and self.supply[kind] >= 1:
		for pr in p_relations:
			re = list(pr.relata)
			# print("re1 %s, re2 %s" % (re[0], re[1]))
			if re[0] == self.name:
				o = re[1]
			else:
				o = re[0]
			for s in stock:
				pr
				if s.owner == o:
					# print("1063")
					if self.resources["gold"] < price:
					 #   print("Fail - not enough money")
						return "fail"
					other = players[o]
					self.resources["gold"] -= price
					other.resources["gold"] += price
					# print(1070)
					market.market[kind].remove(s)
					relations[frozenset({other.name, self.name})].relationship + 0.02
					del s
					if kind in market.resources:
						self.resources[kind] += 1
					else:
						self.goods[kind] += 1
						other.new_development += 0.2
					price = market.buy_price(kind, self.supply[kind])
					print("%s buys %s from %s" % (self.name, kind, other.name))
					market.market_report = market.market_report + " %s buys %s from %s \n" % (self.name, kind, other.name)
					#market.market_report.append("%s buys %s from %s" % (self.name, kind, other.name))
					amount -= 1
					self.supply[kind] -= 1
					price = market.buy_price(kind, self.supply[kind])
					if amount < 1:
						return "success"
					if self.supply[kind] < 1:
						return "fail"

		return "fail"

	#	def ai_buy(self, _type, _amount, market):
	#		print("Wants to buy %s " % (_type))
	#		price = market.buy_price(_type)
	#		while self.resources["gold"] >= price and _amount >= 1 and market.market[_type] >= 1:
	#			self.resources["gold"] -= price
	#			market.gold += price
	#			market.market[_type] -= 1
	#			if _type in market.resources:
	#				self.resources[_type]  += 1
	#			elif(_type == "chemicals"):
	#				self.goods["chemicals"] += 2
	#			else:
	#				self.goods[_type] += 1
	#			_amount -= 1
	#			price = market.buy_price(_type)
	#			print("Buys 1 %s" % (_type))
	#
	#		if _amount < 1:
	#			return "sucess"
	#		else:
	#			return "fail"


	def use_spice_stability(self):
		if self.resources["spice"] >= 1 and self.stability < 0:
			self.resources["spice"] -= 1
			self.stability += 2 / (self.POP + 0.01)
		   # print("Uses spice to increase stability")
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 1.5 and self.stability < 1:
			self.resources["spice"] -= 2
			self.stability += 2 / (self.POP + 0.01)
		 #   print("Uses spice to increase stability")
			if self.stability > 3:
				self.stability = 3
		if self.resources["spice"] >= 2 and self.stability < 2:
		 #   print("Uses spice to increase stability")
			self.resources["spice"] -= 2
			self.stability += 2 / (self.POP + 0.01)
			if self.stability > 3:
				self.stability = 3

	def check_stability(self, market, relations, players):
		if self.stability < 0 and self.resources["spice"] < 2:
			self.ai_buy("spice", 2, market, relations, players)
		elif self.stability < 1 and self.resources["spice"] < 2:
			if self.supply["spice"] >= 2 and self.resources["gold"] >= market.buy_price("spice",
																						self.supply["spice"]) * 4:
				self.ai_buy("spice", 2, market, relations, players)
		elif self.stability < 2 and self.resources["spice"] < 2:
			if self.supply["spice"] >= 4 and self.resources["gold"] >= market.buy_price("spice",
																						self.supply["spice"]) * 6:
				self.ai_buy("spice", 2, market, relations, players)

	def spend_excess_cash(self, market, players, relations):
		count = 20
		if self.type == "major":
			while self.resources["gold"] >= 36 and count > 1:
				for k, v in market.market.items():
					if len(market.market[k]) > 27:
						for i in market.market[k]:
							if i.owner == self.name:
								if i in market.resources:
									market.market[_type].remove(i)
									del i
									self.resources[k] += 1
				count -= 1
		count = 20
		while self.resources["gold"] > 40 and count > 0:
			item = choice(["food", "iron", "cotton", "coal", "dyes", "wood", "spice", "clothing", \
						   "parts", "cannons", "paper", "furniture", "chemicals", "radio", "telephone", "tank", "auto",
						   "fighter"])
			if item in market.resources:
				if self.supply[item] > 10:
					if self.resources[item] < 4:
						self.ai_buy(item, 1, market, relations, players)
			if item in market.goods:
				if self.supply[item] > 7:
					if self.goods[item] < 2:
						self.ai_buy(item, 1, market, relations, players)
			count -= 1

	def ai_sell(self, kind, amount, market, players):
		if len(market.market[kind]) > 32:
			return
		# print("Amount of %s to sell: %s" % (kind, amount))

		player = players[self.name]
		while len(market.market[kind]) < 32 and amount >= 1:
			st = random()
			ID = self.name + str(st)
			new = MarketItem(ID, kind, self.name)
			market.market[kind].append(new)
			if kind in self.resources.keys():
				self.resources[kind] -= 1
			else:
				self.goods[kind] -= 1
			print("Placed %s on market" % (kind))
			#market.market_report.append("%s placed %s on market" % (self.name, kind))
			market.market_report = market.market_report + " %s placed %s on market \n" % (self.name, kind)
			amount -= 1

	# print("Try to sell type %s, amount %s" % (_type, amount))
	#	if market.market[_type] > 32:
	#		print("The market cannot buy any more of that resource (over 30) \n")
	#		return
	#	price = market.sell_price(_type)
	#	if price == 0:
	#		print("The market cannot buy any more of that resource (price 0) \n")
	#		return
	#	while market.gold >= price and market.market[_type] <= 30 and amount >= 1:
	#		print("Sold %s" % (_type))
	#		market.gold -= price
	#		market.market[_type] += 1
	#		self.resources["gold"] += price
	#		if _type in market.resources:
	#			self.resources[_type] -= 1
	#		elif _type in market.goods:
	#			self.new_development +=  0.25
	#			if _type == "chemicals":
	#				self.goods["chemicals"] -= 2
	#		else:
	#			self.goods[_type] -= 1
	#		price = market.sell_price(_type)
	#		amount -= 1


	def ai_factory_production(self, _type, market):
	   # print('Factory Production++++++++++++++++++++++++++++++++++++++++++++++++++')
		stab_rounds = round(self.stability * 2) / 2
		stab_mod = stability_map[stab_rounds]
		# material_mod = 1 - (self.midPOP["managers"]["number"] / 4)
		material_mod = 1 - (self.developments["management"] / 10)

		material_max = 1000

		max_amount = (self.factories[_type]["number"] * stab_mod * self.factory_throughput)
		# print("MAX amount %s" % (max_amount))


		for i in manufacture[_type]:
			if i in self.resources.keys():
				temp = int(self.resources[i] / (manufacture[_type][i] * material_mod))
				# print("man_type_i: %s, material mod: %s self_resource_i %s \n" % (manufacture[_type][i], material_mod, self.resources[i]))
				if temp < material_max:
					material_max = temp
			if i in self.goods.keys():
				temp = int(self.goods[i] / (manufacture[_type][i] * material_mod))
				if temp < material_max:
					material_max = temp
		# material_max -= 1
		# print("material_max: %s " % (material_max))
		amount = min([material_max, max_amount])
		# print("AMOUNT FACT %s ^^^^^^^^^^^^^^^^^^^^^^^^^^^^" % (amount))
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
		self.factories[_type]["used"] = True
		#print(self.factories[_type]["used"])
		print("%s produced %s %s " % (self.name, amount, _type))
		market.report.append("%s produced %s %s " % (self.name, amount, _type))
		self.AP -= 1
		return True

	def ai_craftman_production(self, _type, market):
		if _type not in craft.keys():
			return False
		for i in craft[_type]:
			self.resources[i] -= craft[_type][i]
		self.goods_produced[_type] += 1.0
		self.AP -= 1
		self.crafted = True
		print("%s crafted %s" % (self.name, _type))
		market.report.append("%s crafted %s" % (self.name, _type))
		# print("AP points remaining__: %s \n" % (self.AP))
		return

	def ai_decide_factory_productions(self, market, relations, players):
		if self.AP < 1:
			# print("No action points left")
			return
		priorities = sorted(self.production_priority, key=self.production_priority.get, reverse=True)

		for p in priorities:
			# print(k, v)
			if self.factories[p]["number"] >= 1:
				#	print("Factory owned: %s" % (k))
				if self.factories[p]["used"] == True:
					return
				if len(market.market[p]) < 20:
					cap = self.calculate_how_much_can_produce(p)
					if cap > 3 and (p == "tank" or p == "fighter"):
						self.ai_factory_production(p, market)
					if cap < 4:
						self.supply_factory_with_material(p, market, relations, players)
						cap = self.calculate_how_much_can_produce(p)
						if cap > 3 and (p == "tank" or p == "fighter"):
							self.ai_factory_production(p, market)
						if cap < 4:
							continue
						else:
							self.ai_factory_production(p, market)
							continue
					else:
						# print("Has sufficient material...")
						self.ai_factory_production(p, market)

	def calculate_how_much_can_produce(self, _type):
		cap = 1000
		#	print("calculate_how_much_can_produce: %s" % (_type))

		for k, v in manufacture[_type].items():
			# print(k, v)
			if (k in self.resources.keys() and self.resources[k] == 0) or (
							k in self.goods.keys() and self.goods[k] == 0):
				# print("%s equals 0" % (k))
				cap = 0

				return cap
			else:
				# material_mod = 1 - (self.midPOP["managers"]["number"] / 4)
				material_mod = 1 - (self.developments["management"] / 10)

				if k in self.resources.keys():
					temp = self.resources[k] / (v * material_mod)
					if (self.resources[k] / (v * material_mod)) < cap:
						cap = (self.resources[k] / v * material_mod)
				if k in self.goods.keys():
					temp = self.goods[k] / (v * material_mod)
					if (self.goods[k] / (v * material_mod)) < cap:
						cap = (self.goods[k] / v * material_mod)
	  #  print("Is able of produceing %s %s\n" % (cap, _type))
		return cap

	def supply_factory_with_material(self, _type, market, relations, players):
	  #  print("Try to supply %s factory..." % (_type))
		if _type == "parts" or _type == "cannons":
			cap = 4 * self.factories["parts"]["number"]
			if self.resources["iron"] < cap:
				cost = market.buy_price("iron", self.supply["iron"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.5:
					return
				amount = ceil(cap - self.resources["iron"])
				# amount = min (amount, self.supply["iron"])
				self.ai_buy("iron", amount, market, relations, players)
			cap = 4 * self.factories["parts"]["number"]
			if self.resources["coal"] < cap:
				amount = ceil(cap - self.resources["coal"])
				# amount = min(amount, self.supply["coal"])
				self.ai_buy("coal", amount, market, relations, players)
		elif _type == "clothing":
			cap = 4.3 * self.factories["clothing"]["number"]
			if self.resources["cotton"] < cap:
				cost = market.buy_price("cotton", self.supply["cotton"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.4:
					return
				amount = ceil(cap - self.resources["cotton"])
				# amount = min(amount, self.supply["cotton"])
				self.ai_buy("cotton", amount, market, relations, players)
			if self.resources["dyes"] < 1:
				amount = ceil(3 - self.resources["dyes"])
				# amount = min(amount, self.supply["dyes"])
				self.ai_buy("dyes", amount, market, relations, players)
		elif _type == "furniture":
			cap = 4 * self.factories["furniture"]["number"]
			if self.resources["wood"] < cap:
				cost = market.buy_price("wood", self.supply["wood"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.5:
					return
				amount = ceil(cap - self.resources["wood"])
				# amount = min(amount, self.supply["wood"])
				self.ai_buy("wood", amount, market, relations, players)
			if self.resources["cotton"] < 2.0:
				amount = ceil(2.5 - self.resources["cotton"])
				# amount = min(amount, self.supply["cotton"])
				self.ai_buy("cotton", amount, market, relations, players)
		elif _type == "paper":
			cap = 4.5 * self.factories["parts"]["number"]
			if self.resources["wood"] < cap:
				cost = market.buy_price("wood", self.supply["wood"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.3:
					return
				amount = ceil(cap - self.resources["wood"])
				# amount = min(amount, self.supply["wood"])
				self.ai_buy("wood", amount, market, relations, players)
		elif _type == "chemicals":
			cap = 6 * self.factories["chemicals"]["number"]
			if self.resources["coal"] < cap:
				cost = market.buy_price("coal", self.supply["coal"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.3:
					return
				amount = ceil(cap - self.resources["coal"])
				# amount = min(amount, self.supply["coal"])
				self.ai_buy("coal", amount, market, relations, players)
		elif _type == "gear":

			cap = 3.3 * self.factories["gear"]["number"]
			if self.resources["rubber"] < cap:
				cost = market.buy_price("rubber", self.supply["rubber"])
				gain = market.buy_price(_type, len(market.market[_type]))
				if gain < cost * 1.2:
					return
				amount = ceil(5.2 - self.resources["rubber"])
				# amount = min(amount, self.supply["rubber"])
				self.ai_buy("rubber", amount, market, relations, players)
			if self.resources["iron"] < 2:
				amount = ceil(4 - self.resources["iron"])
				# amount = min(amount, len(market.market["iron"]))
				self.ai_buy("iron", amount, market, relations, players)
			if self.resources["coal"] < 2:
				amount = ceil(4 - self.resources["coal"])
				# amount = min(amount, self.supply["coal"])
				self.ai_buy("coal", amount, market, relations, players)
		elif _type == "radio" or _type == "telephone":
			if self.goods["gear"] < 4:
				amount = ceil(5 - self.goods["gear"])
				# amount = min(amount, self.supply["gear"])
				self.ai_buy("gear", amount, market, relations, players)
		elif _type == "auto":
			if self.goods["gear"] < 4:
				amount = ceil(5 - self.goods["gear"])
				self.ai_buy("gear", amount, market, relations, players)
			if self.goods["parts"] < 4:
				amount = ceil(5 - self.goods["parts"])
				# amount = min(amount, self.supply["parts"])
				self.ai_buy("parts", amount, market, relations, players)
			if self.resources["rubber"] < 4:
				amount = ceil(4 - self.resources["rubber"])
				# amount = min(amount, self.supply["rubber"])
				self.ai_buy("rubber", amount, market, relations, players)
			if self.resources["iron"] < 3.0:
				amount = ceil(5 - self.resources["iron"])
				# amount = min(amount, self.supply["iron"])
		elif _type == "fighter":
			if self.goods["gear"] < 5:
				amount = ceil(5 - self.goods["gear"])
				# amount = min(amount, self.supply["gear"])
				self.ai_buy("gear", amount, market, relations, players)
			if self.goods["parts"] < 4:
				amount = ceil(5 - self.goods["parts"])
				# amount = min(amount, self.supply["parts"])
				self.ai_buy("parts", amount, market, relations, players)
			if self.resources["wood"] < 5:
				amount = ceil(5 - self.resources["wood"])
				# amount = min(amount, self.supply["wood"])
				self.ai_buy("wood", amount, market, relations, players)
			if self.goods["cannons"] < 7:
				amount = ceil(7 - self.goods["cannons"])
				# amount = min(amount, self.supply["cannons"])
				self.ai_buy("cannons", amount, market, relations, players)
		elif _type == "tank":
			if self.goods["gear"] < 5:
				amount = ceil(5 - self.goods["gear"])
				# amount = min(amount, self.supply["gear"])
				tryy = self.ai_buy("gear", amount, market, relations, players)
			# print(tryy)
			if self.goods["parts"] < 5:
				amount = ceil(5 - self.goods["parts"])
				# amount = min(amount, self.supply["parts"])
				self.ai_buy("parts", amount, market, relations, players)
			if self.resources["iron"] < 6:
				amount = ceil(7 - self.resources["iron"])
				# amount = min(amount, self.supply["iron"])
				ty = self.ai_buy("iron", amount, market, relations, players)
			# print(ty)
			if self.goods["cannons"] < 8:
				amount = ceil(10 - self.goods["cannons"])
				ty = self.ai_buy("cannons", amount, market, relations, players)
				#	print(ty)

	def ai_modify_priorities_from_province(self, resource):
		if resource == "food":
			self.technology_priority["steel_plows"] += 0.5
			self.technology_priority["mechanical_reaper"] += 0.5
			self.technology_priority["fertlizer"] += 0.5
			self.improve_province_priority["food"] + 0.25
		if resource == "iron":
			self.technology_priority["square_timbering"] += 0.5
			self.technology_priority["dynamite"] += 0.5
			self.technology_priority["bessemer_process"] += 0.5
			self.technology_priority["ironclad"] += 0.25
			self.technology_priority["muzzle_loaded_arms"] += 0.25
			self.technology_priority["breach_loaded_arms"] += 0.25
			self.technology_priority["machine_guns"] += 0.25
			self.technology_priority["indirect_fire"] += 0.5
			self.improve_province_priority["iron"] += 0.4
			self.build_factory_priority["parts"] += 0.2
			self.improve_province_priority["coal"] += 0.2
			self.build_factory_priority["cannons"] + 0.2
			self.build_factory_priority["tank"] += 0.5
		# self.military_priority["iron_clad"] += 1
		# self.military_priority["frigates"] + 0.1
		if resource == "coal":
			self.technology_priority["square_timbering"] += 0.5
			self.technology_priority["dynamite"] += 0.25
			self.technology_priority["bessemer_process"] += 0.25
			self.technology_priority["chemistry"] += 0.5
			self.technology_priority["synthetic_dyes"] + 0.25
			self.technology_priority["fertlizer"] + 0.5
			self.technology_priority["medicine"] + 0.5
			self.improve_province_priority["coal"] += 0.25
			self.build_factory_priority["parts"] += 0.1
			self.build_factory_priority["cannons"] += 0.1
			self.build_factory_priority["chemicals"] += 0.3
		if resource == "wood":
			self.technology_priority["saw_mill"] += 0.5
			self.technology_priority["pulping"] += 0.5
			self.technology_priority["compound_steam_engine"] += 0.5
			self.build_factory_priority["paper"] += 0.25
			self.build_factory_priority["furniture"] += 0.25
			self.improve_province_priority["wood"] += 0.25
		# self.military_priority["frigates"] + 0.4
		if resource == "cotton":
			self.technology_priority["cotton_gin"] += 0.5
			self.technology_priority["power_loom"] += 0.5
			self.technology_priority["compound_steam_engine"] += 0.25
			self.technology_priority["synthetic_dyes"] + 0.5
			self.technology_priority["chemistry"] += 0.25
			self.build_factory_priority["clothing"] += 0.25
			self.build_factory_priority["furniture"] += 0.1
			self.build_factory_priority["chemicals"] += 0.1
			self.improve_province_priority["cotton"] += 0.25
		# self.military_priority["frigates"] + 0.4
		if resource == "dyes":
			self.technology_priority["synthetic_dyes"] -= 0.5
			self.build_factory_priority["chemicals"] -= 0.1
			self.technology_priority["compound_steam_engine"] += 0.25
			self.improve_province_priority["dyes"] += 0.25
			self.build_factory_priority["clothing"] += 0.2
		if resource == "spice":
			self.technology_priority["steel_plows"] += 0.5
			self.improve_province_priority["spice"] += 0.5
		if resource == "gold":
			self.technology_priority["dynamite"] += 0.25
			self.improve_province_priority["gold"] += 0.25

		if resource == "rubber":
			self.build_factory_priority["gear"] += 0.5
			self.build_factory_priority["telephone"] += 0.3
			self.build_factory_priority["radio"] += 0.3
			self.build_factory_priority["auto"] += 0.4
			self.build_factory_priority["tank"] += 0.5
			self.build_factory_priority["fighter"] += 0.3
			self.improve_province_priority["rubber"] += 0.35
			self.technology_priority["radio"] += 0.25
			self.technology_priority["telephone"] += 0.25

		if resource == "oil":
			self.improve_province_priority["oil"] + 0.5
			self.build_factory_priority["tank"] + 0.2
			self.build_factory_priority["fighter"] + 0.15
			self.build_factory_priority["auto"] += 0.25
			self.technology_priority["rotary_drilling"] += 0.5
			self.technology_priority["oil_drilling"] += 0.5

	def choose_technology(self, market):
		print("Choose Technology")
		options = []
		print("Current Techs:")
		for t in self.technologies:
			print(t)
		print("Research: %.2f" % self.research)
		for k, t in technology_dict.items():
			if k not in self.technologies and t["requirement"] <= self.technologies and self.development_level >= t["min_mid"] and t["cost"] <= self.research:
					print(k, t)
					options.append(k)
		print("Options: %s \n" % (options))
		if len(options) == 0:
			return None
		# priorities = sorted([self.technology_priority(v,k) for (k,v) in self.technology_priority], reverse=True)
		# priorities = (sorted(self.technology_priority.keys(), key=lambda x:x[1]))
		priorities = sorted(self.technology_priority, key=self.technology_priority.get, reverse=True)
		for p in priorities:
			if p in options:
				# priorities = sorted(self.technology_priority, key=my_dict.get)
				self.ai_research_tech(p, market)
				print("Wants to research %s" % p)
				return

	def ai_research_tech(self, choice, market):
		print("%s researched %s" % (self.name, choice))
		_choice = str(choice)
		market.report.append("%s researched %s" % (self.name, _choice))
		self.research -= technology_dict[choice]["cost"]
		self.technologies.add(choice)
		if choice == "professional_armies":
			self.infantry["attack"] += 0.15
			self.infantry["defend"] += 0.15
			self.infantry["manouver"] += 0.2
			self.cavalry["attack"] += 0.15
			self.cavalry["defend"] += 0.15
			self.cavalry["manouver"] += 0.2
			self.cavalry["recon"] += 0.2
			self.artillery["attack"] += 0.15
			self.artillery["defend"] += 0.15
			self.frigates["attack"] += 0.2
		if choice == "flint_lock":
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.3
			self.infantry["defend"] += 0.1
			self.cavalry["attack"] += 0.2
			self.cavalry["defend"] += 0.1
			self.artillery["attack"] += 0.3
			self.artillery["defend"] += 0.1
			self.frigates["attack"] += 0.25

		if (choice == "muzzle_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.3
			self.infantry["defend"] += 0.1
			self.cavalry["attack"] += 0.2
			self.cavalry["defend"] += 0.05
			self.artillery["attack"] += 0.3
			self.artillery["defend"] += 0.1
			self.frigates["attack"] += 0.25
		if (choice == "cement"):
			self.max_fortification += 0.1
		if (choice == "breach_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.1
			self.infantry["attack"] += 0.35
			self.infantry["defend"] += 0.2
			self.cavalry["attack"] += 0.25
			self.cavalry["defend"] += 0.10
			self.artillery["attack"] += 0.35
			self.artillery["defend"] += 0.2
			self.frigates["attack"] += 0.35
		if (choice == "machine_guns"):
			self.irregulars["defend"] += 0.2
			self.infantry["defend"] += 1.0
			self.cavalry["defend"] + 0.1
		if (choice == "indirect_fire"):
			self.artillery["attack"] += 0.15
			self.artillery["defend"] += 0.5
			self.artillery["ammo_use"] += 0.05
			self.iron_clad["attack"] += 0.25
		if (choice == "bombers"):
			self.fighter["attack"] += 1.2
			self.fighter["ammo"] += 0.1
		if (choice == "radar"):
			self.fighter["defend"] += 1.2
			self.battle_ship["attack"] += 1
		if (choice == "telegraph"):
			self.factory_throughput += 1
			self.production_modifier += 0.15
			self.infantry["manouver"] += 0.2
			self.tank["manouver"] += 1
			self.artillery["manouver"] += 0.1
			self.fighter["manouver"] += 1
			self.battle_ship["attack"] += 0.5
		if choice == "electricity":
			self.factory_throughput += 1
			self.production_modifier += 0.15

		if choice == "radio":
			self.reputation += 0.2
			self.stability += 0.2
			self.org_factor += 0.15
			self.infantry["manouver"] += 0.2
			self.tank["manouver"] += 1
			self.artillery["manouver"] += 0.1
			self.fighter["manouver"] += 1
			self.battle_ship["attack"] += 0.5

		if choice == "early_computers":
			self.battle_ship["attack"] += 1
			self.production_modifier += 0.15
		#if choice == "atomic_bomb":
		   # print("Holy Shit!")
			#pause = input()

		# FOR AI ONLY
		if choice == "chemistry":
			self.resource_priority["rubber"] += 2
			self.improve_province_priority["rubber"] += 1.2
		if choice == "oil_drilling":
			self.resource_priority["oil"] += 2
			self.improve_province_priority["oil"] += 1.3
		if choice == "chemistry":
			self.resource_priority["coal"] += 0.2
			self.improve_province_priority["coal"] += 0.2

	def ai_improve_province_options(self):
		# print("Improve province options")
		options = []
		if "high_pressure_steam_engine" not in self.technologies:
			#	print("Does not have high pressure steam engine")
			return options
		if self.new_development >= 1.0:
			for p, prov in self.provinces.items():
				if prov.resource == "food":
					max_dev = 0
					if ("steel_plows" in self.technologies):
						max_dev = 1
					if ("mechanical_reaper" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("food")
				elif prov.resource == "iron":
					# print("got to Iron")
					max_dev = 0
					if ("square_timbering" in self.technologies):
						max_dev = 1
					# print("dev 1")
					# print("level: %s " % (prov.development_level))
					if ("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("iron")
				elif prov.resource == "coal":
					max_dev = 0
					if ("square_timbering" in self.technologies):
						max_dev = 1
					if ("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("coal")
				elif prov.resource == "cotton":
					max_dev = 0
					if ("cotton_gin" in self.technologies):
						max_dev = 1
					if ("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("cotton")

				elif prov.resource == "wood":
					max_dev = 0
					if ("saw_mill" in self.technologies):
						max_dev = 1
					if ("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("wood")
				elif prov.resource == "spice":
					max_dev = 0
					if ("steel_plows" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("spice")
				elif prov.resource == "gold":
					max_dev = 0
					if ("dynamite" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("gold")
				elif prov.resource == "dyes":
					max_dev = 0
					if ("compound_steam_engine" in self.technologies):
						max_dev = 1
					if prov.development_level < max_dev:
						options.append("dyes")
				elif prov.resource == "rubber":
					max_dev = 0
					if "chemistry" in self.technologies:
						max_dev = 1
					if "synthetic_dyes" in self.technologies:
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("rubber")
				elif prov.resource == "oil":
					max_dev = 0
					if "oil_drilling" in self.technologies:
						max_dev = 1
					if "rotary_drilling" in self.technologies:
						max_dev = 2
					if prov.development_level < max_dev:
						options.append("oil")

			if self.shipyard == 0:
				options.append("shipyard")
			if self.shipyard < 2 and "ironclad" in self.technologies:
				options.append("shipyard")
			if self.shipyard < 3 and "oil_powered_ships" in self.technologies:
				options.append("shipyard")
			if self.fortification < self.max_fortification:
				options.append("fortification")

		return options

	def ai_factory_options(self):
		options = []
		if "high_pressure_steam_engine" not in self.technologies:
			print("high_pressure_steam_engine not in technologies! __________________________________")
		if "high_pressure_steam_engine" in self.technologies and self.new_development >= 1.0:

			if self.factories["parts"]["number"] == 0 and self.resource_base["iron"] >= 1:
				options.append("parts")
			if self.factories["parts"]["number"] == 1 and "bessemer_process" in self.technologies and \
							self.resource_base["iron"] >= 1.8 and self.resource_base["coal"] >= 1.0:
				options.append("parts")
			if self.factories["clothing"]["number"] == 0 and self.resource_base["cotton"] >= 0.8:
				options.append("clothing")
			if self.factories["clothing"]["number"] == 0 and self.num_factories() >= 1:
				options.append("clothing")
			if self.factories["clothing"]["number"] == 1 and (
							"power_loom" in self.technologies and self.resource_base["cotton"] >= 1.4):
				options.append("clothing")
			if self.factories["furniture"]["number"] == 0 and self.resource_base["wood"] >= 0.8:
				options.append("furniture")
			if self.factories["furniture"]["number"] == 1 and "electricity" in self.technologies and self.resource_base[
				"wood"] >= 1.4 and self.resource_base["cotton"] >= 0.9:
				options.append("furniture")
			if self.factories["paper"]["number"] == 0 and self.resource_base["wood"] >= 1:
				options.append("paper")
			if self.factories["paper"]["number"] == 1 and "pulping" in self.technologies and self.resource_base[
				"wood"] >= 1.8:
				options.append("paper")
			if self.factories["cannons"]["number"] == 0:
				options.append("cannons")
			if self.factories["cannons"]["number"] == 1 and "bessemer_process" in self.technologies and \
							self.resource_base["iron"] >= 1.6:
				options.append("cannons")
			if self.factories["chemicals"]["number"] == 0 and "chemistry" in self.technologies and self.resource_base[
				"coal"] > 1.2:
				options.append("chemicals")
			if self.factories["chemicals"]["number"] == 1 and "dyes" in self.technologies and self.resource_base[
				"coal"] > 2:
				options.append("chemicals")
			if self.factories["gear"]["number"] == 0 and "electricity" in self.technologies:
				options.append("gear")
			if self.factories["gear"]["number"] == 1 and self.resource_base["rubber"] >= 1.1:
				options.append("gear")
			if self.factories["radio"]["number"] == 0 and "radio" in self.technologies:
				options.append("radio")
			if self.factories["telephone"]["number"] == 0 and "telephone" in self.technologies:
				options.append("telephone")
			if self.factories["fighter"]["number"] == 0 and "flight" in self.technologies:
				options.append("fighter")
			if self.factories["auto"]["number"] == 0 and "automobile" in self.technologies:
				options.append("auto")
			if self.factories["tank"]["number"] == 0 and "mobile_warfare" in self.technologies:
				options.append("tank")
				# print("Tank factory is an option!!!")
		return options

	def ai_build_frigates(self, market):
		self.AP -= 1
		self.resources["wood"] -= 1
		self.resources["cotton"] -= 1
		self.goods["cannons"] -= 1
		self.military_produced["frigates"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("%s builds a Frigate" % (self.name))
		market.report.append("%s builds a Frigate" % (self.name))

	def ai_build_iron_clad(self, market):
		self.AP -= 1
		self.goods["cannons"] -= 1
		self.resources["iron"] -= 1
		self.goods["parts"] -= 1
		self.military_produced["iron_clad"] += 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("%s builds an Ironclad" % (self.name))
		market.report.append("%s builds an Ironclad" % (self.name))

	def ai_build_battle_ship(self):
		self.AP -= 2
		self.goods["cannons"] -= 3
		self.resources["iron"] -= 3
		self.goods["parts"] -= 1
		self.goods["gear"] -= 1
		self.military_produced["battle_ship"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		print("%s build Battle_ship" % (self.name))
		market.report.append("%s build Battle_ship" % (self.name))

	def decide_build_navy(self, market, relations, players):
		print("Decide on navy__###############################################################")
		if self.AP < 1:
			print("No AP left")
			return
		transport_limit = 0
		transport_limit += self.military["frigates"] * 2
		transport_limit += self.military["iron_clad"] * 2
		transport_limit += self.military["battle_ship"] * 3
		
		num_units = self.num_army_units()
		print("Number of Army Units: %s" % (num_units))
		print("Transport Limit %s" % (transport_limit))
		print("num units * per.navy %s" % (num_units*self.personality["Navy"]) )
		print("Personality.navy: %s" % (self.personality["Navy"]))
		print("Number of units: %s" % (num_units))
		print("Num_units times pers.Navy: %s" %(num_units * self.personality["Navy"]))
		print("Transpot Limit: %s" % (transport_limit))
		if transport_limit > num_units * self.personality["Navy"]:
			return
		print("Wants to build navy ***********************************************")
		if self.AP >= 2 and "oil_powered_ships" in self.technologies and self.shipyard == 3:
			if self.goods["cannons"] < 5:
				self.ai_buy("cannons", 3, market, relations, players)
			if self.resources["iron"] < 3:
				self.ai_buy("iron", 3, market, relations, players)
			if self.goods["parts"] < 1:
				self.ai_buy("parts", 1, market, relations, players)
			if self.goods["gear"] < 1:
				self.ai_buy("gear", 1, market, relations, players)
			if self.goods["cannons"] >= 5 and self.resources["iron"] >= 3 and self.goods["parts"] >= 1 and \
							self.goods["gear"] >= 1:
				self.ai_build_battle_ship(market)

		elif "oil_powered_ships" not in self.technologies and "ironclad" in self.technologies and self.shipyard == 2:
			if self.goods["parts"] < 1 and market.buy_price("parts", self.supply["parts"]) < self.resources[
				"gold"] * 1.75:
				self.ai_buy("parts", 1, market, relations, players)
			if self.goods["cannons"] < 3 and market.buy_price("cannons", self.supply["cannons"]) < self.resources[
				"gold"] * 2.5:
				self.ai_buy("cannons", 2, market, relations, players)
			if self.resources["iron"] < 1 and market.buy_price("iron", self.supply["iron"]) < self.resources[
				"gold"] * 1.75:
				self.ai_buy("iron", 1, market, relations, players)
			if self.resources["iron"] >= 1 and self.goods["parts"] >= 1 and self.goods["cannons"] > 3:
				self.ai_build_iron_clad(market)

		elif self.goods["cannons"] >= 2 and self.resources["wood"] >= 1 and self.shipyard >= 1 and self.resources[
			"cotton"] >= 1 and self.AP >= 1 and "ironclad" not in self.technologies:
			self.ai_build_frigates(market)

	def ai_build_factory(self, _type, market, players):
		if _type == "parts" or _type == "cannons":
			self.resource_priority["coal"] += 0.1
			self.resource_priority["iron"] += 0.2
			self.resourse_to_keep["coal"] += 1
			self.resourse_to_keep["iron"] += 2
		if _type == "clothing":
			self.resource_priority["cotton"] += 0.3
			self.resource_priority["dyes"] += 0.4
			self.resourse_to_keep["cotton"] += 3
			self.resourse_to_keep["dyes"] += 1
		if _type == "paper":
			self.resource_priority["wood"] += 0.3
			self.resourse_to_keep["wood"] += 3
		if _type == "furniture":
			self.resource_priority["wood"] += 0.2
			self.resource_priority["cotton"] += 0.1
			self.resourse_to_keep["wood"] += 2
			self.resourse_to_keep["cotton"] += 1
		if _type == "chemicals":
			self.resource_priority["coal"] += 0.3
			self.resourse_to_keep["coal"] += 2
		if _type == "gear":
			self.resourse_to_keep["rubber"] += 2
			self.resource_priority["rubber"] += 0.5
			self.resource_priority["iron"] += 0.1
		if _type == "tank" or _type == "fighter":
			self.resource_priority["oil"] += 0.2
			self.resource_priority["iron"] += 0.1
			self.goods["gear"] -= 1
		if _type == "auto":
			self.resourse_to_keep["rubber"] += 1
			self.resourse_to_keep["iron"] += 1
			self.resource_priority["oil"] += 0.2
			self.resource_priority["rubber"] += 0.2
			self.resource_priority["iron"] += 0.05
			self.goods["gear"] -= 1

		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories[_type]["number"] += 1
		# globe.factories[_type] += 1
		for p in players.values():
			if type(p) == AI:
				if _type != "cannons":
					p.build_factory_priority[_type] -= 0.2
				else:
					p.build_factory_priority[_type] -= 0.1
		self.stability -= 0.2
		if self.stability < -3.0:
			self.stability = -3.0
		self.new_development -= 1
		self.resources["gold"] += 3

		print("%s builds a %s Factory" % (self.name, _type))
		market.report.append("%s builds a %s Factory" % (self.name, _type))

	def ai_develop_province(self, _type, market):
		# print("Develop Province")
		if _type == "shipyard":
			self.ai_build_steam_ship_yard(market)
			return
		if _type == "fortification":
			self.ai_improve_fortifications(market)
			return
		for p, province in self.provinces.items():
			if province.resource == _type:
				# print("consider - res: %s, dev %s " % (province.resource, province.development_level))
				if self.check_if_prov_can_be_dev(p) == True:
					# print("Can a province be developed?")
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
					self.resource_priority["coal"] += 0.05
					self.number_developments += 1
					self.resources["gold"] += 3
					print("%s has developed province the %s producing province of %s" % (self.name, self.provinces[p], _type))
					market.report.append("%s has developed province the %s producing province of %s" % (self.name, self.provinces[p], _type))
					return

	def ai_improve_fortifications(self, market):
		self.AP -= 1
		self.goods["cannons"] -= 1
		self.fortification += 0.1
		print("%s hsa increased its fortification level to %s" % (self.name, self.fortification))

	def ai_build_steam_ship_yard(self, market):
		self.goods["parts"] -= 1
		self.resources["wood"] -= 1
		self.AP - 1
		self.new_development -= 1
		self.shipyard += 1
		blank = ""
		if self.shipyard == 1:
			blank = "wooden"
		if self.shipyard == 2:
			blank = "steam"
		if self.shipyard == 3:
			blank = "oil powered"
		print("%s has completed a shipyard for %s ships" % (self.name, blank))
		market.report.append("%s has completed a shipyard for %s ships" % (self.name, blank))


	def AIbuild_army(self, market, relations, players):
		print("AI Build Army________________________________-")
		if self.proPOP > 4 and self.freePOP < 0.3:
			self.proPOP -= 1
			self.freePOP += 1
		num_units = self.num_army_units()
		if num_units > self.POP * (self.personality["Army"]) * 0.8 and market.turn < 18:
			return
		if num_units > self.POP * self.personality["Army"] and "mobile_warfare" not in self.technologies:
			return
		print("Wants to build army___________________________________________-")
		if self.can_train < 1:
			print("Cannot further train")
			return
		ammo_needed = self.calculate_ammo_needed()
		cans = self.goods["cannons"] - ammo_needed
		if cans < 1:
			self.ai_buy("cannons", 4, market, relations, players)
		if self.goods["cannons"] - ammo_needed < 1:
			print("Not enough cannons")
			return

		tries = 0
		while ((self.goods[
					"cannons"] - self.calculate_ammo_needed()) > 1.5 and self.freePOP > 0.2 and self.can_train >= 1):
			priorities = sorted(self.military_priority, key=self.military_priority.get, reverse=True)
			if "mobile_warfare" in self.technologies:

				if self.military["tank"] < 5:
					if self.goods["tank"] >= 1:
						self.ai_build_tank(market)
					else:
						self.ai_buy("tank", 1, market, relations, players)
				if self.military["fighter"] < 5:
					if self.goods["fighter"] >= 1:
						self.ai_build_fighter(market)
					else:
						self.ai_buy("fighter", 1, market, relations, players)

			for p in priorities:
				if p == "infantry" and self.military["infantry"] < self.POP / 3.4:
					self.ai_build_infantry(market)
				elif p == "cavalry" and "mobile_warfare" not in self.technologies and self.goods["tank"] == 0 and \
								self.military["cavalry"] <= self.POP / 3.8:
					self.ai_build_cavalry(market)
				elif p == "artillery" and self.military["artillery"] <= self.POP / 3.8:
					if self.goods["cannons"] >= 3:
						self.ai_build_artillery(market)
				elif p == "tank":
					if self.goods["tank"] >= 1 and self.military["tank"] <= self.POP / 3.8:
						self.ai_build_tank(market)
					else:
						if self.supply["tank"] > 2 and self.resources["gold"] > market.buy_price("tank", self.supply[
							"tank"]) * 2:
							self.ai_buy("tank", 1, market, relations, players)

				elif p == "fighter" and self.military["fighter"] <= self.POP / 4.2:
					if self.goods["fighter"] >= 1:
						self.ai_build_fighter(market)
					else:
						if self.supply["fighter"] > 2 and self.resources["gold"] > market.buy_price("fighter", self.supply["fighter"]) * 2:
							self.ai_buy("fighter", 1, market, relations, players)

				tries += 1
			if tries > 20:
				return

	def ai_build_tank(self, market):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.can_train -= 1
		self.military_produced["tank"] += 1.0
		self.goods["tank"] -= 1
		self.number_units += 1
		self.military_priority["tank"] -= 0.3
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		#print(self.military_priority[k])
		print("%s has compleated a tank unit" % (self.name))
		market.report.append("%s has completed a tank unit" % (self.name))

	def ai_build_fighter(self, market):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.can_train -= 1
		self.military_produced["fighter"] += 1.0
		self.goods["fighter"] -= 1
		self.number_units += 1
		self.military_priority["fighter"] -= 0.33
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		# print(self.military_priority[k])
		print("%s has completed a fighter unit" % (self.name))
		market.report.append("%s has completed a fighter unit" % (self.name))

	def ai_build_infantry(self, market):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.can_train -= 1
		self.goods["cannons"] -= 1.0
		self.military_produced["infantry"] += 1.0
		self.number_units += 1
		self.military_priority["infantry"] -= 0.45
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("%s has completed an infantry unit" % (self.name))
		market.report.append("%s has completed an infantry unit" % (self.name))

	def ai_build_cavalry(self, market):
		self.resources["food"] -= 1.0
		self.can_train -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.goods["clothing"] -= 0.1
		self.number_units += 1
		self.military_produced["cavalry"] += 1.0
		self.military_priority["cavalry"] -= 0.5
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
	 #   print("%s has completed a cavalry unit" % (self.name)) 
		market.report.append("%s has completed a cavalry unit" % (self.name))

	def ai_build_artillery(self, market):
		self.goods["cannons"] -= 2.0
		self.can_train -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		self.military_produced["artillery"] += 1.0
		self.military_priority["artillery"] -= 0.4
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("%s has completed a artillery unit" % (self.name))
		market.report.append("%s has completed a artillery unit" % (self.name))

	def ai_build_irregulars(self):
		self.goods["cannons"] -= 0.5
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		self.military["irregulars"] += 1.0
		self.military_priority["irregulars"] -= 0.7
		for k in self.military_priority.keys():
			self.military_priority[k] += 0.1
		print("%s has completed an fighter irregulars unit" % (self.name))



	def use_chemicals(self, market, relations, players):
		if self.goods["chemicals"] > 4:
			if self.resources["dyes"] < 3:
				self.goods["chemicals"] -= 1
				self.resources["dyes"] += 1
		   #     print("Turned Chemicals to dyes")
		if self.resources["food"] < 5 and len(market.market["food"]) < 12 and "fertlizer" in self.technologies:
			count = 0
			for p, prov in self.provinces.items():
				if prov.resource == "food":
					count += 1
			while count > 0 and self.goods["chemicals"] > 0:
				self.resources["food"] += 1
				self.goods["chemicals"] -= 1
				count -= 1
			#    print("Turn chemicals to food")
		if "synthetic_rubber" in self.technologies and self.resources["rubber"] < 2 and self.resources["oil"] >= 4:
			self.resources["rubber"] += 1
			self.goods["chemicals"] -= 1
			self.resources["oil"] -= 1
		 #   print("Turns oil and chemicals to rubber")
		if "synthetic_rubber" in self.technologies and self.resources["rubber"] < 2 and self.resources["oil"] <= 5 and \
						self.supply["oil"] > 12 and self.resources["gold"] > 42:
			self.ai_buy("oil", 4, market, relations, players)
		if "synthetic_oil" in self.technologies and self.resources["oil"] < 2 and self.goods["chemicals"] >= 5 and len(
				market.market["oil"]) < 13:
			self.resources["oil"] += 1
			self.goods["chemicals"] -= 3
		   # print("Turns chemicals to oil")

	def use_culture(self, players):
		count = 0
		while self.culture_points >= 2 and count <= 8:
			if self.culture_points < 2:
				return
			if self.culture_points >= 1:
				if self.diplo_action >= 1 and self.reputation < 0.1:
					self.culture_points -= 1
					self.diplo_action -= 1
					self.reputation += 0.1
				  #  print("Improve Reputation______________________________________________")
					count += 1
					continue
			if self.culture_points >= 1:
				if self.stability <= 0.0:
					self.culture_points -= 1
					self.stability += 0.5
				   # print("Increased Stability_______________________________________________")
					count += 1
					continue
			if self.culture_points >= 1:

				if self.diplo_action >= 1 and self.reputation < 0.3:
					self.culture_points -= 1
					self.diplo_action -= 1
					self.reputation += 0.1
				   # print("Improve Reputation______________________________________________")
					count += 1
					continue
			other = 0
			for p in self.provinces.values():
				if p.culture != self.culture:
					other += 1
			if other >= 1 and self.culture_points > 1:
				for p in self.provinces.values():
					if p.culture != self.culture and self.culture_points > 1 and p.culture not in self.accepted_cultures:
						self.culture_points -= 1
						count += 1
						chance = uniform(0, 1)
						if p.type == "uncivilized":
							if chance < 0.66:
								self.accepted_cultures.add(p.culture)
							   # print("Integrated Culture")
								continue
						if p.type == "old":
							if chance < 0.33:
								self.accepted_cultures.add(p.culture)
							  #  print("Integrated Culture")
								continue
						if p.type == "civilized":
							if chance < 0.25:
								self.accepted_cultures.add(p.culture)
							 #   print("Integrated Culture__________________________________________")
								continue
						continue

			if self.diplo_action >= 1 and self.reputation < 0.6 and self.culture_points >= 1:
				self.culture_points -= 1
				count += 1
				self.diplo_action -= 1
				self.reputation += 0.2
		   #     print("Improve Reputation____________________________________________________________")
				continue

			if self.stability < 1.0 and self.culture_points >= 1:
				self.culture_points -= 1
				count += 1
				self.stability += 0.5
		  #      print("Increased Stability______________________________________________________________")
				continue
			# if self.culture >= 3:
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
			if self.resources["gold"] < 40 and self.culture_points >= 1:
				for p in players.values():
					if p.type == "major":
						p.resources["gold"] -= 1
						self.resources["gold"] += 1
						self.culture_points -= 1
						count += 1
						continue

			   # print("Cultural Exports ____________________________________________")
				continue
			if self.stability < 2.25 and self.culture_points >= 1:
				self.culture_points -= 1
				count += 1
				self.stability += 0.5
				if self.stability > 3.0:
					self.stability = 3.0
			 #   print("Increased Stability_________________________________________________")
				continue
			if self.diplo_action >= 1 and self.reputation < 0.75 and self.culture_points >= 1:
				self.culture_points -= 1
				count += 1
				self.diplo_action -= 1
				self.reputation += 0.2
			  #  print("Improve Reputation________________________________________________")
				continue
			count += 1

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

		if "ironclad" in self.technologies and self.military["frigates"] >= 2:
			self.resources["iron"] += 1
			self.military["frigates"] -= 1
			self.milPOP -= 0.2
			self.freePOP += 0.2
			self.number_units -= 1

		if self.military["irregulars"] > 0:
			if self.military["infantry"] >= 3 or self.military["cavalry"] >= 3:
				self.military["irregulars"] -= 1
				self.milPOP -= 0.2
				self.freePOP -= 0.2
				self.number_units -= 1
