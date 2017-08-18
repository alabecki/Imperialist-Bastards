# Scenario 
from player_class import*
from historical.Scenario_provinces import*
from technologies import*
from start import*
from historical.ScenarioNations import*


def get_name_from_major_choice(choice):
	if choice == "1":
		name = "England"
	if choice == "4":
		name = "Germany"
	if choice == "2":
		name = "France"
	if choice == "3":
		name = "Russia"
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
	if choice == "1":
		name = "Demark"
	if choice == "2":
		name = "Sweden"
	if choice == "3":
		name = "Portugal"
	if choice == "4":
		name = "Norway"

def historical():

	provinces = create_provinces()

	players = dict()
	uncivilized_minors = dict()
	i = 1

	modern_major = ["England", "France", "Russia", "Germany", "Austria", "Ottoman", "Italy", "Spain", "Netherlands"]
	modern_minors = ["Denmark", "Sweden", "Portugal", "Norway"]
	old_empires = ["China", "India", "Japan", "Persia"]
	old_minors = ["Korea", "Egypt", "Algeria", "Morocco", "Kazakhstan", "Philippines", "Dia Dam", "Siam", "Malaysia", \
	"Brunei", "Tunisia", "Libya", "Nejid", "Afghanistan", "Bengal", "Hyderabad", "Burma", "Cambodia", "Sulawesi"]
	unciv = ["Mozambique", "Tanzania", "Kenya", "Ethiopia", "New South Whales", "Queensland", "West Australia",
	"South Australia", "New Zealand", "Zululand"]
	unciv_rough = ["Mauritania", "Liberia", "Mali", "Ghana", "Niger", "Nigeria", "Cameroon", "Angola", "Nambia", \
	"Congo", "Madagascar"] 

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
			for m in modern_major:
				print("%s: %s" % (count, m))
				count += 1
			choice = input()
			name = get_name_from_major_choice(choice)
			new = Human(name, "major", i)
			players[name] = new
			player = players[name]
			initialize_major_power(player)
			if choice == "1":
				england(player, provinces)
			if choice == "4":
				germany(player, provinces)
			if choice == "2":
				france(player, provinces)
			if choice == "3":
				russia(player, provinces)
			if choice == "5":
				austria(player, provinces)
			if choice == "6":
				italy(player)
			if choice == "7":
				ottoman(player, provinces)
			if choice == "8":
				spain(player)
			if choice == "9":
				netherlands(player)
			human_choices.append(name)
		if kind == "2":
			print("Which Minor Modern nation will player " + i + " control? \n")
			count = 1
			for m in modern_minors:
				print("%s: %s" % (count, m))
				count += 1
			choice = input()
			name = get_name_from_minor_choice(choice)
			new = Human(choice, "modern_minor", i)
			players[name] = new
			player = players[name]
			initialize_modern_minor(player)
			if choice == "1":
				denmark(player, provinces)
			if choice == "2":
				sweden(player)
			if choice == "3":
				portugal(player, provinces)
			if choice == "4":
				norway(player)
			human_choices.append(name)

		if kind == "3":
			print("This feature is not yet implemented")

	
	print("Initializing AI Players....\n")
	i = num_humans
	for m in modern_major:
		if m not in human_choices:
			new = AI(m, "major", i)
			players[m] = new
			player = players[m]
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
			new = AI(m, "civ_minor", i)
			players[m] = new
			player = players[m]
			initialize_modern_minor(player)
			if player.name == "Denmark":
				denmark(player, provinces)
			if player.name == "Sweden":
				sweden(player, provinces)
			if player.name == "Portugal":
				portugal(player, provinces)
			if player.name == "Norway":
				norway(player, provinces)
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
			if player.name == "Dai Dam":
				dai_dam(player, provinces)
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
			if player.name == "Nejid":
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

	for u in unciv:
		new = Uncivilized_minor(u)
		uncivilized_minors[u] = new
		nation = uncivilized_minors[u]
		if u == "Zululand":
			zululand(nation, provinces)
		if u == "Mozambique":
			mozambique(nation, provinces)
		if u == "Tanzania":
			tanzania(nation, provinces)
		if u == "Kenya":
			kenya(nation, provinces)
		if u == "Ethiopia":
			ethiopia(nation, provinces)
		if u == "New South Wales":
			new_south_wales(nation, provinces)
		if u == "Queensland":
			queensland(nation, provinces)
		if u == "West Australia":
			west_australia(nation, provinces)
		if u == "South Australia":
			south_australia(nation, provinces)
		if u == "New Zealand":
			new_zealand(nation, provinces)

		i += 1

	for u in unciv_rough:
		new = Uncivilized_minor(u)
		uncivilized_minors[u] = new
		nation = uncivilized_minors[u]
		if u == "Mauritania":
			mauritania(nation, provinces)
		if u == "Liberia":
			liberia(nation, provinces)
		if u == "Mali":
			mali(nation, provinces)
		if u == "Ghana":
			ghana(nation, provinces)
		if u == "Niger":
			niger(nation, provinces)
		if u == "Nigeria":
			nigeria(nation, provinces)
		if u == "Cameroon":
			cameroon(nation, provinces)
		if u == "Angola":
			angola(nation, provinces)
		if u == "Nambia":
			nambia(nation, provinces)
		if u == "Ethiopia":
			ethiopia(nation, provinces)
		if u == "Congo":
			congo(nation, provinces)
		if u == "Madagascar":
			madagascar(nation, provinces)
		i += 1

	print("Players")
	for p, player in players.items():
		print(player.name)


	print("Unvivilized Nations:")
	for unciv in uncivilized_minors.values():
		print(unciv.name)
		for p, prov in unciv.provinces.items():
			print(p, prov.name)

	for p, play in players.items():
		if play.capital == "":
			#x = choice(play.provinces.keys())
			for k, v in play.provinces.items():
				play.capital = play.provinces[k]

	for p, play in players.items():
		for p, prov in play.provinces.items():
			res = prov.resource
			#print("What the fuck are you doing?---------------------------")
			play.resources[res] += prov.quality * 1.5
			#play.capital = play.provinces[x].name
	for p1 in players.values():
		borders = set()
		for p2 in players.values():
			if p1.check_for_border(p2) == True:
				borders.add(p2)
		p1.borders = borders 


	keys = set()
	for k in players.keys():
		keys.add(k)

	pairs = findsubsets(keys, 2)
	
	relations = dict()

	for pair in pairs:
		pair = frozenset(pair)
		relations[pair] = Relation(pair)


	for r, rel in relations.items():
		print(r, rel.relata)

	relations[frozenset({"England", "India"})].relationship = -2.5
	relations[frozenset({"England", "France"})].relationship = -1.25
	relations[frozenset({"England", "Italy"})].relationship = 1
	relations[frozenset({"England", "Ottoman"})].relationship = 1
	relations[frozenset({"England", "Russia"})].relationship = -1
	relations[frozenset({"England", "Persia"})].relationship = 1.25
	relations[frozenset({"England", "Egypt"})].relationship = -1.25
	relations[frozenset({"England", "Spain"})].relationship = 0.75
	relations[frozenset({"England", "Germany"})].relationship = -0.5
	relations[frozenset({"France", "Algeria"})].relationship = -1.5
	relations[frozenset({"France", "Germany"})].relationship = -1.75
	relations[frozenset({"France", "Russia"})].relationship = 1.5
	relations[frozenset({"France", "Spain"})].relationship = 1
	relations[frozenset({"France", "Dia Dam"})].relationship = -1
	relations[frozenset({"France", "India"})].relationship = 0.5
	relations[frozenset({"France", "Italy"})].relationship = -0.75
	relations[frozenset({"France", "Ottoman"})].relationship = 0.5
	relations[frozenset({"Italy", "Libya"})].relationship = -1.0
	relations[frozenset({"Germany", "Austria"})].relationship = 2
	relations[frozenset({"Germany", "Italy"})].relationship = 1
	relations[frozenset({"Germany", "Russia"})].relationship = -0.75
	relations[frozenset({"Germany", "Ottoman"})].relationship = 1
	relations[frozenset({"Austria", "Russia"})].relationship = -0.5
	relations[frozenset({"Austria", "Italy"})].relationship = -1
	relations[frozenset({"Russia", "Ottoman"})].relationship = -1
	relations[frozenset({"China", "Russia"})].relationship = -1
	relations[frozenset({"Spain", "Philippines"})].relationship -1



	#for r, rel in relations.items():
	#	print(r, rel.relata)


	market = Market()

	globe = Globe()

	initial = {
		"players" : players, 
		"provinces": provinces, 
		"relations": relations, 
		"uncivilized_minors": uncivilized_minors,
		"market": market,
		"globe": globe,
	 }

	return initial

		





		




























