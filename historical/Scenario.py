# Scenario 
from player_class import*
from historical.Scenario_provinces import*
from technologies import*
from start import*
from historical.ScenarioNations import*

from random import*


def get_name_from_major_choice(choice):
	name = ""
	if choice == "1":
		name = "England"
	if choice == "2":
		name = "France"
	if choice == "3":
		name = "Russia"
	if choice == "4":
		name = "Germany"
	if choice == "5":
		name = "Austria"
	if choice == "6":
		name = "Italy"
	if choice == "7":
		name = "Ottoman"
	if choice == "8":
		name = "Spain"
	if choice == "9":
		name = "Netherlands"
	return name

		
def get_name_from_minor_choice(choice):
	name = ""
	if choice == "1":
		name = "Demark"
	if choice == "2":
		name = "Sweden"
	if choice == "3":
		name = "Portugal"
	if choice == "4":
		name = "Two Sicilies"
	if choice == "5":
		name = "Switzerland"
	return name 
	 

def historical():

	provinces = create_provinces()

	players = dict()
	uncivilized_minors = dict()
	i = 1

	modern_major = ["England", "France", "Russia", "Germany", "Austria", "Italy", "Ottoman", "Spain", "Netherlands"]
	modern_minors = ["Denmark", "Sweden", "Portugal", "Two Sicilies", "Switzerland", "Saxony", \
	"Bavaria", "NorthGermany", "Papal States"]
	old_empires = ["China", "India", "Japan", "Persia"]
	old_minors = ["Korea", "Egypt", "Algeria", "Morocco", "Kazakhstan", "Philippines", "Dai Nam", "Siam", "Malaysia", \
	"Brunei", "Tunisia", "Libya", "Nejd", "Afghanistan", "Bengal", "Hyderabad", "Burma", "Cambodia", "Sulawesi", "Java"]
	#unciv = ["Mozambique", "Tanzania", "Kenya", "Ethiopia", "New South Whales", "Queensland", "West Australia",
	#"South Australia", "New Zealand", "Zululand"]
	#unciv_rough = ["Mauritania", "Liberia", "Mali", "Ghana", "Niger", "Nigeria", "Cameroon", "Angola", "Nambia", \
	#"Congo", "Madagascar"] 

	print("How many nations are to be controlled by human players? \n")
	num_humans = input()
	num_humans = int(num_humans)
	human_choices = []
	for i in range(num_humans):
		print("What sort of nation will the first player be?")
		print("Choose from: (1) modern major, (2) modern minor, (3) old_minor")
		kind = input()
		if kind == "1":
			print("Which Great Power will player " + str(i) + " control? \n")
			count = 1
			choice = ""
			#while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
			while choice not in range(len(modern_major) + 1):
				for m in modern_major:
					print("%s: %s" % (count, m))
					count += 1
				choice = input()
				choice = int(choice)
				count = 1
			choice = str(choice)
			name = get_name_from_major_choice(choice)
			new = Human(name, "major", i)
			players[name] = new
			player = players[name]

			initialize_major_power(player)
			if choice == "1":
				england(player, provinces)
			if choice == "2":
				france(player, provinces)
			if choice == "3":
				russia(player, provinces)
			if choice == "4":
				germany(player, provinces)
			if choice == "5":
				austria(player, provinces)
			if choice == "6":
				italy(player, provinces)
			if choice == "7":
				ottoman(player, provinces)
			if choice == "8":
				spain(player, provinces)
			if choice == "9":
				netherlands(player, provinces)
			human_choices.append(name)
		if kind == "2":
			print("Which Minor Modern nation will player " + str(i) + " control? \n")
			count = 1
			choice = ""
			while choice not in range(6):
				for m in modern_minors:
					if m in ["Denmark", "Sweden", "Portugal", "Two Sicilies", "Switzerland"]:
						print("%s: %s" % (count, m))
						count += 1
				choice = input()
				choice = int(choice)
				count = 1
			choice = str(choice)
			name = get_name_from_minor_choice(choice)
			print("Name: %s" % (name))
			new = Human(name, "minor", i)
			players[name] = new
			player = players[name]
			initialize_modern_minor(player)
			if choice == "1":
				denmark(player, provinces)
			if choice == "2":
				sweden(player, provinces)
			if choice == "3":
				portugal(player, provinces)
			if choice == "4":
				two_sicilies(player, provinces)
			if choice == "5":
				switzerland(player, provinces) 
			human_choices.append(name)


		if kind == "3":
			print("This feature is not yet implemented")

	
	print("Initializing AI Players....\n")
	i = num_humans
	for m in modern_major:
		if m not in human_choices:
			print("Human Choices %s" % (human_choices))
			new = AI(m, "major", i)
			players[m] = new
			player = players[m]
			print("Initialize %s" % (m))
			initialize_major_power(player)
			if player.name == "England":
				england(player, provinces)
			if player.name == "Germany":
				germany(player, provinces)
			if player.name == "France":
				france(player, provinces)
			if player.name == "Russia":
				russia(player, provinces)
			if player.name == "Austria":
				austria(player, provinces)
			if player.name == "Italy":
				italy(player, provinces)
			if player.name == "Ottoman":
				ottoman(player, provinces)
			if player.name == "Spain":
				spain(player, provinces)
			if player.name == "Netherlands":
				netherlands(player, provinces)
			i += 1
	for m in modern_minors:
		if m not in human_choices:
			new = AI(m, "minor", i)
			players[m] = new
			player = players[m]
			initialize_modern_minor(player)
			if player.name == "Denmark":
				denmark(player, provinces)
			if player.name == "Sweden":
				sweden(player, provinces)
			if player.name == "Portugal":
				portugal(player, provinces)
			
			if player.name == "Two Sicilies":
				two_sicilies(player, provinces)
			if player.name == "Switzerland":
				switzerland(player, provinces)
			if player.name == "Saxony":
				saxony(player, provinces)
			if player.name == "Bavaria":
				bavaria(player, provinces)
			if player.name == "NorthGermany":
				northgermany(player, provinces)
			if player.name == "Papal States":
				papal_state(player, provinces) 
			i +=1

	for e in old_empires:
		if e not in human_choices:
			new = AI(e, "old_empire", i)
			players[e] = new
			player = players[e]

			initialize_oldempire(player)
			if player.name == "China":
				china(player, provinces)
			if player.name == "India":
				india(player, provinces)
			if player.name == "Persia":
				persia(player, provinces)
			if player.name == "Japan":
				japan(player, provinces)
			if player.name == "Ottoman":
				ottoman(player, provinces)
			i += 1

	for o in old_minors:
		if o not in human_choices:
			new = AI(o, "old_minor", i)
			players[o] = new
			player = players[o]
			initialize_old_minor(player)
			if player.name == "Korea":
				korea(player, provinces)
			if player.name == "Egypt":
				egypt(player, provinces)
			if player.name == "Algeria":
				algeria(player, provinces)
			if player.name == "Morocco":
				morocco(player, provinces)
			if player.name == "Kazakhstan":
				kazakhstan(player, provinces)
			if player.name == "Philippines":
				philippines(player, provinces)
			if player.name == "Dai Nam":
				dai_nam(player, provinces)
			if player.name == "Siam":
				siam(player, provinces)
			if player.name == "Malaysia":
				malaysia(player, provinces)
			if player.name == "Brunei":
				brunei(player, provinces)
			if player.name == "Tunisia":
				tunisia(player, provinces)
			if player.name == "Libya":
				libya(player, provinces)
			if player.name == "Nejd":
				nejd(player, provinces)
			if player.name == "Afghanistan":
				afghanistan(player, provinces)
			if player.name == "Bengal":
				bengal(player, provinces)
			if player.name == "Hyderabad":
				hyderabad(player, provinces)
			if player.name == "Burma":
				burma(player, provinces)
			if player.name == "Cambodia":
				cambodia(player, provinces)
			if player.name == "Brunei":
				brunei(player, provinces)
			if player.name == "Sulawesi":
				sulawesi(player, provinces)
			if player.name == "Java":
				java(player, provinces)

	#for u in unciv:
	#	new = Uncivilized_minor(u)
	#	uncivilized_minors[u] = new
	#	nation = uncivilized_minors[u]
	#	if u == "Zululand":
	#		zululand(nation, provinces)
	#	if u == "Mozambique":
	#		mozambique(nation, provinces)
	#	if u == "Tanzania":
	#		tanzania(nation, provinces)
	#	if u == "Kenya":
	#		kenya(nation, provinces)
	#	if u == "Ethiopia":
	#		ethiopia(nation, provinces)
	#	if u == "New South Wales":
	#		new_south_wales(nation, provinces)
	#	if u == "Queensland":
	#		queensland(nation, provinces)
	#	if u == "West Australia":
	#		west_australia(nation, provinces)
	#	if u == "South Australia":
	#		south_australia(nation, provinces)
	#	if u == "New Zealand":
	#		new_zealand(nation, provinces)
#
#		i += 1
#
#	for u in unciv_rough:
#		new = Uncivilized_minor(u)
#		uncivilized_minors[u] = new
#		nation = uncivilized_minors[u]
#		if u == "Mauritania":
#			mauritania(nation, provinces)
#		if u == "Liberia":
#			liberia(nation, provinces)
#		if u == "Mali":
#			mali(nation, provinces)
#		if u == "Ghana":
#			ghana(nation, provinces)
#		if u == "Niger":
#			niger(nation, provinces)
#		if u == "Nigeria":
#			nigeria(nation, provinces)
#		if u == "Cameroon":
#			cameroon(nation, provinces)
#		if u == "Angola":
#			angola(nation, provinces)
#		if u == "Nambia":
#			nambia(nation, provinces)
#		if u == "Ethiopia":
#			ethiopia(nation, provinces)
#		if u == "Congo":
#			congo(nation, provinces)
#		if u == "Madagascar":
#			madagascar(nation, provinces)
#		i += 1

	#print("Players")
	#for p, player in players.items():
	#	print(player.name)
	


	#print("Unvivilized Nations:")
	#for unciv in uncivilized_minors.values():
	#	print(unciv.name)
	#	for p, prov in unciv.provinces.items():
	#		print(p, prov.name)

	for p, play in players.items():
		if len(play.capital) == 0:
			x = choice(list(play.provinces.keys()))
			#for k, v in play.provinces.items():
			play.capital.add(play.provinces[k])

	for p, play in players.items():
		for p, prov in play.provinces.items():
			res = prov.resource
			play.resources[res] += prov.quality * 1
			#play.capital = play.provinces[x].name
	for p1 in players.values():
		borders = set()
		for p2 in players.values():
			if p1.check_for_border(p2) == True:
				borders.add(p2.name)
		p1.borders = borders

#	for p1 in players.values():
	#	print(p1.name)
	#	for b in p1.borders:
	#		print(b)
	#	print("\n") 


	keys = set()
	for k in players.keys():
		keys.add(k)

	pairs = findsubsets(keys, 2)
	
	relations = dict()

	for pair in pairs:
		pair = frozenset(pair)
		relations[pair] = Relation(pair)


	#for r, rel in relations.items():
	#	print(r, rel.relata)

	relations[frozenset({"England", "India"})].relationship = -0.75
	relations[frozenset({"England", "France"})].relationship = -1
	relations[frozenset({"England", "Italy"})].relationship = 1
	relations[frozenset({"England", "Ottoman"})].relationship = 1
	relations[frozenset({"England", "Persia"})].relationship = 1.25
	relations[frozenset({"England", "Spain"})].relationship = 0.75
	relations[frozenset({"England", "Germany"})].relationship = -0.75
	relations[frozenset({"England", "China"})].relationship = -0.5
	relations[frozenset({"England", "Japan"})].relationship = 0.65
	relations[frozenset({"England", "Netherlands"})].relationship = 0.5
	relations[frozenset({"England", "Sweden"})].relationship = 0.5
	relations[frozenset({"England", "Egypt"})].relationship = 1



	#relations[frozenset({"England", "Poland"})].relationship = 0.75

	relations[frozenset({"France", "Germany"})].relationship = -1.75
	relations[frozenset({"France", "Russia"})].relationship = 1.5
	relations[frozenset({"France", "Spain"})].relationship = 1
	relations[frozenset({"France", "Italy"})].relationship = -0.5
	relations[frozenset({"France", "Ottoman"})].relationship = 1
	relations[frozenset({"France", "China"})].relationship = 0.5
	relations[frozenset({"France", "Austria"})].relationship = -0.75
	relations[frozenset({"France", "Netherlands"})].relationship = -0.5
	#relations[frozenset({"France", "Poland"})].relationship = 1.25
	relations[frozenset({"France", "Bavaria"})].relationship = 2.5


	relations[frozenset({"Germany", "Austria"})].relationship = 2.2
	relations[frozenset({"Germany", "Italy"})].relationship = 1
	relations[frozenset({"Germany", "Russia"})].relationship = 0.1
	relations[frozenset({"Germany", "Ottoman"})].relationship = 1.1
	relations[frozenset({"Germany", "Netherlands"})].relationship = 0.75
	relations[frozenset({"Germany", "Denmark"})].relationship = 1.5
	relations[frozenset({"Germany", "Saxony"})].relationship = -2
	relations[frozenset({"Germany", "Bavaria"})].relationship = -2
	relations[frozenset({"Germany", "NorthGermany"})].relationship = -2.75


	#relations[frozenset({"Germany", "Poland"})].relationship = -0.5
	#relations[frozenset({"Russia", "Poland"})].relationship = -2
	relations[frozenset({"Austria", "Russia"})].relationship = -0.5
	relations[frozenset({"Austria", "Italy"})].relationship = -2
	relations[frozenset({"Russia", "Ottoman"})].relationship = -1
	relations[frozenset({"Austria", "Saxony"})].relationship = 3

	relations[frozenset({"Italy", "Russia"})].relationship = 0.65
	relations[frozenset({"Italy", "Netherlands"})].relationship = 0.25
	relations[frozenset({"Italy", "Two Sicilies"})].relationship = -2.7
	relations[frozenset({"Italy", "Papal States"})].relationship = -2.7


	relations[frozenset({"Ottoman", "Italy"})].relationship = -0.75
	relations[frozenset({"Spain", "Italy"})].relationship = 0.75
	relations[frozenset({"Sweden", "Russia"})].relationship = -0.75
	relations[frozenset({"Sweden", "Germany"})].relationship = 1.0
	#relations[frozenset({"Sweden", "Norway"})].relationship = -1.0
	relations[frozenset({"Sweden", "Denmark"})].relationship = 1
	relations[frozenset({"Sweden", "Austria"})].relationship = 0.5
	relations[frozenset({"Japan", "Korea"})].relationship = -1
	relations[frozenset({"Japan", "China"})].relationship = -1
	relations[frozenset({"China", "Korea"})].relationship = 3
	relations[frozenset({"Portugal", "Spain"})].relationship = 2
	relations[frozenset({"Portugal", "France"})].relationship = 1


	
	#new0 = CB("Germany", "Austria", "annex", "_Austria", 18)
	#players["Germany"].CB.add(new0)
	new1 = CB("Germany", "Saxony", "annex", "_Saxony", 18)
	#players["Germany"].CB.add(new1)

	#new2 = CB("Germany", "Bavaria", "annex", "_Bavaria", 18)
	#players["Germany"].CB.add(new2)
	new3 = CB("Germany", "NorthGermany", "annex", "_NorthGermany", 20)
	#players["Germany"].CB.add(new3)

	new4 = CB("Italy", "Austria", "annex", "Venezia", 20)
	new5 = CB("Italy", "Papal States", "annex", "Lazio", 20)
	#new6 = CB("Italy", "Two Sicilies", "annex", "Naples", 20)
	#new7 = CB("Italy", "Two Sicilies", "annex", "Sicily", 20)
	players["Italy"].CB.add(new4)
	players["Italy"].CB.add(new5)
	#players["Italy"].CB.add(new6)
	#players["Italy"].CB.add(new7)

	new6 = CB("England", "India", "annex", "Rajputana", 18)


	#for r, rel in relations.items():
	#	print(r, rel.relata)


	market = Market()

	market_items = dict()
		

	#globe = Globe()

	initial = {
		"players" : players, 
		"provinces": provinces, 
		"relations": relations, 
		#"uncivilized_minors": uncivilized_minors,
		"market": market,
		#"globe": globe,
	 }

	return initial

		


def AI_values(player):
	if player.type != "major":
		return
	if player.name in ["Germany", "Italy", "Austria", "Russia"]:
		player.general_priority = "army"
	else:
		player.general_priority = "expansion"


		player.general_priority = "expansion"
	if "power_loom" in player.technologies or "bessemer_process" in player.technologies:
		if player.name != "Netherlands":
			player.general_priority = "industrialize"
	if "chemistry" in player.technologies:
		player.general_priority = "production"
	if "iron_clad" in player.technologies:
		player.general_priority = "expansion"
	if "compound_steam_engine" in player.technologies:
		player.general_priority = "industrialize"
	if "combustion" in player.technologies:
		player.general_priority = "development"
	if "oil_powered_ships" in player.technologies:
		player.general_priority = "expansion"
	if "mobile_warfare" in player.technologies:
		player.general_priority = "army"




		




























