# Scenario 
from player_class import*
from Scenarios.historical.ScenarioNations import*
from Scenarios.historical.Scenario_provinces import*

from technologies import*
from start import*
#from ScenarioNations import*

from random import*

modern_major = ["England", "France", "Russia", "Germany", "Austria", "Italy", "Ottoman", "Spain", "Netherlands"]
modern_minors = ["Denmark", "Sweden", "Portugal", "Two Sicilies", "Switzerland", "Saxony", \
"Bavaria", "NorthGermany", "Papal States"]
old_empires = ["China", "India", "Japan", "Persia"]
old_minors = ["Korea", "Egypt", "Algeria", "Morocco", "Kazakhstan", "Philippines", "Dai Nam", "Siam", "Malaysia", \
"Brunei", "Tunisia", "Libya", "Nejd", "Afghanistan", "Bengal", "Hyderabad", "Burma", "Cambodia", "Bali", "Java"]
#unciv = ["Mozambique", "Tanzania", "Kenya", "Ethiopia", "New South Whales", "Queensland", "West Australia",
#"South Australia", "New Zealand", "Zululand"]
#unciv_rough = ["Mauritania", "Liberia", "Mali", "Ghana", "Niger", "Nigeria", "Cameroon", "Angola", "Nambia", \
#"Congo", "Madagascar"] 

def get_nation_choices():
	return(modern_major, modern_minors, old_empires, old_minors)


def historical(human_player):

	provinces = create_provinces()

	for p in provinces.values():
		p.position = str(p.x) + " " + str(p.y)
		#print(p.position)

	players = dict()
	i = 1
	print("human_player: %s" % human_player)
	if human_player in modern_major:
		new = Human(human_player, "major", i)
		players[human_player] = new
		player = players[human_player]
		initialize_major_power(player)
		if player.name == "England":
			england(player, provinces)
		if player.name == "France":
			france(player, provinces)
		if player.name == "Russia":
			russia(player, provinces)
		if player.name == "Germany":
			germany(player, provinces)
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

	if human_player in modern_minors:
		new = Human(human_player, "minor", i)
		players[human_player] = new
		player = players[human_player]
		initialize_modern_minor(player)
		print("Player name: %s" % player.name)
		if player.name == "Denmark":
			denmark(player, provinces)
		if player.name == "Sweden":
			print("Sweden")
			sweden(player, provinces)
		if player.name == "Portugal":
			portugal(player, provinces)
		if player.name == "Two Sicilies":
			two_sicilies(player, provinces)
		if player.name == "Switzerland":
			switzerland(player, provinces) 

	if human_player in old_empires:
		new = Human(human_player, "old_empire", i)
		players[human_player] = new
		player = players[human_player]
		initialize_oldempire(player)
		if player.name == "China":
			china(player, provinces)
		if player.name == "India":
			india(player, provinces)
		if player.name ==  "Japan":
			japan(player, provinces)
		if player.name == "Persia":
			persia(player, provinces)


	uncivilized_minors = dict()
	

	print("Initializing AI Players....\n")
	for m in modern_major:
		if m != human_player:
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
		if m != human_player:
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
		if e != human_player:
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
		if o != human_player:
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
			if player.name == "Bali":
				bali(player, provinces)
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
			if p1.check_for_border(p2, players) == True:
				borders.add(p2.name)
		p1.borders = borders

	for p in players.values():
		if "professional_armies" in p.technologies:
			p.infantry["attack"] += 0.15
			p.infantry["defend"] += 0.15
			p.infantry["manouver"] += 0.2
			p.cavalry["attack"] += 0.15
			p.cavalry["defend"] += 0.15
			p.cavalry["manouver"] += 0.2
			p.cavalry["recon"] += 0.2
			p.artillery["attack"] += 0.15
			p.artillery["defend"] += 0.15
			p.frigates["attack"] += 0.2

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

	relations[frozenset({"Switzerland", "France"})].relationship = 2
	relations[frozenset({"Switzerland", "Netherlands"})].relationship = 2
	relations[frozenset({"Switzerland", "Germany"})].relationship = 2
	relations[frozenset({"Switzerland", "England"})].relationship = 2
	relations[frozenset({"Switzerland", "Italy"})].relationship = 1.2
	relations[frozenset({"Switzerland", "Austria"})].relationship = 1.2
	relations[frozenset({"Switzerland", "Russia"})].relationship = 1
	relations[frozenset({"Switzerland", "Spain"})].relationship = 0.5
	relations[frozenset({"Switzerland", "Sweden"})].relationship = 1


	
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
	players["Italy"].CB["Austria"] = new4
	players["Italy"].CB["Papal States"] = new5
	#players["Italy"].CB.add(new6)
	#players["Italy"].CB.add(new7)

	new6 = CB("England", "India", "annex", "Rajputana", 18)


	#for r, rel in relations.items():
	#	print(r, rel.relata)


	market = Market()

	market_items = dict()

	market.modern_major = modern_major
	market.modern_minors = modern_minors
	market.old_empires = old_empires
	market.old_minors = old_minors
		

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
	if player.name in ["Germany", "Italy", "Austria", "Russia", "Ottoman"]:
		player.general_priority = "army"
	else:
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




		




























