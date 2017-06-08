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


#constants

NUM_MAJOR_POWERS = 5
NUM_OLD_EMPIRES = 2
NUM_UNCIVILIZRD_MINORS = 0
NUM_OLD_MINORS = 0

NUM_PROV_MAJORS = 5
#NUM_PROV_OLD_EMPIRES = 4
NUM_PROV_UNCIV = 2
NUM_PROV_OLD_MINORS = 2

def findsubsets(S,m):
	return set(combinations(S, m))

def initialize_major_human_power(player):

	player.stability = 1.0
	player.AP = 2
	player.POP = 6.1
	player.freePOP = 5
	player.milPOP = 0.6
	player.numLowerPOP = 5.0

	player.technologies.add("pre_industry_2")
	player.technologies.add("high_pressure_steam_engine")

	player.midPOP["researchers"]['number'] = 0.1
	player.midPOP["officers"]['number'] = 0.1
	player.midPOP["bureaucrats"]['number'] = 0.1
	player.midPOP["artists"]['number'] = 0.1
	player.midPOP["managers"]['number'] = 0.1

	player.numMidPOP = 0.5

	player.resources["gold"] = 10.0
	player.resources["spice"] = 1.0

	player.goods["clothing"] = 1.0
	player.goods["paper"] = 1.0
	player.goods["cannons"] = 0.5
	player.goods["furniture"] = 0.5

	player.military["infantry"] = 2.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 1.0

	player.number_units = 4.0
	player.colonization = 0.5

def initialize_major_AI_power(player):

	player.stability = 1.0
	player.AP = 2
	player.POP = 6.1
	player.freePOP = 5
	player.milPOP = 0.6
	player.numLowerPOP = 5.0

	player.technologies.add("pre_industry_2")
	player.technologies.add("high_pressure_steam_engine")

	player.midPOP["researchers"]['number'] = 0.1
	player.midPOP["officers"]['number'] = 0.1
	player.midPOP["bureaucrats"]['number'] = 0.1
	player.midPOP["artists"]['number'] = 0.1
	player.midPOP["managers"]['number'] = 0.1

	player.numMidPOP = 0.5

	player.resources["gold"]["amount"] = 10.0
	player.resources["spice"]["amount"] = 1.0

	player.goods["clothing"]["amount"] = 1.0
	player.goods["paper"]["amount"] = 1.0
	player.goods["cannons"]["amount"] = 0.5
	player.goods["furniture"]["amount"] = 0.5

	player.military["infantry"] = 2.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 1.0

	player.number_units = 4.0
	player.colonization = 0.5
	player.new_development = 0.5

def initialize_oldemp_human(player):

	player.stability = -1.0
	player.milPOP = 0.9

	player.midPOP["researchers"]['number'] = 0.05
	player.midPOP["officers"]['number'] = 0.05
	player.midPOP["bureaucrats"]['number'] = 0.05
	player.midPOP["artists"]['number'] = 0.05
	player.midPOP["managers"]['number'] = 0.05

	player.numMidPOP = 0.25
	player.technologies.add("pre_industry_1")
	player.resources["gold"] = 12.0
	player.resources["spice"] = 1.0
	player.goods["clothing"] = 0.5
	player.goods["paper"] = 0.5
	player.goods["cannons"] = 0.5
	player.goods["furniture"] = 0.25

	player.military["irregulars"] = 4.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 1.0

	player.techModifier = 0.75

	player.reputation = 0.5

	player.colonization = -5.0

def initialize_oldemp_AI(player):

	player.stability = -1.0
	player.milPOP = 0.9
	player.technologies.add("pre_industry_1")
	player.midPOP["researchers"]['number'] = 0.05
	player.midPOP["officers"]['number'] = 0.05
	player.midPOP["bureaucrats"]['number'] = 0.05
	player.midPOP["artists"]['number'] = 0.05
	player.midPOP["managers"]['number'] = 0.05

	player.numMidPOP = 0.25

	player.resources["gold"]["amount"] = 12.0
	player.resources["spice"]["amount"] = 1.0
	player.goods["clothing"]["amount"] = 0.5
	player.goods["paper"]["amount"] = 0.5
	player.goods["cannons"]["amount"] = 0.5
	player.goods["furniture"]["amount"] = 0.25

	player.military["irregulars"] = 4.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 1.0

	player.techModifier = 0.75

	player.reputation = 0.5

	player.colonization = -5.0

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

		if control == "human":
			new = Human(name, "major", i)
			players[name] = new
			players[name].borders.add(b1)
			players[name].borders.add(b2)
			print(players[name].number)
			print(players[name].borders)

			cheat = input("Would you like to make this player Uber? y/n  \n")
			if cheat == "n":
				initialize_major_human_power(players[name])
			else:
				Create_Uber_Player(players[name])

		elif control == "AI":
			new = AI(name, "major", i)
			players[name] = new
			players[name].borders.add(b1)
			players[name].borders.add(b2)
			print(players[name].number)
			print(players[name].borders)
			initialize_major_AI_power(players[name])
		i += 1

	#Initialize the resources each player has in each province
	for k, player in players.items():
		name = doname()
		player.provinces[name] = Province(name, "food", 1.0, "core", player.name)
		if type(player) == Human:
			player.resources["food"] += 1
		if type(player) == AI:
			player.resources["food"]["amount"] += 1

		prov = 1
		while(prov <= NUM_PROV_MAJORS):
		#for prov in player.provinces:
			res = choice(['food', 'cotton', 'wood', 'coal', 'iron'])
			qual = triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "core", player.name)
			player.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (player.name, res, player.provinces[name].name, qual))
			if type(player) == Human:
				player.resources[res] += 1
			if type(player) == AI:
				player.resources[res]["amount"] += 1
				player.ai_modify_priorities_from_province(res)
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


	print("Now the Old Empires shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_EMPIRES):
		name = doname()
		control = input("Is %s to be controlled by human players or by the AI (type 'human' or 'AI')? \n" % (name))
		if control == "human":
			new = Human(name, "old_empire", i)
			players[name] = new
			initialize_oldemp_human(players[name])

		if control == "AI":
			new = AI(name, "old_empire", i)
			players[name] = new
			initialize_oldemp_AI(players[name])
		i += 1
	for k, empire in players.items():
		if empire.type == "old_empire":
			empire.technologies.add("any")
			num_provinces = randint(6, 8)
			empire.POP = num_provinces + 1.5
			empire.numLowerPOP = empire.POP - 0.25
			empire.freePOP = empire.numLowerPOP - empire.milPOP
			empire.provinces[1] = Province(doname(), "food", 1.0, "core", empire.name)
			if type(empire) == Human:
				empire.resources["food"] += 1
			if type(empire) == AI:
				empire.resources["food"]["amount"] += 1
				empire.ai_modify_priorities_from_province(res)
			prov = 1
			while(prov <= num_provinces):
				res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food', 'gold'])
				qual = triangular(0.5, 1.5, 1.0)
				#player.provinces[prov]["resource"] = res
				#player.provinces(prov)resource =
				name = doname()
				new = Province(name, res, qual, "core", empire.name)
				empire.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (empire.name, res, empire.provinces[name].name, qual))
				if type(empire) == Human:
					empire.resources[res] += 1
				if type(empire) == AI:
					empire.resources[res]["amount"] += 1
				prov += 1

	print("Now the Old Minor Nations shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_MINORS):
		name = doname()
		new = AI(name, "old_minor", i)
		players[name] = new
		initialize_oldemp_AI(players[name])
		players[name].resources["gold"]["amount"] = 5.0
		i += 1
		#print("old minor %s " % (i))

	for k, old_minor in players.items():
		if old_minor.type == "old_minor":
			old_minor.technologies.add("pre_industry_1")
			prov = 1
			while(prov <= NUM_PROV_OLD_MINORS):
				#print("old minor")
				res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food', 'gold'])
				qual = triangular(0.5, 1.5, 1.0)
				name = doname()
				new = Province(name, res, qual, "core", old_minor.name)
				old_minor.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (old_minor.name, res, old_minor.provinces[name].name, qual))
				old_minor.resources[res]["amount"] += 1
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
	i = 0
	while(i <= NUM_UNCIVILIZRD_MINORS):
		name = doname()
		new = Uncivilized_minor(name)
		uncivilized_minors[name] = new
		i += 1

	for k, uncivilized in uncivilized_minors.items():
		prov = 1
		while(prov <= NUM_PROV_OLD_MINORS):
			res = choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food', 'gold'])
			qual = triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "core", uncivilized.name)
			uncivilized.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (uncivilized.name, res, uncivilized.provinces[name].name, qual))
			prov += 1

	market = Market()

	initial = {"players" : players, "relations": relations, "uncivilized_minors": uncivilized_minors, "market": market}


	return initial
