from minor_classes import*
	

def create_provinces():

	provinces = {}
	
	SouthEastEngland = Province("SouthEastEngland", "food", 1.2, "civilized", "English")
	SouthEastEngland.x = 3
	SouthEastEngland.y = 4
	provinces["SouthEastEngland"] = SouthEastEngland
	
	SouthWestEngland = Province("SouthWestEngland", "food", 1.0, "civilized", "English")
	SouthWestEngland.x = 3
	SouthWestEngland.y = 5
	provinces["SouthWestEngland"] = SouthWestEngland
	
	Midlands = Province("Midlands", "iron", 1.1,  "civilized", "English")
	Midlands.x = 2
	Midlands.y = 5
	provinces["Midlands"] = Midlands

	Whales = Province("Whales", "iron", 1.1,  "civilized", "English" )
	Whales.x = 2
	Whales.y = 4
	provinces["Whales"] = Whales
	
	NorthEngland = Province("NorthEngland", "coal", 1.2, "civilized", "English")
	NorthEngland.x = 1
	NorthEngland.y = 5
	provinces["NorthEngland"] = NorthEngland


	Scotland = Province("Scotland", "coal", 1.3, "civilized", "Scottish")
	Scotland.x = 1
	Scotland.y = 4
	provinces["Scotland"] = Scotland

	Ireland = Province("Ireland", "food", 1.1, "civilized", "Irish")
	Ireland.x = 2
	Ireland.y = 2
	provinces["Ireland"] = Ireland

	
	Champagne = Province("Champagne", "iron", 1.0, "Champagne", "French" )
	Champagne.x = 6
	Champagne.y = 6
	Champagne.ocean = False
	provinces["Champagne"] = Champagne
	
	Brittany = Province("Brittany", "food", 1.0, "civilized", "French")
	Brittany.x = 6 
	Brittany.y = 4
	provinces["Brittany"] = Brittany
	

	CentralFrance = Province("CentralFrance", "wood", 1.0, "civilized", "French")
	CentralFrance.x = 7
	CentralFrance.y = 6
	CentralFrance.ocean = False
	provinces["CentralFrance"] = CentralFrance
	
	Aquitaine = Province("Aquitaine", "food", 1.3, "civilized", "French")
	Aquitaine.x = 8
	Aquitaine.y = 5
	provinces["Aquitaine"] = Aquitaine
	
	Alps = Province("Alps", "food", 1.0, "civilized", "French")
	Alps.x = 8
	Alps.y = 6
	provinces["Alps"] = Alps
	
	Normandy = Province("Normandy", "dyes", 0.6, "civilized", "French")
	Normandy.x = 6
	Normandy.y =5
	provinces["Normandy"] = Normandy

	Loire = Province("Loire", "coal", 0.85, "civilized", "French")
	Loire.x = 7
	Loire.y = 5
	provinces["Loire"] = Loire


	EastPrussia = Province("EastPrussia", "food", 1.0, "civilized", "German")
	EastPrussia.x = 5
	EastPrussia.y =10
	provinces["EastPrussia"] = EastPrussia
	
	Brandenburg = Province("Brandenburg", "iron", 1.1, "civilized", "German")
	Brandenburg.x =5
	Brandenburg.y = 9
	Brandenburg.ocean = False
	provinces["Brandenburg"] = Brandenburg
	
	Rhineland = Province("Rhineland", "coal", 1.4, "civilized", "German")
	Rhineland.x = 6
	Rhineland.y = 7
	Rhineland.ocean = False
	provinces["Rhineland"] = Rhineland
	
	WestPoland = Province("WestPoland", "food", 0.9, "civilized", "Polish")
	WestPoland.x = 6
	WestPoland.y = 9
	WestPoland.ocean = False
	provinces["WestPoland"] = WestPoland
	
	Saxony = Province("Saxony", "coal", 1.1, "civilized", "German")
	Saxony.x = 6
	Saxony.y = 8
	Saxony.ocean = False
	provinces["Saxony"] = Saxony
	
	NorthGermany = Province("NorthGermany", "food", 1.1, "civilized", "German")
	NorthGermany.x = 5
	NorthGermany.y = 8
	provinces["NorthGermany"] = NorthGermany
	
	Bavaria = Province("Bavaria", "wood", 1.2, "civilized", "German")
	Bavaria.x = 7
	Bavaria.y = 9
	Bavaria.ocean = False
	provinces["Bavaria"] = Bavaria


	Bohemia = Province("Bohemia", "iron", 1.25, "civilized", "Check")
	Bohemia.x = 7
	Bohemia.y = 10
	Bohemia.ocean = False
	provinces["Bohemia"] = Bohemia

	Slovakia  = Province("Slovakia", "coal", 1.1, "civilized", "Slovakian")
	Slovakia.x = 7
	Slovakia.y = 11
	Slovakia.ocean = False
	provinces["Slovakia"] = Slovakia

	
	Austria = Province("Austria", "food", 1.1, "civilized", "German")
	Austria.x = 7
	Austria.y = 9
	Austria.ocean = False
	provinces["Austria"] = Austria

	
	Hungary = Province("Hungary", "food", 1.1, "civilized", "Hungarian")
	Hungary.x = 8
	Hungary.y = 11
	Hungary.ocean = False
	provinces["Hungary"] = Hungary
	
	Romania = Province("Romania", "oil", 0.75, "civilized", "Romanian")
	Romania.x = 8
	Romania.y = 12
	Romania.ocean = False
	provinces["Romania"] = Romania

	
	Croatia = Province("Croatia", "wood", 1.0, "civilized", "Croatian")
	Croatia.x = 8
	Croatia.y = 10
	provinces["Croatia"] = Croatia

	WestUkraine = Province("WestUkraine", "food", 1.1, "civilized", "Ukrainian")
	WestUkraine.x = 7
	WestUkraine.y = 12
	WestUkraine.ocean = False
	provinces["WestUkraine"] = WestUkraine

	Poland = Province("Poland", "food", 1.0, "civilized", "Polish")
	Poland.x = 6
	Poland.y = 11
	Poland.ocean = False
	provinces["Poland"] = Poland

	Baltic = Province("Baltic", "food", 0.8, "civilized", "Baltic")
	Baltic.x = 5
	Baltic.y = 12
	Baltic.ocean = True
	provinces["Baltic"] = Baltic


	Ukraine = Province("Ukraine", "food", 1.3, "civilized", "Ukraine")
	Ukraine.x = 6
	Ukraine.y = 12
	Ukraine.ocean = False
	provinces["Ukraine"] = Ukraine

	Crimea  = Province("Crimea ", "coal", 1.0, "civilized", "Russian")
	Crimea.x = 7
	Crimea.y =12  
	provinces["Crimea"] = Crimea 
	
	Novgorod = Province("Novgorod", "food", 0.85, "civilized", "Russian")
	Novgorod.x = 4
	Novgorod.y = 12
	provinces["Novgorod"] = Novgorod
	
	Moskva = Province("Moskva", "wood", 1.1, "civilized", "Russian")
	Moskva.x = 6
	Moskva.y = 13
	Moskva.ocean = False
	provinces["Moskva"] = Moskva
	
	Galich = Province("Galich", "wood", 0.75, "civilized", "Russian")
	Galich.x = 6
	Galich.y = 14
	Galich.ocean = False
	provinces["Galich"] = Galich
	
	Caucasia = Province("Caucasia", "oil", 1.25, "civilized", "Russian")
	Caucasia.x = 6
	Caucasia.y = 15
	Caucasia.ocean = False
	provinces["Caucasia"] = Caucasia
	
	Tartaria = Province("Tartaria", "food", 0.55, "civilized", "Russian")
	Tartaria.x = 6
	Tartaria.y = 16
	Tartaria.ocean = False
	provinces["Tartaria"] = Tartaria
	
	Kazen = Province("Kazen", "cotton", 0.7, "civilized", "Russian")
	Kazen.x = 6
	Kazen.y = 17
	Kazen.ocean = False
	provinces["Kazen"] = Kazen

	Samara = Province("Samara", "iron", 0.7, "civilized", "Russian")
	Samara.x = 6
	Samara.y = 18
	Samara.ocean = False
	provinces["Samara"] = Samara
	
	Perm = Province("Perm", "wood", 0.8, "civilized", "Russian")
	Perm.x = 6
	Perm.y = 19
	Perm.ocean = False
	provinces["Perm"] = Perm

	Ural = Province("Ural", "iron", 1.25, "civilized", "Russian")
	Ural.x = 6
	Ural.y = 20
	Ural.ocean = False
	provinces["Ural"] = Ural
	
	Tomsk = Province("Tomsk", "coal", 0.8, "civilized", "Russian")
	Tomsk.x = 6
	Tomsk.y = 21
	Tomsk.ocean = False
	provinces["Tomsk"] = Tomsk

	CentralSiberia = Province("CentralSiberia", "wood", 0.45, "uncivilized", "Siberian")
	CentralSiberia.x = 5
	CentralSiberia.y = 22
	CentralSiberia.ocean = False
	provinces["CentralSiberia"] = CentralSiberia


	Irkutsk = Province("Irkutsk", "wood", 0.5, "uncivilized", "Siberian")
	Irkutsk.x = 5
	Irkutsk.y = 23
	Irkutsk.ocean = False
	provinces["Irkutsk"] = Irkutsk


	Yakutsk = Province("Yakutsk", "gold", 0.75, "uncivilized", "Siberian")
	Yakutsk.x = 5
	Yakutsk.y = 24
	Yakutsk.ocean = False
	provinces["Yakutsk"] = Yakutsk

	Okhotsk = Province("Okhotsk", "food", 0.45, "uncivilized", "Siberian")
	Okhotsk.x = 5
	Okhotsk.y = 25
	provinces["Okhotsk"] = Okhotsk

	Finland = Province("Finland", "wood", 1.0, "civilized", "Finish")
	Finland.x = 3
	Finland.y = 12
	provinces["Finland"] = Finland

	Naples = Province("Naples", "food", 1.1, "civilized", "Italian")
	Naples.x = 10
	Naples.y = 8
	provinces["Naples"] = Naples
	Lazio = Province("Lazio", "food", 1.0, "civilized", "Italian")
	Lazio.x = 9
	Lazio.y = 8
	provinces["Lazio"] = Lazio
	Sardinia_Piedmont = Province("Sardinia_Piedmont", "iron", 0.9, "civilized", "Italian")
	Sardinia_Piedmont.x = 8
	Sardinia_Piedmont.y = 7
	provinces["Sardinia_Piedmont"] = Sardinia_Piedmont
	Venezia = Province("Venezia", "cotton", 1.2, "civilized", "Italian")
	Venezia.x = 8
	Venezia.y = 8
	provinces["Venezia"] = Venezia
	Sicily = Province("Sicily", "coal", 0.8, "civilized", "Italian")
	Sicily.x = 10
	Sicily.y = 7
	provinces["Sicily"] = Sicily

	Bosnia = Province("Bosnia", "food", 0.8, "civilized", "Bosnian")
	Bosnia.x =10
	Bosnia.y =10
	provinces["Bosnia"] = Bosnia

	Bulgaria = Province("Bulgaria", "wood", 0.75, "civilized", "Bulgarian")
	Bulgaria.x = 10
	Bulgaria.x = 11
	provinces["Bulgaria"] = Bulgaria

	Serbia = Province("Serbia", "wood", 0.8, "civilized", "Serbian")
	Serbia.x = 10
	Serbia.y = 11
	provinces["Serbia"] = Serbia
	Greece = Province("Greece", "food", 1.0, "civilized", "Greek")
	Greece.x =11
	Greece.y = 11
	provinces["Greece"] = Greece
	WestTurky = Province("WestTurky", "iron", 0.9, "civilized", "Turkish")
	WestTurky.x = 10
	WestTurky.y =12
	provinces["WestTurky"] = WestTurky
	CentralTurky = Province("CentralTurky", "cotton", 1.0, "civilized", "Turkish")
	CentralTurky.x = 10
	CentralTurky.y = 13
	provinces["CentralTurky"] = CentralTurky
	EastTurky = Province("EastTurky", "food", 1.1, "civilized", "Turkish")
	EastTurky.x = 10
	EastTurky.y = 14
	EastTurky.ocean = False
	provinces["EastTurky"] = EastTurky

	Syria = Province("Syria", "food", 0.75, "old", "Arab")
	Syria.x = 11
	Syria.y = 14
	provinces["Syria"] = Syria
	Iraq = Province("Iraq", "oil", 1.2, "old", "Arab")
	Iraq.x = 12
	Iraq.y = 14
	Iraq.ocean = False
	provinces["Iraq"] = Iraq


	Andalusia = Province("Andalusia", "food", 1.0, "civilized", "Spanish")
	Andalusia.x = 11
	Andalusia.y = 5
	provinces["Andalusia"] = Andalusia

	Leon = Province("Leon", "iron", 1.2, "civilized", "Spanish")
	Leon.x = 10
	Leon.y = 4
	Leon.ocean = False
	provinces["Leon"] = Leon

	Aragon = Province("Aragon", "iron", 1.0, "civilized", "Spanish")
	Aragon.x = 9
	Aragon.y = 5
	provinces["Aragon"] = Aragon
	
	Galicia = Province("Galicia", "coal", 0.85, "civilized", "Spanish")
	Galicia.x = 9
	Galicia.y = 4
	provinces["Galicia"] = Galicia
	
	La_Mancha = Province("La_Mancha", "food", 1.1, "civilized", "Spanish")
	La_Mancha.x = 10
	La_Mancha.y = 5
	provinces["La_Mancha"] = La_Mancha


	Holland = Province("Holland", "food", 1.2, "civilized", "Dutch")
	Holland.x = 4
	Holland.y = 7
	provinces["Holland"] = Holland
	Gelderland = Province("Gelderland", "coal", 1.0, "civilized", "Dutch")
	Gelderland.x = 5
	Gelderland.y = 7
	provinces["Gelderland"] = Gelderland
	Wallonie = Province("Wallonie", "iron", 1.1, "civilized", "Dutch")
	Wallonie.x = 5
	Wallonie.y = 6
	Wallonie.ocean = False
	provinces["Wallonie"] = Wallonie


	Portugal = Province("Portugal", "food", 1.15, "civilized", "Portugal")
	Portugal.x = 11
	Portugal.y = 4
	provinces["Portugal"] = Portugal

	Svealand = Province("Svealand", "iron", 1.6, "civilized", "Swedish")
	Svealand.x = 2
	Svealand.y = 11
	provinces["Svealand"] = Svealand
	Norrland = Province("Norrland", "wood", 0.85, "civilized", "Swedish")
	Norrland.x = 1
	Norrland.y = 11
	provinces["Norrland"] = Norrland
	Ostlandet = Province("Ostlandet", "food", 0.9, "civilized", "Swedish")
	Ostlandet.x = 3
	Ostlandet.y = 11
	provinces["Ostlandet"] = Ostlandet

	Norway = Province("Norway", "wood", 1.0, "civilized", "Norwegian")
	Norway.x = 2
	Norway.y = 10
	provinces["Norway"] = Norway

	Denmark = Province("Denmark", "food", 1.1, "civilized", "Danish")
	Denmark.x = 4
	Denmark.y = 9
	provinces["Denmark"] = Denmark

	UpperEgypt = Province("UpperEgypt", "cotton", 1.4, "old", "Arab")
	UpperEgypt.x = 13
	UpperEgypt.y = 13
	provinces["UpperEgypt"] = UpperEgypt
	MiddleEgypt = Province("MiddleEgypt", "food", 1.0, "old", "Arab")
	MiddleEgypt.x = 14
	MiddleEgypt.y = 13
	MiddleEgypt.ocean = False
	provinces["MiddleEgypt"] = MiddleEgypt
	LowerEgypt = Province("LowerEgypt", "cotton", 0.8, "old", "Arab")
	LowerEgypt.x = 15
	LowerEgypt.y = 13
	LowerEgypt.ocean = False
	provinces["LowerEgypt"] = LowerEgypt
	Sudan = Province("Sudan", "rubber", 0.8, "uncivilized", "Sudanese")
	Sudan.x = 16
	Sudan.y = 13
	Sudan.ocean = False
	provinces["Sudan"] = Sudan

	Algiers = Province("Algiers", "food", 0.8, "old",  "Arab")
	Algiers.x = 13
	Algiers.y = 9
	provinces["Algiers"] = Algiers
	Constantine = Province("Constantine", "iron", 1.3, "old", "Arab")
	Constantine.x = 13
	Constantine.y = 10
	provinces["Constantine"] = Constantine

	Morocco = Province("Morocco", "food", 0.9, "old", "Arab")
	Morocco.x = 13
	Morocco.y = 8
	provinces["Morocco"] = Morocco
	South_Morocco = Province("South_Morocco", "gold", 0.9, "old", "Arab")
	South_Morocco.x = 14
	South_Morocco.y = 8
	provinces["South_Morocco"] = South_Morocco

	Tunis = Province("Tunis", "cotton", 0.8, "old", "Arab")
	Tunis.x = 13
	Tunis.y = 11
	provinces["Tunis"] = Tunis


	Libya = Province("Libya", "oil", 1.0, "old", "Arab")
	Libya.x = 13
	Libya.y = 12
	provinces["Libya"] = Libya


	WestKazakhstan = Province("WestKazakhstan", "cotton", 0.75, "uncivilized", "Kazak")
	WestKazakhstan.x = 7
	WestKazakhstan.y = 16
	WestKazakhstan.ocean = False
	provinces["WestKazakhstan"] = WestKazakhstan
	EastKazakhstan = Province("EastKazakhstan", "food", 0.55, "uncivilized", "Kazak")
	EastKazakhstan.x = 7
	EastKazakhstan.y = 17
	EastKazakhstan.ocean = False 
	provinces["EastKazakhstan"] = EastKazakhstan

	Khuzestan = Province("Khuzestan", "oil", 1.2, "old", "Persian")
	Khuzestan.x = 9
	Khuzestan.y = 15
	provinces["Khuzestan"] = Khuzestan
	Fars = Province("Fars", "food", 1.0, "old", "Persian")
	Fars.x = 11
	Fars.y = 16
	provinces["Fars"] = Fars
	Tehran = Province("Tehran", "cotton", 0.85, "old", "Persian")
	Tehran.x = 10
	Tehran.y = 16
	Tehran.ocean = False
	provinces["Tehran"] = Tehran
	Isfahan = Province("Isfahan", "iron", 1.0, "old",  "Persian")
	Isfahan.x = 11
	Isfahan.y = 15
	provinces["Isfahan"] = Isfahan
	Khorasan = Province("Khorasan", "coal", 0.75, "old", "Persian")
	Khorasan.x = 8
	Khorasan.y = 16	
	Khorasan.ocean = False
	provinces["Khorasan"] = Khorasan

	Nejd = Province("Nejd", "oil", 1.3, "old", "Arab")
	Nejd.x = 12
	Nejd.y = 14
	provinces["Nejd"] = Nejd

	Afghanistan = Province("Afghanistan", "food", 0.75,  "old", "Afghan")
	Afghanistan.x = 9
	Afghanistan.y = 17
	Afghanistan.ocean = False
	provinces["Afghanistan"] = Afghanistan


	Punjab = Province("Punjab", "cotton", 1.0, "old", "Indian")
	Punjab.x = 9
	Punjab.y = 18
	Punjab.ocean = False
	provinces["Punjab"] = Punjab
	United_Provinces = Province("United_Provinces", "food", 1.1, "old", "Indian")
	United_Provinces.x = 9
	United_Provinces.y = 19
	United_Provinces.ocean = False
	provinces["United_Provinces"] = United_Provinces
	Rajputana = Province("Rajputana", "cotton", 1.0, "old", "Indian")
	Rajputana.x = 10
	Rajputana.y = 18
	provinces["Rajputana"] = Rajputana
	Central_India = Province("Central_India", "dyes", 1.0, "old", "Indian")
	Central_India.x = 10
	Central_India.y = 19
	Central_India.ocean = False
	provinces["Central_India"] = Central_India
	Bombay = Province("Bombay", "spice", 1.1, "old", "Indian")
	Bombay.x = 12
	Bombay.y = 19
	provinces["Bombay"] = Bombay
	Madres = Province("Madres", "food", 1.15, "old", "Indian")
	Madres.x = 13
	Madres.y = 19
	provinces["Madres"] = Madres
	Nagpur = Province("Nagpur", "food", 1.0, "old", "Indian")
	Nagpur.x = 10
	Nagpur.y = 20
	provinces["Nagpur"] = Nagpur

	Bengal = Province("Bengal", "dyes", 1.0, "old", "Indian")
	Bengal.x = 10
	Bengal.y =21
	provinces["Bengal"] = Bengal

	Hyderabad = Province("Hyderabad", "cotton", 1.2, "old", "Indian")
	Hyderabad.x = 11
	Hyderabad.y = 19
	provinces["Hyderabad"] = Hyderabad

	Burma = Province("Burma", "wood", 1.1, "old", "Bamar")
	Burma.x =11
	Burma.y = 21
	provinces["Burma"] = Burma

	Bangkok = Province("Bangkok", "food", 0.9, "old", "Thai")
	Bangkok.x = 11
	Bangkok.y = 22
	provinces["Bangkok"] = Bangkok

	Laos = Province("Laos", "spice", 1.1, "old", "Thia")
	Laos.x = 10
	Laos.y = 22
	Laos.ocean = False
	provinces["Laos"] = Laos

	North_Dai_Nam = Province("North_Dai_Nam", "food", 1.25, "old",  "Vietnamese")
	North_Dai_Nam.x = 10
	North_Dai_Nam.y = 23
	provinces[North_Dai_Nam] = North_Dai_Nam
	South_Dai_Nam = Province("South_Dai_Nam", "Spice", 1.2, "old", "Vietnamese")
	South_Dai_Nam.x = 11
	South_Dai_Nam.y = 23
	provinces["South_Dai_Nam"] = South_Dai_Nam

	Cambodia = Province("Cambodia", "rubber", 1.1, "old", "Cambodian")
	Cambodia.x = 12
	Cambodia.y = 23
	provinces["Cambodia"] = Cambodia

	Brunei = Province("Brunei", "oil", 0.8, "old", "Brunei ")
	Brunei.x = 14
	Brunei.y = 25
	provinces["Brunei"] = Brunei

	Java = Province("Java", "spice", 1.2, "old", "Javanese")
	Java.x = 15
	Java.y = 24
	provinces["Java"] = Java

	Malaysia = Province("Malaysia", "rubber", 1.0, "old", "Malaysian")
	Malaysia.x = 13
	Malaysia.y = 22
	provinces["Malaysia"] = Malaysia
	Sumatra = Province("Sumatra", "spice", 1.1, "old", "Malaysian")
	Sumatra.x = 15
	Sumatra.y = 22
	provinces["Sumatra"] = Sumatra

	Sulawesi = Province("Sulawesi", "spice", 1.2, "old", "Sulawesi")
	Sulawesi.x = 14
	Sulawesi.y = 28
	provinces["Sulawesi"] = Sulawesi

	NorthPhilippines = Province("NorthPhilippines", "food", 1.1, "old", "Filipino")
	NorthPhilippines.x = 11
	NorthPhilippines.y = 27
	provinces["NorthPhilippines"] = NorthPhilippines
	SouthPhilippines = Province("SouthPhilippines", "iron", 0.75, "old", "Filipino")
	SouthPhilippines.x = 12
	SouthPhilippines.y = 27
	provinces["SouthPhilippines"] = SouthPhilippines


	Manchuria = Province("Manchuria", "coal", 0.85, "old", "Manchurian")
	Manchuria.x = 6
	Manchuria.y = 26
	provinces["Manchuria"] = Manchuria

	Guangxi = Province("Guangxi", "cotton", 1.0, "old", "Chinese")
	Guangxi.x = 9
	Guangxi.y = 23
	provinces["Guangxi"] = Guangxi

	Guangdong = Province("Guangdong", "food", 1.1, "old", "Chinese")
	Guangdong.x = 9
	Guangdong.y = 24
	provinces["Guangdong"] = Guangdong

	Hunan = Province("Hunan", "cotton", 0.9, "old", "Chinese")
	Hunan.x = 8
	Hunan.y = 23
	Hunan.ocean = False
	provinces["Hunan"] = Hunan

	Mongolia = Province("Mongolia", "food", 0.5, "old", "Mongolian")
	Mongolia.x = 6
	Mongolia.y = 23
	Mongolia.ocean = False
	provinces["Mongolia"] = Mongolia

	Jiangsu = Province("Jiangsu", "food", 1.2, "old", "Chinese")
	Jiangsu.x = 7
	Jiangsu.y = 24
	provinces["Jiangsu"] = Jiangsu
	
	#Jiangxi = Province("Jiangxi", "wood", 0.8, "China")
	Qinghai = Province("Qinghai", "coal", 0.75, "old", "Chinese")
	Qinghai.x = 7
	Qinghai.y = 22
	Qinghai.ocean = False
	provinces["Qinghai"] = Qinghai
	#Shandong = Province("food", "food", 1.2, "China")
	Shanxi = Province("Shanxi", "coal", 0.85, "old", "China")
	Shanxi.x = 6
	Shanxi.y = 24
	provinces["Shanxi"] = Shanxi
	Sichuan = Province("Sichuan", "spice", 1.0, "old", "Chinese")
	Sichuan.x = 8
	Sichuan.y = 22
	Sichuan.ocean = False
	provinces["Sichuan"] = Sichuan
	Zhejiang = Province("Zhejiang", "wood", 0.9, "old", "Chinese")
	Zhejiang.x = 8
	Zhejiang.y = 24
	provinces["Zhejiang"] = Zhejiang
	Liaoning = Province("Liaoning", "iron", 1.0, "old", "Chinese")
	Liaoning.x = 6
	Liaoning.y = 25
	provinces["Liaoning"] = Liaoning

	Pyongyang = Province("Pyongyang", "coal", 1.3, "old",  "Korea")
	Pyongyang.x = 7
	Pyongyang.y = 26
	provinces["Pyongyang"] = Pyongyang
	Sariwon = Province("Sariwon", "iron", 1.2, "old",  "Korea")
	Sariwon.x = 7
	Sariwon.y = 27
	provinces["Sariwon"] = Sariwon
	Seoul = Province("Seoul", "food", 1.2, "old", "Korea")
	Seoul.x = 8
	Seoul.y = 27
	provinces["Seoul"] = Seoul

	Kansai = Province("Kansai", "food", 1.1, "old", "Japanese")
	Kansai.x = 8
	Kansai.y = 29
	provinces["Kansai"] = Kansai
	Tohoku = Province("Tohoku", "iron", 0.85, "old", "Japanese")
	Tohoku.x = 6
	Tohoku.y = 29
	provinces["Tohoku"] = Tohoku
	Chugoku = Province("Chugoku", "cotton", 1.2,  "old", "Japanese")
	Chugoku.x = 9
	Chugoku.y = 29
	provinces["Chugoku"] = Chugoku
	Kanto = Province("Kanto", "food", 1.05, "old", "Japanese")
	Kanto.x = 7
	Kanto.y = 29
	provinces["Kanto"] = Kanto
	Kyushu = Province("Kyushu", "coal", 1.0, "old", "Japanese")
	Kyushu.x = 10
	Kyushu.y = 29
	provinces["Kyushu"] = Kyushu

	Mauritania = Province("Mauritania", "food", 0.8, "old", "Arab")
	Mauritania.x = 15
	Mauritania.y = 8
	provinces["Mauritania"] = Mauritania

	Liberia = Province("Liberia", "rubber", 0.9, "uncivilized", "Kpelle")
	Liberia.x = 16
	Liberia.y = 8
	provinces["Liberia"] = Liberia

	Mali = Province("Mali", "food", 0.75, "uncivilized", "Bambara")
	Mali.x = 15
	Mali.y = 9
	provinces["Mali"] = Mali

	Ghana = Province("Ghana", "food", 0.85, "uncivilized", "Akan")
	Ghana.x = 16
	Ghana.y = 9
	provinces["Ghana"] = Ghana

	Niger = Province("Niger", "cotton", 0.55, "uncivilized", "Hausa")
	Niger.x = 15
	Niger.y = 10
	Niger.ocean = False
	provinces["Niger"] = Niger

	Nigeria = Province("Nigeria", "rubber", 1.2, "uncivilized", "Hausa")
	Nigeria.x = 16
	Nigeria.y =10
	provinces["Nigeria"] = Nigeria

	Cameroon = Province("Cameroon", "wood", 1.0, "uncivilized", "Cameroon")
	Cameroon.x = 17
	Cameroon.y = 10
	provinces["Cameroon"] = Cameroon

	Angola = Province("Angola", "iron", 0.65, "uncivilized", "Ovimbundu")
	Angola.x = 18
	Angola.y = 10
	provinces["Angola"] = Angola

	Nambia = Province("Nambia", "gold", 0.5, "uncivilized", "Bantu")
	Nambia.x = 19
	Nambia.y = 10
	provinces["Nambia"] = Nambia

	Cape = Province("Cape", "gold", 1.0, "uncivilized", "Zulu")
	Cape.x = 20
	Cape.y = 10
	provinces["Cape"] = Cape
	Zululand = Province("Zululand", "food", 1.0, "uncivilized", "Zulu")
	Zululand.x = 20
	Zululand.y = 11
	provinces["Zululand"] = Zululand

	Mozambique = Province("Mozambique", "iron", 0.75, "uncivilized", "Bantu")
	Mozambique.x = 19
	Mozambique.y = 11
	provinces["Mozambique"] = Mozambique

	Tanzania = Province("Tanzania", "food", 1.0, "uncivilized", "Sukuma")
	Tanzania.x = 18
	Tanzania.y = 11
	provinces["Tanzania"] = Tanzania

	Kenya = Province("Kenya", "spice", 0.8, "uncivilized", "Bantu")
	Kenya.x = 17
	Kenya.y = 12
	provinces["Kenya"] = Kenya

	Ethiopia = Province("Ethiopia", "food", 0.8, "uncivilized", "Oromo")
	Ethiopia.x = 16
	Ethiopia.y = 13
	provinces["Ethiopia"] = Ethiopia

	Congo = Province("Congo", "rubber", 0.8, "uncivilized", "Bantu")
	Congo.x = 17
	Congo.y = 11
	Congo.ocean = False
	provinces["Congo"] = Congo

	Madagascar = Province("Madagascar", "wood", 0.8, "uncivilized", "Merina")
	Madagascar.x = 19
	Madagascar.y = 13
	provinces["Madagascar"] = Madagascar

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

	New_Zealand = Province("New Zealand", "cotton", 0.8, "uncivilized", "Aboriginal")
	New_Zealand.x = 15
	New_Zealand.y = 32
	provinces["New Zealand"] = New_Zealand

	return provinces