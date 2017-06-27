# Scenario 
def.historical()



	def initiate_provinces():
		total_provinces = []

		new = Province(name, res, qual, "core", player.name)
			player.provinces[name] = new

		SouthEastEngland = Province("SouthEastEngland", "food", 1.2, "England")
		total_provinces.append(SouthEastEngland)
		SouthWestEngland = Province("SouthWestEngland", "food", 1.0, "England")
		total_provinces.append(SouthWestEngland)
		Midlands = Province("Midlands", "iron", 1.1, "England")
		total_provinces.append(Midlands)
		Whales = Province("Whales", "coal", 1.1, "England" )
		total_provinces.append(Whales)
		NorthEngland = Province("England5", "coal", 1,2, "England")
		total_provinces.append(NorthEngland)

		WestFrance = Province("WestFrance", "cotton", 1.0, "France")
		total_provinces.append(WestFrance)
		EastFrance = Province("EastFrance", "coal", 0.8, "France" )
		total_provinces.append(EastFrance)
		NorthFrance = Province("NorthFrance", "iron", 1.0, "France")
		total_provinces.append(NorthFrance)
		CentralFrance = Province("CentralFrance", "wood", 0.9, "France")
		total_provinces.append(CentralFrance)
		SouthWestFrance = Province("SouthWestFrance", "food", 1.3, "France")
		total_provinces.append(SouthWestFrance)
		SouthEastFrance = Province("SouthEastFrance", "food", 1.4, "France")
		total_provinces.append(SouthEastFrance)

		EastPrussia = Province("EastPrussia", "food", 1.0, "Germany")
		total_provinces.append(EastPrussia)
		Brandenburg = Province("Brandenburg", "iron", 1.1, "Germany")
		total_provinces.append(Brandenburg)
		Rhineland = Province("Rhineland", "coal", 1.6, "Germany")
		total_provinces.append(Rhineland)
		EastPoland = Province("Germany4", "food", 0.9, "Poland")
		total_provinces.append(EastPoland)
		
		NorthGermany = Province("NorthGermany", "food", 1.1, "Germany")
		total_provinces.append(NorthGermany)
		Bavaria = Province("Bavaria", "food", 1.1, "Germany")
		total_provinces.append("Bavaria")



		Bohemia = Provice("Bohemia", "iron", 1.2, "Check")
		total_provinces.append("Bohemia")
		Slovakia  = Province("Slovakia ", "coal", 1.1, "Slovack")
		total_provinces.append("Slovakia")
		Austria = Province("Austria", "food", 1.1, "Austria")
		total_provinces.append("Austria")
		Hungry = Province("Hungry", "food", 1.1, "Hungry")
		total_provinces.append("Hungry")
		Romania = Province("Romania", "food", 0.85, "Romania")
		total_provinces.append("Romania")
		Croatia = Province("Croatia", "wood", 0.9, "Croatia")
		total_provinces.append("Croatia")
		Bosina = Province("Bosina", "food", 0.8, "Bosina")
		total_provinces.append("Bosina")


		Poland = Province("Poland", "food", 0.9, "Poland")
		total_provinces.append("Poland")
		Ukraine = Province("Ukraine", "food", 1.2, "Ukraine")
		total_provinces.append("Ukraine")
		Crimeria = Province("Crimeria", "coal", 1.0, "Russia")
		total_provinces.append("Crimeria")
		Kazack = Province("Kazack", "cotton", 0.85, "Kazack")
		total_provinces.append("Kazack")
		Novgorod = Province("Novgorod", "food", 0.75, "Russia")
		total_provinces.append("Novgorod")
		Moskva = Province("Moskva", "wood", 1.0, "Russia")
		total_provinces.append("Moskva")
		Galich = Province("Galich", "wood", 0.9, "Russia")
		total_provinces.append("Galich")
		Tartaria = Province("Tartaria", "food", 0.7, "Russia")
		total_provinces.append("Tartaria")
		Ural = Province("Ural", "iron", 1.3, "Russia")
		total_provinces.append("Ural")
		Perm = Province("Perm", "wood", 0.75, "Russia")
		total_provinces.append("Perm")
		Caucasia = Province("Caucasia", "cotton", 0.85, "Russia")
		total_provinces.append("Caucasia")
		Tomsk = Province("Tomsk", "coal", 0.85, "Russia")
		total_provinces.append("Tomsk")
		Yakutsk = Province("Yakutsk", "wood", 0.7, "Russia")
		total_provinces.append("Yakutsk")
		Georgia = Province("Georgia", "cotton", 0.9, "Georgia")
		total_provinces.append("Georgia")






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



