
import random
import minor_class
import Technologies

craft = {
    "parts" : "iron",
    "cannon" : "iron",
    "paper" : "wood",
    "clothing" : "cotton",
    "furniture" : "wood",
    "chemicals" : "coal"
        }

manifacture = {
	"parts": {"iron": 0.6, "coal": 0.3},
	"cannon": {"iron": 0.6, "coal": 0.3},
	"paper": {"wood": 0.9},
	"clothing": {"cotton": 0.8, "dyes": 0.1},
	"furniture": {"wood", 0,6, "cotton", 0.3},
	"chemicals": {"coal", 0.6}
			}

stability_map = {
    -1.5: 0.75,
    -1.0: 0.8,
    -0.5: 0.85,
    -0.0: 0.9,
    0.5: 0.95,
    1.0: 1.0,
    1.5: 1.05,
    2.0: 1.1,
    2.5: 1.15,
    3.0: 1.25
}

development_map = {
    0.0: 1.0,
    1.0: 1.75,
    2.0: 2.5
}

class Player(object):

	player_count = 0

	def __init__ (self, _name):

        # Basic Attributes
		self.name = _name
		#self.gold = 10.0
		self.stability = 1.0
        self.stability_mod = 1.0
		self.AP = 2.0

        self.provinces = {}

        #General POP Attributes
		self.POP = 5.9
		self.POP_growth_mod = 1.0
		self.freePOP = 5.0
		self.proPOP = 0.0
		self.production_modifier = 1.0
		self.milPOP = 0.4

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
        self.milPOP = 0.4

        #Good and Resources
		self.resources = {
        "gold": 10.0
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
		"cannon": 0.5,
		"furniture": 0.5,
		"chemicals": 0.0
		}

        self.goods_produced = {
		"parts": 0.0,
		"clothing": 0.0,
		"paper": 0.0,
		"cannon": 0.0,
		"furniture": 0.0,
		"chemicals": 0.0
		}

        #Industry
        self.new_development = 0.0
        self.number_developments = 0.0
		self.factories = set()
		self.factory_build = 4.0
        self.factory_throughput ] 0.4
		self.material_mod = 1.0

        #Technology
		self.technologies = set()
		self.research = 0

        self.chemicals = set()
		#self.tech_added = 0.0

        #diplomacy
        self.reputation = 1.0
        self.diplo_action = 0.0

        #Military
		military = {
			"infantry": 2.0,
			"calverley": 1.0,
			"artillery": 0.0,
			"frigates": 1.0,
			"iron_clad": 0.0
		}

        self.number_units = 4.0

        infantry = {
            "attack": 1.0,
            "defence": 1.5,
            "recon": 0.0,
            "manouver": 0.0,
            "ammo_use": 0.1
        }

        artillery = {
            "attack": 1.75,
            "defend": 1.75,
            "recon": 0.0,
            "manouver": 0.0,
            "ammo_use": 0.2
        }

        calverley = {
            "attack": 1.5,
            "defend": 1.0,
            "recon": 1.0,
            "manouver": 1.0
            "ammo_use": 0.1
        }

        frigate = {
            "attack": 2.0,
            "defend": 2.0,
            "ammo_use": 0.2
        }

        iron_clad = {
            "attack": 4.0,
            "defend": 4.0,
            "ammo_use": 0.2
        }

		fortification = 1.0
        max_fortification = 1.0

		Player.player_count += 1



	def research():
	       print("Which Technology would you like to develop? (Print entire name) \n")
           for k, t in technologies.items():
               if(k is not in self.technologies and if k[t]["requirement"] in self.technologies)
                print(k, t)
            choice = input()
            if(technologies[choice]["cost"] < self.research):
                print("You do not have enough research points to gain that technology. \n")
            else:
                self.research -= technologies[choice]["cost"]
                self.technologies.add(choice)
            if(choice == muzzle_loaded_arms):
                self.infantry["attack"] += 0.25
                self.infantry["defend"] += 0.10
                self.calverley["attack"] += 0.20
                self.calverley["defend"] += 0.10
                self.artillery["attack"] += 0.25
                self.artillery["defend"] += 0.10
                self.frigate["attack"] += 0.25
                self.frigate["attack"] += 0.25
            if(choice == "cement"):
                self.max_fortification += 1
            if(choice == "breach_loaded_arms"):
                self.infantry["attack"] += 0.30
                self.infantry["defend"] += 0.15
                self.calverley["attack"] += 0.25
                self.calverley["defend"] += 0.12
                self.artillery["attack"] += 0.30
                self.artillery["defend"] += 0.15
                self.frigate["attack"] += 0.30
                self.frigate["attack"] += 0.30
            if(choice == "machine_guns" )
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
            if(choice = "synthetic_dyes"):
                self.chemicals.add("dyes")
            if(choice = "fertlizer"):
                self.chemicals.add("fertlizer")
            if(choice = "telegraph"):
                self.production_modifier += 0.1
                self.stability_mod += 0.1
            if(choice = "radio"):
                self.stability_mod += 0.2


	def assign_pop(self):
		if(self.freePOP < 1.0):
			print("You do not have any free POPs\n ")
		else:
			kind = input("Where would you like to assign a POP?: 1, province or 2, production, 3, free a POP \n")
			if(kind == "1"):
                empty == False
                for p in self.provinces:
                    if(p.worked == False):
                        print("Name: %s  Resoruce: %s  Quality: %s \n"% (p.name, p.resoruce, p.quality))
                        empty == True
		            if empty == False:
					    print("All of your provinces are currently being worked \n")
					    return
				    else:
					    print("To which province do you wish to assign a POP? (type in name) \n")
					    choice = input()
					    self.freePOP -= 1.0
                        self.provinces[choice].worked = True
					#self.provinces[p][worked] = True
					return
			elif(kind == "2"):
				self.freePOP -= 1
				self.proPOP += 1
				print("You now have %s POPs assigned to production \n" % (self.proPOP))
				return
            elif(kind == "3"):
                print("From where will you like to free a POP? 1, province or 2, production? \n")
                kind2 = input()
                if(kind2 == "1"):
                    print("From which province would you like to take a POP? (tyoe name)\n")
                    for p in self.provinces:
    					if(self.provinces[p].worked == True):
                            print("Name: %s  Resoruce: %s  Quality: %s \n"% (p.name, p.resoruce, p.quality))
                            choice = input()
                            self.freePOP += 1.0
                            self.province[choice].worked = False
                            print("You now have %s free POPS \n " (self.freePOP)
                if(kind2 == "2"):
                    self.proPOP -= 1
                    self.freePOP += 1
                    print("You now have %s free POPS \n " (self.freePOP)

    def build_unit(self):
        if(freePOP < 0.1):
            print("You do not have enugh free POPs to build a unit \n")
            return
        if(self.goods["cannon"] < 1):
			print("You do not have enough cannons to build any military unites \n")
			return
        print("What kind of unit would you like to build? \n")
        for k, v in military:
            print(k, v)
        choice = input()
        if(choice == "infantry"):
            self.build_infantry()
        if(choice == "calverley"):
            self.build_calverly()
        if(choice == "artillery"):
            self.build_artillery()
        if(choice == "frigate"):
            self.build_frigate()
        if(choice == "iron_clad")
            self.build_ironclad(
        else:
            return

    def build_infantry(self):
        if(self.goods["clothing"] < 0.1):
        	print("You do not have enough clothing to build Infantry \n")
        	return
        self.goods["clothing"] -= 0.1
        self.freePOP -= 0.1
        self.goods["cannon"] -= 1.0
        self.military["infantry"] += 1.0
        print("You now have %s Infantry \n" % (self.military["infantry"]))

    def build_calverly(self):
        if(self.goods["clothing"] < 0.1):
    		print("You do not have enough clothing to build calverley \n")
        	return
        if(self.goods["food"] < 0.1):
    		print("You do not have enough Food to build calverley \n")
    		return
        self.resources["food"] -= 0.1
        self.freePOP -= 0.1
        self.goods["cannon"] -= 1.0
        self.goods["clothing"] -= 0.1
        self.military["calverley"] += 1.0
        print("You now have %s calverley \n" % (self.military["calverley"]))

    def build_artillery(self):
        if(self.goods["clothing"] < 0.1):
    		print("You do not have enough clothing to build artillery \n")
    		return
        if(self.goods["cannons"] < 2.0):
    		print("You do not have enough cannons to build artillery \n")
    		return
        self.goods["cannon"] -= 2.0
        self.freePOP -= 0.1
        self.goods["clothing"] -= 0.1
        self.military["artillery"] += 1.0
        print("You now have %s artillery \n" % (self.military["artillery"]))

	def build_frigate(self):
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		if(self.goods["cannon"] < 1.0):
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
			self.goods["cannon"] -= 1.0
			self.resources["cotton"] -= 1.0
			self.resources["wood"] -= 1.0
			self.military["frigates"] += 1.0
			print("You now have %s \n" % (self.military["frigates"]))
			return

	def build_ironclad(self):
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		if(self.goods["cannon"] < 1.0):
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
			self.goods["cannon"] -= 1.0
			self.resources["iron"] -= 1.0
			self.goods["parts"] -= 1.0
			self.military["iron_clad"]
			print("You now have %s \n" % (self.military["iron_clad"]))
			return

	#def build_fortification(self):

	def build_factory(self, _type):
	    if(self.new_development < 1):
            print("You do not have any Development Points to spend \n")
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
			self.resource["iron"] -= 1.0
			self.goods["parts"] -= 1.0
			factory.update(_type)
            self.stability_mod -= 0.05
			print("You have constructed a %s factory \n" % (_type))
			return

	# to be replaced with develop_province(self)
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
			prov = input("Which province would you like to develop? \n")
            for k, v in self.provinces.items():
                print("Name: %s Resoruce: %s Development: %s, Quality: %s  \n" % \
                (v.name, v.resource, v.development_level, v.quality))
            if(self.provinces[prov].development = 2):
                print("You have already reached the maximum level of development")
                return
			elif(self.provinces[prov].resource = "food"):
                max_dev = 0
                if("steel_plows" in self.technologies):
                    max_dev = 1
                if("mechanical_reaper" in self.technologies):
                    max_dev = 2
            elif(self.provinces[prov].resource = "iron" or self.provinces[prov].resource = "coal"):
                max_dev = 0
                if("square_timbering" in self.technologies):
                    max_dev = 1
                if("dynamite" in self.technologies):
                    max_dev = 2
            elif(self.provinces[prov].resource = "cotton"):
                max_dev = 0
                if("cotton_gin" in self.technologies):
                    max_dev = 1
                if("compound_steam_engine" in self.technologies):
                    max_dev = 2
            elif(self.provinces[prov].resource = "wood"):
                max_dev = 0
                if("saw_mill" in self.technologies):
                    max_dev = 1
                if("compound_steam_engine" in self.technologies):
                    max_dev = 2
            elif(self.provinces[prov].resource = "spice"):
                max_dev = 1
            elif(self.provinces[prov].resource = "gold"):
                max_dev = 0
                if("dynamite" in self.technologies):
                    max_dev = 1
            elif(self.provinces[prov].resource = "dyes"):
                max_dev = 0
                if("compound_steam_engine" in self.technologies):
                    max_dev = 1
            if self.provinces[prov].development = max_dev:
                    print("You cannot further develop this province at this time")
                    return
                else:
                    self.resources["iron"] -= 0.5
			        self.resources["parts"] -= 1.0
    		        self.resources["wood"] -= 1.0
    		        self.AP -= 1
                    self.new_development -= 1
                    self.provinces[prov].development_level += 1
                    self.number_developments += 1
                    print("You have developed province %s, its development level is now %s \n" % (prov, provinces[prov].development_level))


	def craftman_production(self):
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type = input("What kind of good do you want to produce with craftsmen?: parts cannons clothes paper furniture \n")
		if(self.resources[craft[_type]] < 1.1):
			print("You do not have enough %s with which to make %s \n" % (craft[_type], _type))
			return
		else:
			self.resources[craft[_type]] -= 1.2
            self.goods_produced[_type] += 1.0
			self.AP -= 1
			print("The  %s will be ready next turn \n" % (_type))
			return

	def factory_production(self):
		if(self.AP < 1):
			print("You do not have any Action Points left \n")
			return
		_type = input("What kind of good do you want to produce with factory?: parts cannons clothes paper furniture chemicals \n")
		if(_type in self.factories == False):
			print("You do not have a %s factory \n" % (_type))
			return
		elif(_type == parts):
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		elif(_type = "cannon"):
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		elif(_type == "paper"):
			if("pulping" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		elif(_type == "furniture"):
			if("electricity" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		elif(_type == "clothing"):
			if("power_loom" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		elif(_type == "chemicals"):
				max_amount = (self.factory_throughput + 4) * stability[self.stability]
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		amount = input("How many %s do you want to produce? \n" % (_type))
		if(amount > max_amount):
			print("You can only build %s items at a time with a %s factory \n" % (self.factory_throughput, _type))
			return
		else:
			for i in manifacture[_type]:
				if(manifacture[_type][i] * amount * material_mod > self.resources[i]):
					print("You do not have sufficient %s for your factory to produce %s %s \n" % (i, amount, _type))
					return
				else:
					for i in manifacture[_type]:
						self.resources[i] -= manifacture[_type][i] * amount * material_mod
                    if (_type = "chemicals" and "dyes" in player.technologies:
                        option = input("Would you like your chemicals to count as dyes? y/n")
                        if(option == "y"):
                            self.resources["dyes"] + amount
					self.goods_produced[_type] += 1.0
					print("Next turn you will receive %s %s" % (self.goods_produced[_type], _type))
					return

	def collect_resources(self):
		for k, p in self.provinces:
			#if(self.provinces[i]["worked"] == True):
			if(p.worked == True):
				quality = p.quality
			    dev = p.development
                    self.resources[p.resource] += development[p.development_level] * stability[self.stability]


	def view_inventory(self):
		print("gold: %s \n" % (self.gold))
		for key, value in self.resources.items():
			print (" %s : %s \n" % (key, value))
		for key, value in self.goods.items():
			print (" %s : %s \n" % (key, value))

    def view_inventory_production_needs(self):
        for key, value in self.resources.items():
            if(key == "food" or key == "spice" or key = "coal"):
                if(key == "food"):
                    need = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry "] * 0.1
                if(key == "spice"):
                    need = (self.numMidPOP * 0.2)
                if(key == "coal"):
                    need = 0.3 * self.number_developments
                current_production  = 0
                for p in provinces:
                    if p.resource == key and p.worked == True:
                        current_production += development[p.development_level] * stability[self.stability]
                forcast = (player.resources[key] + current_production) - need
                print("Resource: %s, Current Supply: %s, Current Consumption: %s, Current Production: %s, New Turn Forcast %s \n" % \
                key, need, current_production, forecast)
        need = {
            "clothing": (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2),
            "furniture":(self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2),
            "paper":(self.numMidPOP * 0.3)
        }
        clothing_need = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
        furniture_need = (self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2)
        paper_need = (self.numMidPOP * 0.3)
        for key, value in self.goods.items():
                if(key == "clothing" or key == "furniture" or key == "paper"):
                    print("Good: %s, Current Supply: %s, Current Consumption %s, Current Production: %s, New Turn Forecast %s \n" % \
                    (key, self.goods["clothing"], need[key], self.goods_produced[key], ((self.goods["clothing"] + \
                    self.goods_produced[key]) - need[key]) )),





        for key, value in self.resources.items():
            current_production  = 0
            for p in provinces:
                if p.resource == key and p.worked == True:
                    current_production = development[p.development_level] * stability[self.stability]
            need = 0
            if(key = "food"):
                need = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry "] * 0.1
            if(key = "clothing"):
                need = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
            if(key = "furniture"):
                need = (self.numMidPOP * 0.3)
            if(key = "spice"):
                need = (self.numMidPOP * 0.2)
            forcast = (player.resources[key] + current_production) - need
            print("Resource: %s, Current Supply: %s, Current Production: %s, Current Consumption: %s, New Turn Forcast: %s  \n" %  \
            (key, player.resources[key], current_production, need, forcast))


	def calMaintenance(self):
		mFood = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry "] * 0.1
		mClothing = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
		mFurniture = (self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2)
		mPaper = (self.numMidPOP * 0.3)
		mSpice = (self.numMidPOP * 0.2)
		mArms = (self.numMidPOP["officers"] * 0.3)
		return [mFood, mClothing, mFurniture, mPaper, mSpice, mArms]

	def payMaintenance(self):
		temp = calMaintenance()
		if(self.resources["food"] < temp(0)):
			freePOP -= (self.resources["food"] - temp(0))
			stability -= 0.2
			self.resources["food"] = 0.0
			self.midGrowth = False
		else:
			self.resources["food"] -= temp(0)
		if(self.resources["clothing"] < temp(1)):
			stability -= 0.05
			self.resources["clothing"] = 0.0
			self.midGrowth = False
		else:
			self.resources["clothing"] -= temp(1)
		if(self.resources["furniture"] < temp(2)):
			stability -= 0.05
			self.midGrowth = False
			self.resources["furniture"] = 0.0
		else:
			self.resources["furniture"] -= temp(2)
		if(self.resources["paper"] < temp(3)):
			stability -= 0.05
			self.resources["paper"] = 0.0
			self.midGrowth = False
		else:
			self.resources["paper"] -= temp(3)
		if(self.resources["spice"] < temp(4)):
			stability -= 0.075
			self.resources["spice"] = 0.0
			self.midGrowth = False
		else:
			self.resources["spice"] -= temp(4)
		if(self.resources["arms"] < temp(5))
            temp = self.numMidPOP["officers"] * 0.9
			self.numMidPOP["officers"] -= temp
			self.numMidPOP -= temp
			self.freePOP += temp
		else:
			self.resources["arms"] -= temp(5)
		if(self.resources["coal"] < 0.3 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")
		while(self.resources["coal"] >= 0.3):
			for k, prov in self.provinces:
				if(prov.development_level.level = 1):
					self.resources["coal"] -= 0.25
					self.provinces(prov).railroad.powered = True
                elif(prov.development_level.level = 2):
    				self.resources["coal"] -= 0.5
    				self.provinces(prov).railroad.powered = True

	def popChange(self):
		if(self.resources["food"] > 0.5):
			change =  self.POP * 0.04
			if(self.stability > 0):
				change += (self.POP * 0.04) * (stability[self.stability] * self.POP_growth_mod)
			mChemicals = (self.numMidPOP * 0.15)
			if(self.goods["chemicals"] >= mChemicals):
				self.goods["chemicals"] -= mChemicals
				change += 0.1 * self.numMidPOP
			self.freePOP += change
			self.numLowerPOP += change
			self.POP += change

	def popMidChange(self):
		if(stability < -2):
			return
		if(midGrowth == False):
			return
		else:
			change = 0.1 + ((self.midPOP["bureaucrats"]/2) + (self.midPOP["researchers"]/4))* stability[self.stability]
			self.numMidPOP += change
			self.POP += change
			for item in self.midPOP.values():
                item["number"] += change * item["priority"]


	def turn(self):
		self.collect_resources()
		self.payMaintenance()
		self.stability -= (numLowerPOP * 0.01) + (numMidPOP * 0.02)
		self.stability += ((self.midPOP["bureaucrats"]/6) + (self.midPOP["artists"]/3)) * self.stability_mod
		self.popChange()
		self.popMidChange()
		self.AP = int(proPOP) * self.production_modifier
		self.research += ((0.2 + (self.midPOP["researchers"] * 0.8) + (self.midPOP["managers"] * 0.2))) * stability[self.stability]
		self.diplomacy += 0.2 + (self.midPOP["bureaucrats"]) * self.reputation
