# Scenario 
from player_class import*

def.historical():

	def england(player):
		
		player.artillry["artillery"] = 0
		player.military["frigates"] = 2.0
		player.colonization = 1.0
		player.diplo_action = 1.0

		SouthEastEngland = Province("SouthEastEngland", "food", 1.2, "civilized", "England")
		player.provinces["SouthEastEngland"] = SouthEastEngland
		SouthWestEngland = Province("SouthWestEngland", "food", 1.0, "England")
		player.provinces["SouthWestEngland"] = SouthWestEngland
		Midlands = Province("Midlands", "iron", 1.1, "England")
		player.provinces["Midlands"] = Midlands
		Whales = Province("Whales", "coal", 1.1, "England" )
		player.provinces["whales"] = Whales
		NorthEngland = Province("England5", "coal", 1,2, "England")
		player.provinces["NorthEngland"] = NorthEngland
		Ireland = Province("Ulster", "food", 1.1, "Ireland")
		player.provinces["Ireland"] = Ireland
		Scotland = Province("Scotand", "coal", 1.3, "Scotand")
		player.provinces["Scotland"] = Scotland


	def france(player):

		#FRANCE
		WestFrance = Province("WestFrance", "cotton", 1.0, "France")
		player.provinces["WestFrance"] = WestFrance
		EastFrance = Province("EastFrance", "coal", 0.8, "France" )
		player.provinces["EastFrance"] = EastFrance
		NorthFrance = Province("NorthFrance", "iron", 1.0, "France")
		player.provinces["NorthFrance"] = NorthFrance
		CentralFrance = Province("CentralFrance", "wood", 0.9, "France")
		player.provinces["CentralFrance"] = CentralFrance
		SouthWestFrance = Province("SouthWestFrance", "food", 1.3, "France")
		player.provinces["SouthWestFrance"] = SouthWestFrance
		SouthEastFrance = Province("SouthEastFrance", "food", 1.4, "France")
		player.provinces["SouthEastFrance"] = SouthEastFrance
		Normandy = Province("Normandy", "dyes", 0.65, "France")
		player.provinces["Normandy"] = Normandy

		player.borders.add("Germany")
		player.borders.add("Netherlands")
		player.borders.add("Italy")
		player.borders.add("Spain")

	def germany(player):

		player.military["frigates"] = 0
		player.military["cavalry"] = 2

		player.midPOP["bureaucrats"]["number"] = 0
		player.midPOP["officers"]["number"] = 0
		player.colonization = 0

		player.borders.add("France")
		player.borders.add("Demark")
		player.borders.add("Austria")
		player.borders.add("Russia")
		player.borders.add("Netherlands")

		EastPrussia = Province("EastPrussia", "food", 1.0, "Germany")
		player.provinces["EastPrussia"] = EastPrussia
		Brandenburg = Province("Brandenburg", "iron", 1.1, "Germany")
		player.provinces["Brandenburg"] = Brandenburg
		Rhineland = Province("Rhineland", "coal", 1.4, "Germany")
		player.provinces["Rhineland"] = Rhineland
		EastPoland = Province("EastPoland", "food", 0.9, "Poland")
		player.provinces["EastPoland"] = EastPoland
		Saxony = Province("Saxony", "coal", 1.1, "Germany")
		player.provinces["Saxony"] = Saxony
		NorthGermany = Province("NorthGermany", "food", 1.1, "Germany")
		player.provinces["NorthGermany"] = NorthGermany
		Bavaria = Province("Bavaria", "wood", 1.1, "Germany")
		player.provinces["Bavaria"] = Bavaria

	def austria(player):
		player.military["frigates"] = 0
		player.military["cavalry"] = 2
		player.colonization = 0

		player.add.borders("Germany")
		player.add.borders("Russia")
		player.add.borders("Italy")
		player.add.borders("Ottoman")

		Bohemia = Provice("Bohemia", "iron", 1.25, "Check")
		player.provinces["Bohemia"] = Bohemia
		Slovakia  = Province("Slovakia ", "coal", 1.1, "Slovack")
		player.provinces["Slovakia"] = Slovakia
		Austria = Province("Austria", "food", 1.1, "Austria")
		player.provinces["Austria"] = Austria
		Hungry = Province("Hungry", "food", 1.1, "Hungry")
		player.provinces["Hungary"] = Hungary
		Romania = Province("Romania", "oil", 0.75, "Romania")
		player.provinces["Romaina"] = Romaina
		Croatia = Province("Croatia", "wood", 0.9, "Croatia")
		player.provinces["Croatia"] = Croatia

	def russia(player):
		player.military["frigates"] = 0
		player.military["irregulars"] = 1
		player.colonization = -3 

		player.borders.add("Germany")
		player.borders.add("Austria")
		player.borders.add("Ottoman")
		player.borders.add("Persia")
		player.borders.add("Afghanistan")
		player.borders.add("China")

		player.midPOP["bureaucrats"] = 0
		player.midPOP["officers"] = 0
		player.midPOP["artists"] = 0
		player.midPOP["researchers"] = 0

		player.POP = 8
		player.numMidPOP = 0
		player.numLowerPOP = 8
		player.freePOP = 7

		Poland = Province("Poland", "food", 1.0, "Poland")
		player.provinces["Poland"] = Poland
		Ukraine = Province("Ukraine", "food", 1.3, "Ukraine")
		player.provinces["Ukraine"] = Ukraine
		Crimeria = Province("Crimeria", "coal", 1.0, "Russia")
		player.provinces["Crimeria"] = Crimeria
		Kazack = Province("Kazack", "cotton", 0.75, "Kazack")
		player.provinces["Kazack"] = Kazack
		Novgorod = Province("Novgorod", "food", 0.75, "Russia")
		player.provinces["Novgorod"] = Novgorod
		Moskva = Province("Moskva", "wood", 1.0, "Russia")
		player.provinces["Muskva"] = Muskva
		Galich = Province("Galich", "wood", 0.75, "Russia")
		player.provinces["Galich"] = Galich
		Tartaria = Province("Tartaria", "food", 0.65, "Russia")
		player.provinces["Tartaria"] = Tartaria
		Ural = Province("Ural", "iron", 1.3, "Russia")
		player.provinces["Ural"] = Ural
		Perm = Province("Perm", "wood", 0.75, "Russia")
		player.provinces["Perm"] = Perm
		Caucasia = Province("Caucasia", "oil", 1.25, "Russia")
		player.provinces["Caucasia"] = Caucasia
		Tomsk = Province("Tomsk", "coal", 0.8, "Russia")
		player.provinces["Tomsk"] = Tomsk
		Yakutsk = Province("Yakutsk", "wood", 0.75, "Russia")
		player.provinces["Yakutsk"] = Yakutsk
		Georgia = Province("Georgia", "cotton", 0.8, "Georgia")
		player.provinces["Ceorgia"] = Georgia
		Finland = Province("Finland", "wood", 1.0, "Finland")
		player.provinces["Finland"] = Finland



	def italy(player): #major
		player.military["artillery"] = 0
		player.milPOP = 0.8
		
		player.POP = 6.55
		player.numLowerPOP = 5.55
		player.freePOP = 4

		player.research = -1

		player.borders.add("France")
		player.borders.add("Austria")

		player.midPOP["officers"] = 0
		player.numMidPOP = 0.75
	
		Two_Sicilies = Province("Two_Sicilies", "food", 1.1, "Italy")
		player.provinces["Two_Sicilies"] = Two_Sicilies
		Lazio = Province("Lazio", "food", 1.0, "Italy")
		player.provinces["Lazio"] = Lazio
		Sardinia_Piedmont = Province("Sardinia_Piedmont", "food", 1.2, "Italy")
		player.provinces["Sardinia_Piedmont"] = Sardinia_Piedmont
		Venezia = Province("Venezia", "cotton", 1.2, "Italy")
		player.provinces["Venezia"] = Venezia
		Emilia = Province("Emilia", "iron", 0.85, "Italy")
		player.provinces["Emilia"] = Emilia


	def ottoman(player):  #Old Empire

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

		Bosina = Province("Bosina", "food", 0.8, "Bosina")
		player.provinces["Bosina"] = Bosina
		Bulgaria = Province("Bulgaria," "wood", 0.75, "Bulgaria")
		player.provinces["Bulgaria"] = Bulgaria
		Serbia = Province("Serbia", "wood", 0.75, "Serbia")
		player.provinces["Serbia"] = Serbia
		Greece = Province("Greece", "food", 1.0, "Greece")
		player.provinces["Greece"] = Greece
		EastTurky = Province("EastTurky", "food", 1.1, "Ottoman")
		player.provinces["EastTurky"] = EastTurky
		CentralTurky = Province("CentralTurky", "cotton", 1.0, "Ottoman")
		player.provinces["CentralTurky"] = CentralTurky
		WestTurky = Province("WestTurky", "iron", 0.9, "Ottoman")
		player.provinces["WestTurky"] = WestTurky
		Syria = Province("Syria", "food", 0.75, "Arab")
		player.provinces["Syria"] = Syria
		Iraq = Province("Iraq", "oil", 1.2, "Arab")
		player.provinces["Iraq"] = Iraq

		player.colonization = -1

	def spain(player): #Old Empire

		player.military["irregulars"] = 2
		player.military["infantry"]	= 1	
 		player.colonization = 0 
 		player.frigates = 1
		
 		player.POP = 6
		player.numLowerPOP = 6
		player.freePOP = 5

		player.numMidPOP = 0

		player.borders.add("France")
		player.borders.add("Portugal")

		Castilla = Province("Castilla", "iron", 1.2. "Spain")
		player.provinces["Castilla"] = Castilla
		Galicia = Province("Galicia", "coal", 0.9, "Spain")
		player.provinces["Galicia"] = Galicia
		Catalonia = Province("Catalonia", "food", 1.1, "Spain")
		player.provinces["Catalonia"] = Catalonia
		Aragon = Province("Aragon", "iron", 1.1, "Spain")
		player.provinces["Aragon"] = Aragon
		Valencia = Province("Valencia", "food", 0.8, "Spain")
		player.provinces["Valencia"] = Valencia

	def netherlands(player): # major power

		player.military["artillery"] = 0
		player.midPOP["officers"] = 0
		player.o

		player.POP = 5.55
		player.freePOP = 4
		player.milPOP = 0.8
		player.numLowerPOP = 4.8
		player.numMidPOP = 0.75

		Holland = Province("Holland", "food", 1.2, "Netherlands")
		player.provinces["Holland"] = Holland
		Gelderland = Province("Gelderland", "coal", 1.0, "Netherlands")
		player.provinces["Gelderland"] = Gelderland
		Wallonie = Province("Wallonie", "iron", 1.1, "Netherlands")
		player.provinces["Wallonie"] = Wallonie


	def portugal(player): # old_minor
		#Portugal
		Portugal = Province("Portugal", "food", 1.1, "Portugal")

		player.borders.add("Spain")
		player.provinces["Portugal"] = Portugal


	def sweeden(player): # adv minor
		#Sweeden
		player.midPOP["researchers"]["number"] = 0.25
		player.numMidPOP = 0.25
		player.POP = 3.85
		player.freePOP = 3

		player.borders.add("Russia")
		player.borders.add("Norway")

		Svealand = Province("Svealand", "iron", 1.6, "Sweeden")
		player.provinces["Svealand"] = Svealand
		Norrland = Province("Norrland", "wood", 1.0, "Sweeden")
		player.provinces["Norrland"] = Norrland
		Ostlandet = Province("Ostlandet", "food", 0.85, "Sweeden")
		player.provinces["Ostlandet"] = Ostlandet


	def norway(player): #ad minor
		Norway = Province("Norway", "wood", 1.0, "Norway")
		player.provinces["Norway"] = Norway
		player.borders.add("Sweeden")

	def denmark(player): #adv minor
		Denmark = Province("Denmark", "food", 1.1, "Denmark")
		player.provinces["Denmark"] = Denmark

		player.borders.add("Germany")
	
	def egypt(player): # Old minor
		#Egypt
	
		player.POP = 4.6
		player.freePOP = 4
	
		UpperEgypt = Province("UpperEgypt", "cotton", 1.3, "Arab")
		player.provinces["UpperEgypt"] = UpperEgypt
		MiddleEgypt = Province("MiddleEgypt", "food", 1.0, "Arab")
		player.provinces["MiddleEgypt"] = MiddleEgypt
		LowerEgypt = Province("LowerEgypt", "cotton", 0.8, "Arab")
		player.provinces["LowerEgypt"] = LowerEgypt
		Sudan = Province("Sudan", "rubber", 0.8, "Sudan")
		player.provinces["Sudan"] = Sudan

		player.borders.add("Ottoman")
		player.borders.add("Ethiopia")
		player.borders.add("Libya")



	def algeria(player): #old minor

		Algiers = Province("Algiers", "food", 0.8, "Arab")
		player.provinces["Algiers"] = Algiers
		Constantine = Province("Constatnine", "iron", 1.3, "Arab")
		player.provinces["Constatnine"] = Constatnine

		player.borders.add("Morocco")
		player.borders.add("Tunisia")

	def morocco(player): # old minor
		#Morocco
		Morocco = Province("Morocco", "food", 0.9, "Arab")
		player.provinces["Morocco"] = Morocco
		South_Morocco = Province("South_Morocco", "gold", 0.9, "Arab")
		player.provinces["South_Morocco"] = South_Morocco

		player.borders.add("Algeria")
		player.borders.add("Mauritania")

	def tunisia(player): #old minor
		Tunis = Province("Tunis", "cotton", 0.8, "Arab")
		player.provinces["Tunis"] = Tunis

		player.borders.add("Libya")
		player.borders.add("Algeria")


	def libya(player): #old minor
		Libya = Province("Libya", "oil", 1.0, "Arab")
		player.provinces["Libya"] = Libya

		player.borders.add("Egypt")
		player.borders.add("Tunisia")


	def persia(player): # Old Empire

		player.POP = 5
		player.freePOP = 4

		Khuzestan = Province("Khuzestan", "oil", 1.2, "Persia")
		Fars = Province("Fars", "food", 1.0, "Persia")
		Luristan = Province("Luristan", "cotton", 0.8, "Persia")
		Isfahan = Province("Isfahan", "iron", 1.0, "Persia")
		Khorasan = Province("Khorasan", "coal", 0.75, "Persia")

		#Nejd
		Nejd = Province("Nejd", "oil", 1.4, "Arab")

		#Abu Dhabi
		Abu_Dhabi = Province("Abu_Dhabi", "oil", 1.2, "Arab")

		#Oman
		Oman = Province("Oman", "spice", 0.75, "Arab")

		#Yemen
		Yemen = Province("Yemen", "food", 0.65, "Arab")

		#Afghanistan
		Afghanistan = Province("Afghanistan", "food", 0.8, "Afghanistan")


		#India
		Punjab = Province("Punjab", "cotton", 1.0, "India")
		Bengal = Province("Bengal", "dyes", 1.0, "India")
		United_Provinces = Province("United Provinces", "food", 1.0, "India")
		Rajputana = Province("Rajputana", "cotton", 0.9, "India")
		Central_India = Province("Central_India", "dyes", 1.1, "India")
		Hyderabad = Province("Hyderabad", "cotton", 1.2, "India")
		Bombay = Province("Hyderabad", "food", 1.25, "India")
		Ceylon = Province("Ceylon", "spice", 1.1, "India")

		#Burma 
		Burma = Province("Burma", "wood", 1.0, "Burma")

		#Siam 
		Bangkok = Province("Bangkok", "wood", 0.9, "Siam")
		Laos = Province("Loas", "food", 1.2, "Siam")

		#Dai_Nam
		North_Dai_Nam = Province("North_Dai_Nam", "food", 1.25, "Dai_Nam")
		South_Dai_Nam = Province("South_Dai_Nam", "Spice", 1.1, "Dai_Nam")

		#Cambodia
		Cambodia = Province("Cambodia", "rubber", 1.1, "Cambodia")
		#Maluku
		Maluku = Province("Maluku", "spice", 1.1, "Maluku")

		#Singapore
		Singapore = Province("Singapore", "rubber", 1.1, "Singapore")

		Brunei = Province("Brunei", "oil", 0.8, "Brunei ")


		#Liberia 
		Liberia = Province("Liberia", "rubber", 0.9, "Liberia") 

		#Java
		Java = Province("Java", "spice", 1.1, "Java")

		#Malaysia 
		Malaysia = Province("Malaysia", "rubber", 1.0, "Malaysia ")
		Sumatra = Province("Su,atra", "oil", 0.75, "Sumatra")

		#Borneo 
		Borneo = Province("Borneo", "oil", 0.75, "Borneo")

		#Sulawesi
		Sulawesi = Province("Sulawesi", , 0.85, "Sulawesi")

		#Philippines
		NorthPhilippines = Province("NorthPhilippines", "food", 1.1, "Philippines")
		SouthPhilippines = Province("SouthPhilippines", "iron", 0.75, "Philippines")


		#China
		Manchuria = Province("Manchuria", "coal", 0.85, "China")
		Guangxi = Province("Guangxi", "cotton", 1,0, "China")
		Guangdong = Province("Guangdong", "wood", 0.85, "China")
		Hunan = Province("Hunan", "cotton", 0.9, "China")
		Mongolia = Province("Mongolia", "food", 0.7, "Mongolia")
		Jiangsu = Province("Jiangsu", "food", 1.2, "China")
		Jiangxi = Province("Jiangxi", "wood", 0.8, "China")
		Qinghai = Province("Qinghai", "coal", 0.75, "China")
		Shandong = Province("food", "food", 1.2, "China")
		Shanxi = Province("Shanxi", "coal", 0.85, "China")
		Sichuan = Province("Sichuan", "spice", 1.0, "China")
		Zhejiang = Province("Zhejiang", "wood", 0.9, "China")
		Zhili = Province("Zhili", "iron", 0.8, "China")

		#Korea
		Pyongyang = Province("Pyongyang", "coal", 1.3, "Korea")
		Sariwon = Province("Sariwon", "iron", 1.2, "Korea")
		Seoul = Province("Seoul", "food", 1.2 "Korea")

		#Japan
		Tohoku = Province("Tohoku", "iron", 0.85, "Japan")
		Chugoku_Shikoku = Province("cotton", 1.1. "Japan")
		Chubu = Province("Chubu", "food", 1.0, "Japan")
		Kanto = Province("Kanto", "food", 1.2, "Japan")
		Kyushu = Province("Kyushu", "coal", 1.0, "Japan")

		#Mauritania 
		Mauritania = Province("Mauritania", "food", 0.8, "Arab")

		#Senegal 
		Senegal = Province("Senegal", "food", 1.1, "Senegal")

		Mali = Province("Mali", "food", 0.7, "Mali")

		#Nigeria
		Nigeria = Province("Nigeria", 1.2, "Nigeria")
		NigerDelta = Province("NigerDelta", "coal", 1.0, "Nigeria")

		#Ethiopia
		Ethiopia = Province("Ethiopia", "food", 0.8, "Ethiopia")

		#
		Somaliland = Province("Somaliland", "food", 0.9, "Somaliland")

		Guinea = Province("Guinea", "food", 0.8, "Guinea")

		#Liberia 
		Liberia = Province("Liberia", "rubber", 0.9, "Liberia")

		#Ivory_Coast 
		Ivory_Coast = Province("Ivory_Coast", "spice", 0.8, "Ivory_Coast")

		Ghana = Province("Ghana", "food", 0.85, "Ghana")

		Cameroon = Province("Cameroon", "wood", 1.0, "Cameroon")

		Gabon = Province("Gabon", "wood", 0.8, "Gabon")

		Congo = Province("Congo", "rubber", 0.8, "Congo")


		Angola = Province("Angola", "iron", 0.65, "Angola")

		Zambia = Province("Zambia", "food", 0.8, "Zambia")

		Uganda = Province("Uganda", "cotton", 0.8, "Uganda")

		Kenya = Province("Kenya", "spice", 0.7, "Kenya")

		Zanzibar = Province("Zanzibar", "food", 0.8, "Zanzibar")

		Lourenco_Marques = Province("Lourenco_Marques", "food", 0.75, "Lourenco_Marques")

		Mocambique = Province("Mocambique", "iron", 0.75, "Mocambique")

		#Zululand
		Cape = Province("cape", "gold", 1.0, "Zululand")
		Zululand = Province("Zululand", "food", 1.0, "Zululand")

		Madagascar = Province("Madagascar", "wood", 0.8, "Madagascar")

		New_South_Wales = Province("New_South_Wales", "food", 0.9, "Aboriginal")
		South_Australia = Province("South_Australia", "cotton", 0.85, "Aboriginal")
		West_Australia = Province("West_Australia", "gold", 1.0, "Aboriginal")
		Queensland = Province("Queensland", "food", 0.8, "Aboriginal")

		New_Zealand = Province("New_Zealand", "cotton", 0.85, "Aboriginal")




























	def england(player):

		player.stability = 1.0
		player.AP = 2
		player.POP = 6.8
		player.freePOP = 6
		player.milPOP = 0.6
		player.numLowerPOP = 5.0



		player.technologies.add("pre_industry_2")
		player.technologies.add("high_pressure_steam_engine")

		player.midPOP["researchers"]['number'] = 0.0
		player.midPOP["officers"]['number'] = 0.0
		player.midPOP["bureaucrats"]['number'] = 0.0
		player.midPOP["artists"]['number'] = 0.0
		player.midPOP["managers"]['number'] = 0.0

		player.numMidPOP = 0.0

		player.resources["gold"] = 12.0
		player.resources["spice"] = 0.0

		player.goods["clothing"] = 0.0
		player.goods["paper"] = 0.0
		player.goods["cannons"] = 1.0
		player.goods["furniture"] = 0.0

		player.military["infantry"] = 2.0
		player.military["cavalry"] = 1.0
		player.military["frigates"] = 1.0

		player.number_units = 4.0
		player.colonization = 0.5
		player.new_development = 1.0



