# Scenario 
from player_class import*
from Scenario_provinces import*
from technologies import*


def get_name_from_major_choice(choice):
	if choice == "1":
		name = "England"
	if choice == "4":
		name == "Germany"
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
	return name

def get_name_from_minor_choice(choice):
	if choice == "1":
		name = "Netherlands"
	if choice == "2":
		name = "Sweden"
	if choice = "3":
		name = "Portugal"
	if choice = "4":
		name = "Norway"

def.historical():

	players = dict()
	i = 1

	modern_major = ["England", "France", "Russia", "Germany", "Austria", "Ottoman", "Italy", "Spain", "Netherlands"]
	modern_minors = ["Sweden", "Portugal", "Norway"]
	old_empires = ["China", "India", "Japan", "Persia"]
	old_minors = ["Korea", "Egypt", "Algeria", "Morocco", "Kazakhstan", "Philippines", "Dia Dam", "Siam", "Malaysia" \
	"Brunei", "Tunisia", "Libya", "Nejid", "Afghanistan", "Bengal", "Hyderabad", "Burma", "Cambodia", "Brunei" "Sulawesi"]
	unciv = ["Mozambique", "Tanzania", "Kenya", "Ethiopia", "New South Whales", "Queensland", "West Australia",
	"South Australia", "New Zealand", "Zululand"]
	unciv_rough = ["Mauritania", "Liberia", "Mali", "Ghana", "Niger", "Nigeria", "Cameroon", "Angola", "Nambia", \
	"Congo"] 

	print("How many nations are to be controlled by human players? \n")
	num_humans = input()
	human_choices = []
	for i in range(num_humans):
		print("What sort of nation will the first player be?")
		print("Choose from: (1) modern major, (2) modern minor, (3) old_minor")
		kind = input()
		if kind == "1":
			print("Which Great Power will player " + i + " control? \n")
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
				england(player)
			if choice == "4":
				player.germany(player)
			if choice == "2":
				france(player)
			if choice == "3":
				russia(player)
			if choice == "5":
				austria(player)
			if choice == "6":
				italy(player)
			if choice == "7":
				ottoman(player)
			if choice == "8":
				spain(player)
			human_choices.append(name)
		if kind == "2":
			print("Which Minor Modern nation will player " + i + " control? \n")
			count = 1
			for m in modern_minors:
				print("%s: %s" % (count, m))
				count += 1
			choice = input()
			name = get_name_from_minor_choice(choice)
			new = Human(choice, "minor", i)
			players[name] = new
			player = players[name]
			initialize_modern_minor(player)
			if choice == "1":
				netherlands(player)
			if choice == "2":
				sweden(player)
			if choice = "3":
				portugal(player)
			if choice = "4":
				norway(player)
			human_choices.append(name)

		if kind == "3":
			print("This feature is not yet implemented")

	
	print("Initializing AI Players....\n")
	i = num_humans
	for m in major_powers:
		if m not in human_choices:
			new = AI(m, "major", i)
			players[m] = new
			player = players[m]
			initialize_major_power(player)
			if player.name == "England":
				england(player)
			if player.name == "Germany":
				player.germany(player)
			if player.name == "France":
				france(player)
			if player.name == "Russia":
				russia(player)
			if player.name == "Austria":
				austria(player)
			if player.name == "Italy":
				italy(player)
			if player.name == "Ottoman":
				ottoman(player)
			if player.name == "Spain":
				spain(player)
			i += 1
	for m in minor_powers:
		if m not in human_choices:
			new = AI(m, "minor", i)
			players[m] = new
			player = players[m]
			initialize_modern_minor(player)
			if player.name == "Netherlands":
				netherlands(player)
			if player.name == "Sweden":
				sweden(player)
			if player.name = "Portugal":
				portugal(player)
			if player.name = "Norway":
				norway(player)
			i +=1

	for e in old_empires:
		if e not in human_choices:
			new = AI(e, "old_empire", i)
			players[e] = new
			player = players[e]
			initialize_oldemp(player)
			if player.name = "China":
				china(player)
			if player.name = "India":
				india(player)
			if player.name = "Persia":
				persia(player)
			if player.name = "Japan":
				japan(player)
			i += 1

	for o in old_minors:
		if o not in human_choices:
			new = AI(e, "old_minor", i)
			player[o] = new
			initialize_old_minor(player)
			if player.name == "Korea":
				korea(player)
			if player.name == "Egypt":
				egypt(player)
			if player.name == "Algeria":
				algeria(player)
			if player.name == "Morocco":
				morocco(player)
			if player.name == "Kazakhstan":
				kazakhstan(player)
			if player.name == "Philippines":
				philippines(player)
			if player.name == "Dai Dam"
				dai_dam(player)
			if player.name == "Siam":
				siam(player)
			if player.name == "Malaysia":
				malaysia(player)
			if player.name == "Brunei":
				brunei(player)
			if player.name == "Tunisia":
				tunisia(player)
			if player.name == "Libya":
				libya(player)
			if player.name == "Nejid":
				nejd(player)
			if player.name == "Afghanistan":
				afghanistan(player)
			if player.name == "Bengal":
				bengal(player)
			if player.name == "Hyderabad":
				hyderabad(player)
			if player.name == "Burma":
				burma(player)
			if player.name == "Cambodia":
				cambodia(player)
			if player.name == "Brunei":
				brunei(player)
			if player.name = "Sulawesi":
				sulawesi(player)

	for u in unciv:
		new = Uncivilized_minor_rough(u)
		uncivilized_minors[u] = new
		nation = uncivilized_minors[u]
		if u == "Zululand":
			zululand(nation)
		if u = "Mozambique":
			mozambique(nation)
		if u == "Tanzania":
			tanzania(nation)
		if u == "Kenya":
			kenya(nation)
		if u == "Ethiopia":
			ethiopia(nation)
		if u == "New South Whales":
			new_south_whales(nation)
		if u == "Queensland":
			queensland(nation)
		if u == "West Australia":
			west_australia(nation)
		if u == "South Australia":
			south_australia(nation)
		if u == "New Zealand"
			new_zealand(nation)

		i += 1

	for u in unciv_rough:
		new = Uncivilized_minor_rough(u)
		uncivilized_minors[u] = new
		nation = uncivilized_minors[u]
		if u == "Mauritania":
			mauritania(nation)
		if u == "Liberia":
			liberia(nation)
		if u == "Mali":
			mali(nation)
		if u == "Ghana":
			ghana(nation)
		if u == "Niger":
			niger(nation)
		if u == "Nigeria":
			nigeria(nation)
		if u == "Cameroon":
			cameroon(nation)
		if u == "Angola":
			angola(nation)
		if u == "Nambia":
			nambia(nation)
		if u == "Ethiopia":
			ethiopia(nation)
		if u == "Congo":
			congo(nation)
	

		i += 1


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

	market = Market()

	initial = {
		"players" : players, 
		"provinces": provinces, 
		"relations": relations, 
		"uncivilized_minors": uncivilized_minors,
		"market": market
	 }

		


		unciv = ["Mauritania", "Liberia", "Mali", "Ghana", "Niger", "Nigeria", "Cameroon", "Angola", "Nambia", "Zululand", \
	"Mozambique", "Tanzania", "Kenya", "Ethiopia", "Congo", "New South Whales", "Queensland", "West Australia",
	"South Australia", "New Zealand" ]

	def england(player, provinces):

		player.technologies.add("pre_industry_2")
		player.technologies.add("pre_industry_3")
		player.technologies.add("high_pressure_steam_engine")
		player.culture = "English"
		player.accpted_cultures.add("Scottish")
		player.capital = "SouthEastEngland"
		player.artillry["artillery"] = 0
		player.military["frigates"] = 2.0
		player.colonization = 1.0
		player.diplo_action = 1.0

		player.provinces["SouthEastEngland"] = provinces["SouthEastEngland"]
		player.provinces["SouthWestEngland"] = provinces["SouthWestEngland"]
		player.provinces["Midlands"] = provinces["Midlands"]
		player.provinces["whales"] = provinces["Whales"]
		player.provinces["NorthEngland"] = provinces["NorthEngland"]
		player.provinces["Scotland"] = provinces["Scotland"]
		player.provinces["Ireland"] = provinces["Ireland"]


	def france(player, provinces):

		player.culture = French
		player.capital = CentralFrance
		player.technologies.add("pre_industry_2")
		player.technologies.add("pre_industry_3")

		player.provinces["Loire"] = provinces["Loire"] 
		player.provinces["Champagne"] = provinces["Champagne"]
		player.provinces["Brittany"] = provinces["Brittany"]
		player.provinces["CentralFrance"] = provinces["CentralFrance"]
		player.provinces["Aquitaine"] = provinces["Aquitaine"]
		player.provinces["Alps"] = provinces["Alps"]
		player.provinces["Normandy"] = provinces["Normandy"]


	def germany(player, provinces):

		player.culture = "German"
		player.capital = "Brandenburg"
		player.technologies.add("pre_industry_2")
		player.technologies.add("pre_industry_3")

		player.military["frigates"] = 0
		player.military["cavalry"] = 2

		player.midPOP["manangers"]["number"] = 0
		player.midPOP["officers"]["number"] = 0.5
		player.colonization = 0

	
		player.provinces["EastPrussia"] = provinces["EastPrussia"]
		player.provinces["Brandenburg"] = provinces["Brandenburg"]
		player.provinces["Rhineland"] = provinces["Rhineland"]
		player.provinces["WestPoland"] = provinces["WestPoland"]
		player.provinces["Saxony"] = provimces["Saxony"]
		player.provinces["NorthGermany"] = provinces["NorthGermany"]
		player.provinces["Bavaria"] = provinces["Bavaria"]

	def austria(player, provinces):

		player.culture = "German"
		player.accepted_cultures = {"Check", "Hungarian" }
		player.capital = "Austria"
		player.technologies.add("pre_industry_2")

		player.military["frigates"] = 0
		player.military["cavalry"] = 2
		player.colonization = 0

		player.provinces["Bohemia"] = provinces["Bohemia"]
		player.provinces["Slovakia"] = provinces["Slovakia"]
		player.provinces["Austria"] = provinces["Austria"]
		player.provinces["Hungary"] = provinces["Hungary"]
		player.provinces["Romania"] = provinces["Romania"]
		player.provinces["Croatia"] = provinces["Croatia"]
		player.provinces["EastUkraine"] = provinces["EastUkraine"]


	def russia(player, provinces):

		player.culture = "Russian"
		player.capital = "Novgorod"

		player.technologies.add("pre_industry_2")

		player.military["frigates"] = 0
		player.military["irregulars"] = 1
		player.colonization = -3 

		player.midPOP["bureaucrats"] = 0
		player.midPOP["officers"] = 0
		player.midPOP["artists"] = 0
		player.midPOP["researchers"] = 0

		player.POP = 8
		player.numMidPOP = 0
		player.numLowerPOP = 8
		player.freePOP = 7

		player.provinces["Poland"] = provinces["Poland"]
		player.provinces["Ukraine"] = provinces["Ukraine"]
		player.provinces["Crimea "] = provinces["Crimea"] 
		player.provinces["Novgorod"] = provinces["Novgorod"]
		player.provinces["Muskva"] = provinces["Muskva"]
		player.provinces["Galich"] = provinces["Galich"]	
		player.provinces["Caucasia"] = provinces["Caucasia"]	
		player.provinces["Tartaria"] = provinces["Tartaria"]	
		player.provinces["Kazen"] = provinces["Kazen"]
		player.provinces["Samara"] = provinces["Samara"]	
		player.provinces["Perm"] = provinces["Perm"]
		player.provinces["Ural"] = provinces["Ural"]
		player.provinces["Tomsk"] = provinces["Tomsk"]
		player.provinces["CentralSiberia"] = CentralSiberia
		player.provinces["Irkutsk"] = provinces["Irkutsk"]
		player.provinces["Yakutsk"] = provinces["Yakutsk"]
		player.provinces["Okhotsk"] = provinces["Okhotsk"]
		player.provinces["Finland"] = ["Finland"]


	def italy(player, provinces): #major

		player.culture = "Italian"
		player.capital = "Lazio"

		player.technologies.add("pre_industry_2")

		player.military["artillery"] = 0
		player.milPOP = 0.8
		
		player.POP = 6.55
		player.numLowerPOP = 5.55
		player.freePOP = 4

		player.research = -1


		player.midPOP["officers"] = 0
		player.numMidPOP = 0.75
	
		player.provinces["Naples"] = provinces["Naples"]
		player.provinces["Lazio"] = provinces["Lazio"]
		player.provinces["Sardinia_Piedmont"] = provinces["Sardinia_Piedmont"]	
		player.provinces["Venezia"] = provinces["Venezia"]	
		player.provinces["Sicily"] = provinces["Sicily"]


	def ottoman(player, provinces):  #Old Empire

		player.culture = "Turkish"
		player.capital = "WestTurky"

		player.military["irregulars"] = 3
		player.military["infantry"]	= 1	
 		player.colonization = -3 

 		player.POP = 6
		player.numLowerPOP = 6
		player.freePOP = 5

		player.numMidPOP = 0

		player.borders.add("Austria")
		player.borders.add("Russia")
		player.borders.add("Egypt")
		player.borders.add("Nejd")
		player.borders.add("Persia")

		player.provinces["Bosnia"] = provinces["Bosnia"]
		player.provinces["Bulgaria"] = provinces["Bulgaria"]
		player.provinces["Serbia"] = provinces["Serbia"]
		player.provinces["Greece"] = provinces["Greece"]
		player.provinces["WestTurky"] = provinces ["WestTurky"]	
		player.provinces["CentralTurky"] = provinces["CentralTurky"]
		player.provinces["EastTurky"] = provinces["EastTurky"]
		player.provinces["Syria"] = provinces["Syria"]	
		player.provinces["Iraq"] = provinces["Iraq"]

		player.colonization = -1

	def spain(player, provinces): 

		player.culture = "Spanish"
		player.capital = "Leon"

		player.technologies.add("pre_industry_2")

		player.military["irregulars"] = 2
		player.military["infantry"]	= 1	
 		player.colonization = 0 
 		player.frigates = 1
		
 		player.POP = 6
		player.numLowerPOP = 6
		player.freePOP = 5

		player.numMidPOP = 0

		player.provinces["Andalusia"] = provinces["Andalusia"]
		player.provinces["Leon"] = provinces["Leon"]
		player.provinces["Aragon"] = provinces["Aragon"]	
		player.provinces["Galicia"] = provinces["Galicia"]
		player.provinces["La_Mancha"] = provinces["La_Mancha"]
	

	def netherlands(player, provinces): # major power

		player.culture = "Dutch"
		player.capital = "Holland"
		player.technologies.add("pre_industry_2")


		player.military["artillery"] = 0
		player.midPOP["officers"] = 0

		player.POP = 5.55
		player.freePOP = 4
		player.milPOP = 0.8
		player.numLowerPOP = 4.8
		player.numMidPOP = 0.75

		player.provinces["Holland"] = provinces["Holland"]
		player.provinces["Gelderland"] = provinces["Gelderland"]
		player.provinces["Wallonie"] = provinces["Wallonie"]


	def portugal(player, provinces): # old_minor
		#Portugal
		player.culture = "Portuguese"
		player.technologies.add("pre_industry_2")

		player.borders.add("Spain")
		player.provinces["Portugal"] = provinces["Portugal"]


	def Sweden(player, provinces): # adv minor
		#Sweden
		player.capital = "Ostlandet"
		player.culture = "Swedish"
		player.technologies.add("pre_industry_2")


		player.midPOP["researchers"]["number"] = 0.25
		player.numMidPOP = 0.25
		player.POP = 3.85
		player.freePOP = 3

		
		player.provinces["Svealand"] = provinces["Svealand"]
		player.provinces["Norrland"] = provinces["Norrland"]
		player.provinces["Ostlandet"] = provinces["Ostlandet"]


	def norway(player, provinces): #ad minor
		player.culture = "Norwegian"
		player.provinces["Norway"] = provinces["Norway"]
		player.technologies.add("pre_industry_2")

		
		player.borders.add("Sweden")

	def denmark(player, provinces): #adv minor
		player.culture = "Danish"
		player.technologies.add("pre_industry_2")

		player.provinces["Denmark"] = provinces["Denmark"]

	
	def egypt(player, provinces): # Old minor
		#Egypt
		player.culture = "Arab"
		player.capital = "UpperEgypt"
		player.POP = 4.6
		player.freePOP = 4
	
		
		player.provinces["UpperEgypt"] = provinces["UpperEgypt"]
		player.provinces["MiddleEgypt"] = provinces["MiddleEgypt"]
		player.provinces["Sudan"] = provinces["Sudan"]

	

	def algeria(player, provinces): #old minor

		player.capital = "Algiers"
		player.culture = "Arab"

		player.provinces["Algiers"] = provinces["Algiers"]
		player.provinces["Constantine"] = provinces["Constantine"]


	def morocco(player, provinces): # old minor
		#Morocco
		player.culture = "Arab"
	
		player.provinces["Morocco"] = provinces["Morocco"]
		player.provinces["South_Morocco"] = provinces["South_Morocco"]


	def tunisia(player, provinces): #old minor
		player.culture = "Arab"
	
		player.provinces["Tunis"] = provinces["Tunis"]

	def libya(player, provinces): #old minor
		player.culture = "Arab"
	
		player.provinces["Libya"] = provinces["Libya"]

	def kazakhstan (player, provinces) #old minor
		player.culture = "Kazak"

		player.provinces["WestKazakhstan"] = provinces["WestKazakhstan"]
		player.provinces["EastKazakhstan"] = provinces["EastKazakhstan"]


	def persia(player, provinces): # Old Empire
		player.culture = "Persian"
		player.capital = "Tehran"

		player.POP = 5
		player.freePOP = 4

		player.provinces["Khuzestan"] = provinces["Khuzestan"]	
		player.provinces["Fars"] = provinces["Fars"]
		player.provinces["Tehran"] = provinces["Tehran"]
		player.provinces["Isfahan"] = provinces["Isfahan"]
		player.provinces["Khorasan"] = provinces["Khorasan"]

	
	def nejd(player, provinces): #old minor
		player.culture = "Arab"

		player.provinces["Nejd"] = provinces["Nejd"]


	def afghanistan(player, provinces):
		player.culture = "Afghan"
	
		player.provinces[Afghanistan] = provinces["Afghanistan"]


	def india(player, provinces): # Old Empire

		player.culture = "Indian"
		player.capital = "Central_India"
 		player.colonization = -3 

 		player.POP = 10
		player.numLowerPOP = 10
		player.freePOP = 9

		player.numMidPOP = 0
	
		player.provinces["Punjab"] = provinces["Punjab"]
	
		player.provinces["United Provinces"] = provinces["United_Provinces"]
		
		player.provinces["Rajputana"] = provinces["Rajputana"]
		
		player.provinces["Central_India"] = provinces["Central_India"]
		
		player.provinces["Bombay"] = provinces["Bombay"]
		
		player.provinces["Madres"] = provinces["Madres"]
		
		player.provinces["Nagpur"] = provinces["Nagpur"]


	def bengal(player, provinces):
		player.culture = "Indian"
	
		player.provinces["Bengal"] = provinces["Bengal"]

	def hyderabad(player, provinces):
		player.culture = "Indian"

		player.provinces["Hyderabad"] = provinces["Hyderabad"]
		#Burma 
	def burma(player, provinces):
		player.culture = "Bamar"
1
		player.provinces["Burma"] = provinces["Burma"]

	def siam(player, provinces): 
		player.capital = "Bangkok"
		player.culture = "Thai"

		player.provinces["Bangkok"] = provinces["Bangkok"]
		player.provinces["Laos"] = provinces["Laos"]
		Laos.x = 10
		Laos.y = 22
	def dai_dam(player, provinces):
		player.capital = "North_Dai_Nam"
		player.culture = "Vietnamese"

		player.provinces[North_Dai_Nam] = provinces["North_Dai_Nam"]
		player.provinces["South_Dai_Nam"] = provinces["South_Dai_Nam"]

	def cambodia(player, provinces):
		player.culture = "Cambodian"
		player.provinces["Cambodia"] = provinces["Cambodia"]

		#Singapore
		#Singapore = Province("Singapore", "rubber", 1.1, "Singapore")
	def brunei(player, provinces):
		culture = "Brunei"
	
		player.provinces["Brunei"] = provinces["Brunei"]

	def java(player, provinces):
		player.culture = "Javanese"
		player.provinces["Java"] = provinces["Java"]

	def malaysia(player, provinces): 
		player.culture = "Malaysian"
		player.capital = "Malaysia"
		
		player.provinces["Malaysia"] = provinces["Malaysia"]
		
		player.provinces["Sumatra"] = provinces["Sumatra"]


	def	sulawesi(player, provinces):
		player.culture = "Sulawesi"
		player.provinces["Sulawesi"] = provinces["Sulawesi"]


	def philippines(player, provinces):
		player.culture = "Filipino"
		player.capital = "NorthPhilippines"
		
		player.provinces["NorthPhilippines"] = provinces["SouthPhilippines"]
		player.provinces["SouthPhilippines"] = SouthPhilippines["SouthPhilippines"]


	def china(player, provinces):
		player.capital = "Liaoning"
		player.culture = "Chinese"

		player.military["irregulars"] = 5
		player.milPOP = 1.2
		player.POP = 11.2
		player.freePOP = 10


		player.provinces["Manchuria"] = provinces["Manchuria"]

		player.provinces["Guangxi"] = provinces["Guangxi"]

		player.provinces["Guangdong"] = provinces["Guangdong"]

		player.provinces["Hunan"] = provinces["Hunan"]

		player.provinces["Mongolia"] = provinces["Mongolia"]

		player.provinces["Jiangsu"] = provinces["Jiangsu"]
		
		player.provinces["Qinghai"] = provinces["Qinghai"]
	
		player.provinces["Shanxi"] = provinces["Shanxi"]
		
		player.provinces["Sichuan"] = provinces["Sichuan"]
	
		player.provinces["Zhejiang"] = provinces["Zhejiang"]
	
		player.provinces["Liaoning"] = provinces["Liaoning"]


	def korea(player, provinces):
		player.culture = "Korean"
		player.capital = "Pyongyang"
		
		player.provinces["Pyongyang"] = provinces["Pyongyang"]
		player.provinces["Sariwon"] = provinces["Sariwon"]
		player.provinces["Seoul"] = provinces["Seoul"]

	def Japan(player, provinces): 

		player.POP = 7
		player.freePOP = 6

		player.capital = "Kansai"
		
		player.provinces["Kansai"] = provinces["Kansai"]
		
		player.provinces["Tohoku"] = provinces["Tohoku"]
	
		player.provinces["Chugoku"] = provinces["Chugoku"]
	
		player.provinces["Kanto"] = provinces["Kanto"]
	
		player.provinces["Kyushu"] = provinces["Kyushu"]




	def mauritania(player, provinces):
		player.culture = "Arab" 
		player.provinces["Mauritania"] = provinces["Mauritania"]

	def liberia(player, provinces): 
		player.culture = "Kpelle"
		player.provinces["Liberia"] = provinces["Liberia"]


	def mali(player, provinces):
		player.culture = "Bambara"
		player.provinces["Mali"] = provinces["Mali"]

	def ghana(player, provinces):
		player.culture = "Akan"
		player.provinces["Ghana"] = provinces["Ghana"]

	def niger(player, provinces):
		player.culture = "Hausa"
		player.provinces["Niger"] = provinces["Niger"]

	def nigeria(player, provinces):
		player.culture = "Hausa"

		player.provinces["Nigeria"] = provinces["Nigeria"]

	def cameroon(player, provinces):
		player.culture = "Cameroon"
	
		player.provinces["Cameroon"] = provinces["Cameroon"]

	def angola(player, provinces):
		player.culture = "Ovimbundu"
	
		player.provinces["Angola"] = provinces["Angola"]

	def nambia(player, provinces):
		player.culture = "Bantu"
		player.provinces["Nambia"] = provinces["Nambia"]

	def zululand(player, provinces):
		player.capital = Zululand
		player.culture = "Zulu"


		player.provinces["Cape"] = provinces["Cape"]
		player.provinces["Zululand"] = provinces["Zululand"]

	def mozambique(player, provinces):
		player.culture = "Bantu"
		player.provinces["Mozambique"] = provinces["Mozambique"]

	def tanzania(player, provinces):
		player.culture = "Sukuma"

		player.provinces["Tanzania"] = provinces["Tanzania"]

	def kenya(player, provinces):
		player.culture = "Bantu"
		player.provinces["Kenya"] = provinces["Kenya"]

	def ethiopia(player, provinces):
		player.culture = "Oromo"
	
		player.provinces["Ethiopia"] = provinces["Ethiopia"]

	def congo(player, provinces):
		player.culture = "Bantu"

		player.provinces["Congo"] = provinces["Congo"]

	def madagascar(player, provinces):
		player.culture = "Merina"
	
		player.provinces["Madagascar"] = provinces["Madagascar"]


	def new_south_whales(player, provinces):
		player.culture = "Aboriginal"
	
		player.provinces["New South Whales"] = provinces["New_South_Wales"]

	def queensland(player, provinces):
		player.culture = "Aboriginal"

		player.provinces["Queensland"] = provinces["Queensland"]

	def south_australia(player, provinces):
		player.culture = "Aboriginal"
	
		player.provinces["South Australia"] = provinces["South_Australia"]

	def west_australia(player, provinces):
		player.culture = "Aboriginal"

		player.provinces["West Australia"] = provinces["West_Australia" ]

	def new_zealand(player, provinces):
		player.culture = "Aboriginal"
		player.provinces["New Zealand"] = provinces["New Zealand"]



		































