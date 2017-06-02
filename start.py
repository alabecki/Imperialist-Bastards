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
from empire_class import*
from Old_Minor_Class import*


#constants

NUM_MAJOR_POWERS = 6
NUM_OLD_EMPIRES = 4
NUM_UNCIVILIZRD_MINORS = 4
NUM_OLD_MINORS = 4

NUM_PROV_MAJORS = 5
#NUM_PROV_OLD_EMPIRES = 4
NUM_PROV_UNCIV = 2
NUM_PROV_OLD_MINORS = 2

def findsubsets(S,m):
	return set(combinations(S, m))


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
		#control = input("Is %s to be controlled by human players or by the AI? \n" % (name))
		new = Player(name, "human", i)
		players[name] = new
		players[name].borders.add(b1)
		players[name].borders.add(b2)
		print(players[name].number)
		print(players[name].borders)
		i += 1
	#Initialize the resources each player has in each province
	for k, player in players.items():
		name = doname()
		player.provinces[name] = Province(name, "food", 1.0, "core", player.name)
		#player.provinces.append(Province("1", "food", 1.0))
		player.resources["food"] += 1
		player.technologies.add("pre_industry_2")
		prov = 1
		while(prov <= NUM_PROV_MAJORS):
		#for prov in player.provinces:
			res = random.choice(['food', 'cotton', 'wood', 'coal', 'iron'])
			qual = random.triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "core", player.name)
			player.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (player.name, res, player.provinces[name].name, qual))
			player.resources[res] += 1
			prov += 1
		temp = player.borders
		player.borders = set()
		if player.number == NUM_MAJOR_POWERS:
			temp = set([1, NUM_MAJOR_POWERS-1])
		for k2, p2 in players.items():
			if p2.number in temp:
			 	player.borders.add(p2.name)
		print (players[k].borders)

		cheat = input("Would you like to make this player Uber? y/n  \n")
		if cheat == "n":
			continue
		else:
			Create_Uber_Player(player)
			assign_to_all_provinces(player)


	print("Now the Old Empires shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_EMPIRES):
		name = doname()
		new = Empire(name, "human", i)
		players[name] = new
		i += 1
	for k, empire in players.items():
		if type(empire) == Empire:
			num_provinces = randint(6, 8)
			empire.POP = num_provinces + 1.5
			empire.numLowerPOP = empire.POP - 0.25
			empire.freePOP = empire.numLowerPOP - empire.milPOP
			empire.provinces[1] = Province(doname(), "food", 1.0, "core", empire.name)
			empire.resources["food"] += 1
			player.technologies.add("any")
			prov = 1
			while(prov <= num_provinces):
				res = random.choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food'])
				qual = random.triangular(0.5, 1.5, 1.0)
				#player.provinces[prov]["resource"] = res
				#player.provinces(prov)resource =
				name = doname()
				new = Province(name, res, qual, "core", empire.name)
				empire.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (empire.name, res, empire.provinces[name].name, qual))
				empire.resources[res] += 1
				prov += 1

	print("Now the Old Minor Nations shall be initialized \n")
	i = 1
	while( i <= NUM_OLD_MINORS):
		name = doname()
		new = Old_minor(name, "AI", i)
		players[name] = new
		i += 1
		#print("old minor %s " % (i))

	for k, old_minor in players.items():
		if type(old_minor) == Old_minor:
			player.technologies.add("any")
			prov = 1
			while(prov <= NUM_PROV_OLD_MINORS):
				#print("old minor")
				res = random.choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food'])
				qual = random.triangular(0.5, 1.5, 1.0)
				name = doname()
				new = Province(name, res, qual, "core", old_minor.name)
				old_minor.provinces[name] = new
				print("Player %s is assigned %s at %s with %s quality\n" % (old_minor.name, res, prov, qual))
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
	i = 0
	while(i <= NUM_UNCIVILIZRD_MINORS):
		name = doname()
		new = Uncivilized_minor(name)
		uncivilized_minors[name] = new
		i += 1

	for k, uncivilized in uncivilized_minors.items():
		prov = 1
		while(prov <= NUM_PROV_OLD_MINORS):
			res = random.choice(['food', 'cotton', 'wood', 'coal', 'iron', 'spice', 'dyes', 'food'])
			qual = random.triangular(0.5, 2.0, 1.0)
			name = doname()
			new = Province(name, res, qual, "core", uncivilized.name)
			uncivilized.provinces[name] = new
			print("Player %s is assigned %s at %s with %s quality\n" % (uncivilized.name, res, uncivilized.provinces[name].name, qual))
			prov += 1

	market = Market()

	initial = {"players" : players, "relations": relations, "uncivilized_minors": uncivilized_minors, "market": market}


	return initial
