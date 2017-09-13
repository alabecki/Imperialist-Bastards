
from player_class import*
import random
import minor_classes
from technologies import technology_dict
from commands import*


class Human(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(Human, self).__init__(_name, _type, number, *args, **kwargs)


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
		#if(self.goods["furniture"] < 1.0):
		#	print("You do not have enough furniture to increase your population \n")
		#	return
		else:
			self.POP += 1.0
			self.freePOP += 1.0
			self.numLowerPOP += 1
			self.resources["food"] -= 1.0
			self.goods["clothing"] -= 1.0
			#self.furniture["furniture"] -= 1.0
			self.POP_increased += 1
			self.stability -= 0.1
			if med == True:
				self.goods["chemicals"] -= 1.0
			print("Your nation now has a population of %s with %s free POPS \n" % (self.POP, self.freePOP))
			return

	def increase_middle_class(self):
		if "pre_industry_2" not in self.technologies:
			print("You must research pre_industry_3 before you can increase your middle class\n" )
			return
		if(self.freePOP < 0.2):
			print("You do not have any free POPs")
			return
		requirement = self.determine_middle_class_need()
		check = self.check_mid_requirement(requirement)
		if check == False:
			print("You cannot increase your middle class at this time")
			print("To increase your middle class you need 1 splce plus:")
			for r in requirement:
				print(r)
			return
		else:
			for m, mid in self.midPOP.items():
				if self.midPOP[m]["number"] < least_mid:
					least_mid = self.midPOP[m]["number"]
			least_mid = max(0.2, least_mid)
			m_options = []
			for m, mid in self.midPOP.items():
				if self.midPOP[m]["number"] >= 2:
					continue
				if self.midPOP[m]["number"] < least_mid * 2:
					m_options.append(m)
			_type = ""
			while _type not in m_options:
				print("What kind of middle class POP would you like to create?")
				for mo in m_options:
					print(mo, end = "  ")
				_type = input()

			self.resources["spice"] -= 1
			for r in requirement:
				self.goods[r] -= 1
				print("Spends 1 %s" % (r))
			self.numLowerPOP -= 0.20
			self.numMidPOP += 0.20
			self.midPOP[_type]["number"] += 0.20
			self.freePOP -= 0.20
			self.new_development += 0.5
			if _type == "officers":
				self.milPOP -= 0.2
				self.freePOP +=  0.2
				self.choose_doctrine()
			print("You now have %s %s" % (self.midPOP[_type]["number"], _type))

	def choose_doctrine(self):
		print("Which military doctrine would you like to choose?")
		for md in military_doctrines:
			if "flight" not in self.technologies and (md == "Fighter_Offense" or md == "Fighter_Defense"):
				continue
			if md not in self.doctrines:
				print(md)
		choice = " "
		while choice not in military_doctrines:
			choice = input()
		self.doctrines.add(choice)
		if choice == "Sea_Doctrine1" or choice == "Sea_Doctrine2":
			self.frigates["attack"] += 0.3
			self.iron_clad["attack"] += 0.32
			self.battle_ship["attack"] += 1
			return 
		if choice == "Infantry_Offense":
			self.infantry["attack"] += 0.25
		if choice == "Mobile_Offense":
			self.cavalry["attack"] += 0.3
			self.tank["attack"] += 0.5
		if choice == "Artillery_Offense":
			self.artillery["attack"] += 0.4
		if choice == "Fighter_Offense":
			self.fighter["attack"] += 0.25
		if choice == "Infantry_Defense":
			self.infantry["defend"] += 0.3
		if choice == "Mobile_Defense":
			self.cavalry["defend"] += 0.25
			self.tank["attack"] += 0.4
		if choice == "Artillery_Defense":
			self.artillery["defend"] += 0.4
		if choice == "Fighter_Defense":
			self.fighter["defend"] += 0.3
		if choice == "Enhanced_Mobility":
			self.cavalry["manouver"] + 0.5
			self.tank["manouver"] + 1
			self.fighter["manouver"] + 1
	

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

			if(choice == "muzzle_loaded_arms"):
				self.irregulars["attack"] += 0.15
				self.irregulars["defend"] += 0.1
				self.infantry["attack"] += 0.3
				self.infantry["defend"] += 0.1
				self.cavalry["attack"] += 0.2
				self.cavalry["defend"] += 0.05
				self.artillery["attack"] += 0.3
				self.artillery["defend"] += 0.1
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
			if(choice == "machine_guns" ):
				self.irregulars["defend"] += 0.2
				self.infantry["defend"] += 1.0
				self.cavalry["defend"] + 0.1
			if(choice == "indirect_fire"):
				self.artillery["attack"] += 0.15
				self.artillery["defend"] += 0.5
				self.artillery["ammo_use"] += 0.05
				self.iron_clad["attack"] += 0.25
			if(choice == "bombers"):
				self.fighter["attack"] += 1.2
				self.fighter["ammo"] += 0.1
			if(choice == "radar"):
				self.fighter["defend"] += 1.2
				self.battle_ship["attack"] += 1
			if(choice == "telegraph"):
				self.factory_throughput += 1
				self.production_modifier += 0.15
				self.org_factor += 0.15
			if choice == "electricity":
				self.factory_throughput += 1
				self.production_modifier += 0.15
			if choice == "radio":
				self.reputation += 0.2
				self.stability += 0.2
				self.org_factor += 0.15

			if choice == "early_computers":
				self.battle_ship["attack"] += 1
				self.production_modifier += 1.5
			if choice == "atomic_bomb":
				print("Holy Shit!")
				pause = input()



	def spice_to_stability(self):
		if self.resources["spice"] > 2:
			print("You do not have enough spice raise your stability")
			return
		if self.stability >= 3:
			print("Your stability cannot be further increased")
		else:
			self.resources["spice"] -= 1
			self.stability + 0.5
			if self.stability > 3:
				self.stability = 3
		print("Your stability is now %s " % (self.stability))

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
		if self.resources["spice"] < 1:
			print("You do not have enough spice")
		else:
			if self.resources["spice"] >= 1 and self.stability < 3:
				self.resources["spice"] -=1
				self.stability += 2/(self.POP + 0.01) 
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


	def disband_unit(self):
		kind = " "
		while kind not in self.military.keys():
			print("What kind of unit would you like to disband?")
			for k, v in self.military.items():
				if v >= 1:
					print(k, v)
			kind = input()
		self.milPOP -= 0.2
		self.freePOP += 0.2
		self.number_units -= 1
		if kind == "infantry":
			self.military["infantry"] -= 1
			self.resources["iron"] += 1
		if kind == "irregulars":
			self.military["irregulars"] -= 1
		if kind == "cavalry":
			self.military["cavalry"] -= 1
			self.resources["iron"] += 1
		if kind == "artillery":
			self.military["artillery"] -= 1
			self.resources["iron"] += 2
		if kind == "frigates":
			self.military["frigates"] -= 1
			self.resources["iron"] += 1
		if kind == "iron_clad":
			self.military["iron_clad"] -= 1
			self.resources["iron"] += 3
		if kind == "fighter":
			self.military["fighter"] -= 1
			self.resources["iron"] += 2
		if kind == "tank":
			self.military["tank"] -= 1
			self.resources["iron"] += 3
		if kind == "battle_ship":
			self.military["battle_ship"] -= 1
			self.resources["iron"] += 7



	def build_infantry(self):
		if self.can_train < 1:
			print("You cannon train any more land units this turn")
			return
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.military_produced["infantry"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0
		print("Infantry will be ready at the start of next turn")

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
			self.military_produced["cavalry"] += 1.0
			self.number_units += 1.0
			self.can_train -= 1.0
			print("Cavalry will be ready at the start of next turn")

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
		self.military_produced["artillery"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0
		print("Artillery will be ready at the start of next turn")

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
		self.military_produced["tank"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0
		print("Tank will be ready at the start of next turn")


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
		self.military_produced["fighter"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0
		print("Fighter will be ready at the start of next turn")


	def build_frigates(self):
		if self.AP < 1:
			print("You do not have enough action points")
			return
		if self.resources["wood"] < 1:
			print("You do not have enough wood")
			return
		if self.goods["cannons"] < 1:
			print("You do not have enough cannons")
			return
		if self.resources["cotton"] < 1:
			print("You do not have enough cotton")
			return
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["cannons"] -= 1.0
			self.resources["cotton"] -= 1.0
			self.resources["wood"] -= 1.0
			self.military_produced["frigates"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.number_units +=1
			print("Frigates will be ready at the start of next turn")
			return

	def build_ironclad(self):
		if self.shipyard < 2:
			print("You need a level 2 shipyard before you may build Iron Clad")
			print("(Building a level 2 shipyard required that you research the 'iron_clad' technology.)")
			return
		if self.AP < 1:
			print("You do not have enough action points")
			return
		if self.goods["parts"] < 1:
			print("You do not have enough parts")
			return
		if self.goods["cannons"] < 1:
			print("You do not have enough cannons")
			return
		if self.resources["iron"] < 1:
			print("You do not have enough iron")
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["cannons"] -= 1.0
			self.goods["parts"] -= 1.0
			self.resources["iron"] -= 1.0
			self.military_produced["iron_clad"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.number_units += 1
			print("Ironclad will be ready at the start of next turn")
			return

	def build_battleship(self):
		if self.shipyard < 3:
			print("You need a level 3 shipyard before you may build Battleship")
			print("(Building a level 3 shipyard required that you research the 'oil_powered_ships' technology.)")
			return
		if self.AP < 2:
			print("You do not have enough action points")
			return
		if self.goods["cannons"] < 3:
			print("You do not have enough cannons")
			return
		if self.resources["iron"] < 3:
			print("You do not have enough iron")
			return
		if self.goods["parts"] < 1:
			print('You do not have enough parts')
			return
		if self.goods["gear"] < 1:
			print("You do not have enough gear")
			return
		if self.freePOP < 0.2:
			print("You do not have any freePOPs")
			return
		else:
			self.goods["cannons"] -= 3
			self.resources["iron"] -= 3
			self.goods["parts"] -= 1
			self.goods["gear"] -= 1
			self.military_produced["battle_ship"] += 1.0
			self.freePOP -= 0.2
			self.milPOP += 0.2
			self.number_units += 1
			print("Battleship will be ready at the start of next turn")
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
			#if self.factories["ship_yard"] == 0:
			#	options.append["ship_yard"]
			#if self.factories["ship_yard"] == 1 and "iron_clad" in self.technologies:
			#	options.append["ship_yard"]
			#if self.factories["ship_yard"] == 2 and "oil_powered_ships" in self.technologies:
			#	options.append["ship_yard"]
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
			if self.factories["chemicals"]["number"] == 1 and "dyes" in self.technologies:
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
		if len(options) == 0:
			print("You cannot build any factories at this time")
			return
		choice = ""
		while choice not in options:
			print("What kind of factry would you like to build?")
			for o in options:
				print (o)
			choice = input()

		self.AP -= 1
		self.resources["iron"] -= 1.0
		self.goods["parts"] -= 1.0
		self.factories[choice]["number"] += 1
		market.global_factories[choice] += 1
		self.stability -= 0.3
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
		elif self.fortification >= 1.1 and "cement" not in self.technologies:
			print("You cannot further upgrade your fortifications without cement \n")
			return
		elif self.fortification >= 1.2:
			print("You have already upgraded your fortifications as much as possible \n")
			return
		else:
			self.AP -= 1
			self.goods["cannons"] -= 1
			self.fortification += 0.1
			print("Your fortresses now modifies your defense strength by a scalar if %s \n" % (self.fortification))
			return

	def build_steam_ship_yard(self):
		if(self.new_development < 1):
			print("You do not have any Development Points to spend \n")
			return
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		if self.resources["wood"] < 1:
			print("You do not have enough wood \n")
			return
		if(self.goods["parts"] < 1.0):
			print("You do not have enough parts \n")
			return
		max_ship_yard_level = 1
		if "iron_clad" in self.technologies:
			max_ship_yard_level = 2
		if "oil_powered_ships" in self.technologies:
			max_ship_yard_level = 3
		if self.shipyard == max_ship_yard_level:
			print("Your Shipyard cannot be further upgraded at this time")
			return
		self.AP -= 1
		self.goods["parts"] -= 1
		self.resources["wood"] -= 1
		self.shipyard += 1
		print("Your shipyard has been upgraded to level %s" % (self.shipyard))
	

	def develop_province(self):
		if(self.new_development < 1):
			print("You do not have any Development Points to spend \n")
			return
		elif(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		#elif(self.resources["wood"] < 1.0):
		#	print("You do not have enough wood \n")
		#	return
		elif(self.resources["iron"] < 1):
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
			elif(self.provinces[prov].resource == "oil"):
				max_dev = 0
				if("oil_drilling" in self.technologies):
					max_dev = 1
				if "rotary_drilling" in self.technologies:
					max_dev = 2

			elif(self.provinces[prov].resource == "rubber"):
				max_dev = 0
				if("chemistry" in self.technologies):
					max_dev = 1
				if "synthetic_dyes" in self.technologies:
					max_dev = 2
			if self.provinces[prov].development_level == max_dev:
				print("You cannot further develop this province at this time")
				return
			else:
				self.resources["iron"] -= 1
				self.goods["parts"] -= 1.0
				#self.resources["wood"] -= 1.0
				self.AP -= 1
				self.new_development -= 1
				self.provinces[prov].development_level += 1
				self.number_developments += 1
				print("You have developed province %s, its development level is now %s \n" % (prov, self.provinces[prov].development_level))


	def craftman_production(self):
		craft = {
		"parts": {"iron": 0.67, "coal": 0.33},
		"cannons": {"iron": 0.67, "coal": 0.33},
		"paper": {"wood": 1.0},
		"clothing": {"cotton": 0.9, "dyes": 0.3},
		"furniture": {"wood": 0.67, "cotton": 0.33},
			}
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type = " "
		while _type not in self.goods.keys():
			_type = input("What kind of good do you want to produce with craftsmen?: parts cannons clothing paper furniture \n")
		
		for i in craft[_type]:
			if i in self.resources.keys():
				if(craft[_type][i] > self.resources[i]):
					print("You do not have sufficient %s to craft %s \n" % (i, amount, _type))
					return
		else:
			for i in craft[_type]:
				self.resources[i] -= craft[_type][i]
			self.goods_produced[_type] += 1.0
			self.AP -= 1
			#self.new_development -= 0.05
			print("The  %s will be ready next turn \n" % (_type))
			return


	def factory_production(self):
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
		stab_rounds = round(self.stability * 2) / 2
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type =  " "
		while _type not in self.goods.keys():
			for k in self.factories.keys():
				print(k)
			_type = input("What kind of good do you want to produce with factory? \n")
		if self.factories[_type]["number"] == 0:
			print("You do not have a %s factory \n" % (_type))
			return
		if self.factories[_type]["used"] == True:
			print("You have already used your %s factory this round" % (_type))
		else:
			stab_rounds = round(self.stability* 2) / 2
			stab_mod = stability_map[stab_rounds]
			max_amount = self.factories[_type]["number"] * stab_mod * self.factory_throughput
			material_mod = 1 - (self.midPOP["managers"]["number"] / 4)
			max_amount = max_amount/(material_mod + 0.0001)
			amount = input("How many %s do you want to produce? (max: %s) \n" % (_type, max_amount))
			amount = int(amount)
			if(amount > max_amount):
				print("You can only build %s items at a time with a %s factory \n" % (max_amount, _type))
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
						self.factories[_type]["used"] = True
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
			need = 0
			if(key == "food" or key =="coal" or key == "oil"):
				if(key == "food"):
					need = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
				if(key == "coal"):
					need = 0.1 * self.number_developments
				if(key == "oil"):
					if self.numMidPOP > 4.5:
						need = (self.numMidPOP - 4.5)/2
				current_production  = 0
				for k, p in self.provinces.items():
					if p.resource == key and p.worked == True:
						current_production += development_map[p.development_level] * stability_map[stab_rounds] * p.quality
				forecast = (self.resources[key] + current_production) - need
				print("Resource: %s, Current Supply: %s, Current Consumption: %s, Current Production: %s, New Turn Forecast %s \n" % \
				(key, self.resources[key], need, current_production, forecast))


	def use_culture(self, players):
		if self.culture_points < 1:
			print("Your barbaric nation does not have any culture points at this time")
			return
		choice = " "
		while (choice not in culture_commands.keys()):
			for k, v in culture_commands.items():
				print("%s: %s" % (k,v))
			choice = input()
		if choice == "1":
			self.culture_points -= 1
			self.stability += 0.5
			if self.stability > 3:
				self.stability = 3
			print("Your stability is now %s" % (self.stability))
		if choice == "2":
			if self.diplo_action < 1:
				print("You need at least 1 diplo action for that")
				return
			self.culture_points -= 1
			self.diplo_action -= 1
			self.reputation += 0.1
			print("Your reputation is now %s" % (self.reputation))
		if choice == "3":
			options = []
			for p, prov in self.provinces.items():
				if prov.culture != self.culture and prov.culture not in self.accepted_cultures:
					options.append(prov)
			if len(options) == 0:
				print("Fortunately, you have no provinces in need of assimalation")
				return
			else:
				print("Which province would you like to try to include?")
				for o in options:
					print(o.name) 
				opt = input()
				opt = self.provinces[opt]
				self.culture_points -= 1
				chance = uniform(0, 1)
				print("Roll: %s" % (chance))
				if opt.type == "uncivilized":
					if chance < 0.66:
						self.accepted_cultures.add(opt.culture)
						print("Integrated Culture")
					else:
						print("Not this time :(")
				if opt.type == "old":
					if chance < 0.33:
						self.accepted_cultures.add(opt.culture)
						print("Integrated Culture") 
					else:
						print("Not this time :(")

				if opt.type == "civilized":
					if chance < 0.25:
						opt.culture = self.culture
						self.accepted_cultures.add(opt.culture)
						print("Integrated Culture")
					else:
						print("Not this time :(")

		if choice == "4":
			gain = 0
			for p in players.values():
				if p.type == "major":
					p.resources["gold"] -= 1
					self.resources["gold"] += 1
					gain += 1
			self.culture_points -= 1
			print("You have gained %s gold" % (gain))

		if choice == "5":
			self.use_spice_stability()


		#if choice == "4":
		#	if self.culture_points < 2:
		#		print("You do not have enough culture points at this time")
		#		return 
		#	else:
		#		print("On which nation would you like to remove an accepted culture?")
		#		for p, player in players.items():
		#			if player.accepted_cultures > 1:
		#				print(other)
		#		opt = input()
		#		other = players[opt]
		#		print("Which culture shall to attempt to remove?")
		#		for c in other.accepted_cultures:
		#			print (c)
		#		popt = input()
		#		chance = uniform(0, 1)
		#		if chance < 0.2:
		#			other.accepted_cultures.discard(popt)
		#			print("Sucess! You have removed %s from the accepted culture of %s" (popt, other.name))
		#		else:
		#			print("You have failed to spread your culture this time around")
		#		self.culture_points -= 2
		#if choice == "5":
		#	if self.culture_points < 3:
		#		print("You do not have enough culture points to steal mid POPs at this time")
		#		return 
		#	options = []
		#	for o, other in players.items():
		#		if other.type == "major" and other.midPOP["culture"]["number"] < self.midPOP["culture"]["number"]:
		#			options.append(other)
		#	if len(options) == 0:
		#		print("Your worthless culture is not superior to anyone's! What is wrong with you?")
		#		return
		#	else:
		#		print("From which player would you like to steal a mid POP?")
		#		for o in options:
		#			print(o.name, o.numMidPOP)
		#		steal = input()
		#		chance = choice(["science", "military", "management", "culture", "bureaucrats"])
		#		players[steal].midPOP[chance]["number"] -= 0.25
		#		players[steal].numMidPOP -= 0.25
		#		players[steal].resources["gold"] -= 5
		#		players[steal].POP -= 0.25
		#		self.midPOP[chance]["number"] += 0.25
		#		self.numMidPOP += 0.25
		#		self.resources["gold"] += 5
		#		self.POP += 0.25
		#		self.culture_points -= 3


				