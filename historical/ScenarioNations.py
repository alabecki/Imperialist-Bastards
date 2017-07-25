from player_class import*
from minor_classes import*

def england(player, provinces):

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")
	player.technologies.add("high_pressure_steam_engine")
	player.culture = "English"
	player.accepted_cultures.add("Scottish")
	player.capital = "SouthEastEngland"
	player.military["artillery"] = 0
	player.military["frigates"] = 2.0
	player.colonization = 1.0
	player.diplo_action = 1.0

	player.provinces["SouthEastEngland"] = provinces["SouthEastEngland"]
	player.provinces["SouthWestEngland"] = provinces["SouthWestEngland"]
	player.provinces["Midlands"] = provinces["Midlands"]
	player.provinces["Whales"] = provinces["Whales"]
	player.provinces["NorthEngland"] = provinces["NorthEngland"]
	player.provinces["Scotland"] = provinces["Scotland"]
	player.provinces["Ireland"] = provinces["Ireland"]


def france(player, provinces):

	player.culture = "French"
	player.capital = "CentralFrance"
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

	player.midPOP["managers"]["number"] = 0
	player.midPOP["officers"]["number"] = 0.5
	player.colonization = 0


	player.provinces["EastPrussia"] = provinces["EastPrussia"]
	player.provinces["Brandenburg"] = provinces["Brandenburg"]
	player.provinces["Rhineland"] = provinces["Rhineland"]
	player.provinces["WestPoland"] = provinces["WestPoland"]
	player.provinces["Saxony"] = provinces["Saxony"]
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
	player.provinces["WestUkraine"] = provinces["WestUkraine"]


def russia(player, provinces):

	player.culture = "Russian"
	player.capital = "Novgorod"

	player.technologies.add("pre_industry_2")

	player.military["frigates"] = 0
	player.military["irregulars"] = 1
	player.colonization = -3 

	player.midPOP["bureaucrats"]["number"] = 0
	player.midPOP["officers"]["number"] = 0
	player.midPOP["artists"]["number"] = 0
	player.midPOP["researchers"]["number"] = 0

	player.POP = 9
	player.numMidPOP = 0
	player.numLowerPOP = 9
	player.freePOP = 8

	player.provinces["Poland"] = provinces["Poland"]
	player.provinces["Ukraine"] = provinces["Ukraine"]
	player.provinces["Baltic"] = provinces["Baltic"]
	player.provinces["Crimea "] = provinces["Crimea"] 
	player.provinces["Novgorod"] = provinces["Novgorod"]
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
	player.provinces["Finland"] = provinces["Finland"]


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


	player.midPOP["officers"]["number"] = 0
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
	player.military["frigates"] = 1
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
	player.midPOP["officers"]["number"] = 0

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
	player.capital = "Portugal"

	player.borders.add("Spain")
	player.provinces["Portugal"] = provinces["Portugal"]


def sweden(player, provinces): # adv minor
	#Sweden
	player.capital = "Ostlandet"
	player.culture = "Swedish"
	player.technologies.add("pre_industry_2")


	player.midPOP["researchers"]["number"] = 0.25
	player.numMidPOP = 0.25
	player.POP = 3.85
	player.numLowerPOP = 3.6
	player.freePOP = 3

	
	player.provinces["Svealand"] = provinces["Svealand"]
	player.provinces["Norrland"] = provinces["Norrland"]
	player.provinces["Ostlandet"] = provinces["Ostlandet"]


def norway(player, provinces): #ad minor

	player.capital = "Norway"

	player.culture = "Norwegian"
	player.provinces["Norway"] = provinces["Norway"]
	player.technologies.add("pre_industry_2")

	
def denmark(player, provinces): #adv minor
	player.culture = "Danish"
	player.technologies.add("pre_industry_2")
	player.capital = "Denmark"


	player.provinces["Denmark"] = provinces["Denmark"]


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



def algeria(player, provinces): #old minor

	player.capital = "Algiers"
	player.culture = "Arab"

	player.provinces["Algiers"] = provinces["Algiers"]
	player.provinces["Constantine"] = provinces["Constantine"]


def morocco(player, provinces): # old minor
	#Morocco
	player.culture = "Arab"
	player.capital = "Morocco"
	player.provinces["Morocco"] = provinces["Morocco"]
	player.provinces["South_Morocco"] = provinces["South_Morocco"]


def tunisia(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "Tunis"
	player.provinces["Tunis"] = provinces["Tunis"]

def libya(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "Libya"
	player.provinces["Libya"] = provinces["Libya"]

def kazakhstan (player, provinces): #old minor
	player.culture = "Kazak"
	player.capital =  "WestKazakhstan"
	player.provinces["WestKazakhstan"] = provinces["WestKazakhstan"]
	player.provinces["EastKazakhstan"] = provinces["EastKazakhstan"]


def persia(player, provinces): # Old Empire
	player.culture = "Persian"
	player.capital = "Tehran"

	player.POP = 5
	player.numLowerPOP = 5
	player.freePOP = 4

	player.provinces["Khuzestan"] = provinces["Khuzestan"]	
	player.provinces["Fars"] = provinces["Fars"]
	player.provinces["Tehran"] = provinces["Tehran"]
	player.provinces["Isfahan"] = provinces["Isfahan"]
	player.provinces["Khorasan"] = provinces["Khorasan"]


def nejd(player, provinces): #old minor
	player.culture = "Arab"
	player.capital = "Nejd"
	player.provinces["Nejd"] = provinces["Nejd"]


def afghanistan(player, provinces):
	player.culture = "Afghan"
	player.capital = "Afghanistan"
	player.provinces["Afghanistan"] = provinces["Afghanistan"]

def india(player, provinces): # Old Empire

	player.culture = "Indian"
	player.capital = "Central_India"
	player.colonization = -3 
	player.POP = 10
	player.numLowerPOP = 10
	player.freePOP = 9
	player.numMidPOP = 0

	player.provinces["Punjab"] = provinces["Punjab"]

	player.provinces["United_Provinces"] = provinces["United_Provinces"]
	
	player.provinces["Rajputana"] = provinces["Rajputana"]
	
	player.provinces["Central_India"] = provinces["Central_India"]
	
	player.provinces["Bombay"] = provinces["Bombay"]
	
	player.provinces["Madres"] = provinces["Madres"]
	
	player.provinces["Nagpur"] = provinces["Nagpur"]


def bengal(player, provinces):
	player.culture = "Indian"
	player.capital = "Bengal"

	player.provinces["Bengal"] = provinces["Bengal"]

def hyderabad(player, provinces):
	player.culture = "Indian"
	player.capital = "Hyderabad" 
	player.provinces["Hyderabad"] = provinces["Hyderabad"]
	#Burma 
def burma(player, provinces):
	player.culture = "Bamar"
	player.capital  = "Burma"

	player.provinces["Burma"] = provinces["Burma"]

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
	player.capital = "Cambodia" 
	player.provinces["Cambodia"] = provinces["Cambodia"]

	#Singapore
	#Singapore = Province("Singapore", "rubber", 1.1, "Singapore")
def brunei(player, provinces):
	culture = "Brunei"
	player.capital = "Brunei" 

	player.provinces["Brunei"] = provinces["Brunei"]

def java(player, provinces):
	player.culture = "Javanese"
	player.capital = "Java"
	player.provinces["Java"] = provinces["Java"]

def malaysia(player, provinces): 
	player.culture = "Malaysian"
	player.capital = "Malaysia"
	
	player.provinces["Malaysia"] = provinces["Malaysia"]
	
	player.provinces["Sumatra"] = provinces["Sumatra"]


def	sulawesi(player, provinces):
	player.culture = "Sulawesi"
	player.capital = "Sulawesi"
	player.provinces["Sulawesi"] = provinces["Sulawesi"]


def philippines(player, provinces):
	player.culture = "Filipino"
	player.capital = "NorthPhilippines"
	
	player.provinces["NorthPhilippines"] = provinces["SouthPhilippines"]
	player.provinces["SouthPhilippines"] = provinces["SouthPhilippines"]


def china(player, provinces):
	player.capital = "Liaoning"
	player.culture = "Chinese"

	player.military["irregulars"] = 5
	player.milPOP = 1.2
	player.POP = 11.2
	player.numLowerPOP = 11.2
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

def japan(player, provinces): 

	player.POP = 7
	player.freePOP = 6
	player.numLowerPOP = 7

	player.capital = "Kansai"
	
	player.provinces["Kansai"] = provinces["Kansai"]
	
	player.provinces["Tohoku"] = provinces["Tohoku"]

	player.provinces["Chugoku"] = provinces["Chugoku"]

	player.provinces["Kanto"] = provinces["Kanto"]

	player.provinces["Kyushu"] = provinces["Kyushu"]




def mauritania(player, provinces):
	player.culture = "Arab" 
	player.provinces["Mauritania"] = provinces["Mauritania"]
	player.harsh = True


def liberia(player, provinces): 
	player.culture = "Kpelle"
	player.provinces["Liberia"] = provinces["Liberia"]
	player.harsh = True


def mali(player, provinces):
	player.culture = "Bambara"
	player.provinces["Mali"] = provinces["Mali"]
	player.harsh = True


def ghana(player, provinces):
	player.culture = "Akan"
	player.provinces["Ghana"] = provinces["Ghana"]

def niger(player, provinces):
	player.culture = "Hausa"
	player.provinces["Niger"] = provinces["Niger"]
	player.harsh = True


def nigeria(player, provinces):
	player.culture = "Hausa"
	player.harsh = True

	player.provinces["Nigeria"] = provinces["Nigeria"]

def cameroon(player, provinces):
	player.culture = "Cameroon"
	player.harsh = True	
	player.provinces["Cameroon"] = provinces["Cameroon"]

def angola(player, provinces):
	player.culture = "Ovimbundu"
	player.harsh = True	
	player.provinces["Angola"] = provinces["Angola"]

def nambia(player, provinces):
	player.culture = "Bantu"
	player.provinces["Nambia"] = provinces["Nambia"]
	player.harsh = True


def zululand(player, provinces):
	player.capital = "Zululand"
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
	player.harsh = True
	player.provinces["Congo"] = provinces["Congo"]

def madagascar(player, provinces):
	player.culture = "Merina"
	player.harsh = True
	player.provinces["Madagascar"] = provinces["Madagascar"]


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
	player.provinces["New Zealand"] = provinces["New Zealand"]