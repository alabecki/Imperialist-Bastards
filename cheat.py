from technologies import technology_dict


def Create_Uber_Player(player):
	player.stability = 2.0
	player.AP = 10
	player.POP = 17.25
	player.freePOP = 10
	player.milPOP = 2.25

	player.midPOP["researchers"]['number'] = 1
	player.midPOP["officers"]['number'] = 1
	player.midPOP["bureaucrats"]['number'] = 1
	player.midPOP["artists"]['number'] = 1
	player.midPOP["managers"]['number'] = 1

	player.numMidPOP = 5.0

	player.technologies.add("pre_industry_2")

	player.resources["gold"] = 20.0
	player.resources["food"] = 20.0
	player.resources["iron"] = 20.0
	player.resources["wood"] = 20.0
	player.resources["coal"] = 20.0
	player.resources["cotton"] = 20.0
	player.resources["spice"] = 20.0
	player.resources["dyes"] = 10.0

	player.goods["parts"] = 5.0
	player.goods["clothing"] = 5.0
	player.goods["paper"] = 5.0
	player.goods["cannons"] = 5.0
	player.goods["furniture"] = 5.0


	player.military["infantry"] = 4.0
	player.military["cavalry"] = 3.0
	player.military["artillery"] = 3.0
	player.military["frigates"] = 5.0


	player.numLowerPOP = 12.25

	player.new_development = 3.0
	player.research = 5.0
	player.diplo_action = 5.0


	player.number_units = 15.0

	player.colonization = 2.0

def assign_to_all_provinces(player):
	for k, p in player.provinces.items():
		if p.worked == False and player.freePOP >= 1.0:
			print(p.name)
			p.worked = True
			print("check2")
			player.freePOP -= 1.0
