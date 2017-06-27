
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
		elif(self.goods["furniture"] < 1.0):
			print("You do not have any furniture \n")
			return
		elif(self.resources["spice"] < 1.0):
			print("You do not have any spice \n")
			return
		elif(self.goods["paper"] < 2.0):
			print("You do not have enough paper \n")
			return
		elif(self.goods["clothing"] < 1.0):
			print("You do not have enough clothing \n")
			return

		_type = input("What kind of middle class POP would you like to create?: researchers officers  \
			bureaucrats artists managers \n")
		if(self.midPOP[_type] > 1.6):
			print("You have already created as many %s a permitted \n")
			return
		self.resources["spice"] -= 1.0
		self.goods["furniture"] -= 1.0
		self.goods["paper"] -= 2.0
		self.goods["clothing"] -= 1.0
		self.numLowerPOP -= 0.25
		self.numMidPOP += 0.25
		self.midPOP[_type] += 0.25
		self.freePOP -= 0.25
		self.new_development += 1.0


	def research_tech(self):
			print("Which Technology would you like to develop? (Print entire name) \n")
			print("You currently have %s Research Points \n" % (self.research))
			options = []
			for k, t in technology_dict.items():
				if(k not in self.technologies and t["requirement"] in self.technologies):
					print(k, t)
					options.append(k)
			choice = " "
			while choice not in options:
				choice = input()
			if(technology_dict[choice]["cost"] > self.research):
				print("You do not have enough research points to gain that technology. \n")
				return
			else:
				self.research -= technology_dict[choice]["cost"]
				self.technologies.add(choice)
				print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n ")
				print("Your ingenius researches have discovered %s \n " % (choice))
			if(choice == "muzzle_loaded_arms"):
				self.irregulars["attack"] += 0.1
				self.irregulars["defend"] += 0.06
				self.infantry["attack"] += 0.25
				self.infantry["defend"] += 0.10
				self.cavalry["attack"] += 0.20
				self.cavalry["defend"] += 0.10
				self.artillery["attack"] += 0.25
				self.artillery["defend"] += 0.10
				self.frigates["attack"] += 0.25
				self.frigates["attack"] += 0.25
			if(choice == "cement"):
				self.max_fortification += 0.1
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
				self.frigates["attack"] += 0.30
			if(choice == "machine_guns" ):
				self.irregulars["defend"] += 0.2
				self.infantry["defend"] += 1.0
				self.cavalry["defend"] + 0.15
			if(choice == "indirect_fire"):
				self.artillery["attack"] += 0.1
				self.artillery["defend"] += 0.5
				self.iron_clad["attack"] += 0.25
				self.iron_clad["defend"] += 0.25
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
		elif(choice == "frigates"):
			self.build_frigates()
		elif(choice == "iron_clad"):
			self.build_ironclad()
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

	def build_frigates(self):
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		if(self.goods["cannons"] < 1.0):
			print("You do not have enough cannons \n")
			return
		elif(self.resources["cotton"] < 1.0):
			print("You do not have enough cotton \n")
			return
		elif(self.resources["wood"] < 1.0):
			print("You do not have enough wood \n")
			return
		else:
			self.AP -= 1
			self.goods["cannons"] -= 1.0
			self.resources["cotton"] -= 1.0
			self.resources["wood"] -= 1.0
			self.military["frigates"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2

			print("You now have %s frigates \n" % (self.military["frigates"]))
			return

	def build_ironclad(self):
		if self.steam_ship_yard == False:
			print("You cannot build Ironclads without a steam_ship_yard \n")
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		elif(self.goods["cannons"] < 1.0):
			print("You do not have enough cannons \n")
			return
		elif(self.resources["iron"] < 1.0):
			print("You do not have enough iron \n")
			return
		elif(self.goods["parts"] < 1.0):
			print("You do not have enough parts \n")
			return
		else:
			self.AP -= 1
			self.goods["cannons"] -= 1.0
			self.resources["iron"] -= 1.0
			self.goods["parts"] -= 1.0
			self.military["iron_clad"] += 1
			self.freePOP -= 0.2
			self.milPOP += 0.2
			print("You now have %s \n" % (self.military["iron_clad"]))
			return


	def build_factory(self, _type, market):
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
		else:
			self.AP -= 1
			self.resources["iron"] -= 1.0
			self.goods["parts"] -= 1.0
			self.factories.add(_type)
			market.global_factories[_type] += 1
			self.stability -= 0.5
			self.new_development -= 1
			print("You have constructed a %s factory \n" % (_type))
			return

	def build_steam_ship_yard(self):
		if "iron_clad" not in self.technologies:
			print("The Ironclad technology is required to build a Steam Ship Port \n")
			return
		if(self.goods["parts"] < 1 or self.resources["iron"] < 1 or self.resources["wood"]):
			print("You do not have sufficient resources to build a ship yard \n")
			return
		if(self.AP < 1):
			print("You do not have enough action points \n")
			return
		if self.steam_ship_yard == True:
			print("You have already built a steap ship yard")
		if(self.new_development < 1):
			print("You do not have enough development points \n")
			return
		else:
			self.goods["parts"] -= 1
			self.resources["iron"] -= 1
			self.resources["wood"] -= 1
			self.AP -1
			self.new_development -1
			self.steam_ship_yard = True
			print("Your empire now has a steam shipyard and can begin builing mighty Ironclad Ships! %s \n" % (player.fortification))

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
		"chemicals": {"coal": 0.5}
				}
		stab_rounds = round(self.stability * 2) / 2
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type =  " "
		while _type not in self.goods.keys():
			_type = input("What kind of good do you want to produce with factory?: parts cannons clothes paper furniture chemicals \n")
		if(_type not in self.factories):
			print("You do not have a %s factory \n" % (_type))
			return
		else:
			max_amount = self.factory_throughput * stability_map[stab_rounds]
			material_mod = 1 - (self.midPOP["managers"]["number"] / 3)
			if(_type == "parts"):
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
			amount = input("How many %s do you want to produce? (max: %s) \n" % (_type, max_amount))
			amount = int(amount)
			if(amount > max_amount):
				print("You can only build %s items at a time with a %s factory \n" % (self.factory_throughput, _type))
				return
			else:
				for i in manufacture[_type]:
					if(manufacture[_type][i] * amount * material_mod > self.resources[i]):
						print("You do not have sufficient %s for your factory to produce %s %s \n" % (i, amount, _type))
						return
					else:
						for i in manufacture[_type]:
							self.resources[i] -= manufacture[_type][i] * amount * material_mod
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
		if self.culture < 1:
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
			self.culture -= 1
			self.stability += 1
		if choice == "2":
			options = []
			for p, prov in provinces():
				if p.culture != self.name:
					options.append(prov)
			if len(options) == 0:
				print("Fortunately, you have no provinces in need of assimalation")
				return
			else:
				print("Which province would you like to assimilate?")
				for o in options:
					print(o.name) 
				opt = input()
				self.province[opt].culture = player.name
		if choice == "3":
			for p in players.values():
				if p.type == "major":
					p.resources["gold"] -= 1
					self.resources["gold"] += 1
		if choice == "4":
			if len(self.borders) == 0:
				print("Since you do not border any other nations, you cannot spread your culture")
				return
			if self.culture < 2:
				print("You do not have enough culture points to spread your culture at this time")
				return 
			else:
				print("To which nation would you like to spread your culture?")
				for other in player.borders:
					print(other)
				opt = input()
				other = players[opt]
				for p, prov in other.provinces.items():
					print("Name: %s, Resource: %s, Quality: %s, Dev Level:  %s" % (p.name, p.resource, p.quality, p.development_level))
				print("To which province shall we spread our elevated culture?")
				popt = input()
				p.provinces[popt].culture = self.name
		if choice == "5":
			if self.culture < 3:
				print("You do not have enough culture points to steap mid POPs at this time")
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
				self.culture -= 3


