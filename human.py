
from player_class import*
from random import*
import minor_classes
from technologies import technology_dict

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


pro_input = {
	"1": "parts",
	"2": "cannons",
	"3": "clothing",
	"4": "paper",
	"5": "furniture",
	"6": "chemicals",
	"7": "gear",
	"8": "telephone",
	"9": "radio",
	"10": "auto",
	"11": "fighter",
	"12": "tank"
}


class Human(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(Human, self).__init__(_name, _type, number, *args, **kwargs)


	def can_improve_prov(self, prov):
		if self.number_developments < 1 or self.AP < 1 or self.goods["parts"] < 1 or self.resources["wood"] < 1:
			return False


		if(self.provinces[prov].development_level == 2):
			return False

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
		if self.provinces[prov].development_level >= max_dev:
			return False
		else:
			return True

	def work_p(self, prov):
		self.provinces[prov].worked = True
		self.freePOP -= 1

	def free_p(self, prov):
		self.provinces[prov].worked = False
		self.freePOP += 1

	def dev_p(self, prov):
		self.provinces[prov].development_level += 1
		self.AP -= 1
		self.goods["parts"] -= 1
		self.resources["wood"] -=1
		self.new_development -=1

	def increase_pop(self):
		self.POP += 1.0
		self.freePOP += 1.0
		self.numLowerPOP += 1
		self.resources["food"] -= 1.0
		self.goods["clothing"] -= 1.0
		#self.furniture["furniture"] -= 1.0
		self.stability -= 0.1
		if self.POP_increased == 1:
			self.goods["chemicals"] -= 1.0
		self.POP_increased += 1

		return

	def development_options(self):
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
				print(d)
		return d_options




	def increase_development(self, _type):
			
		requirement = self.determine_middle_class_need()
		for r in requirement:
			if r == "spice":
				self.resources["spice"] -= 1
			else:
				self.goods[r] -= 1.0
		self.numLowerPOP -= 0.5
		self.numMidPOP += 0.5
		self.development_level += 1
		#self.midPOP[m_selection]["number"] += 0.2
		self.developments[_type] += 1
		self.freePOP -= 0.5
		if _type == "management" or _type == "government": 
			self.new_development += 1
		if _type == "military":
			self.milPOP -= 0.4
			self.freePOP +=  0.4
			self.choose_doctrine(choice)
			print("Your %s level is now %s" % (_type, self.developments[_type]))

	
	def doctrine_options(self):
		options = []
		for md in military_doctrines:
			if "flight" not in self.technologies and (md == "Fighter_Offense" or md == "Fighter_Defense"):
				continue
			if md not in self.doctrines:
				options.append(md)
		return options


	def choose_doctrine(self, choice):
		
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
	

	def research_tech(self, choice):
			self.research -= technology_dict[choice]["cost"]
			self.technologies.add(choice)
			if choice == "professional_armies":
				self.infantry["attack"] += 0.15
				self.infantry["defend"] += 0.15
				self.cavalry["attack"] += 0.15
				self.cavalry["defend"] += 0.15
				self.artillery["attack"] += 0.15
				self.artillery["defend"] += 0.15
				self.frigates["attack"] += 0.2
			if choice == "flint_lock":
				self.infantry["attack"] += 0.3
				self.infantry["defend"] += 0.1
				self.cavalry["attack"] += 0.2
				self.cavalry["defend"] += 0.1
				self.artillery["attack"] += 0.3
				self.artillery["defend"] += 0.1
				self.frigates["attack"] += 0.25
			if(choice == "muzzle_loaded_arms"):
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
				self.infantry["attack"] += 0.35
				self.infantry["defend"] += 0.2
				self.cavalry["attack"] += 0.25
				self.cavalry["defend"] += 0.10
				self.artillery["attack"] += 0.35
				self.artillery["defend"] += 0.2
				self.frigates["attack"] += 0.35
			if(choice == "machine_guns" ):
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
				self.production_modifier += 0.15
			if choice == "atomic_bomb":
				print("Holy Shit!")



	def spice_to_stability(self):
		if self.resources["spice"] > 2:
			print("You do not have enough spice to raise your stability")
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

	def use_Spice_Stability(self):
		self.resources["spice"] -=1
		self.stability += 2/(self.POP + 0.01) 
		if self.stability > 3:
			self.stability = 3
		print("Your stability is now %s " % (self.stability))



	def disband_unit(self, kind):
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

	def build_army_unit(self, _type):
		if _type == "infantry":
			self.build_infantry()
		if _type == "artillery":
			self.build_artillery()
		if _type == "cavalry":
			self.build_cavalry()
		if _type == "tank":
			self.build_tank()
		if _type == "fighter":
			self.build_fighter()
		if _type == "frigates":
			self.build_frigates()
		if _type == "iron_clad":
			self.build_ironclad()
		if _type == "battle_ship":
			self.build_battleship()


	def build_infantry(self):
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.military_produced["infantry"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0

	def build_cavalry(self):
		self.resources["food"] -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.goods["cannons"] -= 1.0
		self.military_produced["cavalry"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0

	def build_artillery(self):
		self.goods["cannons"] -= 2.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military_produced["artillery"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0

	def build_tank(self):
		self.goods["tank"] -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military_produced["tank"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0


	def build_fighter(self):
		self.goods["fighter"] -= 1
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.military_produced["fighter"] += 1.0
		self.number_units += 1.0
		self.can_train -= 1.0


	def build_frigates(self):
		self.AP -= 1
		self.goods["cannons"] -= 1.0
		self.resources["cotton"] -= 1.0
		self.resources["wood"] -= 1.0
		self.military_produced["frigates"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units +=1
		

	def build_ironclad(self):
		self.AP -= 1
		self.goods["cannons"] -= 1.0
		self.goods["parts"] -= 1.0
		self.resources["iron"] -= 1.0
		self.military_produced["iron_clad"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		

	def build_battleship(self):	
		self.AP -= 1
		self.goods["cannons"] -= 3
		self.resources["iron"] -= 3
		self.goods["parts"] -= 1
		self.goods["gear"] -= 1
		self.military_produced["battle_ship"] += 1.0
		self.freePOP -= 0.2
		self.milPOP += 0.2
		self.number_units += 1
		


	def improve_fortifications(self):
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
		if "ironclad" in self.technologies:
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
	
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type = " "
		while _type not in ["1", "2", "3", "4", "5"]:
			print("What kind of good do you want to produce with craftsmen?:") 
			_type = input("1: parts,  2: cannons, 3: clothing, 4: paper, 5: furniture \n")
		
		_type = pro_input[_type]
		print("Type after conversion: %s" % (_type))
		for i in craft[_type]:
			if i in self.resources.keys():
				if(craft[_type][i] > self.resources[i]):
					print("You do not have sufficient %s to craft %s \n" % (i, _type))
					return
		else:
			for i in craft[_type]:
				self.resources[i] -= craft[_type][i]

			self.goods_produced[_type] += 1.0
			self.AP -= 1
			#self.new_development -= 0.05
			print("The  %s will be ready next turn \n" % (_type))
			for k, p in self.goods_produced.items():
				print("%s: %s " % (k, p))
			return



	def factory_production(self):

		stab_rounds = round(self.stability * 2) / 2
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type =  " "
		while _type not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
			for k in self.factories.keys():
				print(k)
			print("What kind of good do you want to produce in a factory?:") 
			print("1: parts,  2: cannons, 3: clothing, 4: paper, 5: furniture, 6: chemicals")
			print("7: gears, 8: telephones, 9: radio, 10: auto, 11: fighter, 12: tank")
			_type = input()
		
		_type = pro_input[_type]
		if self.factories[_type]["number"] == 0:
			print("You do not have a %s factory \n" % (_type))
			return
		if self.factories[_type]["used"] == True:
			print("You have already used your %s factory this round" % (_type))
		else:
			stab_rounds = round(self.stability* 2) / 2
			stab_mod = stability_map[stab_rounds]
			max_amount = self.factories[_type]["number"] * stab_mod * self.factory_throughput
			material_mod = 1 -  (self.developments["management"]/10)
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
	#	for key, value in self.resources.items():
	#		if key != "gold":
	#			print (" %s : %s \n" % (key, value))
	#	for key, value in self.goods.items():
	#		print (" %s : %s \n" % (key, value))

		for (k1,v1), (k2,v2) in zip(self.resources.items(), self.goods.items()):
			print(" %-10s: %-8.2f        %-10s: %-8.2f" % (k1, v1, k2, v2))


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
				print("Current Needs:")
				print("Resource: %-4s, Current Supply: %-4.2f, Current Consump: %.2f, Current Pro: %.2f, Forecast %.2f \n" % \
				(key, self.resources[key], need, current_production, forecast))


	def check_for_non_accepted_cultures(self):
		options = []
		for p, prov in self.provinces.items():
			if prov.culture != self.culture and prov.culture not in self.accepted_cultures:
				options.append(prov.name)
		return options 

	def increase_Stability(self):
		self.culture_points -= 1
		self.stability += 0.5
		if self.stability > 3:
			self.stability = 3

	def improve_Reputation(self):
		self.culture_points -= 1
		self.diplo_action -= 1
		self.reputation += 0.1

	def integrate_Culture(self, prov):
		self.culture_points -= 1
		chance = uniform(0, 1)
		print("Roll: %s" % (chance))
		if opt.type == "uncivilized":
			if chance < 0.66:
				self.accepted_cultures.add(prov)
				print("Integrated Culture")
			else:
				print("Not this time :(")
		if opt.type == "old":
			if chance < 0.33:
				self.accepted_cultures.add(prov)
				print("Integrated Culture") 
			else:
				print("Not this time :(")

		if opt.type == "civilized":
			if chance < 0.25:
				opt.culture = self.culture
				self.accepted_cultures.add(prov)
				print("Integrated Culture")
			else:
				print("Not this time :(")

	def export_Culture(self, players):
		gain = 0
		for p in players.values():
			if p.type == "major":
				p.resources["gold"] -= 1
				gain += 1
		self.culture_points -= 1
		self.resources["gold"] += gain
		print("You have gained %s gold" % (gain))


	def create_synthetic_dyes(self):
		self.goods["chemicals"] -= 1
		self.resources["dyes"] += 1

	def chem_to_food(self):
		self.goods["chemicals"] -= 1
		self.resources["food"] += 1

	def create_synthetic_rubber(self):
		self.goods["chemicals"] -= 1
		self.goods["oil"] -= 1
		self.goods["rubber"] += 1

	def create_synthetic_oil(self):
		self.goods["chemicals"] -= 3
		self.goods["oil"] += 1
	

	def improve_Relations(self, other, relations):
		relata = frozenset([self.name, other])
		self.diplo_action -=1
		other = players[other]
		relations[relata].relationship += min(1, 5/(other.POP + 0.001))
		self.reputation += 0.02

	def damage_Relations(self, other, relations):
		relata = frozenset([self.name, other])
		self.diplo_action -=1
		other = players[other]
		relations[relata].relationship -= min(1, 10/(other.POP + 0.001))
		self.reputation -= 0.02

	def check_for_claims(self, other, provinces):
		options = []
		for o in self.objectives:
			if o in self.provinces.keys():
				continue
			op = provinces[o]
			if op.owner == other:
				options.append(o)
		return options 


	def gain_CB(self, other, annex):
		annex = provinces[annex]
		self.diplo_action -= 1
		new = CB(self, annex.owner, "annex", annex.name, 5)
		self.CB.add(new)
		self.reputation -= 0.025


	def destabilize_Nation(self, other, players, relations):
		amount = 0
		other = players[other]
		if other.type == "old_empire" or other.type == "old_minor":
			amount = random()/2
		else:
			amount = random()/4
		other.stability -= amount
		if other.stability < -3.0:
			other.stability = -3.0
		self.diplo_action -=1
		self.reputation -= 0.033
		relata = frozenset([self.name, other.name])
		relations[relata].relationship -= 0.2

	def bribeNation(self, other, relations):
		relata = frozenset([self.name, other])
		self.resources["gold"] -= 2
		relations[relata].relationship += min(1, 8/(other.POP + 0.001))

	
	def sabotage_Relatons(self, other1, other2, players, relations):
		relata = frozenset([other1, other2])
		other1 = players[other1]
		other2 = players[other2]
		modifier = 4/((PA.POP + PB.POP)/2)
		relations[relata].relationship -= modifier
		print("Relations between %s and %s have been reduced by %s to %s" % \
			(PA.name, PB.name, modifier, relations[relata].relationship))
		self.diplo_action -= 1
		self.reputation -= 0.025

	def embargo_Nation(self, other, players, relations):
		other = players[other]
		if self.name in other.embargo:
			other.embargo.remove(self.name)
		else:
			other.embargo.add(self.name)
		name = other.name
		relata = frozenset([self.name, name])
		relations[relata].relationship -= 0.25
		self.diplo_action -= 1





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


				