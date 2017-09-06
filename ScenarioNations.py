from player_class import*
from minor_classes import*
from AI import*

def england(player, provinces):

	player.technologies.add("pre_industry_3")
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")
	player.technologies.add("high_pressure_steam_engine")
	player.culture = "English"
	player.accepted_cultures.add("Scottish")
	player.capital = "SouthEastEngland"
	player.military["artillery"] = 0
	player.military["frigates"] = 2.0
	player.colonization = 2
	player.diplo_action = 2	####################

	player.resources["gold"] = 12    ##############

	player.provinces["SouthEastEngland"] = provinces["SouthEastEngland"]
	player.provinces["SouthWestEngland"] = provinces["SouthWestEngland"]
	player.provinces["Midlands"] = provinces["Midlands"]
	player.provinces["Whales"] = provinces["Whales"]
	player.provinces["NorthEngland"] = provinces["NorthEngland"]
	player.provinces["Scotland"] = provinces["Scotland"]
	player.provinces["Ireland"] = provinces["Ireland"]

	player.doctrines = {"Sea_Doctrine1"}
	player.frigates["attack"] += 0.3
	player.iron_clad["attack"] += 0.32
	player.battle_ship["attack"] += 1


	player.objectives = {"SouthEastEngland", "SouthEastEngland", "Midlands", "Whales", "NorthEngland", \
	"Scotland", "Ireland", "Bombay", "_Bengal", "_Hyderabad", "UpperEgypt", "MiddleEgypt", "Sudan", \
	"United_Provinces", "Rajputana", "Madres", "Nagpur", "_Burma", "_Brunei", "_Malaysia", "_Nejd", \
	"Iraq", "Guangdong", "Punjab", "Central_India"}


	if type(player) == AI:
		player.personality["Army"] = 1.15
		player.personality["Navy"] = 0.9
		player.improve_province_priority["shipyard"] = 2.4
		player.personality["Offensive"] = 0.55
		player.build_factory_priority["parts"] = 1.5
		player.build_factory_priority["clothing"] = 1.4
		player.resource_priority["cotton"] = 2.4
		player.resource_priority["dyes"] = 2.9
		player.improve_province_priority["cotton"] = 1.2
		player.improve_province_priority["dyes"] = 1.1


		player.reputation = 1.1



def france(player, provinces):

	player.culture = "French"
	player.capital = "CentralFrance"
	player.technologies.add("pre_industry_3")
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")

	player.provinces["Loire"] = provinces["Loire"] 
	player.provinces["Champagne"] = provinces["Champagne"]
	player.provinces["Brittany"] = provinces["Brittany"]
	player.provinces["CentralFrance"] = provinces["CentralFrance"]
	player.provinces["Aquitaine"] = provinces["Aquitaine"]
	player.provinces["Alps"] = provinces["Alps"]
	player.provinces["Normandy"] = provinces["Normandy"]

	player.doctrines = {"Artillery_Offense"}
	player.artillery["attack"] += 0.4

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.78
		player.improve_province_priority["shipyard"] = 1.8
		player.personality["Offensive"] = 0.38
		player.improve_province_priority["shipyard"] = 2.2


	player.objectives = {"Loire", "Champagne", "Brittany", "CentralFrance", "Aquitaine", "Alps", \
	"Normandy", "Piedmont", "Wallonie", "Gelderland", "Aragon", "Algiers", "Constantine", "_Burma",\
	"Syria", "_Morocco", "South_Morocco", "Laos", "North_Dai_Nam", "South_Dai_Nam", "_Cambodia", "Bombay", \
	"Khuzestan"} 

	player.sphere = {"Bavaria", "Lazio"}


def germany(player, provinces):

	player.culture = "German"
	player.capital = "Brandenburg"
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")
	player.technologies.add("flintlock")
	player.stability = 2

	player.POP = 5.4
	player.freePOP = 3.6
	player.numLowerPOP = 4.6

	player.military["frigates"] = 0
	player.military["cavalry"] = 2

	player.colonization = 0

	player.provinces["EastPrussia"] = provinces["EastPrussia"]
	player.provinces["Brandenburg"] = provinces["Brandenburg"]
	player.provinces["Rhineland"] = provinces["Rhineland"]
	player.provinces["WestPoland"] = provinces["WestPoland"]
	#player.provinces["Saxony"] = provinces["Saxony"]
	#player.provinces["NorthGermany"] = provinces["NorthGermany"]
	#player.provinces["Bavaria"] = provinces["Bavaria"]

	player.doctrines = {"Mobile_Offense"}
	player.cavalry["attack"] += 0.3
	player.tank["attack"] += 0.5

	if type(player) == AI:
		player.personality["Army"] = 1.7
		player.personality["Navy"] = 0.65
		player.build_factory_priority["paper"] = 1.3
		player.personality["Offensive"] = 0.68
		player.diplo_action = 3
		player.military["artillery"] = 2
		player.milPOP = 1.2
		player.POP = 6.6
		player.freePOP = 4.6
		player.numLowerPOP = 5.8
		player.goods["cannons"] = 3
		player.technologies.add("high_pressure_steam_engine")
		player.resources["gold"] = 18




	player.objectives = {"EastPrussia", "Brandenburg", "_NorthGermany", "_Bavaria", "Rhineland", \
	"_Saxony", "WestPoland", "_Poland", "_Austria", "Bohemia", "Wallonie", "Gelderland", "Baltic", \
	"_Malaysia", "Bangkok", "Khuzestan"}

	

def saxony(player, provinces):
	player.culture = "German"
	player.capital = "_Saxony"
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")
	player.provinces["_Saxony"] = provinces["_Saxony"]
	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01


def northgermany(player, provinces):
	player.culture = "German"
	player.capital = "_NorthGermany"
	player.provinces["_NorthGermany"] = provinces["_NorthGermany"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")


def bavaria(player, provinces):
	player.culture = "German"
	player.capital = "_Bavaria"
	player.provinces["_Bavaria"] = provinces["_Bavaria"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")
	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01


def austria(player, provinces):

	player.culture = "German"
	player.accepted_cultures = {"Check", "Hungarian" }
	player.capital = "_Austria"
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")

	player.resources["food"] = 2

	player.military["frigates"] = 0
	
	player.colonization = 0

	player.number_units = 4
	player.freePOP = 6.8
	player.milPOP = 0.8

	player.shipyard = 0
	player.stability = 1.5

	player.doctrines = {"Infantry_Offense"}
	player.infantry["attack"] += 0.25

	player.provinces["Bohemia"] = provinces["Bohemia"]
	player.provinces["Slovakia"] = provinces["Slovakia"]
	player.provinces["_Austria"] = provinces["_Austria"]
	player.provinces["Hungary"] = provinces["Hungary"]
	#player.provinces["Romania"] = provinces["Romania"]
	player.provinces["Croatia"] = provinces["Croatia"]
	player.provinces["WestUkraine"] = provinces["WestUkraine"]
	player.provinces["Venezia"] = provinces["Venezia"]	


	player.objectives = {"Romania", "Wallonie", "_Bavaria", "_Saxony", "Bosnia", "Venezia", "WestUkraine"}
	sphere = {"_Saxony"}

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.5
		player.improve_province_priority["shipyard"] = 1.3
		player.build_factory_priority["paper"] = 1.2



def russia(player, provinces):

	player.culture = "Russian"
	player.capital = "Novgorod"

	player.sprawl = True

	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")

	player.shipyard = 0

	player.military["frigates"] = 0
	player.military["irregulars"] = 1
	player.colonization = -3 

	player.midPOP["bureaucrats"]["number"] = 0
	player.midPOP["officers"]["number"] = 0
	player.midPOP["artists"]["number"] = 0
	player.midPOP["researchers"]["number"] = 0.2

	player.diplo_action = 2

	player.POP = 10.2
	player.numMidPOP = 0.2
	player.numLowerPOP = 10
	player.freePOP = 9

	player.provinces["_Poland"] = provinces["_Poland"]
	player.provinces["Ukraine"] = provinces["Ukraine"]
	player.provinces["Baltic"] = provinces["Baltic"]
	player.provinces["Crimea"] = provinces["Crimea"] 
	player.provinces["Novgorod"] = provinces["Novgorod"]
	player.provinces["Finland"] = provinces["Finland"]
	player.provinces["Moskva"] = provinces["Moskva"]
	player.provinces["Galich"] = provinces["Galich"]	
	player.provinces["Caucasia"] = provinces["Caucasia"]	
	player.provinces["Tartaria"] = provinces["Tartaria"]	
	player.provinces["Kazen"] = provinces["Kazen"]
	player.provinces["Samara"] = provinces["Samara"]	
	player.provinces["Perm"] = provinces["Perm"]
	player.provinces["Ural"] = provinces["Ural"]
	player.provinces["Tomsk"] = provinces["Tomsk"]
	player.provinces["CentralSiberia"] = provinces["CentralSiberia"]
	player.provinces["Irkutsk"] = provinces["Irkutsk"]
	player.provinces["Yakutsk"] = provinces["Yakutsk"]
	player.provinces["Okhotsk"] = provinces["Okhotsk"]

	if type(player) == AI:
		player.personality["Army"] = 1.25
		player.personality["Navy"] = 0.45
		player.personality["Offensive"] = 0.40
		player.build_factory_priority["paper"] = 1.15
		player.build_factory_priority["furniture"] = 1.3
		player.resource_priority["wood"] = 1.1
		player.improve_province_priority["wood"] = 1.2

	player.objectives = {"_Poland", "WestPoland", "WestUkraine", "Finland", "EastKazakhstan", \
	"WestKazakhstan", "EastPrussia", "Manchuria"}


def italy(player, provinces): #major

	player.culture = "Italian"
	player.capital = "Piedmont"

	player.stability = 2
	player.diplo_action = 3


	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")

	player.POP = 4.8
	player.numLowerPOP = 5
	player.freePOP = 3.4

	
	player.resources["gold"] = 10.0

	player.midPOP["researchers"]["number"] = 0.0
	player.midPOP["bureaucrats"]["number"] = 0.0

	player.numMidPOP = 0.4



	#player.provinces["Naples"] = provinces["Naples"]
	#player.provinces["Sicily"] = provinces["Sicily"]
	player.provinces["Piedmont"] = provinces["Piedmont"]	
	#player.provinces["Venezia"] = provinces["Venezia"]	
	#player.provinces["Lazio"] = provinces["Lazio"]


	if type(player) == AI:
		player.personality["Army"] = 1.15
		player.personality["Navy"] = 0.8
		player.build_factory_priority["furniture"] = 1.12
		player.build_factory_priority["clothing"] = 1.12
		player.POP = 4.8
		player.numLowerPOP = 5
		player.freePOP = 3.4

	player.objectives = {"Naples", "Lazio", "Venezia", "Piedmont", "Sicily", "_Libya", "Croatia", \
	"Greece", "UpperEgypt", "MiddleEgypt", "Sudan", "Tunis"}


def two_sicilies(player, provinces):
	player.culture = "Italian"
	player.capital = "Naples"
	player.provinces["Naples"] = provinces["Naples"]
	player.provinces["Sicily"] = provinces["Sicily"]

def papal_state(player, provinces):
	player.culture = "Italian"
	player.capital = "Lazio"
	player.provinces["Lazio"] = provinces["Lazio"]



def switzerland(player, provinces):
	player.culture = "Swiss"
	player.capital = "_Switzerland"
	player.resources["gold"] = 12

	player.military["infantry"] = 3
	player.number_units = 3
	player.midPOP["researchers"]["number"] = 0.2

	player.POP = 3.6
	player.freePOP = 2.8
	player.milPOP = 0.6
	player.numLowerPOP = 3.4

	player.provinces["_Switzerland"] = provinces["_Switzerland"]

	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01



def ottoman(player, provinces):  

	player.culture = "Turkish"
	player.capital = "WestTurky"
	player.resources["gold"] = 3

	player.military["irregulars"] = 2
	player.military["infantry"] = 2.0
	player.military["cavalry"] = 1.0
	player.military["frigates"] = 0.0
	player.military["artillery"] = 0.0

	player.number_units = 5.0
	player.diplo_action = 0.0

	player.shipyard = 0


	player.colonization = -3 
	player.POP = 9
	player.numLowerPOP = 9
	player.freePOP = 8
	player.numMidPOP = 0

	player.midPOP["researchers"]["number"] = 0
	player.midPOP["officers"]["number"] = 0
	player.midPOP["artists"]["number"] = 0
	player.midPOP["bureaucrats"]["number"] = 0
	player.midPOP["managers"]["number"] = 0

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.6


	
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
	player.provinces["Romania"] = provinces["Romania"]

	if type(player) == "AI":
		player.personality["Army"] = 1.25
		player.personality["Navy"] = 0.6
		player.personality["Offensive"] = 0.40

	player.objectives = {"Bosnia", "Bulgaria", "Serbia", "Greece", "WestTurky", "CentralTurky", "EastTurky", \
	"Syria", "Iraq", "UpperEgypt", "MiddleEgypt", "_Libya", "Tunis", "Hungary", "Romania", "_Austria", \
	"Crimea", "_Nejd", "Khuzestan"}


def spain(player, provinces): 

	player.culture = "Spanish"
	player.capital = "Leon"

	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")


	player.military["irregulars"] = 1
	player.military["infantry"]	= 1	
	player.colonization = 0 
	player.military["frigates"] = 1
	player.POP = 7
	player.numLowerPOP = 7
	player.freePOP = 6
	player.numMidPOP = 0

	player.midPOP["researchers"]["number"] = 0
	player.midPOP["officers"]["number"] = 0
	player.midPOP["artists"]["number"] = 0
	player.midPOP["bureaucrats"]["number"] = 0
	player.midPOP["managers"]["number"] = 0

	player.provinces["Andalusia"] = provinces["Andalusia"]
	player.provinces["Leon"] = provinces["Leon"]
	player.provinces["Aragon"] = provinces["Aragon"]	
	player.provinces["Galicia"] = provinces["Galicia"]
	player.provinces["La_Mancha"] = provinces["La_Mancha"]

	if type(player) == AI:
		player.personality["Army"] = 1.15
		player.personality["Navy"] = 0.75
		player.improve_province_priority["shipyard"] = 1.9
		player.personality["Offensive"] = 0.60

	player.objectives = {"Andalusia", "Leon", "Aragon", "Galicia", "La_Mancha", "_Morocco", "South_Morocco", \
	"NorthPhilippines", "SouthPhilippines", "_Portugal", "Sicily", "Naples", "Wallonie", "Aquitaine"}



def netherlands(player, provinces): # major power

	player.culture = "Dutch"
	player.capital = "Holland"
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")
	player.technologies.add("flintlock")

	player.resources["spice"] = 1



	player.military["artillery"] = 0
	player.military["frigates"] = 2
	player.midPOP["officers"]["number"] = 0

	player.POP = 7
	player.freePOP = 5.4
	player.numLowerPOP = 6.4
	player.numMidPOP = 0.6

	player.provinces["Holland"] = provinces["Holland"]
	player.provinces["Gelderland"] = provinces["Gelderland"]
	player.provinces["Wallonie"] = provinces["Wallonie"]

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.9
		player.improve_province_priority["shipyard"] = 2.6
		player.personality["Offensive"] = 0.4
		player.resource_priority["spice"] = 2.2

	player.objectives = {"Holland", "Gelderland", "Wallonie", "_NorthGermany", "Sumatra", "_Brunei",  \
	"_Sulawesi", "_Java", "Madres", "Bombay"}



def portugal(player, provinces): # old_minor
	#Portugal
	player.culture = "Portuguese"
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")



	player.resources["gold"] = 10.0
	player.resources["spice"] = 2

	if type(player) == AI:
		player.personality["Navy"] = 1
		player.personality["Army"] = 1.25
		player.improve_province_priority["shipyard"] = 3


	player.midPOP["researchers"]["number"] = 0.2

	player.military["calvary"] = 1
	player.military["frigates"] = 1

	player.POP = 3.6
	player.freePOP = 2.6
	player.milPOP = 0.8
	player.numLowerPOP = 3.4
	player.numMidPOP = 0.2
	player.colonization = 1.0

	player.shipyard = 1

	player.capital = "_Portugal"

	player.borders.add("Spain")
	player.provinces["_Portugal"] = provinces["_Portugal"]

	if type(player) == AI:
		player.personality["Army"] = 1.3
		player.personality["Navy"] = 1.4
		player.improve_province_priority["shipyard"] = 2.3


	player.number_units = 3

	player.colonization = 1
	player.diplo_action = 1

	player.objectives = {"_Nejd", "Madres", "Bombay", "Guangdong"}


#def poland(player, provinces):
#	player.capital = "_Poland"
#	player.culture = "Polish"
#	player.technologies.add("pre_industry_2")
#	player.technologies.add("flintlock")


#	player.provinces["_Poland"] = provinces["_Poland"]
#	player.provinces["WestPoland"] = provinces["WestPoland"]
#	player.provinces["WestUkraine"] = provinces["WestUkraine"]


#	player.military["infantry"] = 3.0
#	player.milPOP = 0.6

#	player.objectives = {"_Poland", "WestPoland", "WestUkraine", "Ukraine", "Baltic", "EastPrussia", \
#	"Novgorod"}

def sweden(player, provinces): # adv minor
	#Sweden
	player.capital = "Ostlandet"
	player.culture = "Swedish"
	player.technologies.add("pre_industry_2")
	player.technologies.add("flintlock")


	player.military["infantry"] = 3.0
	player.milPOP = 0.6
	player.number_units = 3


	player.midPOP["researchers"]["number"] = 0.2
	player.numMidPOP = 0.2
	player.POP = 4.8
	player.numLowerPOP = 4.6
	player.freePOP = 4

	
	player.provinces["Svealand"] = provinces["Svealand"]
	player.provinces["Norrland"] = provinces["Norrland"]
	player.provinces["Ostlandet"] = provinces["Ostlandet"]
	player.provinces["_Norway"] = provinces["_Norway"]

	#player.provinces["Finland"] = provinces["Finland"]

	player.objectives = {"Svealand", "Norrland", "Ostlandet", "_Norway", "_Denmark", "Novgorod", \
	 "Baltic", "EastPrussia"}


#def norway(player, provinces): #ad minor

#	player.capital = "_Norway"

#	player.culture = "Norwegian"
#	player.provinces["_Norway"] = provinces["_Norway"]
#	player.technologies.add("pre_industry_2")
#	player.technologies.add("flintlock")

	
def denmark(player, provinces): #adv minor
	player.culture = "Danish"
	player.technologies.add("pre_industry_2")
	player.capital = "_Denmark"
	player.technologies.add("flintlock")


	player.provinces["_Denmark"] = provinces["_Denmark"]
	player.objectives = {"_Norway", "_NorthGermany"}


def egypt(player, provinces): # Old minor
	#Egypt
	player.culture = "Arab"
	player.capital = "UpperEgypt"
	player.POP = 4.6
	player.numLowerPOP = 4.6
	player.freePOP = 4

	
	player.provinces["UpperEgypt"] = provinces["UpperEgypt"]
	player.provinces["MiddleEgypt"] = provinces["MiddleEgypt"]
	player.provinces["Sudan"] = provinces["Sudan"]

	objectives = {"UpperEgypt", "MiddleEgypt", "Sudan", "_Libya", "Syria", "Iraq", "_Nejd", "Tunis"}


def algeria(player, provinces): #old minor

	player.capital = "Algiers"
	player.culture = "Arab"

	player.provinces["Algiers"] = provinces["Algiers"]
	player.provinces["Constantine"] = provinces["Constantine"]


def morocco(player, provinces): # old minor
	#Morocco
	player.culture = "Arab"
	player.capital = "_Morocco"
	player.provinces["_Morocco"] = provinces["_Morocco"]
	player.provinces["South_Morocco"] = provinces["South_Morocco"]


def tunisia(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "Tunis"
	player.provinces["Tunis"] = provinces["Tunis"]

def libya(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "_Libya"
	player.provinces["_Libya"] = provinces["_Libya"]

def kazakhstan (player, provinces): #old minor
	player.culture = "Kazak"
	player.capital =  "WestKazakhstan"
	player.provinces["WestKazakhstan"] = provinces["WestKazakhstan"]
	player.provinces["EastKazakhstan"] = provinces["EastKazakhstan"]


def persia(player, provinces): # Old Empire
	player.culture = "Persian"
	player.capital = "Tehran"

	player.POP = 7
	player.numLowerPOP = 7
	player.freePOP = 6
	player.colonization = -2

	player.resources["gold"] = 10

	player.provinces["Khuzestan"] = provinces["Khuzestan"]	
	player.provinces["Fars"] = provinces["Fars"]
	player.provinces["Tehran"] = provinces["Tehran"]
	player.provinces["Isfahan"] = provinces["Isfahan"]
	player.provinces["Khorasan"] = provinces["Khorasan"]

	if type(player) == "AI":
		player.personality["Navy"] = 0.4

	player.objectives = {"Khorasan", "Khuzestan", "Fars", "Isfahan", "Khorasan", "Iraq", "Syria", \
	"_Afghanistan", "Caucasia", "Punjab", "UpperEgypt", "_Nejd"}


def nejd(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "_Nejd"
	player.provinces["_Nejd"] = provinces["_Nejd"]


def afghanistan(player, provinces):
	player.culture = "Afghan"
	player.capital = "_Afghanistan"
	player.provinces["_Afghanistan"] = provinces["_Afghanistan"]

def india(player, provinces): # Old Empire

	player.culture = "Indian"
	player.capital = "Central_India"
	player.colonization = -3 
	player.POP = 10
	player.numLowerPOP = 10
	player.freePOP = 9
	player.numMidPOP = 0
	player.research = -1.0

	player.sprawl = True

	player.provinces["Punjab"] = provinces["Punjab"]

	player.provinces["United_Provinces"] = provinces["United_Provinces"]
	
	player.provinces["Rajputana"] = provinces["Rajputana"]
	
	player.provinces["Central_India"] = provinces["Central_India"]
	
	player.provinces["Bombay"] = provinces["Bombay"]
	
	player.provinces["Madres"] = provinces["Madres"]
	
	player.provinces["Nagpur"] = provinces["Nagpur"]

	if type(player) == "AI":
		player.personality["Army"] = 1
		player.personality["Navy"] = 0.25

	player.objectives = {"Punjab", "United_Provinces", "Rajputana", "Central_India", "Bombay", \
	"Madres", "Nagpur", "_Bengal", "_Hyderabad", "_Burma", "_Afghanistan"}


def bengal(player, provinces):
	player.culture = "Indian"
	player.capital = "_Bengal"

	player.provinces["_Bengal"] = provinces["_Bengal"]

def hyderabad(player, provinces):
	player.culture = "Indian"
	player.capital = "_Hyderabad" 
	player.provinces["_Hyderabad"] = provinces["_Hyderabad"]
	#Burma 
def burma(player, provinces):
	player.culture = "Bamar"
	player.capital  = "_Burma"

	player.provinces["_Burma"] = provinces["_Burma"]

def siam(player, provinces): 
	player.capital = "Bangkok"
	player.culture = "Thai"


	player.provinces["Bangkok"] = provinces["Bangkok"]
	player.provinces["Laos"] = provinces["Laos"]
	
def dai_dam(player, provinces):
	player.capital = "North_Dai_Nam"
	player.culture = "Vietnamese"

	player.provinces[North_Dai_Nam] = provinces["North_Dai_Nam"]
	player.provinces["South_Dai_Nam"] = provinces["South_Dai_Nam"]


def cambodia(player, provinces):
	player.culture = "Cambodian"
	player.capital = "_Cambodia" 
	player.provinces["_Cambodia"] = provinces["_Cambodia"]

	#Singapore
	#Singapore = Province("Singapore", "rubber", 1.1, "Singapore")
def brunei(player, provinces):
	culture = "Brunei"
	player.capital = "_Brunei" 
	player.provinces["_Brunei"] = provinces["_Brunei"]

def java(player, provinces):
	player.culture = "Javanese"
	player.capital = "_Java"
	player.provinces["_Java"] = provinces["_Java"]
	player.resources["spice"] = 1


def malaysia(player, provinces): 
	player.culture = "Malaysian"
	player.capital = "_Malaysia"
	
	player.provinces["_Malaysia"] = provinces["_Malaysia"]
	
	player.provinces["Sumatra"] = provinces["Sumatra"]
	#player.provinces["Singapour"] = provinces["Singapour"]
	player.resources["spice"] = 1



def	sulawesi(player, provinces):
	player.culture = "Sulawesi"
	player.capital = "_Sulawesi"
	player.provinces["_Sulawesi"] = provinces["_Sulawesi"]
	player.resources["spice"] = 1



def philippines(player, provinces):
	player.culture = "Filipino"
	player.capital = "NorthPhilippines"
	
	player.provinces["NorthPhilippines"] = provinces["NorthPhilippines"]
	player.provinces["SouthPhilippines"] = provinces["SouthPhilippines"]


def china(player, provinces):
	player.capital = "Liaoning"
	player.culture = "Chinese"

	player.military["irregulars"] = 5
	player.milPOP = 1.2
	player.POP = 11.2
	player.numLowerPOP = 11.2
	player.freePOP = 10

	player.sprawl = True

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

	if type(player) == AI:
		player.personality["Navy"] = 0.25

	player.objectives = {"Manchuria", "Guangxi", "Guangdong", "Hunan", "Mongolia", "Jiangsu", "Qinghai", \
	"Shanxi", "Sichuan", "Zhejiang", "Liaoning", "North_Dai_Nam", "South_Dai_Nam", "Okhotsk"}


def korea(player, provinces):
	player.culture = "Korean"
	player.capital = "Pyongyang"
	
	player.provinces["Pyongyang"] = provinces["Pyongyang"]
	player.provinces["Sariwon"] = provinces["Sariwon"]
	player.provinces["Seoul"] = provinces["Seoul"]

def japan(player, provinces): 

	player.POP = 7.2
	player.freePOP = 6
	player.numLowerPOP = 7
	player.government = "absolute monarchy"

	player.numMidPOP = 0.2
	player.midPOP["researchers"]["number"] = 0.2

	player.resources["gold"] = 10

	player.capital = "Kansai"
	
	player.provinces["Kansai"] = provinces["Kansai"]
	
	player.provinces["Tohoku"] = provinces["Tohoku"]

	player.provinces["Chugoku"] = provinces["Chugoku"]

	player.provinces["Kanto"] = provinces["Kanto"]

	player.provinces["Kyushu"] = provinces["Kyushu"]

	if type(player) == AI:
		player.build_factory_priority["cannons"] += 0.15
		player.personality["Army"] = 1.3
		player.personality["Navy"] = 1.0

	player.objectives = {"Kansai", "Tohoku", "Chugoku", "Kanto", "Kyushu", "Pyongyang", "Sariwon", \
	"Seoul", "Sumatra", "_Malaysia", "_Brunei", "Manchuria", "_Java", "NorthPhilippines", \
	"SouthPhilippines", "Liaoning"}



def mauritania(player, provinces):
	player.culture = "Arab" 
	player.provinces["_Mauritania"] = provinces["_Mauritania"]
	player.harsh = True


def liberia(player, provinces): 
	player.culture = "Kpelle"
	player.provinces["_Liberia"] = provinces["_Liberia"]
	player.harsh = True


def mali(player, provinces):
	player.culture = "Bambara"
	player.provinces["_Mali"] = provinces["_Mali"]
	player.harsh = True


def ghana(player, provinces):
	player.culture = "Akan"
	player.provinces["_Ghana"] = provinces["_Ghana"]

def niger(player, provinces):
	player.culture = "Hausa"
	player.provinces["_Niger"] = provinces["_Niger"]
	player.harsh = True


def nigeria(player, provinces):
	player.culture = "Hausa"
	player.harsh = True

	player.provinces["_Nigeria"] = provinces["_Nigeria"]

def cameroon(player, provinces):
	player.culture = "Cameroon"
	player.harsh = True	
	player.provinces["_Cameroon"] = provinces["_Cameroon"]

def angola(player, provinces):
	player.culture = "Ovimbundu"
	player.harsh = True	
	player.provinces["_Angola"] = provinces["_Angola"]

def nambia(player, provinces):
	player.culture = "Bantu"
	player.provinces["_Nambia"] = provinces["_Nambia"]
	player.harsh = True


def zululand(player, provinces):
	player.capital = "Zululand"
	player.culture = "Zulu"
	player.harsh = True

	player.provinces["Cape"] = provinces["Cape"]
	player.provinces["_Zululand"] = provinces["_Zululand"]

def mozambique(player, provinces):
	player.culture = "Bantu"
	player.provinces["_Mozambique"] = provinces["_Mozambique"]

def tanzania(player, provinces):
	player.culture = "Sukuma"

	player.provinces["_Tanzania"] = provinces["_Tanzania"]

def kenya(player, provinces):
	player.culture = "Bantu"
	player.provinces["_Kenya"] = provinces["_Kenya"]

def ethiopia(player, provinces):
	player.culture = "Oromo"
	player.provinces["_Ethiopia"] = provinces["_Ethiopia"]
	player.harsh = True


def congo(player, provinces):
	player.culture = "Bantu"
	player.harsh = True
	player.provinces["_Congo"] = provinces["_Congo"]

def madagascar(player, provinces):
	player.culture = "Merina"
	player.harsh = True
	player.provinces["_Madagascar"] = provinces["_Madagascar"]


def new_south_wales(player, provinces):
	player.culture = "Aboriginal"
	player.provinces["New_South_Wales"] = provinces["New_South_Wales"]

def queensland(player, provinces):
	player.culture = "Aboriginal"

	player.provinces["Queensland"] = provinces["Queensland"]

def south_australia(player, provinces):
	player.culture = "Aboriginal"

	player.provinces["South_Australia"] = provinces["South_Australia"]

def west_australia(player, provinces):
	player.culture = "Aboriginal"

	player.provinces["West_Australia"] = provinces["West_Australia" ]

def new_zealand(player, provinces):
	player.culture = "Aboriginal"
	player.provinces["_New Zealand"] = provinces["_New Zealand"]