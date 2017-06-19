# Scenario 
def.historical()



	def initiate_provinces:
		total_provinces = []

		new = Province(name, res, qual, "core", player.name)
			player.provinces[name] = new

		England1 = Province("England1", "food", 1.2, "England")
		total_provinces.append(England1)
		England2 = Province("England2", "iron", 1.1, "England")
		total_provinces.append(England2)
		England3 = Province("England3", "coal", 1.3, "England")
		total_provinces.append(England3)
		England4 = Province("England4", "coal", 1.1, "England" )
		total_provinces.append(England4)
		England5 = Province("England5", "cotton", 0.65, "England")
		total_provinces.append(England5)

		France1 = Province("France1", "food", 1.4, "France")
		total_provinces.append(France1)
		France2 = Province("France2", "food", 1.2, "France" )
		total_provinces.append(France2)
		France3 = Province("France3", "cotton", 1.1, "France")
		total_provinces.append(France3)
		France4 = Province("France4", "iron", 0.9, "France")
		total_provinces.append(France4)
		France5 = Province("France5", "dyes", 0.7, "France")
		total_provinces.append(France5)
		France6 = Province("France6", "coal", 0.8, "France")

		





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



