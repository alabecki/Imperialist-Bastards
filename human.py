
from player_class import*
import random
import minor_classes
from technologies import technology_dict
from commands import*


class Human(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(Human, self).__init__(_name, _type, number, *args, **kwargs)

		#Good and Resources
		self.resources = {
			"gold": 0.0,
			"food": 0.0,
			"iron": 0.0,
			"wood": 0.0,
			"coal": 0.0,
			"cotton": 0.0,
			"spice": 0.0,
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

	def increase_pop(self):
		med = False
		if(self.POP_increased > 1):
			print("You have already increased your population as much as possible this turn \n")
			return
		if(self.POP_increased == 1.0):
			print("You will need to consume a chemical (medicine) to increase your POP again \n")
			if self.goods["chemicals"] < 1:
				print("You do not have any chemicals")
				return
			else:
				med = input("Are you willing to spend medicine to increase your population? (y/n)\n")
				if med == "n":
					return
				else:
					med = True
		if(self.resources["food"] < 1.0):
			print("You do not have enough food to increase your population \n")
			return
		if(self.goods["clothing"] < 1.0):
			print("You do not have enough clothing to increase your population \n")
			return
		if(self.goods["furniture"] < 1.0):
			print("You do not have enough furniture to increase your population \n")
			return
		else:
			self.POP += 1.0
			self.freePOP += 1.0
			self.numLowerPOP += 1
			self.resources["food"] -= 1.0
			self.goods["clothing"] -= 1.0
			self.furniture["furniture"] -= 1.0
			self.increase_pop += 1
			self.stability -= 0.1
			if med == True:
				self.goods["medicine"] -= 1.0
			print("Your nation now has a population of %s with %s free POPS \n" % (self.POP), self.freePOP)
			return

	def increase_middle_class(self):
		if(self.freePOP < 0.5):
			print("You do not have any free POPs")
			return
		requirement = ["paper"]
		if self.resources["spice"] < 1:
			print("You do not have any spice")
			return
		if self.goods["paper"] < 1:
			print("You do not have any paper")
			return
		if self.numMidPOP >= 2: 
			if self.goods["clothing"] < 1:
				print("You do not have any clothing")
				return
			else: 
				requirement.append("clothing")
		if self.numMidPOP >= 3:
			if self.goods["furniture"] < 1:
				print("You do not have any furniture")
				return
			else:
				requirement.append("furniture")
		if self.numMidPOP >= 4:
			if self.goods["paper"] < 2:
				print("You do not have enough paper")
				return
			else:
				requirement.append("paper")
		if self.numMidPOP >= 5:
			if self.goods["chemicals"] < 1:
				print("You do not have any chemicals")
				return
			else:
				requirement.append("chemicals")
		if self.numMidPOP >= 6:
			if self.goods["radio"] < 1:
				print("You do not have enough radios")
				return
			else:
				requirement.append("radio")
		if self.numMidPOP >= 7:
			if self.goods["telephone"] < 1:
				print("You do not have any telephones")
				return
			else:
				requirement.append("telephone")
		if self.numMidPOP >= 8:
			if self.goods["auto"] < 1:
				print("You do not have any telehones")
				return
			else:
				requirement.append("auto")
		_type = input("What kind of middle class POP would you like to create?: researchers officers  \
				bureaucrats artists managers \n")
		if(self.midPOP[_type] >= 2.0):
			print("You have already created as many %s a permitted \n")
			return
		self.goods["spice"] -= 1
		for r in requirement:
			self.goods[r] -1
		self.numLowerPOP -= 0.25
		self.numMidPOP += 0.25
		self.midPOP[_type] += 0.25
		self.freePOP -= 0.25
		self.new_development += 0.5
	

	def research_tech(self):
			print("Which Technology would you like to develop? (Print entire name) \n")
			print("You currently have %s Research Points \n" % (self.research))
			options = []
			for k, t in technology_dict.items():
				if k not in self.technologies and t["requirement"] <= self.technologies \
				and self.research >= t["cost"] and self.numMidPOP >= t["min_mid"]:
					print(k, t)
					options.append(k)
			if len(options) == 0:
				print("You cannot research any technologies at this time")
				return
			choice = " "
			while choice not in options:
				choice = input()
			
			self.research -= technology_dict[choice]["cost"]
			self.technologies.add(choice)
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n ")
			print("Your ingenius researches have discovered %s \n " % (choice))
			if(choice == "muzzle_loaded_arms"):
				self.irregulars["attack"] += 0.15
				self.irregulars["defend"] += 0.1
				self.infantry["attack"] += 0.25
				self.infantry["defend"] += 0.10
				self.cavalry["attack"] += 0.20
				self.cavalry["defend"] += 0.08
				self.artillery["attack"] += 0.25
				self.artillery["defend"] += 0.10
				self.frigates["attack"] += 0.25
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
				self.iron_clad["defend"] += 0.25
			if(choice == "steel_plate_armor"):
				self.iron_clad["attack"] += 0.45
			if(choice == "bombers"):
				self.fighter["attack"] += 1
				self.fighter["oil"] += 0.05
				self.fighter["ammo"] += 0.1
			if(choice == "radar"):
				self.fighter["defend"] += 0.5
				self.battle_ship["attack"] += 1

	def spice_to_stability(self):
		if self.resources["spice"] > 2:
			print("You do not have enough spice raise your stability")
			return
		if self.stability >= 3:
			print("Your stability cannot be further increased")
		else:
			self.resources["spice"] -=2
			self.stability +1
			if self.stability > 3:
				self.stability = 3

	def assign_POP(self):
		kind = " "
		_choices = list(range(1, 4))
		choices = ''.join(str(e) for e in _choices)
		while (str(kind) not in choices):
			kind = input("Where would you like to assign a POP?: 1, province or 2, production, 3, free a POP \n")
		if(kind == "1"):
			if(self.freePOP < 1.0):
				print("You do not have any free POPs\n ")
				return
			empty = False
			print("Free POPs: %s" % (self.freePOP))
			for k, p in self.provinces.items():
				if(p.worked == False):
					print("Name: %s  Resoruce: %s  Quality: %s \n"% (p.name, p.resource, p.quality))
					empty = True
			if empty == False:
				print("All of your provinces are currently being worked \n")
				return
			else:
				print("To which province do you wish to assign a POP? (type in name) \n")
				choice = " "
				while choice not in self.provinces.keys():
					choice = input()
				self.freePOP -= 1.0
				self.provinces[choice].worked = True
				print("%s is being worked and will now produce for you while it remains worked \n" % (self.provinces[choice].name))
							#self.provinces[p][worked] = True
				return
		elif(kind == "2"):
			if(self.freePOP < 1.0):
				print("You do not have any free POPs\n ")
				return
			self.freePOP -= 1
			self.proPOP += 1
			print("You now have %s POPs assigned to production \n" % (self.proPOP))
			return
		elif(kind == "3"):
			print("From where will you like to free a POP? 1, province or 2, production? \n")
			kind2 = " "
			_choices = list(range(1, 3))
			choices = ''.join(str(e) for e in _choices)
			while (str(kind2) not in choices):
				kind2 = input()
			if(kind2 == "1"):
				print("From which province would you like to take a POP? (tyoe name)\n")
				for k, v in self.provinces.items():
					if(v.worked == True):
						print("Name: %s  Resoruce: %s  Quality: %s \n"% (v.name, v.resource, v.quality))
				choice = " "
				while choice not in self.provinces.keys():
					choice = input()
				self.freePOP += 1.0
				self.provinces[choice].worked = False
				print("%s is no longer being worked \n" % (self.provinces[choice].name))
				print("You now have %s free POPS \n " % (self.freePOP))
			elif(kind2 == "2"):
				if self.proPOP < 1:
					print("You do not currently have any POPs working in production \n")
				else:
					self.proPOP -= 1
					self.freePOP += 1
					print("You now have %s free POPS  and %s POPs working in production\n " % (self.freePOP, self.proPOP))

	def use_spice_stability(self):
		if self.resources["spice"] < 2:
			print("You do not have enough spice")
		else:
			self.resources["spice"] -=2
			self.stability +1
			if self.stability > 3:
				self.stability = 3
		print("Your stability is now %s " % (self.stability))


	def build_unit(self):
		if(self.freePOP < 0.2):
			print("You do not have enugh free POPs to build a unit \n")
			return
			if(self.goods["cannons"] < 1):
				print("You do not have enough cannons to build any military unites \n")
			return
		print("What kind of unit would you like to build? \n")
		for k, v in self.military.items():
			print(k, v)
		choice = " "
		while choice not in self.military.keys():
			choice = input()
		if(choice == "infantry"):
			self.build_infantry()
		elif(choice == "cavalry"):
			self.build_cavalry ()
		elif(choice == "artillery"):
			self.build_artillery()
		elif(choice == "tank"):
			self.build_tank()
		elif(choice == "fighter"):
			self.build_fighter()
		elif(choice == "frigates"):
			self.build_frigates()
		elif(choice == "iron_clad"):
			self.build_ironclad()
		elif(choice == "battle_ship"):
			self.build_battleship()
		else:
			return

	def build_infantry(self):
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.military["infantry"] += 1.0
		self.num_units += 1.0
		self.can_train -= 1.0
		print("You now have %s Infantry \n" % (self.military["infantry"]))

	def build_cavalry(self):
		if(self.resources["food"] < 1):
			print("You do not have enough Food to build cavalry \n")
			return
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		else:
			self.resources["food"] -= 1
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.goods["cannons"] -= 1.0
			self.military["cavalry"] += 1.0
			self.num_units += 1.0
			self.can_train -= 1.0
			print("You now have %s cavalry \n" % (self.military["cavalry"]))

	def build_artillery(self):
		if(self.goods["cannons"] < 2.0):
			print("You do not have enough cannons to build artillery \n")
			return
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		self.goods["cannons"] -= 2.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military["artillery"] += 1.0
		self.num_units += 1.0
		self.can_train -= 1.0
		print("You now have %s artillery \n" % (self.military["artillery"]))

	def build_tank(self):
		if self.goods["tank"] < 1:
			print("You do not have any tanks to turn into units")
			return
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		self.goods["tank"] -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military["tank"] += 1.0
		self.num_units += 1.0
		self.can_train -= 1.0
		print("You now have %s tanks \n" % (self.military["tank"]))


	def build_fighter(self):
		if self.goods["fighter"] < 1:
			print("You do not have any fighters to turn into units")
			return
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		self.goods["fighter"] -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military["fighter"] += 1.0
		self.num_units += 1.0
		self.can_train -= 1.0
		print("You now have %s fighters \n" % (self.military["fighter"]))


	def build_frigates(self):
		if self.goods["frigates"] < 1:
			print("You do not have any frigates made to turn into units")
			return
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["frigates"] -= 1.0
			self.military["frigates"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2
			print("You now have %s frigates \n" % (self.military["frigates"]))
			return

	def build_ironclad(self):
		if self.goods["iron_clad"] < 1:
			print("You do not have any iron clads made to turn into units")
			return
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["iron_clad"] -= 1.0
			self.military["iron_clad"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2
			print("You now have %s iron clads \n" % (self.military["iron_clad"]))
			return

	def build_battleship(self):
		if self.goods["battle_ship"] < 1:
			print("You do not have any battle ships made to turn into units")
			return
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["battle_ship"] -= 1.0
			self.military["battle_ship"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2

			print("You now have %s battle ships \n" % (self.military["battle_ship"]))
			return


	def build_factory(self, market):
		if(self.new_development < 1):
			print("You do not have any Development Points to spend \n")
			return
		if("high_pressure_steam_engine" not in self.technologies):
			print("you need the High Pressure Steam Engine technology to build factories \n")
			return
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		if(self.resources["iron"] < 1.0):
			print("You do not have enough iron to build a factory \n")
			return
		elif(self.goods["parts"] < 1.0):
			print("You do not have enough parts to build a factory \n")
			return
		options = []
		if "high_pressure_steam_engine" in self.technologies and self.new_development >= 1.0:
			if self.factories["ship_yard"] == 0:
				options.append["ship_yard"]
			if self.factories["ship_yard"] == 1 and "iron_clad" in self.technologies:
				options.append["ship_yard"]
			if self.factories["ship_yard"] == 2 and "oil_powered_ships" in self.technologies:
				options.append["ship_yard"]
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
			if self.factories("telephone") < 2 and "telephone" in self.technologies:
				options.append("telephone")
			if self.factories("fighter") < 2 and "flight" in self.technologies:
				options.append("fighter")
			if self.factories("auto") < 2 and "automobile" in self.technologies:
				options.append("auto")
			if self.factories("tank") < 2 and "mobile_warfare" in self.technologies:
				options.append("tank")
		if len(options) == 0:
			print("You cannot build any factories at this time")
			return
		choice = ""
		while choice not in options:
			print("What kind of factry would you like to build?")
			for o in options:
				print (options)
			choice = input()

		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories[choice] += 1
		market.global_factories[choice] += 1
		self.stability -= 0.33
		self.new_development -= 1
		print("You have constructed a %s factory \n" % (choice))
		return

	def improve_fortifications(self):
		if self.AP < 1:
			print("You do not have enough action points \n")
			return
		elif self.goods["cannons"] < 1:
			print("You do not have enough cannoms \n")
			return
		elif self.fortification == 1.1:
			if "cement" not in self.technologies:
				print("You cannot further upgrade your fortifications without cement \n")
				return
		elif self.fortification == 1.2:
			print("You have already upgraded your fortifications as much as possible \n")
			return
		else:
			self.AP -= 1
			self.goods["cannons"] -= 1
			self.fortification += 0.1
			print("Your fortresses now modifies your defense strength by a scalar if %s \n" % (self.fortification))
			return


	def develop_province(self):
		if(self.new_development < 1):
			print("You do not have any Development Points to spend \n")
			return
		elif(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		elif(self.resources["wood"] < 1.0):
			print("You do not have enough wood \n")
			return
		elif(self.resources["iron"] < 0.5):
			print("You do not have enough iron \n")
			return
		elif(self.goods["parts"] < 1.0):
			print("You do not have enough parts \n")
			return
		else:
			for k, v in self.provinces.items():
				print("Name: %s Resoruce: %s Development: %s, Quality: %s  \n" % (v.name, v.resource, v.development_level, v.quality))
			prov = " "
			while prov not in self.provinces.keys():
				prov = input("Which province would you like to develop? \n")
			if(self.provinces[prov].development_level == 2):
				print("You have already reached the maximum level of development")
				return
			elif(self.provinces[prov].resource == "food"):
				max_dev = 0
				if("steel_plows" in self.technologies):
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
			if self.provinces[prov].development_level == max_dev:
				print("You cannot further develop this province at this time")
				return
			else:
				self.resources["iron"] -= 0.5
				self.goods["parts"] -= 1.0
				self.resources["wood"] -= 1.0
				self.AP -= 1
				self.new_development -= 1
				self.provinces[prov].development_level += 1
				self.number_developments += 1
				print("You have developed province %s, its development level is now %s \n" % (prov, self.provinces[prov].development_level))


	def craftman_production(self):
		craft = {
			"parts" : "iron",
			"cannons" : "iron",
			"paper" : "wood",
			"clothing" : "cotton",
			"furniture" : "wood",
			"chemicals" : "coal"
			}
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type = " "
		while _type not in self.goods.keys():
			_type = input("What kind of good do you want to produce with craftsmen?: parts cannons clothing paper furniture \n")
		if(self.resources[craft[_type]] < 1.2):
			print("You do not have enough %s with which to make %s \n" % (craft[_type], _type))
			return
		else:
			self.resources[craft[_type]] -= 1.1
			self.goods_produced[_type] += 1.0
			self.AP -= 1
			self.new_development -= 0.05
			print("The  %s will be ready next turn \n" % (_type))
			return


	def factory_production(self):
		manufacture = {
		"parts": {"iron": 0.6, "coal": 0.4},
		"cannons": {"iron": 0.6, "coal": 0.4},
		"paper": {"wood": 1.0},
		"clothing": {"cotton": 0.8, "dyes": 0.2},
		"furniture": {"wood": 0.65, "cotton": 0.35},
		"chemicals": {"coal": 0.5},
		"gear": {"rubber": 0.5, "iron": 0.3, "coal": 0.2},
		"radio": {"gear": 0.85, "wood": 0.15},
		"telephone": {"gear": 0.85, "wood": 0.15},
		"fighter": {"wood": 0.5, "gear": 0.5, "parts": 0.5, "arms": 1.0},   # 2.5 
		"auto": {"rubber": 0.5, "gear": 0.5, "parts": 0.5, "iron": 0.5},		#2
		"tank": {"auto": 1, "iron": 1.0, "arms": 1.5},  #4 
		"frigate": {"cannons": 1.0, "wood": 1.0, "cotton": 1.0},
		"iron_clad": {"cannons": 1.0, "iron": 1.0, "parts": 1.0},
		"battle_ship": {"cannons": 3.0, "iron": 3.0, "parts": 1.0, "gear": 1.0 }  #8 
			}
		stab_rounds = round(self.stability * 2) / 2
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type =  " "
		while _type not in self.goods.keys():
			for k in self.factories.keys():
				print(k)
			_type = input("What kind of good do you want to produce with factory? \n")
		if self.factories[_type] == 0:
			print("You do not have a %s factory \n" % (_type))
			return
		else:
			max_amount = self.factories[_type] * stab_rounds * 4
			material_mod = 1 - (self.midPOP["managers"]["number"] / 3)
			amount = input("How many %s do you want to produce? (max: %s) \n" % (_type, max_amount))
			amount = int(amount)
			if(amount > max_amount):
				print("You can only build %s items at a time with a %s factory \n" % (self.factory_throughput, _type))
				return
			else:
				for i in manufacture[_type]:
					if i in self.resources.keys():
						if(manufacture[_type][i] * amount * material_mod > self.resources[i]):
							print("You do not have sufficient %s for your factory to produce %s %s \n" % (i, amount, _type))
							return
					if i in self.goods.keys():
						if(manufacture[_type][i] * amount * material_mod > self.goods[i]):
							print("You do not have sufficient %s for your factory to produce %s %s \n" % (i, amount, _type))
							return
					else:
						for i in manufacture[_type]:
							if i in self.resources.keys():
								self.resources[i] -= manufacture[_type][i] * amount * material_mod
							else:
								self.goods[i] -= manufacture[_type][i] * amount * material_mod
						self.goods_produced[_type] += amount
						self.AP -= 1
						print("Next turn you will receive %s %s" % (self.goods_produced[_type], _type))
						return


	def view_inventory(self):
		#print("gold: %s \n" % (self.gold))
		for key, value in self.resources.items():
			if key != "gold":
				print (" %s : %s \n" % (key, value))
		for key, value in self.goods.items():
			print (" %s : %s \n" % (key, value))

	def view_inventory_production_needs(self):
		stab_rounds = round(self.stability * 2) / 2
		for key, value in self.resources.items():
			if(key == "food" or key == "spice" or key =="coal"):
				if(key == "food"):
					need = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
				if(key == "spice"):
					need = (self.numMidPOP * 0.2)
				if(key == "coal"):
					need = 0.3 * self.number_developments
				current_production  = 0
				for k, p in self.provinces.items():
					if p.resource == key and p.worked == True:
						current_production += development_map[p.development_level] * stability_map[stab_rounds] * p.quality
				forecast = (self.resources[key] + current_production) - need
				print("Resource: %s, Current Supply: %s, Current Consumption: %s, Current Production: %s, New Turn Forecast %s \n" % \
				(key, self.resources[key], need, current_production, forecast))


	def use_culture(self):
		if self.culture_points < 1:
			print("Your barbaric nation does not have any culture points at this time")
			return
		_choices = list(range(1,6))
		choices + ''.join(str(e for e in _choices))
		choice = " "
		while (choice not in choices):
			for k, v in culture_commands.items():
				print("%s: %s" % (k,v))
			choice = input()
		if choice == "1":
			self.culture_points -= 1
			self.stability += 0.5
		if choice == "2":
			options = []
			for p, prov in provinces():
				if p.culture != self.culture and p.cultre not in self.accepted_cultures:
					options.append(prov)
			if len(options) == 0:
				print("Fortunately, you have no provinces in need of assimalation")
				return
			else:
				print("Which province would you like to try to include?")
				for o in options:
					print(o.name) 
				opt = input()
				self.culture_points -= 1
				chance = uniform(0, 1)
				if opt.type == "uncivilized":
					if chance < 0.40:
						self.accepted_cultures.add(opt.culture)
						print("Assimlated Culture")
				if opt.type == "old":
					if chance < 0.20:
						self.accepted_cultures.add(opt.culture)
						print("Assimlated Culture") 
				if opt.type == "civilized":
					if chance < 0.10:
						opt.culture = self.culture
						self.accepted_cultures.add(opt.culture)
						print("Included Culture")
		if choice == "3":
			for p in players.values():
				if p.type == "major":
					p.resources["gold"] -= 1
					self.resources["gold"] += 1
		if choice == "4":
			if self.culture_points < 2:
				print("You do not have enough culture points at this time")
				return 
			else:
				print("On which nation would you like to remove an accepted culture?")
				for p, player in players.items():
					if player.accepted_cultures > 1:
						print(other)
				opt = input()
				other = players[opt]
				print("Which culture shall to attempt to remove?")
				for c in other.accepted_cultures:
					print (c)
				popt = input()
				chance = uniform(0, 1)
				if chance < 0.2:
					other.accepted_cultures.discard(popt)
					print("Sucess! You have removed %s from the accepted culture of %s" (popt, other.name))
				else:
					print("You have failed to spread your culture this time around")
				self.culture_points -= 2
		if choice == "5":
			if self.culture_points < 3:
				print("You do not have enough culture points to steal mid POPs at this time")
				return 
			options = []
			for o, other in players.items():
				if other.type == "major" and other.midPOP["artists"]["number"] < self.midPOP["artists"]["number"]:
					options.append(other)
			if len(options) == 0:
				print("Your worthless culture is not superior to anyone's! What is wrong with you?")
				return
			else:
				print("From which player would you like to steal a mid POP?")
				for o in options:
					print(o.name, o.numMidPOP)
				steal = input()
				chance = choice(["researchers", "officers", "managers", "artists", "bureaucrats"])
				players[steal].midPOP[chance]["number"] -= 0.25
				players[steal].numMidPOP -= 0.25
				players[steal].resources["gold"] -= 5
				players[steal].POP -= 0.25
				self.midPOP[chance]["number"] += 0.25
				self.numMidPOP += 0.25
				self.resources["gold"] += 5
				self.POP += 0.25
				self.culture_points -= 3


