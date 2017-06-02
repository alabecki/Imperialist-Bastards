

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

	def __init__ (self, _name, _human, number):
		# Basic Attributes
		self.human = _human
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
		"researchers": {"number": 0.1, "priority": 0.2},
		"officers": {"number": 0.1, "priority": 0.2},
		"bureaucrats": {"number": 0.1, "priority": 0.2},
		"artists": {"number": 0.1, "priority": 0.2},
		"managers": {"number": 0.1, "priority": 0.2}
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
				self.calverley["attack"] += 0.20
				self.calverley["defend"] += 0.10
				self.artillery["attack"] += 0.25
				self.artillery["defend"] += 0.10
				self.frigate["attack"] += 0.25
				self.frigate["attack"] += 0.25
			if(choice == "cement"):
				self.max_fortification += 0.1
			if(choice == "breach_loaded_arms"):
				self.irregulars["attack"] += 0.15
				self.irregulars["defend"] += 0.08
				self.infantry["attack"] += 0.30
				self.infantry["defend"] += 0.15
				self.calverley["attack"] += 0.25
				self.calverley["defend"] += 0.12
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
				while choice not in self.province.keys():
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

	def build_unit(self):
		if(self.freePOP < 0.15):
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
		if(self.goods["clothing"] < 0.15):
			print("You do not have enough clothing to build Infantry \n")
			return
		self.goods["clothing"] -= 0.15
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.goods["cannons"] -= 1.0
		self.military["infantry"] += 1.0
		print("You now have %s Infantry \n" % (self.military["infantry"]))

	def build_cavalry(self):
		if(self.goods["clothing"] < 0.1):
			print("You do not have enough clothing to build cavalry \n")
			return
		elif(self.resources["food"] < 0.1):
			print("You do not have enough Food to build cavalry \n")
			return
		else:
			self.resources["food"] -= 0.15
			self.freePOP -= 0.15
			self.milPOP += 0.15
			self.goods["cannons"] -= 1.0
			self.goods["clothing"] -= 0.1
			self.military["cavalry"] += 1.0
			print("You now have %s cavalry \n" % (self.military["cavalry"]))

	def build_artillery(self):
		if(self.goods["clothing"] < 0.1):
			print("You do not have enough clothing to build artillery \n")
			return
		if(self.goods["cannons"] < 2.0):
			print("You do not have enough cannons to build artillery \n")
			return
		self.goods["cannons"] -= 2.0
		self.goods["clothing"] -= 0.1
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.military["artillery"] += 1.0
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
			self.freePOP -= 0.15
			self.milPOP += 0.15
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
			print("Youd do not have enough parts \n")
			return
		else:
			self.AP -= 1
			self.goods["cannons"] -= 1.0
			self.resources["iron"] -= 1.0
			self.goods["parts"] -= 1.0
			self.military["iron_clad"] += 1
			self.freePOP -= 0.15
			self.milPOP += 0.15
			print("You now have %s \n" % (self.military["iron_clad"]))
			return


	def build_factory(self, _type):
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
			self.stability_mod -= 0.05
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
		if(self.resources[craft[_type]] < 1.0):
			print("You do not have enough %s with which to make %s \n" % (craft[_type], _type))
			return
		else:
			self.resources[craft[_type]] -= 1.2
			self.goods_produced[_type] += 1.0
			self.AP -= 1
			self.new_development -= 0.05
			print("The  %s will be ready next turn \n" % (_type))
			return


	def factory_production(self):
		manufacture = {
			"parts": {"iron": 0.6, "coal": 0.3},
			"cannon": {"iron": 0.6, "coal": 0.3},
			"paper": {"wood": 0.9},
			"clothing": {"cotton": 0.8, "dyes": 0.1},
			"furniture": {"wood", 0,6, "cotton", 0.3},
			"chemicals": {"coal", 0.6}
					}
		stab_rounds = round(self.stability * 2) / 2
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type =  " "
		while _type not in self.goods.key():
			_type = input("What kind of good do you want to produce with factory?: parts cannons clothes paper furniture chemicals \n")
		if(_type not in self.factories):
			print("You do not have a %s factory \n" % (_type))
			return
		else:
			max_amount = self.factory_throughput * stability_map[stab_rounds]
			material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
			if(_type == "parts"):
				if("bessemer_process" in self.technologies):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
			elif(_type == "cannons"):
				if("bessemer_process" in self.technologies):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
			elif(_type == "paper"):
				if("pulping" in self.technologies):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
			elif(_type == "furniture"):
				if("electricity" in self.technologies):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
			elif(_type == "clothing"):
				if("power_loom" in self.technologies):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
			elif(_type == "chemicals"):
					max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
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
						print("Next turn you will receive %s %s" % (self.goods_produced[_type], _type))
						return

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
		need = {
			"clothing": (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2),
			"furniture":(self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2),
			"paper":(self.numMidPOP * 0.3),
			"cannons":(self.midPOP["officers"]["number"] * 0.3)
			}
		for key, value in self.goods.items():
			if(key == "clothing" or key == "furniture" or key == "paper" or key == "cannons"):
				print("Good: %s, Current Supply: %s, Current Consumption %s, Current Production: %s, New Turn Forecast %s \n" % \
				(key, self.goods[key], need[key], self.goods_produced[key], ((self.goods[key] + self.goods_produced[key]) - need[key]) ))

	def calMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
		mClothing = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
		mFurniture = (self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2)
		mPaper = (self.numMidPOP * 0.3)
		mSpice = (self.numMidPOP * 0.2)
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
		return stab_change


	def popChange(self):
		if(self.resources["food"] > 0.5):
			change =  self.POP * 0.04
			if(self.stability > 0):
				stab_rounds = round(self.stability * 2) / 2
				change += (self.POP * 0.04) * (stability_map[stab_rounds] * self.POP_growth_mod)
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
			change = 0.1 + ((self.midPOP["bureaucrats"]["number"]/2) + (self.midPOP["researchers"]["number"]/4))* stability_map[stab_rounds]
			self.numMidPOP += change
			self.POP += change
			print("Middle Class population change: %s \n" % (change))
			for key, value in self.midPOP.items():
				value["number"] += change * value["priority"]
				print("%s increased by %s" % (key, change * value["priority"]))


	def setMiddleClassPriorities(self):
		middletypes = []
		for k in self.midPOP.keys():
			middletypes.append(k)
		ordinal = 1
		while ordinal < 6:
			for t in middletypes:
				print(t)
			p =  " "
			while p not in middletypes:
				p = input("What is your %s st priority? \n" % (ordinal))
			self.midPOP[p]["priority"] = m_priority_map[str(ordinal)]
			middletypes.remove(p)
			ordinal += 1


	def turn(self):
		self.collect_resources()
		self.collect_goods()
		stab_change0 = self.payMaintenance()
		stab_change1 = (self.numLowerPOP * 0.01) + (self.numMidPOP * 0.02)
		print("Stab change 1 " + str(stab_change1))
		self.stability -= (stab_change1 + stab_change0)
		print("Stab modifier: " + str(self.stability_mod))
		stab_change2 = ((self.midPOP["bureaucrats"]["number"]/6) + (self.midPOP["artists"]["number"]/3)) * self.stability_mod
		print("Stab change 2 " + str(stab_change2))
		stab_rounds = round(self.stability * 2) / 2
		self.stability += stab_change2
		if self.stability < -3.0:
			self.stability = -3.0
		if self.stability > 3.0:
			self.stability = 3.0
		total_stab_change = stab_change2 - (stab_change1 + stab_change0)
		print("Stability changes by: %s" % (total_stab_change))
		self.popChange()
		self.popMidChange()
		self.AP = int(self.proPOP) * self.production_modifier
		research_gain = ((0.2 + (self.midPOP["researchers"]["number"] * 0.8) + (self.midPOP["managers"]["number"] * 0.2))) * stability_map[stab_rounds]
		print("Research points gained: %s " % (research_gain))
		self.research += research_gain
		diplo_gain = 0.2 + (self.midPOP["bureaucrats"]["number"]) * self.reputation
		self.diplo_action += diplo_gain
		print("Diplo_action gain: %s " % (diplo_gain))
		col_gain =  ((self.military["frigates"] + self.military["iron_clad"])/5 + self.midPOP["bureaucrats"]["number"]/2)
		self.colonization += col_gain
		print("Colonization point gain: %s" % (col_gain))
