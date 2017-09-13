from minor_classes import*
	

def create_provinces():

	provinces = {}
	
	SouthEastEngland = Province("SouthEastEngland", "England", "food", 1.1, "civilized", "English")
	SouthEastEngland.x = 3
	SouthEastEngland.y = 4
	provinces["SouthEastEngland"] = SouthEastEngland
	
	SouthWestEngland = Province("SouthWestEngland", "England", "wood", 1.0, "civilized", "English")
	SouthWestEngland.x = 3
	SouthWestEngland.y = 5
	provinces["SouthWestEngland"] = SouthWestEngland
	
	Midlands = Province("Midlands", "England", "iron", 1.0,  "civilized", "English")
	Midlands.x = 2
	Midlands.y = 5
	provinces["Midlands"] = Midlands

	Whales = Province("Whales", "England", "iron", 1.0,  "civilized", "English" )
	Whales.x = 2
	Whales.y = 4
	provinces["Whales"] = Whales
	
	NorthEngland = Province("NorthEngland", "England", "coal", 1.1, "civilized", "English")
	NorthEngland.x = 1
	NorthEngland.y = 5
	provinces["NorthEngland"] = NorthEngland


	Scotland = Province("Scotland", "England", "coal", 1.0, "civilized", "Scottish")
	Scotland.x = 1
	Scotland.y = 4
	provinces["Scotland"] = Scotland

	Ireland = Province("Ireland", "England", "food", 1.0, "civilized", "Irish")
	Ireland.x = 2
	Ireland.y = 2
	provinces["Ireland"] = Ireland

	
	Champagne = Province("Champagne", "France", "iron", 1.0, "Champagne", "French" )
	Champagne.x = 6
	Champagne.y = 6
	Champagne.ocean = False
	provinces["Champagne"] = Champagne
	
	Brittany = Province("Brittany", "France", "food", 1.0, "civilized", "French")
	Brittany.x = 6 
	Brittany.y = 4
	provinces["Brittany"] = Brittany
	

	CentralFrance = Province("CentralFrance", "France", "wood", 1.1, "civilized", "French")
	CentralFrance.x = 7
	CentralFrance.y = 6
	CentralFrance.ocean = False
	provinces["CentralFrance"] = CentralFrance
	
	Aquitaine = Province("Aquitaine", "France", "food", 1.3, "civilized", "French")
	Aquitaine.x = 8
	Aquitaine.y = 5
	provinces["Aquitaine"] = Aquitaine
	
	Alps = Province("Alps", "France", "cotton", 1.0, "civilized", "French")
	Alps.x = 8
	Alps.y = 6
	provinces["Alps"] = Alps
	
	Normandy = Province("Normandy", "France", "food", 1.0, "civilized", "French")
	Normandy.x = 6
	Normandy.y =5
	provinces["Normandy"] = Normandy

	Loire = Province("Loire", "France", "coal", 1.0, "civilized", "French")
	Loire.x = 7
	Loire.y = 5
	provinces["Loire"] = Loire


	EastPrussia = Province("EastPrussia", "Germany", "food", 1.0, "civilized", "German")
	EastPrussia.x = 5
	EastPrussia.y =10
	provinces["EastPrussia"] = EastPrussia
	
	Brandenburg = Province("Brandenburg", "Germany", "iron", 1.1, "civilized", "German")
	Brandenburg.x =5
	Brandenburg.y = 9
	Brandenburg.ocean = False
	provinces["Brandenburg"] = Brandenburg
	
	Rhineland = Province("Rhineland", "Germany", "coal", 1.4, "civilized", "German")
	Rhineland.x = 6
	Rhineland.y = 7
	Rhineland.ocean = False
	provinces["Rhineland"] = Rhineland
	
	WestPoland = Province("WestPoland", "Germany", "food", 0.95, "civilized", "Polish")
	WestPoland.x = 6
	WestPoland.y = 9
	WestPoland.ocean = False
	provinces["WestPoland"] = WestPoland
	
	Saxony = Province("_Saxony", "Saxony", "coal", 1.1, "civilized", "German")
	Saxony.x = 6
	Saxony.y = 8
	Saxony.ocean = False
	provinces["_Saxony"] = Saxony
	
	NorthGermany = Province("_NorthGermany", "NorthGermany", "food", 1.1, "civilized", "German")
	NorthGermany.x = 5
	NorthGermany.y = 8
	provinces["_NorthGermany"] = NorthGermany
	
	Bavaria = Province("_Bavaria", "Bavaria", "wood", 1.2, "civilized", "German")
	Bavaria.x = 7
	Bavaria.y = 8
	Bavaria.ocean = False
	provinces["_Bavaria"] = Bavaria


	Bohemia = Province("Bohemia", "Austria", "iron", 1.25, "civilized", "Check")
	Bohemia.x = 7
	Bohemia.y = 9
	Bohemia.ocean = False
	provinces["Bohemia"] = Bohemia

	Slovakia  = Province("Slovakia", "Austria", "coal", 1.1, "civilized", "Slovakian")
	Slovakia.x = 7
	Slovakia.y = 10
	Slovakia.ocean = False
	provinces["Slovakia"] = Slovakia

	
	Austria = Province("_Austria", "Austria", "food", 1.2, "civilized", "German")
	Austria.x = 8
	Austria.y = 9
	Austria.ocean = False
	provinces["_Austria"] = Austria

	
	Hungary = Province("Hungary", "Austria", "food", 1, "civilized", "Hungarian")
	Hungary.x = 8
	Hungary.y = 11
	Hungary.ocean = False
	provinces["Hungary"] = Hungary
	
	Romania = Province("Romania", "Ottoman", "oil", 0.75, "civilized", "Romanian")
	Romania.x = 8
	Romania.y = 12
	Romania.ocean = False
	provinces["Romania"] = Romania

	
	Croatia = Province("Croatia", "Austria", "wood", 1.0, "civilized", "Croatian")
	Croatia.x = 8
	Croatia.y = 10
	provinces["Croatia"] = Croatia

	WestUkraine = Province("WestUkraine", "Austria", "food", 1.1, "civilized", "Ukrainian")
	WestUkraine.x = 7
	WestUkraine.y = 11
	WestUkraine.ocean = False
	provinces["WestUkraine"] = WestUkraine

	Poland = Province("_Poland", "Russia", "food", 1.0, "civilized", "Polish")
	Poland.x = 6
	Poland.y = 10
	Poland.ocean = False
	provinces["_Poland"] = Poland

	Baltic = Province("Baltic", "Russia", "food", 0.8, "civilized", "Baltic")
	Baltic.x = 5
	Baltic.y = 11
	Baltic.ocean = True
	provinces["Baltic"] = Baltic


	Ukraine = Province("Ukraine", "Russia", "food", 1.3, "civilized", "Ukraine")
	Ukraine.x = 6
	Ukraine.y = 11
	Ukraine.ocean = False
	provinces["Ukraine"] = Ukraine

	Crimea  = Province("Crimea", "Russia", "coal", 1.1, "civilized", "Russian")
	Crimea.x = 6
	Crimea.y =12  
	provinces["Crimea"] = Crimea 
	
	Novgorod = Province("Novgorod", "Russia", "food", 0.85, "civilized", "Russian")
	Novgorod.x = 4
	Novgorod.y = 11
	provinces["Novgorod"] = Novgorod
	
	Moskva = Province("Moskva", "Russia", "wood", 1.1, "civilized", "Russian")
	Moskva.x = 6
	Moskva.y = 13
	Moskva.ocean = False
	provinces["Moskva"] = Moskva
	
	Galich = Province("Galich", "Russia", "wood", 0.75, "civilized", "Russian")
	Galich.x = 7
	Galich.y = 14
	Galich.ocean = False
	provinces["Galich"] = Galich
	
	Caucasia = Province("Caucasia", "Russia", "oil", 1.3, "civilized", "Russian")
	Caucasia.x = 8
	Caucasia.y = 15
	Caucasia.ocean = False
	provinces["Caucasia"] = Caucasia
	
	Tartaria = Province("Tartaria", "Russia", "food", 0.55, "civilized", "Russian")
	Tartaria.x = 9
	Tartaria.y = 16
	Tartaria.ocean = False
	provinces["Tartaria"] = Tartaria
	
	Kazen = Province("Kazen", "Russia", "cotton", 0.7, "civilized", "Russian")
	Kazen.x = 8
	Kazen.y = 17
	Kazen.ocean = False
	provinces["Kazen"] = Kazen

	Samara = Province("Samara", "Russia", "iron", 0.7, "civilized", "Russian")
	Samara.x = 8
	Samara.y = 18
	Samara.ocean = False
	provinces["Samara"] = Samara
	
	Perm = Province("Perm", "Russia", "wood", 0.85, "civilized", "Russian")
	Perm.x = 8
	Perm.y = 19
	Perm.ocean = False
	provinces["Perm"] = Perm

	Ural = Province("Ural", "Russia", "iron", 1.25, "civilized", "Russian")
	Ural.x = 8
	Ural.y = 20
	Ural.ocean = False
	provinces["Ural"] = Ural
	
	Tomsk = Province("Tomsk", "Russia", "coal", 1.0, "civilized", "Russian")
	Tomsk.x = 8
	Tomsk.y = 21
	Tomsk.ocean = False
	provinces["Tomsk"] = Tomsk

	CentralSiberia = Province("CentralSiberia", "Russia", "wood", 0.65, "uncivilized", "Siberian")
	CentralSiberia.x = 7
	CentralSiberia.y = 22
	CentralSiberia.ocean = False
	provinces["CentralSiberia"] = CentralSiberia


	Irkutsk = Province("Irkutsk", "Russia", "wood", 0.65, "uncivilized", "Siberian")
	Irkutsk.x = 6
	Irkutsk.y = 23
	Irkutsk.ocean = False
	provinces["Irkutsk"] = Irkutsk


	Yakutsk = Province("Yakutsk", "Russia", "gold", 0.75, "uncivilized", "Siberian")
	Yakutsk.x = 5
	Yakutsk.y = 24
	Yakutsk.ocean = False
	provinces["Yakutsk"] = Yakutsk

	Okhotsk = Province("Okhotsk", "Russia", "food", 0.5, "uncivilized", "Siberian")
	Okhotsk.x = 5
	Okhotsk.y = 25
	provinces["Okhotsk"] = Okhotsk

	Finland = Province("Finland", "Russia", "wood", 1.1, "civilized", "Finish")
	Finland.x = 3
	Finland.y = 11
	provinces["Finland"] = Finland

	Naples = Province("Naples", "Two Sicilies", "food", 1.1, "civilized", "Italian")
	Naples.x = 10
	Naples.y = 8
	provinces["Naples"] = Naples
	Lazio = Province("Lazio", "Papal States", "food", 1.0, "civilized", "Italian")
	Lazio.x = 9
	Lazio.y = 8
	provinces["Lazio"] = Lazio
	Piedmont  = Province("Piedmont", "Italy", "iron", 1.0, "civilized", "Italian")
	Piedmont .x = 8
	Piedmont .y = 7
	provinces["Piedmont"] = Piedmont 
	Venezia = Province("Venezia", "Austria", "cotton", 1, "civilized", "Italian")
	Venezia.x = 8
	Venezia.y = 8
	provinces["Venezia"] = Venezia
	Sicily = Province("Sicily",  "Two Sicilies", "coal", 1.0, "civilized", "Italian")
	Sicily.x = 11
	Sicily.y = 7
	provinces["Sicily"] = Sicily


	Switzerland = Province("_Switzerland", "Switzerland", "gold", 1.2, "civilized", "Swiss")
	Switzerland.x = 7
	Switzerland.y = 7
	provinces["_Switzerland"] = Switzerland
	Switzerland.ocean = False


	Bosnia = Province("Bosnia", "Ottoman", "food", 0.8, "civilized", "Bosnian")
	Bosnia.x =9
	Bosnia.y =19
	provinces["Bosnia"] = Bosnia

	Bulgaria = Province("Bulgaria", "Ottoman", "wood", 0.8, "civilized", "Bulgarian")
	Bulgaria.x = 9
	Bulgaria.x = 12
	provinces["Bulgaria"] = Bulgaria

	Serbia = Province("Serbia", "Ottoman", "wood", 0.85, "civilized", "Serbian")
	Serbia.x = 9
	Serbia.y = 11
	provinces["Serbia"] = Serbia
	Greece = Province("Greece", "Ottoman", "food", 1.0, "civilized", "Greek")
	Greece.x =11
	Greece.y = 11
	provinces["Greece"] = Greece
	WestTurky = Province("WestTurky", "Ottoman", "iron", 1.0, "civilized", "Turkish")
	WestTurky.x = 10
	WestTurky.y =13
	provinces["WestTurky"] = WestTurky
	CentralTurky = Province("CentralTurky", "Ottoman", "cotton", 0.9, "civilized", "Turkish")
	CentralTurky.x = 10
	CentralTurky.y = 14
	provinces["CentralTurky"] = CentralTurky
	EastTurky = Province("EastTurky", "Ottoman", "food", 1.1, "civilized", "Turkish")
	EastTurky.x = 10
	EastTurky.y = 15
	EastTurky.ocean = False
	provinces["EastTurky"] = EastTurky

	Syria = Province("Syria", "Ottoman", "food", 0.75, "old", "Arab")
	Syria.x = 11
	Syria.y = 14
	provinces["Syria"] = Syria
	Iraq = Province("Iraq", "Ottoman", "oil", 1.0, "old", "Arab")
	Iraq.x = 12
	Iraq.y = 14
	Iraq.ocean = False
	provinces["Iraq"] = Iraq


	Andalusia = Province("Andalusia", "Spain", "food", 1.0, "civilized", "Spanish")
	Andalusia.x = 11
	Andalusia.y = 5
	provinces["Andalusia"] = Andalusia

	Leon = Province("Leon", "Spain", "iron", 1.2, "civilized", "Spanish")
	Leon.x = 10
	Leon.y = 4
	Leon.ocean = False
	provinces["Leon"] = Leon

	Aragon = Province("Aragon", "Spain", "iron", 1.0, "civilized", "Spanish")
	Aragon.x = 9
	Aragon.y = 5
	provinces["Aragon"] = Aragon
	
	Galicia = Province("Galicia", "Spain", "coal", 1.0, "civilized", "Spanish")
	Galicia.x = 9
	Galicia.y = 4
	provinces["Galicia"] = Galicia
	
	La_Mancha = Province("La_Mancha", "Spain", "food", 1.0, "civilized", "Spanish")
	La_Mancha.x = 10
	La_Mancha.y = 5
	provinces["La_Mancha"] = La_Mancha


	Holland = Province("Holland", "Netherlands", "food", 1.2, "civilized", "Dutch")
	Holland.x = 4
	Holland.y = 7
	provinces["Holland"] = Holland
	Gelderland = Province("Gelderland", "Netherlands", "coal", 1.1, "civilized", "Dutch")
	Gelderland.x = 5
	Gelderland.y = 7
	provinces["Gelderland"] = Gelderland
	Wallonie = Province("Wallonie", "Netherlands", "iron", 1.1, "civilized", "Dutch")
	Wallonie.x = 5
	Wallonie.y = 6
	Wallonie.ocean = False
	provinces["Wallonie"] = Wallonie


	Portugal = Province("_Portugal", "Portugal", "food", 1.2, "civilized", "Portugal")
	Portugal.x = 11
	Portugal.y = 4
	provinces["_Portugal"] = Portugal

	Svealand = Province("Svealand", "Sweden", "iron", 1.6, "civilized", "Swedish")
	Svealand.x = 2
	Svealand.y = 10
	provinces["Svealand"] = Svealand
	Norrland = Province("Norrland", "Sweden", "wood", 0.9, "civilized", "Swedish")
	Norrland.x = 1
	Norrland.y = 10
	provinces["Norrland"] = Norrland
	Ostlandet = Province("Ostlandet", "Sweden", "food", 0.9, "civilized", "Swedish")
	Ostlandet.x = 3
	Ostlandet.y = 10
	provinces["Ostlandet"] = Ostlandet

	Norway = Province("_Norway", "Sweden", "wood", 1.1, "civilized", "Norwegian")
	Norway.x = 2
	Norway.y = 9
	provinces["_Norway"] = Norway

	Denmark = Province("_Denmark", "Denmark", "food", 1.2, "civilized", "Danish")
	Denmark.x = 4
	Denmark.y = 9
	provinces["_Denmark"] = Denmark

	UpperEgypt = Province("UpperEgypt", "Egypt", "cotton", 1.2, "old", "Arab")
	UpperEgypt.x = 13
	UpperEgypt.y = 13
	provinces["UpperEgypt"] = UpperEgypt
	MiddleEgypt = Province("MiddleEgypt", "Egypt", "food", 1.0, "old", "Arab")
	MiddleEgypt.x = 14
	MiddleEgypt.y = 13
	MiddleEgypt.ocean = False
	provinces["MiddleEgypt"] = MiddleEgypt
	#LowerEgypt = Province("LowerEgypt", "Egypt", "cotton", 0.8, "old", "Arab")
	#LowerEgypt.x = 15
	#LowerEgypt.y = 13
	#LowerEgypt.ocean = False
	#provinces["LowerEgypt"] = LowerEgypt
	Sudan = Province("Sudan", "Egypt", "rubber", 1.3, "uncivilized", "Sudanese")
	Sudan.x = 15
	Sudan.y = 13
	Sudan.ocean = False
	provinces["Sudan"] = Sudan

	Algiers = Province("Algiers", "Algeria", "food", 0.8, "old",  "Arab")
	Algiers.x = 13
	Algiers.y = 9
	provinces["Algiers"] = Algiers
	Constantine = Province("Constantine", "Algeria", "iron", 1.2, "old", "Arab")
	Constantine.x = 13
	Constantine.y = 10
	provinces["Constantine"] = Constantine

	Morocco = Province("_Morocco", "Morocco", "food", 0.9, "old", "Arab")
	Morocco.x = 13
	Morocco.y = 8
	provinces["_Morocco"] = Morocco
	South_Morocco = Province("South_Morocco", "Morocco", "gold", 1.0, "old", "Arab")
	South_Morocco.x = 14
	South_Morocco.y = 8
	provinces["South_Morocco"] = South_Morocco

	Tunis = Province("Tunis", "Tunisia", "cotton", 0.7, "old", "Arab")
	Tunis.x = 13
	Tunis.y = 11
	provinces["Tunis"] = Tunis


	Libya = Province("_Libya", "Libya", "food", 0.8, "old", "Arab")
	Libya.x = 13
	Libya.y = 12
	provinces["_Libya"] = Libya


	WestKazakhstan = Province("WestKazakhstan", "Kazakhstan", "cotton", 0.7, "uncivilized", "Kazak")
	WestKazakhstan.x = 9
	WestKazakhstan.y = 17
	WestKazakhstan.ocean = False
	provinces["WestKazakhstan"] = WestKazakhstan
	EastKazakhstan = Province("EastKazakhstan", "Kazakhstan", "food", 0.7, "uncivilized", "Kazak")
	EastKazakhstan.x = 9
	EastKazakhstan.y = 18
	EastKazakhstan.ocean = False 
	provinces["EastKazakhstan"] = EastKazakhstan

	Khuzestan = Province("Khuzestan", "Persia", "oil", 1.0, "old", "Persian")
	Khuzestan.x = 12
	Khuzestan.y = 15
	provinces["Khuzestan"] = Khuzestan
	Fars = Province("Fars", "Persia", "food", 1.0, "old", "Persian")
	Fars.x = 11
	Fars.y = 15
	provinces["Fars"] = Fars
	Tehran = Province("Tehran", "Persia", "cotton", 0.85, "old", "Persian")
	Tehran.x = 10
	Tehran.y = 16
	Tehran.ocean = False
	provinces["Tehran"] = Tehran
	Isfahan = Province("Isfahan", "Persia", "iron", 1.0, "old",  "Persian")
	Isfahan.x = 11
	Isfahan.y = 15
	provinces["Isfahan"] = Isfahan
	Khorasan = Province("Khorasan", "Persia", "coal", 0.9, "old", "Persian")
	Khorasan.x = 11
	Khorasan.y = 16	
	Khorasan.ocean = False
	provinces["Khorasan"] = Khorasan

	Nejd = Province("_Nejd", "Nejd", "oil", 1.1, "old", "Arab")
	Nejd.x = 13
	Nejd.y = 14
	provinces["_Nejd"] = Nejd

	Afghanistan = Province("_Afghanistan", "Afghanistan", "food", 0.8,  "old", "Afghan")
	Afghanistan.x = 9
	Afghanistan.y = 17
	Afghanistan.ocean = False
	provinces["_Afghanistan"] = Afghanistan


	Punjab = Province("Punjab", "India", "cotton", 1.0, "old", "Indian")
	Punjab.x = 10
	Punjab.y = 17
	Punjab.ocean = False
	provinces["Punjab"] = Punjab
	United_Provinces = Province("United_Provinces", "India", "food", 1.4, "old", "Indian")
	United_Provinces.x = 9
	United_Provinces.y = 19
	United_Provinces.ocean = False
	provinces["United_Provinces"] = United_Provinces
	Rajputana = Province("Rajputana", "India", "cotton", 1.0, "old", "Indian")
	Rajputana.x = 10
	Rajputana.y = 18
	provinces["Rajputana"] = Rajputana
	Central_India = Province("Central_India", "India", "dyes", 1.1, "old", "Indian")
	Central_India.x = 10
	Central_India.y = 19
	#Central_India.ocean = False
	provinces["Central_India"] = Central_India
	Bombay = Province("Bombay", "India", "spice", 1.0, "old", "Indian")
	Bombay.x = 12
	Bombay.y = 19
	provinces["Bombay"] = Bombay
	Madres = Province("Madres", "India", "rubber", 1.0, "old", "Indian")
	Madres.x = 13
	Madres.y = 19
	provinces["Madres"] = Madres
	Nagpur = Province("Nagpur", "India", "food", 1.4, "old", "Indian")
	Nagpur.x = 10
	Nagpur.y = 20
	provinces["Nagpur"] = Nagpur

	Bengal = Province("_Bengal", "Bengal", "dyes", 1.0, "old", "Indian")
	Bengal.x = 10
	Bengal.y =21
	provinces["_Bengal"] = Bengal

	Hyderabad = Province("_Hyderabad", "Hyderabad", "cotton", 1.2, "old", "Indian")
	Hyderabad.x = 11
	Hyderabad.y = 19
	provinces["_Hyderabad"] = Hyderabad

	Burma = Province("_Burma", "Burma", "rubber", 1.3, "old", "Bamar")
	Burma.x =11
	Burma.y = 21
	provinces["_Burma"] = Burma

	Bangkok = Province("Bangkok", "Siam", "food", 1.1, "old", "Thai")
	Bangkok.x = 11
	Bangkok.y = 22
	provinces["Bangkok"] = Bangkok

	Laos = Province("Laos", "Siam", "spice", 1.2, "old", "Thia")
	Laos.x = 10
	Laos.y = 22
	Laos.ocean = False
	provinces["Laos"] = Laos

	North_Dai_Nam = Province("North_Dai_Nam", "Dai Nam", "food", 1.2, "old",  "Vietnamese")
	North_Dai_Nam.x = 10
	North_Dai_Nam.y = 23
	provinces["North_Dai_Nam"] = North_Dai_Nam
	South_Dai_Nam = Province("South_Dai_Nam", "Dai Nam", "spice", 1.2, "old", "Vietnamese")
	South_Dai_Nam.x = 11
	South_Dai_Nam.y = 23
	provinces["South_Dai_Nam"] = South_Dai_Nam

	Cambodia = Province("_Cambodia", "Cambodia", "rubber", 1.3, "old", "Cambodian")
	Cambodia.x = 12
	Cambodia.y = 23
	provinces["_Cambodia"] = Cambodia

	Brunei = Province("_Brunei", "Brunei", "oil", 1.0, "old", "Brunei ")
	Brunei.x = 14
	Brunei.y = 25
	provinces["_Brunei"] = Brunei

	Java = Province("_Java", "Java", "spice", 1.3, "old", "Javanese")
	Java.x = 15
	Java.y = 24
	provinces["_Java"] = Java

	Malaysia = Province("_Malaysia", "Malaysia", "rubber", 1.4, "old", "Malaysian")
	Malaysia.x = 13
	Malaysia.y = 22
	provinces["_Malaysia"] = Malaysia
	Sumatra = Province("Sumatra", "Malaysia", "spice", 1.2, "old", "Malaysian")
	Sumatra.x = 15
	Sumatra.y = 22
	provinces["Sumatra"] = Sumatra

	#Singapour = Province("Singapour", "rubber", 1.0, "old", "Malaysian")
	#Singapour.x = 15
	#Singapour.y = 23
	#provinces["Singapour"] = Singapour

	Sulawesi = Province("_Sulawesi", "Sulawesi", "spice", 1.4, "old", "Sulawesi")
	Sulawesi.x = 14
	Sulawesi.y = 28
	provinces["_Sulawesi"] = Sulawesi

	NorthPhilippines = Province("NorthPhilippines", "Philippines", "food", 1.2, "old", "Filipino")
	NorthPhilippines.x = 11
	NorthPhilippines.y = 27
	provinces["NorthPhilippines"] = NorthPhilippines
	SouthPhilippines = Province("SouthPhilippines", "Philippines", "iron", 0.9, "old", "Filipino")
	SouthPhilippines.x = 12
	SouthPhilippines.y = 27
	provinces["SouthPhilippines"] = SouthPhilippines


	Manchuria = Province("Manchuria", "China", "coal", 1.0, "old", "Manchurian")
	Manchuria.x = 6
	Manchuria.y = 26
	provinces["Manchuria"] = Manchuria

	Guangxi = Province("Guangxi", "China", "cotton", 0.9, "old", "Chinese")
	Guangxi.x = 9
	Guangxi.y = 23
	provinces["Guangxi"] = Guangxi

	Guangdong = Province("Guangdong", "China", "food", 1.2, "old", "Chinese")
	Guangdong.x = 9
	Guangdong.y = 24
	provinces["Guangdong"] = Guangdong

	Hunan = Province("Hunan", "China", "cotton", 0.85, "old", "Chinese")
	Hunan.x = 8
	Hunan.y = 23
	Hunan.ocean = False
	provinces["Hunan"] = Hunan

	Mongolia = Province("Mongolia", "China", "wood", 0.65, "old", "Mongolian")
	Mongolia.x = 6
	Mongolia.y = 23
	Mongolia.ocean = False
	provinces["Mongolia"] = Mongolia

	Jiangsu = Province("Jiangsu", "China", "food", 1.2, "old", "Chinese")
	Jiangsu.x = 7
	Jiangsu.y = 24
	provinces["Jiangsu"] = Jiangsu
	
	#Jiangxi = Province("Jiangxi", "wood", 0.8, "China")
	Qinghai = Province("Qinghai", "China", "coal", 1.0, "old", "Chinese")
	Qinghai.x = 7
	Qinghai.y = 22
	Qinghai.ocean = False
	provinces["Qinghai"] = Qinghai
	#Shandong = Province("food", "food", 1.2, "China")
	Shanxi = Province("Shanxi", "China", "coal", 1.0, "old", "China")
	Shanxi.x = 6
	Shanxi.y = 24
	provinces["Shanxi"] = Shanxi
	Sichuan = Province("Sichuan", "China", "spice", 1.0, "old", "Chinese")
	Sichuan.x = 8
	Sichuan.y = 22
	Sichuan.ocean = False
	provinces["Sichuan"] = Sichuan
	Zhejiang = Province("Zhejiang", "China", "wood", 1.1, "old", "Chinese")
	Zhejiang.x = 8
	Zhejiang.y = 24
	provinces["Zhejiang"] = Zhejiang
	Liaoning = Province("Liaoning", "China", "iron", 1.0, "old", "Chinese")
	Liaoning.x = 6
	Liaoning.y = 25
	provinces["Liaoning"] = Liaoning

	Pyongyang = Province("Pyongyang", "Korea", "coal", 1.2, "old",  "Korea")
	Pyongyang.x = 7
	Pyongyang.y = 26
	provinces["Pyongyang"] = Pyongyang
	Sariwon = Province("Sariwon", "Korea", "iron", 1.2, "old",  "Korea")
	Sariwon.x = 7
	Sariwon.y = 27
	provinces["Sariwon"] = Sariwon
	Seoul = Province("Seoul", "Korea", "food", 1.2, "old", "Korea")
	Seoul.x = 8
	Seoul.y = 27
	provinces["Seoul"] = Seoul

	Kansai = Province("Kansai", "Japan", "food", 1.3, "old", "Japanese")
	Kansai.x = 8
	Kansai.y = 29
	provinces["Kansai"] = Kansai
	Tohoku = Province("Tohoku", "Japan", "iron", 1.0, "old", "Japanese")
	Tohoku.x = 6
	Tohoku.y = 29
	provinces["Tohoku"] = Tohoku
	Chugoku = Province("Chugoku", "Japan", "cotton", 1.0,  "old", "Japanese")
	Chugoku.x = 9
	Chugoku.y = 29
	provinces["Chugoku"] = Chugoku
	Kanto = Province("Kanto", "Japan",  "food", 1.1, "old", "Japanese")
	Kanto.x = 7
	Kanto.y = 29
	provinces["Kanto"] = Kanto
	Kyushu = Province("Kyushu", "Japan", "coal", 1.0, "old", "Japanese")
	Kyushu.x = 10
	Kyushu.y = 29
	provinces["Kyushu"] = Kyushu

	

	'''Mauritania = Province("_Mauritania", "food", 0.8, "old", "Arab")
	Mauritania.x = 15
	Mauritania.y = 8
	provinces["_Mauritania"] = Mauritania

	Liberia = Province("_Liberia", "rubber", 0.9, "uncivilized", "Kpelle")
	Liberia.x = 16
	Liberia.y = 8
	provinces["_Liberia"] = Liberia

	Mali = Province("_Mali", "food", 0.75, "uncivilized", "Bambara")
	Mali.x = 15
	Mali.y = 9
	provinces["_Mali"] = Mali

	Ghana = Province("_Ghana", "food", 0.85, "uncivilized", "Akan")
	Ghana.x = 16
	Ghana.y = 9
	provinces["_Ghana"] = Ghana

	Niger = Province("_Niger", "cotton", 0.55, "uncivilized", "Hausa")
	Niger.x = 15
	Niger.y = 10
	Niger.ocean = False
	provinces["_Niger"] = Niger

	Nigeria = Province("_Nigeria", "rubber", 1.2, "uncivilized", "Hausa")
	Nigeria.x = 16
	Nigeria.y =10
	provinces["_Nigeria"] = Nigeria

	Cameroon = Province("_Cameroon", "wood", 1.0, "uncivilized", "Cameroon")
	Cameroon.x = 17
	Cameroon.y = 10
	provinces["_Cameroon"] = Cameroon

	Angola = Province("_Angola", "iron", 0.65, "uncivilized", "Ovimbundu")
	Angola.x = 18
	Angola.y = 10
	provinces["_Angola"] = Angola

	Nambia = Province("_Nambia", "gold", 0.5, "uncivilized", "Bantu")
	Nambia.x = 19
	Nambia.y = 10
	provinces["_Nambia"] = Nambia

	Cape = Province("Cape", "gold", 1.0, "uncivilized", "Zulu")
	Cape.x = 20
	Cape.y = 10
	provinces["Cape"] = Cape
	Zululand = Province("_Zululand", "food", 1.0, "uncivilized", "Zulu")
	Zululand.x = 20
	Zululand.y = 11
	provinces["_Zululand"] = Zululand

	Mozambique = Province("_Mozambique", "iron", 0.75, "uncivilized", "Bantu")
	Mozambique.x = 19
	Mozambique.y = 11
	provinces["_Mozambique"] = Mozambique

	Tanzania = Province("_Tanzania", "food", 1.0, "uncivilized", "Sukuma")
	Tanzania.x = 18
	Tanzania.y = 11
	provinces["_Tanzania"] = Tanzania

	Kenya = Province("_Kenya", "spice", 0.8, "uncivilized", "Bantu")
	Kenya.x = 17
	Kenya.y = 12
	provinces["_Kenya"] = Kenya

	Ethiopia = Province("_Ethiopia", "food", 0.8, "uncivilized", "Oromo")
	Ethiopia.x = 16
	Ethiopia.y = 13
	provinces["_Ethiopia"] = Ethiopia

	Congo = Province("_Congo", "rubber", 0.8, "uncivilized", "Bantu")
	Congo.x = 17
	Congo.y = 11
	Congo.ocean = False
	provinces["_Congo"] = Congo

	Madagascar = Province("_Madagascar", "wood", 0.8, "uncivilized", "Merina")
	Madagascar.x = 19
	Madagascar.y = 13
	provinces["_Madagascar"] = Madagascar

	New_South_Wales = Province("New_South_Wales", "food", 0.9, "uncivilized", "Aboriginal")
	New_South_Wales.x = 18
	New_South_Wales.y = 31
	provinces["New_South_Wales"] = New_South_Wales

	Queensland = Province("Queensland", "food", 0.8, "uncivilized", "Aboriginal")
	Queensland.x = 17
	Queensland.y = 31
	provinces["Queensland"] = Queensland

	South_Australia = Province("South_Australia", "cotton", 0.85, "uncivilized", "Aboriginal")
	South_Australia.x = 18
	South_Australia.y = 30
	provinces["South_Australia"] = South_Australia

	West_Australia = Province("West_Australia", "gold", 1.0, "uncivilized", "Aboriginal")
	West_Australia.x = 17
	West_Australia.y = 30
	provinces["West_Australia"] = West_Australia 

	New_Zealand = Province("_New Zealand", "cotton", 0.8, "uncivilized", "Aboriginal")
	New_Zealand.x = 15
	New_Zealand.y = 32
	provinces["_New Zealand"] = New_Zealand'''

	return provinces