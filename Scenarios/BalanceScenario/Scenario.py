# Scenario 
from player_class import*
#from technologies import*
from start import*
#from ScenarioNations import*
from random import*
from Scenarios.BalanceScenario.ScenarioNations import*
from Scenarios.BalanceScenario.Scenario_provinces import*


def balance(human_player):

	provinces = create_provinces()

	for p in provinces.values():
		p.position = str(p.x) + " " + str(p.y)


	players = dict()
	i = 1

	modern_major = ["Bambaki", "Hyle", "Trope", "Sidero", "Isorropia", "Karbouno"]
	old_empires = []
	modern_minors = ["Situs", "Hythen", "Intero", "Kora", "Southo", "Cindra", "Estos", "Lian", "Bulgo" ]
	old_minors = ["Kaygree", "Kish", "Rabus", "Sparko", "Argos", "Mancha", "Gelder", "Porta", "Norra", \
	"Wego", "Arbaca", "Egaro"]


	print("human_player: %s" % human_player)
	new = Human(human_player, "major", i)
	players[human_player] = new
	player = players[human_player]
	initialize_major_power(player)
	if player.name == "Bambaki":
		bambaki(player, provinces)
	if player.name == "Hyle":
		hyle(player, provinces)
	if player.name == "Trope":
		trope(player, provinces)
	if player.name == "Sidero":
		sidero(player, provinces)
	if player.name == "Isorropia":
		isorropia(player, provinces)
	if player.name == "Karbouno":
		karbouno(player, provinces)
	i += 1


	
	print("Initializing AI Players....\n")
	for m in modern_major:
		if m != human_player:
			new = AI(m, "major", i)
			players[m] = new
			player = players[m]
			initialize_major_power(player)
			if player.name == "Bambaki":
				bambaki(player, provinces)
			if player.name == "Hyle":
				hyle(player, provinces)
			if player.name == "Trope":
				trope(player, provinces)
			if player.name == "Sidero":
				sidero(player, provinces)
			if player.name == "Isorropia":
				isorropia(player, provinces)
			if player.name == "Karbouno":
				karbouno(player, provinces)


		
			i += 1
	for m in modern_minors:
		if m != human_player:
			new = AI(m, "civ_minor", i)
			players[m] = new
			player = players[m]
			initialize_modern_minor(player)
			if player.name == "Situs":
				situs(player, provinces)
			if player.name == "Hythen":
				hythen(player, provinces)
			if player.name == "Intero":
				intero(player, provinces)
			if player.name == "Kora":
				kora(player, provinces)
			if player.name == "Southo":
				southo(player, provinces)
			if player.name == "Cindra":
				cindra(player, provinces)
			if player.name == "Estos":
				estos(player, provinces)
			if player.name == "Lian":
				lian(player, provinces)
			if player.name == "Bulgo":
				bulgo(player, provinces)


			i +=1

	for o in old_minors:
		if o != human_player:
			new = AI(o, "old_minor", i)
			players[o] = new
			player = players[o]
			initialize_old_minor(player)
			if player.name == "Kaygree":
				kaygree(player, provinces)
			if player.name == "Kish":
				kish(player, provinces)
			if player.name == "Rabus":
				rabus(player, provinces)
			if player.name == "Sparko":
				sparko(player, provinces)
			if player.name == "Argos":
				argos(player, provinces)
			if player.name == "Mancha":
				mancha(player, provinces)
			if player.name == "Gelder":
				gelder(player, provinces)
			if player.name == "Porta":
				porta(player, provinces)
			if player.name == "Norra":
				norra(player, provinces)
			if player.name == "Wego":
				wego(player, provinces)
			if player.name == "Arbaca":
				arbaca(player, provinces)
			if player.name == "Egaro":
				egaro(player, provinces)
		i += 1

	print("Players")
	for p, play in players.items():
		print(play.name)
		print("Provinces_________________________________________________________")
		for prov in play.provinces.values():
			print(prov.name)


	for p, play in players.items():
		if len(play.capital) == 0:
			provs = list(play.provinces.keys())
			print("%s has %d provinces" % (p, len(play.provinces.keys())))
			cap = choice(list(play.provinces.keys()))
			#for k, v in play.provinces.items():
			play.capital.add(cap)

	for p, play in players.items():
		for p, prov in play.provinces.items():
			res = prov.resource
			#print("What the fuck are you doing?---------------------------")
			play.resources[res] += prov.quality
			#play.capital = play.provinces[x].name
	for p1 in players.values():
		borders = set()
		#print("p1 capital: %s" % (p1.capital))
		for p2 in players.values():
			#print("p2 capital: %s" % (p2.capital))
			if p1.check_for_border(p2, players) == True:
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

	#for r, rel in relations.items():
	#	print(r, rel.relata)

	old_provs = []
	for p, pl in players.items():
		if pl.type == "old_minor":
			for prov in pl.provinces.values():
				old_provs.append(prov.name)


	for p, pl in players.items():
		if pl.type == "major":
			pl.objectives = old_provs

	market = Market()

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

		





		




























