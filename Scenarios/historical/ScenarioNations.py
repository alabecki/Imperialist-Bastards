from player_class import*
from minor_classes import*
from AI import*

def england(player, provinces):
	player.colour = "firebrick3"
	player.developments["government"] = 1

	#player.technologies.add("high_pressure_steam_engine")
	player.culture = "English"
	player.accepted_cultures.add("Scottish")
	player.capital.add("SouthEastEngland")
	player.military["artillery"] = 0.0
	player.military["frigates"] = 2.0
	player.colonization = 1
	player.new_development = 3
	player.development_level = 2
	#player.diplo_action = 10
	#player.resources["food"] = 5
	#player.resources["spice"] = 2
	#player.goods["clothing"] = 3
	#player.goods["furniture"] =3
	#player.goods["paper"] = 3
	player.goods["parts"] = 1
	#player.goods["cannons"] = 4
	#player.research = 8
 
	player.provinces["SouthEastEngland"] = provinces["SouthEastEngland"]
	player.provinces["SouthWestEngland"] = provinces["SouthWestEngland"]
	player.provinces["Midlands"] = provinces["Midlands"]
	player.provinces["Whales"] = provinces["Whales"]
	player.provinces["NorthEngland"] = provinces["NorthEngland"]
	player.provinces["Scotland"] = provinces["Scotland"]
	player.provinces["Ireland"] = provinces["Ireland"]


	player.objectives = {"SouthEastEngland", "SouthEastEngland", "Midlands", "Whales", "NorthEngland", \
	"Scotland", "Ireland", "Bombay", "_Bengal", "_Hyderabad", "UpperEgypt", "MiddleEgypt", 
	"United_Provinces", "Rajputana", "Madres", "Nagpur", "_Burma", "_Malaysia", \
	"Iraq", "Guangdong", "Punjab", "Central_India"}


	if type(player) == AI:
		player.diplo_action = 1
		player.personality["Army"] = 1.15
		player.personality["Navy"] = 0.95
		player.improve_province_priority["shipyard"] = 99
		player.personality["Offensive"] = 0.55
		player.build_factory_priority["parts"] = 2
		player.build_factory_priority["clothing"] = 1.7
		player.resource_priority["cotton"] = 1.7
		player.resource_priority["dyes"] = 1.7
		player.improve_province_priority["cotton"] = 1.3
		player.improve_province_priority["dyes"] = 1
		player.sphere_targets = {"Netherlands", "Sweden", "Denmark", "Persia", "Portugal"}
		player.mid_class_priority["government"] += 0.1
		player.resourse_to_keep["dyes"] = 18
		player.resourse_to_keep["cotton"] = 18
		player.resources["cotton"] = 2



def france(player, provinces):
	player.colour = "navy"

	player.developments["culture"] = 1
	player.development_level = 2
	player.culture = "French"
	player.capital.add("CentralFrance")


	player.provinces["Loire"] = provinces["Loire"] 
	player.provinces["Champagne"] = provinces["Champagne"]
	player.provinces["Brittany"] = provinces["Brittany"]
	player.provinces["CentralFrance"] = provinces["CentralFrance"]
	player.provinces["Aquitaine"] = provinces["Aquitaine"]
	player.provinces["Alps"] = provinces["Alps"]
	player.provinces["Normandy"] = provinces["Normandy"]

	player.resources["gold"] = 18
	player.new_development = 2


	if type(player) == AI:
		player.diplo_action = 1
		player.personality["Army"] = 1.28
		player.personality["Navy"] = 0.8
		player.personality["Offensive"] = 0.4
		player.sphere_targets = {"Spain", "Denmark", "Portugal", "Switzerland", "Japan", "Papal States"}
		player.improve_province_priority["shipyard"] = 99
		player.mid_class_priority["culture"] += 0.15
		player.stability = 1.5



	player.objectives = {"Loire", "Champagne", "Brittany", "CentralFrance", "Aquitaine", "Alps", \
	"Normandy", "Piedmont", "Wallonie", "Algiers", "Constantine", "_Burma",\
	"Syria", "_Morocco", "South_Morocco", "Laos", "North_Dai_Nam", "South_Dai_Nam", "_Cambodia", "Bombay", \
	"Khuzestan", "Tunis", "_Bengal"} 

	player.sphere = {"Bavaria", "Lazio"}


def germany(player, provinces):
	player.colour = "dark green"

	player.developments["military"] = 1
	player.development_level = 2
	player.new_development = 2
	player.culture = "German"
	player.capital.add("Brandenburg")
	player.stability = 2

	player.POP = 4.6
	player.freePOP = 3.6
	player.numLowerPOP = 4.2

	player.military["frigates"] = 0
	player.military["cavalry"] = 2

	player.colonization = 0

	player.numMidPOP = 0.4
	player.milPOP = 0.6

	player.provinces["EastPrussia"] = provinces["EastPrussia"]
	player.provinces["Brandenburg"] = provinces["Brandenburg"]
	player.provinces["Rhineland"] = provinces["Rhineland"]
	player.provinces["WestPoland"] = provinces["WestPoland"]
	#player.provinces["Saxony"] = provinces["Saxony"]
	#player.provinces["NorthGermany"] = provinces["NorthGermany"]
	#player.provinces["Bavaria"] = provinces["Bavaria"]

	player.doctrines = {"Discipline"}
	player.infantry["attack"] += 0.15
	player.infantry["defend"] += 0.15
	player.artillery["attack"] += 0.1
	player.artillery["defend"] += 0.1
	player.tank["attack"] += 0.2
	player.tank["defend"] += 0.2
	player.cavalry["attack"] += 0.1
	player.cavalry["defend"] += 0.1
 
	if type(player) == AI:
		player.personality["Army"] = 1.35
		player.personality["Navy"] = 0.68
		player.build_factory_priority["paper"] = 1.3
		player.personality["Offensive"] = 0.68
		player.diplo_action = 3
		player.military["artillery"] = 2
		player.milPOP = 0.8
		player.POP = 6.2
		player.freePOP = 4.6
		player.numLowerPOP = 5.8
		player.goods["cannons"] = 3
		player.technologies.add("high_pressure_steam_engine")
		player.resources["gold"] = 18
		player.improve_province_priority["shipyard"] = 28
		player.sphere_targets = {"Denmark", "Switzerland", "Sweden", "Japan", "Ottoman", \
		"Persia", "India", "Austria"}
		player.mid_class_priority["military"] += 0.2
		player.mid_class_priority["management"] += 0.1
		player.stability = 1.5
 	
	player.objectives = {"EastPrussia", "Brandenburg", "_NorthGermany", "_Bavaria", "Rhineland", \
	"_Saxony", "WestPoland", "_Poland", "Wallonie", "_Malaysia", "Bangkok", "Khuzestan", "_Norway"}

	
def saxony(player, provinces):
	player.culture = "German"
	player.capital.add("_Saxony")
	player.colour = "goldenrod"
	
	player.provinces["_Saxony"] = provinces["_Saxony"]
	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01


def northgermany(player, provinces):
	player.culture = "German"
	player.colour = "lime green"
	player.capital.add("_NorthGermany")
	player.provinces["_NorthGermany"] = provinces["_NorthGermany"]
	

def bavaria(player, provinces):
	player.culture = "German"
	player.colour = "cyan"
	player.capital.add("_Bavaria")
	player.provinces["_Bavaria"] = provinces["_Bavaria"]
	
	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01


def austria(player, provinces):
	player.colour = "gold"

	player.developments["culture"] = 1
	player.development_level = 2
	player.new_development = 2
	player.culture = "German"
	player.accepted_cultures = {"Check"}
	player.capital.add("_Austria")
	player.numMidPOP = 0.4
	
	player.resources["food"] = 2

	player.military["frigates"] = 0
	player.military["infantry"] += 1
	
	player.colonization = 0


	player.shipyard = 0
	player.stability = 1.5


	player.provinces["Bohemia"] = provinces["Bohemia"]
	player.provinces["Slovakia"] = provinces["Slovakia"]
	player.provinces["_Austria"] = provinces["_Austria"]
	player.provinces["Hungary"] = provinces["Hungary"]
	#player.provinces["Romania"] = provinces["Romania"]
	player.provinces["Croatia"] = provinces["Croatia"]
	player.provinces["WestUkraine"] = provinces["WestUkraine"]
	player.provinces["Venezia"] = provinces["Venezia"]	


	player.objectives = {"Bohemia", "Slovakia", "_Austria", "Hungary", "Croatia", "Romania", "Wallonie", \
	"_Bavaria", "_Saxony", "Serbia", "Venezia", "WestUkraine"}
	sphere = {"_Saxony"}

	if type(player) == AI:
		player.personality["Army"] = 1.23
		player.personality["Navy"] = 0.5
		player.improve_province_priority["shipyard"] = 7
		player.build_factory_priority["paper"] = 1.2
		player.sphere_targets = {"Spain", "Denmark", "Portugal", "Switzerland", "Egypt", "India", "Persia"}



def russia(player, provinces):
	player.colour = "OrangeRed4"
	player.culture = "Russian"
	player.capital.add("Novgorod")
	player.stability = - 1.0

	#player.sprawl = True

	player.shipyard = 0

	player.military["frigates"] = 0
	player.military["irregulars"] = 1
	player.colonization = -1 

	player.numMidPOP = 0.2

	player.diplo_action = 0

	player.POP = 9.7
	#player.numMidPOP = 0.2
	player.numLowerPOP = 9.5
	player.freePOP = 8.7

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
		player.improve_province_priority["shipyard"] = 8
		player.sphere_targets = {"Ottoman", "Denmark", "Japan", "Korea", "India"}


	player.objectives = {"Ukraine", "Baltic", "Okhotsk", "_Poland", "WestPoland", "WestUkraine", \
	"Finland", "EastKazakhstan", "Yakutsk", "Ural", "Perm", "Moskva", "Novgorod", "Caucasia", "Crimea", \
	"WestKazakhstan", "Manchuria", "Romania"}


def italy(player, provinces): #major
	player.colour = "green2"

	player.culture = "Italian"
	player.capital.add("Piedmont")

	player.diplo_action = 2

	player.POP = 3.6
	player.numLowerPOP = 3.4
	player.freePOP = 2.4
	
	player.resources["gold"] = 8.0
	player.numMidPOP = 0.5

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
		player.sphere_targets = {"Spain", "Portugal", "Switzerland", "Japan", "Persia"}
		player.improve_province_priority["shipyard"] = 32


	player.objectives = {"Naples", "Lazio", "Venezia", "Piedmont", "Sicily", "_Libya", "Croatia", \
	"Greece", "UpperEgypt", "MiddleEgypt", "Sudan", "Tunis", "Alps"}


def two_sicilies(player, provinces):
	player.colour = "magenta"
	player.culture = "Italian"
	player.capital.add("Naples")
	player.provinces["Naples"] = provinces["Naples"]
	player.provinces["Sicily"] = provinces["Sicily"]

def papal_state(player, provinces):
	player.colour = "ivory3"
	player.culture = "Italian"
	player.capital.add("Lazio")
	player.provinces["Lazio"] = provinces["Lazio"]



def switzerland(player, provinces):
	player.colour = "MediumPurple1"
	player.culture = "Swiss"
	player.capital.add("_Switzerland")
	player.resources["gold"] = 12
	player.resources["food"] = 2

	player.military["infantry"] = 3
	player.number_units = 3
	player.developments["research"] = 1
	player.development_level = 1
	player.new_development = 1
	player.numMidPOP = 0.2
	player.POP = 3.2
	player.freePOP = 2.4
	player.milPOP = 0.6
	player.numLowerPOP = 3

 
	player.provinces["_Switzerland"] = provinces["_Switzerland"]


	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.001
		player.improve_province_priority["shipyard"] = 0.01



def ottoman(player, provinces):  
	player.colour = "DarkOrchid2"

	player.culture = "Turkish"
	player.capital.add("WestTurky")
	player.resources["gold"] = 3
	player.technologies = {"basic_civ", "pre_modern"}


	player.military["artillery"] = 0.0

	player.number_units = 4.0
	player.diplo_action = 0.0

	player.shipyard = 0
	player.new_development = 0
	player.stability = -1
	player.development_level = 0
	player.developments["research"] = 0

	player.colonization = -3
	player.milPOP = 0.8
	player.POP = 8
	player.numLowerPOP = 8
	player.freePOP = 8
	player.numMidPOP = 0

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.6
	
	player.borders.add("Austria")
	player.borders.add("Russia")
	player.borders.add("Egypt")
	player.borders.add("Nejd")
	player.borders.add("Persia")

	#player.provinces["Bosnia"] = provinces["Bosnia"]
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
		player.improve_province_priority["shipyard"] = 9
		player.sphere_targets = {"Tunis", "Libya", "Algeria", "Egypt"}



	player.objectives = {"Bulgaria", "Serbia", "Greece", "WestTurky", "CentralTurky", "EastTurky", \
	"Syria", "Iraq", "UpperEgypt", "MiddleEgypt", "_Libya", "Tunis", "Hungary", "Romania", "_Austria", \
	"Crimea", "_Nejd", "Khuzestan"}


def spain(player, provinces): 
	player.colour = "yellow"

	player.culture = "Spanish"
	player.capital.add("Leon")

	player.colonization = 0 
	player.POP = 7
	player.numLowerPOP = 7
	player.freePOP = 6
	player.numMidPOP = 0

	player.resources["gold"] = 6

	player.developments["research"] = 0
	player.development_level = 0

	player.provinces["Andalusia"] = provinces["Andalusia"]
	player.provinces["Leon"] = provinces["Leon"]
	player.provinces["Aragon"] = provinces["Aragon"]	
	player.provinces["Galicia"] = provinces["Galicia"]
	player.provinces["La_Mancha"] = provinces["La_Mancha"]

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.9
		player.personality["Offensive"] = 0.60
		player.improve_province_priority["shipyard"] = 32
		player.sphere_targets = {"Spain", "Sweden", "Denmark", "Portugal", "Switzerland", "Japan"}


	player.objectives = {"Andalusia", "Leon", "Aragon", "Galicia", "La_Mancha", "_Morocco", "South_Morocco", \
	"NorthPhilippines", "SouthPhilippines", "_Portugal", "Sicily", "Naples", "Wallonie", "_Brunei", "Madres"}



def netherlands(player, provinces): # major power
	player.colour = "orange"

	player.culture = "Dutch"
	player.capital.add("Holland")

	player.resources["spice"] = 1



	player.military["artillery"] = 0
	player.military["frigates"] = 2
	player.development_level = 1

	player.POP = 5.7
	player.freePOP = 4.5
	player.numLowerPOP = 5.5
	player.numMidPOP = 0.2

	player.provinces["Holland"] = provinces["Holland"]
	#player.provinces["Gelderland"] = provinces["Gelderland"]
	player.provinces["Wallonie"] = provinces["Wallonie"]

	if type(player) == AI:
		player.personality["Army"] = 1.2
		player.personality["Navy"] = 0.9
		player.improve_province_priority["shipyard"] = 99
		player.personality["Offensive"] = 0.35
		player.resource_priority["spice"] = 2.2
		player.sphere_targets = {"Denmark", "Portugal", "Switzerland", "Ottoman", "Persia", "China"}
		#player.mid_class_priority["researchers"] += 0.1

	player.objectives = {"Holland", "Wallonie", "Rhineland", "Sumatra", "_Brunei",  \
	"_Bali", "_Java", "Madres", "Bombay"}



def portugal(player, provinces): # old_minor
	#Portugal
	player.culture = "Portuguese"
	player.colour = "dark olive green"


	player.resources["gold"] = 10.0
	player.resources["spice"] = 2

	if type(player) == AI:
		player.personality["Navy"] = 1
		player.personality["Army"] = 1.25
		player.improve_province_priority["shipyard"] = 99



	player.military["calvary"] = 1
	player.military["frigates"] = 2

	player.POP = 3.8
	player.freePOP = 2.8
	player.milPOP = 1.0
	player.numLowerPOP = 3.8
	player.colonization = 0.5

	player.shipyard = 1

	player.capital.add("_Portugal")

	player.borders.add("Spain")
	player.provinces["_Portugal"] = provinces["_Portugal"]


	player.number_units = 3

	player.colonization = 1
	player.diplo_action = 1

	player.objectives = {"_Nejd", "Madres", "Bombay", "Guangdong", "_Java", "South_Morocco"}


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
	player.colour = "deep sky blue"

	player.capital.add("Ostlandet")
	player.culture = "Swedish"
	
	player.military["infantry"] = 3.0
	player.milPOP = 0.6
	player.number_units = 3

	player.development_level = 0
	player.numMidPOP = 0.5
	player.POP = 4.8
	player.numLowerPOP = 4.3
	player.freePOP = 3.7

	
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
	player.capital.add("_Denmark")
	player.colour = "saddle brown"

	player.provinces["_Denmark"] = provinces["_Denmark"]
	player.objectives = {"_Norway", "_NorthGermany"}


def egypt(player, provinces): # Old minor
	#Egypt
	player.colour = "coral"
	player.culture = "Arab"
	player.capital.add("UpperEgypt")
	player.POP = 4.8
	player.numLowerPOP = 4.8
	player.freePOP = 4
	player.milPOP = 0.6
	player.military["infantry"] = 4
	.0

	
	player.provinces["UpperEgypt"] = provinces["UpperEgypt"]
	player.provinces["MiddleEgypt"] = provinces["MiddleEgypt"]
	player.provinces["Sudan"] = provinces["Sudan"]

	objectives = {"UpperEgypt", "MiddleEgypt", "Sudan", "_Libya", "Syria", "Iraq", "_Nejd", "Tunis"}


def algeria(player, provinces): #old minor

	player.capital.add("Algiers")
	player.culture = "Arab"
	player.colour = "SlateBlue3"

	player.provinces["Algiers"] = provinces["Algiers"]
	player.provinces["Constantine"] = provinces["Constantine"]


def morocco(player, provinces): # old minor
	#Morocco
	player.culture = "Arab"
	player.colour = "peach puff"
	player.capital.add("_Morocco")
	player.provinces["_Morocco"] = provinces["_Morocco"]
	player.provinces["South_Morocco"] = provinces["South_Morocco"]


def tunisia(player, provinces): #old minor
	player.culture = "Arab"
	player.colour = "yellow4"
	player.capital.add("Tunis")
	player.provinces["Tunis"] = provinces["Tunis"]

def libya(player, provinces): #old minor
	player.colour = "sea green"
	player.culture = "Arab"
	player.capital.add("_Libya")
	player.provinces["_Libya"] = provinces["_Libya"]

def kazakhstan (player, provinces): #old minor
	player.culture = "Kazak"
	player.colour = "deep sky blue"
	player.capital.add("WestKazakhstan")
	player.provinces["WestKazakhstan"] = provinces["WestKazakhstan"]
	player.provinces["EastKazakhstan"] = provinces["EastKazakhstan"]


def persia(player, provinces): # Old Empire
	player.colour = "saddle brown"

	player.culture = "lemon chiffon"
	player.capital.add("Tehran")

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
		player.personality["Navy"] = 0.3
		player.sphere_targets = {"Afghanistan", "Nejd"}
		player.personality["Offensive"] = 0.35


	player.objectives = {"Khorasan", "Khuzestan", "Fars", "Isfahan", "Khorasan", "Iraq", "Syria", \
	"_Afghanistan", "Caucasia", "Punjab", "UpperEgypt", "_Nejd"}


def nejd(player, provinces): #old minor
	player.culture = "Arab"
	player.colour = "green4"
	player.capital.add("_Nejd")
	player.provinces["_Nejd"] = provinces["_Nejd"]


def afghanistan(player, provinces):
	player.colour = "gray8"
	player.culture = "Afghan"
	player.capital.add("_Afghanistan")
	player.provinces["_Afghanistan"] = provinces["_Afghanistan"]
	player.fortification = 1.1


def india(player, provinces): # Old Empire
	player.colour = "purple"

	player.culture = "Indian"
	player.capital.add("Central_India")
	player.colonization = -3 
	player.POP = 10
	player.numLowerPOP = 10
	player.freePOP = 9
	player.numMidPOP = 0
	player.stability = -1.5

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
		player.improve_province_priority["shipyard"] = 3
		player.sphere_targets = {"Burma", "Cambodia"}
		player.personality["Offensive"] = 0.3
		player.build_factory_priority["clothing"] = 1.7




	player.objectives = {"Punjab", "United_Provinces", "Rajputana", "Central_India", "Bombay", \
	"Madres", "Nagpur", "_Bengal", "_Hyderabad", "_Burma", "_Afghanistan"}


def bengal(player, provinces):
	player.culture = "Indian"
	player.capital.add("_Bengal")
	player.colour = "DarkOliveGreen1"

	player.provinces["_Bengal"] = provinces["_Bengal"]

def hyderabad(player, provinces):
	player.colour = "sandy brown"
	player.culture = "Indian"
	player.capital.add("_Hyderabad") 
	player.provinces["_Hyderabad"] = provinces["_Hyderabad"]
	#Burma 
def burma(player, provinces):
	player.colour = "chartreuse4"
	player.culture = "Bamar"
	player.capital.add("_Burma")
	player.fortification = 1.1

	player.provinces["_Burma"] = provinces["_Burma"]

def siam(player, provinces): 
	player.capital.add("Bangkok")
	player.culture = "Thai"
	player.colour = "ivory4"
	player.provinces["Bangkok"] = provinces["Bangkok"]
	player.provinces["Laos"] = provinces["Laos"]
	
def dai_nam(player, provinces):
	player.capital.add("North_Dai_Nam")
	player.culture = "Vietnamese"
	player.colour = "yellow2"

	player.provinces["North_Dai_Nam"] = provinces["North_Dai_Nam"]
	player.provinces["South_Dai_Nam"] = provinces["South_Dai_Nam"]


def cambodia(player, provinces):
	player.culture = "Cambodian"
	player.colour  = "red3"
	player.capital.add("_Cambodia") 
	player.provinces["_Cambodia"] = provinces["_Cambodia"]

	#Singapore
	#Singapore = Province("Singapore", "rubber", 1.1, "Singapore")
def brunei(player, provinces):
	culture = "Brunei"
	player.colour = "yellow3"
	player.capital.add("_Brunei") 
	player.provinces["_Brunei"] = provinces["_Brunei"]

def java(player, provinces):
	player.colour = "orange4"
	player.culture = "Javanese"
	player.capital.add("_Java")
	player.provinces["_Java"] = provinces["_Java"]
	player.resources["spice"] = 1


def malaysia(player, provinces): 
	player.culture = "Malaysian"
	player.capital.add("_Malaysia")
	player.colour = "dark khaki"
	
	player.provinces["_Malaysia"] = provinces["_Malaysia"]
	
	player.provinces["Sumatra"] = provinces["Sumatra"]
	#player.provinces["Singapour"] = provinces["Singapour"]
	player.resources["spice"] = 1



def	bali(player, provinces):
	player.culture = "Bali"
	player.colour = "misty rose"
	player.capital.add("_Bali")
	player.provinces["_Bali"] = provinces["_Bali"]
	player.resources["spice"] = 1



def philippines(player, provinces):
	player.culture = "Filipino"
	player.capital.add("NorthPhilippines")
	player.colour = "HotPink1"
	
	player.provinces["NorthPhilippines"] = provinces["NorthPhilippines"]
	player.provinces["SouthPhilippines"] = provinces["SouthPhilippines"]


def china(player, provinces):
	player.colour = "red4"

	player.capital.add("Liaoning")
	player.culture = "Chinese"

	player.military["irregulars"] = 5
	player.milPOP = 1.2
	player.POP = 11.2
	player.numLowerPOP = 11.2
	player.freePOP = 10
	player.stability = -2

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
		player.improve_province_priority["shipyard"] = 5


	player.objectives = {"Manchuria", "Guangxi", "Guangdong", "Hunan", "Mongolia", "Jiangsu", "Qinghai", \
	"Shanxi", "Sichuan", "Zhejiang", "Liaoning", "North_Dai_Nam", "South_Dai_Nam", "Okhotsk"}


def korea(player, provinces):
	player.culture = "Korean"
	player.capital.add("Pyongyang")
	player.colour = "SpringGreen3"
	
	player.provinces["Pyongyang"] = provinces["Pyongyang"]
	player.provinces["Sariwon"] = provinces["Sariwon"]
	player.provinces["Seoul"] = provinces["Seoul"]

def japan(player, provinces): 
	player.colour = "gold2"

	player.POP = 7
	player.freePOP = 6.1
	player.numLowerPOP = 6.5
	player.government = "absolute monarchy"

	player.numMidPOP = 0.5
	player.milPOP = 0.4
	
	player.developments["military"] = 1
	player.development_level = 1



	player.military["irregulars"] = 2.0
	player.military["infantry"] = 1.0
	
	player.infantry["attack"] += 0.25


	player.resources["gold"] = 10

	player.capital.add("Kansai")
	
	player.provinces["Kansai"] = provinces["Kansai"]
	
	player.provinces["Tohoku"] = provinces["Tohoku"]

	player.provinces["Chugoku"] = provinces["Chugoku"]

	player.provinces["Kanto"] = provinces["Kanto"]

	player.provinces["Kyushu"] = provinces["Kyushu"]

	if type(player) == AI:
		player.build_factory_priority["cannons"] += 0.15
		player.personality["Army"] = 1.5
		player.personality["Navy"] = 1
		player.improve_province_priority["shipyard"] = 80
		player.personality["Offensive"] = 0.6



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