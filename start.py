from pprint import pprint
from random import*
from itertools import product, combinations

from name_generator import*


from cheat import*
from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from combat import*
from human import*
from AI import*
from globe import*


#constants

NUM_MAJOR_POWERS = 6
NUM_OLD_EMPIRES = 3
NUM_UNCIVILIZRD_MINORS = 4
NUM_OLD_MINORS = 4

NUM_PROV_MAJORS = 6
#NUM_PROV_OLD_EMPIRES = 4
NUM_PROV_UNCIV = 2
NUM_PROV_OLD_MINORS = 2


def findsubsets(S,m):
	return set(combinations(S, m))

def initialize_major_power(player):

	player.stability = 0.5
	player.government = "absolute monarchy"
	player.AP = 2
	player.POP = 7.5
	player.freePOP = 5.7
	player.milPOP = 0.8
	player.numLowerPOP = 6.5
	player.type = "major"

	player.shipyard = 1


	player.technologies = {"basic_civ", "pre_modern", "pre_industry", "professional_armies"}
	#player.technologies.add("pre_industry_3")
	#player.technologies.add("pre_industry_2")
	#player.technologies.add("flintlock")
	#player.technologies.add("high_pressure_steam_engine")

	#player.midPOP["researchers"]["number"] = 0.2
	#player.midPOP["officers"]["number"] = 0.2
	#player.midPOP["managers"]["number"] = 0.0
	#player.midPOP["bureaucrats"]["number"] = 0.2
	#player.midPOP["artists"]["number"] = 0.2

	#player.numMidPOP = 0.8
	player.development_level = 1
	player.developments["research"] = 1
	player.numMidPOP = 0.5

	player.resources["gold"] = 12.0
	
	player.goods["cannons"] = 2

	player.military["infantry"] = 2.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 1.0
	player.military["artillery"] = 1.0

	player.number_units = 5.0
	player.colonization = 0.5
	player.new_development = 1.0
	player.diplo_action = 1.0

def initialize_modern_minor(player):
	player.stability = 1.0
	player.government = "absolute monarchy"
	player.AP = 1
	player.POP = 2.9
	player.freePOP = 2.5
	player.milPOP = 0.4
	player.numLowerPOP = 2.9
	player.type = "minor"

	player.goods["cannons"] = 1.0
	

	player.technologies = {"basic_civ", "pre_modern", "pre_industry", "professional_armies"}



	player.resources["gold"] = 7.0
	
	player.military["infantry"] = 2.0
	player.number_units = 2


def initialize_oldempire(player):

	player.stability = 0.0
	player.milPOP = 0.8
	player.government = "despotism"
	player.type = "old_empire"

	player.numMidPOP = 0.0
	player.resources["gold"] = 14.0
	player.resources["spice"] = 0.0
	player.goods["clothing"] = 0.0
	player.goods["paper"] = 0.0
	player.goods["cannons"] = 1.0
	player.goods["furniture"] = 0.0

	player.military["infantry"] = 3.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 0.0

	player.technologies = {"basic_civ", "pre_modern"}


	player.techModifier = 0.75

	player.reputation = 0.5

	player.colonization = -5.0


def initialize_old_minor(player):

	player.stability = 0
	player.milPOP = 0.6
	player.government = "despotism"
	player.type = "old_minor"

	player.POP = 3.6
	player.numLowerPOP = 3.6
	player.freePOP = 3
	player.technologies = {"basic_civ", "pre_modern"}


	player.resources["gold"] = 6.0


	player.military["infantry"] = 2.0
	player.military["frigates"] = 0.0

	player.techModifier = 0.6

	player.reputation = 0.5

	player.colonization = -5.0


def initilize_uncivilized(player):
	player.stability = -1.0
	player.milPOP = 0.4
	player.government = "despotism"
	player.technologies.add("basic_civ")

	player.POP = 2.4
	player.numLowerPOP = 2.4
	player.freePOP = 2
	#player.technologies.add("pre_industry_1")
	player.resources["gold"] = 4.0
	player.military["infantry"] = 1.0
	player.techModifier = 0.5
	player.reputation = 0.6
	player.colonization = -8.0




def start_game():

	print("____________________________________________________________________________________________ \n")
	print ("Welcome to Imperialist Bastards! \n")
	print ("___________________________________________________________________________________________ \n \n")

	#Initialization

	players = dict()
	i = 1
	while( i <= NUM_MAJOR_POWERS):
		name = input("Please enter the name of Nation %s : \n" % (i))
		if i == 1:
			b1 = NUM_MAJOR_POWERS
			b2 = 2
		elif (i > 1 and i < NUM_MAJOR_POWERS):
			b1 = i-1
			b2 = i+1
		else:
			b1 == NUM_MAJOR_POWERS -1
			b2 == 1
		control = input("Is %s to be controlled by human players or by the AI (type 'human' or 'AI')? \n" % (name))
		cheat = " "
		if control == "human":
			new = Human(name, "major", i)
			players[name] = new
			players[name].borders.add(b1)
			players[name].borders.add(b2)
			cheat = input("Would you like to make this player Uber? y/n  \n")
			if cheat == "y":
				Create_Uber_Player(players[name])
			#initialize_major_power(players[name])
			else:
				initialize_major_power(players[name])


		if control == "AI":
			new = AI(name, "major", i)
			players[name] = new
			players[name].borders.add(b1)
			players[name].borders.add(b2)
			initialize_major_power(players[name])

		i += 1

	#Initialize the resources each player has in each province
	for k, player in players.items():
		name = doname()
		player.provinces[name] = Province(name, "food", 1.0, "civilized", player.name)
		player.resources["food"] += 1

		prov = 1
		while(prov < NUM_PROV_MAJORS):
		#for prov in player.provinces:
			#res = choice(['food', 'cotton', 'wood', 'coal', 'iron'])
			res = " "
			chance = uniform(0, 1)
			print("Chance: %s " % (chance))
			if chance <= 0.26:
				res = "food"
			elif chance > 0.26 and chance<= 0.43:  
				res = "iron"
			elif chance > 0.43 and chance <= 0.60:
				res = "cotton"
			elif chance > 0.60 and chance<= 0.77:
				res = "coal"
			elif chance > 0.77 and chance<= 0.96:
				res = "wood"
			elif chance > 0.96 and chance<= 0.97:
				res = "dyes"
			elif chance > 0.97 and chance <= 0.98:
				res = "oil"
			elif chance > 0.98:
				res = "gold"
			qual = triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "civilized", player.name)
			player.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (player.name, res, player.provinces[name].name, qual))
			player.resources[res] += 1
			if type(player) == AI:
				player.ai_modify_priorities_from_province(res)
				personality = choice(["militant", "colonizers", "industry", "science_culture"])

			prov += 1
		
		temp = player.borders
		player.borders = set()
		if player.number == NUM_MAJOR_POWERS:
			temp = set([1, NUM_MAJOR_POWERS-1])
		for k2, p2 in players.items():
			if p2.number in temp:
			 	player.borders.add(p2.name)
		print (players[k].borders)

		if player.freePOP >= len(player.provinces):
			assign_to_all_provinces(player)
		if type(player) == AI:
			for p, prov in player.provinces.items():
				player.resource_base[prov.resource] += prov.quality

	print("Now the Old Empires shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_EMPIRES):
		name = doname()
		control = input("Is %s to be controlled by human players or by the AI (type 'human' or 'AI')? \n" % (name))
		if control == "human":
			new = Human(name, "old_empire", i)
			players[name] = new
			initialize_oldemp(players[name])

		if control == "AI":
			new = AI(name, "old_empire", i)
			players[name] = new
			initialize_oldemp(players[name])
		i += 1
	for k, empire in players.items():
		if empire.type == "old_empire":
			empire.technologies.add("any")
			num_provinces = randint(6, 8)
			empire.POP = num_provinces
			empire.numLowerPOP = empire.POP
			empire.freePOP = empire.numLowerPOP - empire.milPOP
			empire.provinces[1] = Province(doname(), "food", 1.0, "old", empire.name)
			empire.resources["food"] += 1
			prov = 1
			while(prov < num_provinces):
				#res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food'])
				res = " "
				chance = uniform(0, 1)
				if chance <= 0.28:
					res = "food"
				elif chance > 0.28 and chance<= 0.38:  
					res = "iron"
				elif chance > 0.38 and chance<= 0.50:
					res = "cotton"
				elif chance > 0.50 and chance<= 0.60:
					res = "coal"
				elif chance > 0.60 and chance<= 0.73:
					res = "wood"
				elif chance > 0.73 and chance<= 0.77:
					res = "dyes"
				elif chance > 0.77 and chance <= 0.90:
					res = "spice"
				elif chance > 0.90 and chance <= 0.95:
					res = "rubber"	
				elif chance > 0.95:
					res = "oil"

				qual = triangular(0.5, 1.5, 1.0)
				#player.provinces[prov]["resource"] = res
				#player.provinces(prov)resource =
				name = doname()
				new = Province(name, res, qual, "old", empire.name)
				empire.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (empire.name, res, empire.provinces[name].name, qual))
				empire.resources[res] += 1
				if type(empire) == AI:
					empire.ai_modify_priorities_from_province(res)
				prov += 1

	print("Now the Old Minor Nations shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_MINORS):
		name = doname()
		new = AI(name, "old_minor", i)
		players[name] = new
		initialize_old_minor(players[name])
		players[name].resources["gold"] = 5.0
		i += 1
		#print("old minor %s " % (i))

	for k, old_minor in players.items():
		if old_minor.type == "old_minor":
			old_minor.technologies.add("pre_industry_1")
			prov = 1
			while(prov <= NUM_PROV_UNCIV):
				#print("old minor")
				#res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'spice','dyes', 'food', 'gold'])
				res = " "
				chance = uniform(0, 1)
				if chance <= 0.30:
					res = "food"
				elif chance > 0.30 and chance <= 0.38:  
					res = "iron"
				elif chance > 0.38 and chance<= 0.46:
					res = "cotton"
				elif chance > 0.46 and chance<= 0.56:
					res = "coal"
				elif chance > 0.56 and chance<= 0.64:
					res = "wood"
				elif chance > 0.64 and chance<= 0.70:
					res = "dyes"
				elif chance > 0.70 and chance<= 0.84:
					res = "spice"
				elif chance > 0.84 and chance <= 0.92:
					res = "rubber"
				elif chance > 0.92 and chance <= 0.98:
					res = "oil"
				elif chance > 0.98:
					res = "gold"

				qual = triangular(0.5, 1.5, 1.0)
				name = doname()
				new = Province(name, res, qual, "old", old_minor.name)
				old_minor.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (old_minor.name, res, old_minor.provinces[name].name, qual))
				old_minor.resources[res] += 1
				prov += 1

	keys = set()
	for k in players.keys():
		keys.add(k)

	pairs = findsubsets(keys, 2)
	#for pair in pairs:
		#print(pair)
	relations = dict()

	for pair in pairs:
		pair = frozenset(pair)
		relations[pair] = Relation(pair)

	print("Now we add Uncivilized Minor Nations")
	uncivilized_minors = dict()
	i = 1
	while(i <= NUM_UNCIVILIZRD_MINORS):
		name = doname()
		new = Uncivilized_minor(name)
		uncivilized_minors[name] = new
		i += 1

	for k, uncivilized in uncivilized_minors.items():
		prov = 1
		while(prov <= NUM_PROV_UNCIV):
			#res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'spice', 'dyes', 'food', 'gold'])
			
			res = " "
			chance = uniform(0, 1)
			if chance <= 0.28:
				res = "food"
			elif chance > 0.28 and chance<= 0.36:  
				res = "iron"
			elif chance > 0.36 and chance<= 0.44:
				res = "cotton"
			elif chance > 0.44 and chance<= 0.52:
				res = "coal"
			elif chance > 0.52 and chance<= 0.60:
				res = "wood"
			elif chance > 0.60 and chance<= 0.68:
				res = "dyes"
			elif chance > 0.68 and chance<= 0.83:
				res = "spice"
			elif chance > 0.83 and chance <= 91:
				res = "rubber"
			elif chance > 0.91 and chance <= 98:
				res = "oil"
			elif chance > 98:
				res = "gold"

			qual = triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "uncivilized", uncivilized.name)
			uncivilized.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (uncivilized.name, res, uncivilized.provinces[name].name, qual))
			prov += 1

	market = Market()

	initial = {"players" : players, "relations": relations, "uncivilized_minors": uncivilized_minors, "market": market}


	return initial
