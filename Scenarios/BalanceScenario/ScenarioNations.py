from player_class import*
from minor_classes import*
from AI import*

from Scenarios.BalanceScenario.Scenario_provinces import*

def bambaki(player, provinces):

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")
#	player.technologies.add("high_pressure_steam_engine")
	player.culture = "Bambaki"


	player.provinces["Fonie"] = provinces["Fonie"]
	player.provinces["Fivne"] = provinces["Fivne"]
	player.provinces["Fiten"] = provinces["Fiten"]
	player.provinces["Sine"] = provinces["Sine"]
	player.provinces["Siten"] = provinces["Siten"]
	player.provinces["Severen"] = provinces["Severen"]

	if type(player) == AI:
		player.resource_priority["dyes"] = 3
		player.improve_province_priority["cotton"] = 1.3
		player.improve_province_priority["dyes"] = 1.1
		player.mid_class_priority["culture"] += 0.2
		player.build_factory_priority["clothing"] = 1.4
		player.resourse_to_keep["dyes"] = 16
		player.personality["Navy"] = 0.78



def hyle(player, provinces):

	player.culture = "Hyle"
	
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

	player.provinces["Foleven"] = provinces["Foleven"] 
	player.provinces["Fotwee"] = provinces["Fotwee"]
	player.provinces["Threlve"] = provinces["Threlve"]
	player.provinces["Fothra"] = provinces["Fothra"]
	player.provinces["Threthre"] = provinces["Threthre"]
	player.provinces["Tothra"] = provinces["Tothra"]
	if type(player) == AI:
		player.mid_class_priority["military"] += 0.1
		player.build_factory_priority["furniture"] = 0.1



def trope(player, provinces):

	player.culture = "Trope"
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


	player.provinces["Niten"] = provinces["Niten"]
	player.provinces["Teetee"] = provinces["Teetee"]
	player.provinces["Teaven"] = provinces["Teaven"]
	player.provinces["Nineven"] = provinces["Nineven"]
	player.provinces["Eateven"] = provinces["Eateven"]
	player.provinces["Seleven"] = provinces["Seleven"]
	if type(player) == AI:
		player.mid_class_priority["government"] += 0.2

def sidero(player, provinces):

	player.culture = "Sidero"

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

	player.provinces["Seele"] = provinces["Seele"]
	player.provinces["Sitwee"] = provinces["Sitwee"]
	player.provinces["Fithee"] = provinces["Fithee"]
	player.provinces["Sifoo"] = provinces["Sifoo"]
	player.provinces["Fivfoo"] = provinces["Fivfoo"]
	player.provinces["Thesee"] = provinces["Thesee"]
	if type(player) == AI:
		player.mid_class_priority["military"] += 0.2
		player.build_factory_priority["parts"] = 1.4
		player.resource_priority["oil"] += 0.3

	


def isorropia(player, provinces):

	player.culture = "Isorropia"


	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


	player.provinces["Nifeenee"] = provinces["Nifeenee"]
	player.provinces["Efetee"] = provinces["Efetee"]
	player.provinces["Sevfif"] = provinces["Sevfif"]
	#player.provinces["Eigsix "] = provinces["Eigsix"] 
	player.provinces["Seasix"] = provinces["Seasix"]
	player.provinces["Eisev"] = provinces["Eisev"]
	if type(player) == AI:
		player.mid_class_priority["management"] += 0.2
		player.resource_priority["rubber"] = 2



def karbouno(player, provinces): #major

	player.culture = "Karbouno"
	#player.capital = "Lazio"

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


	player.provinces["Sevteeve"] = provinces["Sevteeve"]
	player.provinces["Fogaro"] = provinces["Fogaro"]
	player.provinces["Togema"] = provinces["Togema"]	
	player.provinces["Sartarva"] = provinces["Sartarva"]	
	player.provinces["Sifoto"] = provinces["Sifoto"]
	player.provinces["Sisivo"] = provinces["Sisivo"]
	if type(player) == AI:
		player.mid_class_priority["research"] += 0.2
		player.build_factory_priority["chemicals"] = 1.4
		player.resource_priority["spice"] = 2


def situs(player, provinces):  
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

	player.culture = "Situs"
	player.provinces["Enee"] = provinces["Enee"]
	player.provinces["Tennini"] = provinces["Tennini"]


def hythen(player, provinces): 
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


	player.culture = "Hythen"
	player.provinces["Perma"] = provinces["Perma"]
	player.provinces["Urten"] = provinces["Urten"]



def intero(player, provinces): # major power
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

	player.culture = "Intero"
	player.provinces["Tomski"] = provinces["Tomski"]
	player.provinces["Teetsito"] = provinces["Teetsito"]


def kora(player, provinces): # old_minor
	#Portugal
	player.culture = "Kora"
	player.provinces["Irku"] = provinces["Irku"]
	player.provinces["Yakutsk"] = provinces["Yakutsk"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


def southo(player, provinces): # adv minor
	#Sweden
	player.culture = "Southo"
	
	player.provinces["Okho"] = provinces["Okho"]
	player.provinces["Findee"] = provinces["Findee"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")


def cindra(player, provinces): #ad minor
	player.culture = "Cindra"

	player.provinces["Napa"] = provinces["Napa"]
	player.provinces["Lazo"] = provinces["Lazo"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

	
def estos(player, provinces): #adv minor
	player.culture = "Estos"
	player.provinces["Vene"] = provinces["Vene"]
	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")
	player.provinces["Eta"] = provinces["Eta"]


def lian(player, provinces): # Old minor
	#Egypt
	player.culture = "Lian"

	player.provinces["Silseva"] = provinces["Silseva"]
	player.provinces["Bosa"] = provinces["Bosa"]

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

def bulgo(player, provinces): #old minor
	player.culture = "Bulgo"

	player.provinces["Garia"] = provinces["Garia"]
	player.provinces["Sebia"] = provinces["Sebia"]

	player.technologies.add("pre_industry_2")
	player.technologies.add("pre_industry_3")

def kaygree(player, provinces): # old minor
	#Morocco
	player.culture = "Kaygree"
	player.provinces["Tura"] = provinces["Tura"]
	player.provinces["Grayto"] = provinces["Grayto"]


def kish(player, provinces): #old minor
	player.culture = "Kish"
	player.provinces["EastKish"] = provinces["EastKish"]
	player.provinces["WestKish"] = provinces["WestKish"]

def rabus(player, provinces): #old minor
	player.culture = "Rabus"
	player.provinces["EastRabus"] = provinces["EastRabus"]
	player.provinces["WestRabus"] = provinces["WestRabus"]


def sparko(player, provinces): #old minor
	player.culture = "Sparko"
	player.provinces["EastSparko"] = provinces["EastSparko"]
	player.provinces["WestSparko"] = provinces["WestSparko"]


def argos(player, provinces): # Old Empire
	player.culture = "Argos"

	player.provinces["NorthArgos"] = provinces["NorthArgos"]
	player.provinces["SouthArgos"] = provinces["SouthArgos"]


def mancha(player, provinces): #old minor
	player.culture = "Mancha"
	player.provinces["NorthMancha"] = provinces["NorthMancha"]
	player.provinces["SouthMancha"] = provinces["SouthMancha"]


def gelder(player, provinces):
	player.culture = "Gelder"
	player.provinces["NorthGelder"] = provinces["NorthGelder"]
	player.provinces["SouthGelder"] = provinces["SouthGelder"]



def porta(player, provinces):
	player.culture = "Porta"

	player.provinces["NorthPorta"] = provinces["NorthPorta"]
	player.provinces["SouthPorta"] = provinces["SouthPorta"]


def norra(player, provinces):
	player.culture = "Norra"
	player.provinces["WestNorra"] = provinces["WestNorra"]
	player.provinces["EastNorra"] = provinces["EastNorra"]

	#Burma 
def wego(player, provinces):
	player.culture = "Wego"
	player.provinces["WestWego"] = provinces["WestWego"]
	player.provinces["EastWego"] = provinces["EastWego"]


def arbaca(player, provinces): 
	player.culture = "Arbaca"

	player.provinces["WestArbaca"] = provinces["WestArbaca"]
	player.provinces["EastArbaca"] = provinces["EastArbaca"]
	
def egaro(player, provinces):
	player.culture = "Egaro"

	player.provinces["WestEgaro"] = provinces["WestEgaro"]
	player.provinces["EastEgaro"] = provinces["EastEgaro"]
