
#!/usr/bin/env python3

#/usr/bin/python3

from pprint import pprint
from random import*
from itertools import product, combinations
import sys
import operator
import gc
import os


from name_generator import*

from cheat import*
from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from combat import*
#from naval import*
from commands import*
from start import*
from save import*
from AI import*
from human_turn import*
from AI_turn import*
from globe import*

from Scenarios.historical.Scenario import* 
from Scenarios.BalanceScenario.Scenario import*
#sys.path.insert(0, 'C:\Users\Labecki\Documents\Python\game\historical')

# Main Game Loop

run = True
while True:

	print("####################################################################################################### ")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
	print( "____________________________ Welcome to Imperialist Bastards! ________________________________________ ")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
	print("######################################################################################################## ")
	print(" _____________________________________ Main Menu ______________________________________________________ ")
	print("\n")
	print("_____________________________ Please select one of the following: _____________________________________")
	print("------------------------ --------- Start a Random Game (N) --------------------------------------------")
	print("------------------------------------ Start a Scenario (S)---------------------------------------------- ")
	print("------------------------------------ Load a Saved Game --(L) ------------------------------------------ "    )
	print("-------------------------------------- Options ---------(O) ------------------------------------------- ")
	print("---------------------------------------- Exit ----------(E) ------------------------------------------- " )
	print("_______________________________________________________________________________________________________")

	initial = dict()
	selection = " "
	while selection not in ["N", "S", "L", "O", "E"]:
		selection = input()

	if selection == "N":
		initial = start_game()
	elif selection == "S":

		print("Which Scenario would you like to play?")
		print("(a) Quasi-Historical Scenario")
		print("(b) Fictional Balance Scenario")
		scen = ""
		scen_options = ["a", "(a)", "b", "(b)"]
		while scen not in scen_options:
			scen = input()
		if scen == "a" or scen == "(a)":
			initial = historical()
		if scen == "b" or scen == "(b)":
			initial = balance()
	elif selection == "L":
		name = input("What is the name of the save that you want to load? \n")
		print("Loading %s" % (name))
		state = load_game(name)
		#players = initial["players"]
		#print("Players:")
		players = dict()
		provinces = dict()
		relations = dict()
		#uncivilized_minors = dict()
		market = Market 
		for k, v in state.items():
			if type(v) == AI or type(v) == Human:
				players[k] = v
			if type(v) == Province:
				provinces[k] = v
			if type(v) == Relation:
				relations[k] = v
			if k == "relations":
				relations = v
			if k == "market":
				market = deepcopy(v)
			if k == "provinces":
				provinces = v
		copy_state = deepcopy(list(state.keys()))
		for k in copy_state:
			del state[k]
		del state
		del copy_state
	
		initial = {"players": players, "provinces": provinces, "relations": relations, "market": market}

		#for k, v in players.items():
		#	print(k, v)
	elif selection == "O":
		print("Did you really think we were going to give you options? \n")
		print("Maybe we will give you some options someday... \n")
	elif selection == "E":
		print("Good bye. Feel free to come back when you are in the mood for exploits and conquests \n")
		sys.exit(0)

	players = initial["players"]
	provinces = initial["provinces"]
	relations = initial["relations"]
	#uncivilized_minors = initial["uncivilized_minors"]
	market = initial["market"]
	#globe = initial["globe"]

	AUTO_SAVE = False
	auto_name = "auto_save"
	print("\n")
	print("Would you like to turn auto save on? (y/n) \n")
	auto = input()
	if auto == "y":
		AUTO_SAVE = True
		print("Please choose a name for the auto save file ...")
		auto_name = input()
		print("Saving game as %s ....." % (auto_name))
		save_game(auto_name, players, relations, market, provinces)



	def AI_turnS(auto_save, players, relations, market, provinces):
		market.turn +=1
		order = list(players.keys())
		shuffle(order)
		for k, v in market.market.items():
			for i in v:
				if i.owner not in players.keys():
					market.market[k].remove(i)
					del i
		for o in order:
			if o not in players.keys():
				continue
			if type(players[o]) == AI:
				AI_turn(players, players[o], market, relations, provinces)
			else:
				player = players[o]

			for k in player.goods_produced.keys():
				player.goods_produced[k] = 0
		gc.collect()
		
		if auto_save != "":
	
			#if market.turn % 2 == 1:

			print("Saving....\n")
			save_game(auto_save, players, relations, market, provinces)

						


	_continue = True
	while(_continue == True):
		
		market.turn +=1
		print("\n Turn: %s \n" % (market.turn))
		print("|-------------------------- Market --------------------------|")
		#print("Gold in market: %s \n" % (market.gold))
		for k1,k2 in zip(market.resources, market.goods):
			print( " %-20s: %-5.2f      %-20s: %-5.2f" % (k1, len(market.market[k1]), k2, len(market.market[k2])))
		#for k in market.market_keys:
		#for k, v in market.market.items():
	#		print (k, len(market.market[k]))
		print("Players len: %s " % (len(players.keys())))
		print("Prov len: %s" % (len(provinces.keys())))
		print("Relations len %s" % (len(relations.keys())))
		print("\n")
		print("< Press Enter >")
		cont = input()
		order = list(players.keys())
		print("order len %s" % (len(order)))
		shuffle(order)
		for k, v in market.market.items():
			for i in v:
				if i.owner not in players.keys():
					market.market[k].remove(i)
					del i
		for o in order:
			if o not in players.keys():
				continue
			if type(players[o]) == AI:
				AI_turn(players, players[o], market, relations, provinces)
			else:
				player = players[o]

	

		#for player in players.values():
		#	if type(player) == AI:
		#		AI_turn(players, player, market, turn)
		#	if type(player) == Human:

				for k in player.goods_produced.keys():
					player.goods_produced[k] = 0



				print("############################################################################################################### \n ")
				print("%s, it is your turn to exploit the globe for the greatness of your nation! \n" % (player.name))
				while(True):
					print(" ######################################################################################################## \n")
					

					#count = 1
					#if count > 1:
				#		for k in player.goods_produced.keys():
				#			player.goods_produced[k] = 0
				#	count +=1
					print("Turn: %s" %(market.turn))
					player.calculate_access_to_goods(market)
					print("%s, what is your imperial decree? \n" % (player.name))
					print("AP: %s    " % (player.AP))
					for i in commands:
						print(i)
					print("help: (h)")
				
					#for key, value in commands.items():
					#	print(key, value)
					command = ""
					#while (command not in commands.keys()):
					while command not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "h"]:
						command = input()
					if command == "1":
						print("What would you like to know? ################################################################################\n")
						for i in information:
							print(i)
						info_command = " "
						while info_command not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
							info_command = input()
						if info_command == "1":
							print("\n")
							print(" Currently, your glorious empire has: ###################################################################\n")
							print(" Gold: %-12.2f             Stability %-12.2f          Action Points: %-12.2f" % \
							(player.resources["gold"], player.stability, player.AP))
							print(" Culture Points: %-12.2f   Diplo Points: %-12.2f      Science Points: %-12.2f" % \
							(player.culture_points, player.diplo_action, player.research))
							print(" Col Points: %-12.2f       Num of colonies: %-12.s   Col. Points needed: %-12s" % \
							(player.colonization, player.num_colonies, player.num_colonies * 1.5)) 
							print(" Free POPS: %-12.2f        Population: %-12.2f        Mid Pops: %-12.2f" % \
							(player.freePOP, player.POP, player.numMidPOP))
							print(" Dev Points: %-12.2f       Dev Level: %-12.2f         Reputation: %-12.2f" %  \
							(player.new_development, player.number_developments, player.reputation))
					

							print("\n")
							print(" Factories:")   
							f_key_one = ["parts", "cannons", "clothing", "paper", "furniture", "chemicals"]
							f_key_two = ["gear", "telephone", "radio", "auto", "fighter", "tank"]
							for k1, k2 in zip(f_key_one, f_key_two):
								print(" %-12s  Level: %-6.2f  Used: %-12s   %-12s  Level: %-6.2f  Used: %-6s" % \
								(k1, player.factories[k1]["number"], player.factories[k1]["used"], k2, player.factories[k2]["number"], player.factories[k2]["used"]))
							#for k, v in player.factories.items():
							#	print("%22s: Level: %.2f, Used %-8s" k,v["number"], v["used"])
							print("\n")
							print(" Objectives:")
							for o in player.objectives:
								if o not in player.provinces.keys():
									print(o, end = ", ")
							print("\n")
							print(" CBs:----------------------------------")
							for cb in player.CB:
								print(cb.province, cb.opponent)
							if len(player.CB) == 0:
								print("None")
							print(" You are currently embargoed by:")
							if len(player.embargo) == 0:
								print("None")
							for e in player.embargo:
								print(e, end = " ")
							print("\n")


						if info_command == "2":
							print("\n")
							print(" Province Overview: ######################################################################################## \n")
							for k, province in player.provinces.items():
								print(" %-16s 	Res: %s 	Dev Level: %s 	Worked?: %s 	Quality: %.2f    Culture: %s" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality, province.culture))
						if info_command == "3":
							print("\n")
							print(" Population Overview: ####################################################################################### \n")
							print(" Total Population: %.2f 	    Unassigned Pops: %.2f 	Lower Class Pops: %.2f 	Development Level: %.2f \n" % \
							(player.POP, player.freePOP, player.numLowerPOP, player.development_level))
							print(" Urban Worker Pops: %.2f 	Military Pops: %.2f \n" % (player.proPOP, player.milPOP))
							print("Development Levels")
							for d, dev in player.developments.items():
								print("%-12s: %-12.2f" % (d, dev))
							#for k, v in player.midPOP.items():
							#	print(" %-12s: %-12.2f"  % (k, v["number"]))
						if info_command == "4" :
							print("\n")
							print(" Military Overview: ################################################################################################")
							print("\n")
							print("Infantry -   Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" %  \
								(player.military["infantry"],player.infantry["attack"], player.infantry["defend"], player.infantry["manouver"]))
							print("Cavalry -    Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(player.military["cavalry"],  player.cavalry["attack"], player.cavalry["defend"], player.cavalry["manouver"]))
							print("Artillery -  Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(player.military["artillery"], player.artillery["attack"], player.artillery["defend"], player.artillery["manouver"]))
							print("Fighter -    Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(player.military["fighter"], player.fighter["attack"], player.fighter["defend"], player.fighter["manouver"]))
							print("Tank -       Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(player.military["tank"], player.tank["attack"], player.tank["defend"], player.tank["manouver"]))
							print("Frigate -    Num: %.2f   Att: %.2f" % (player.military["frigates"], player.frigates["attack"]))
							print("Ironclad -   Num: %.2f   Att: %.2f" % (player.military["iron_clad"], player.iron_clad["attack"]))
							print("Battleship - Num: %.2f   Att: %.2f" % (player.military["battle_ship"], player.battle_ship["attack"]))
							print("\n")
							
							ammo_needed = calculate_ammo_needed(player)
							oil_needed = calculate_oil_needed(player)
							print("Ammo (number of cannons) needed for land combat: %-24s" % (ammo_needed))
							print("Oil Needed for land combat: %-24s" % (oil_needed))
							ammo_navy_needed = calculate_ammo_needed_navy(player)
							oil_navy_needed = calculate_oil_needed_navy(player)
							print("Ammo (number of cannons) needed for naval combat: %-24s" % (ammo_navy_needed))
							print("Oil Needed for naval combat %-24s" % (oil_navy_needed))


						if info_command == "5":
							print("\n")
							print("Inventory: ##########################################################################################################\n")
							for (k1,v1), (k2,v2) in zip(player.resources.items(), player.goods.items()):
								print(" %-10s: %-8.2f        %-10s: %-8.2f" % (k1, v1, k2, v2))

						#	for k in market.resources:
							#for k, v in player.resources.items():
						#		print(" %s: %.2f " % (k, player.resources[k]) )
							#for k, v in player.goods.items():
						#	for k in market.goods:
						#		print(" %s: %.2f " % (k, player.goods[k]) )
						if info_command == "6":
							player.view_inventory_production_needs()
						if info_command == "7":
							for k, v in foreign_intelligence.items():
								print (k, v)
							which = input()
							if which == "1":
								for i in range(int(len(players.keys())/5+1)):
									print("    ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
								nation = input("Please input the NAME of the nation you would like to view \n")
								nation = players[nation]
								print("Information Report on %s: ###################################################################\n" % (nation.name))
										#print("Gold: %s 				Action Points: %s \n" % (player.gold, player.AP))								
								print(" Gold: %-12.2f             Population %-12.2f         Action Points: %-12.2f" % \
								(nation.resources["gold"], nation.POP, nation.AP))
								print(" Culture Points: %-12.2f   Diplo Points: %-12.2f      Science Points: %-12.2f" % \
								(nation.culture_points, nation.diplo_action, nation.research))
								print(" Col Points: %-12.2f       Num of colonies: %-12.3f   Col. Points needed: %-12s" % \
								(nation.colonization, nation.num_colonies, nation.num_colonies * 1.5)) 
								print(" Free POPS: %-12.2f        Low Pops: %-12.2f          Mid Pops: %-12.2f" % (nation.freePOP, nation.numLowerPOP, nation.numMidPOP))
								print(" Dev Points: %-12.2f       Dev Level: %-12.2f         Reputation: %-12.2f" % (nation.new_development, nation.number_developments, nation.reputation))


								print(" Factories_________________________________________________________________________")   
								f_key_one = ["parts", "cannons", "clothing", "paper", "furniture", "chemicals"]
								f_key_two = ["gear", "telephone", "radio", "auto", "fighter", "tank"]
								for k1, k2 in zip(f_key_one, f_key_two):
									print(" %-12s  Level: %-6.2f  Used: %-12s   %-12s  Level: %-6.2f  Used: %-6s" % \
								(k1, nation.factories[k1]["number"], nation.factories[k1]["used"], k2, nation.factories[k2]["number"], nation.factories[k2]["used"]))
							#for k, v in player.factories.items():
								
								print("Province Overview: ######################################################################################## \n")
								for k, province in nation.provinces.items():
									print("Name: %-16s 	Resource: %-10s 	Development Level: %s 	Worked?: %s 	Quality: %s   Culture: %s \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality, province.culture))
								print("Population Overview: ######################################################################################### \n")
								#for k, v in nation.midPOP.items():
								#	print("%s: %.2f, priority: %.2f \n"  % (k, v["number"], v["priority"]))
								for d, dev in nation.developments.items():
									print("%s: %.2f" % (d, dev))
								print("Military Overview: ################################################################################################ \n")
								print("Infantry -   Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" %  \
								(nation.military["infantry"], nation.infantry["attack"], nation.infantry["defend"], nation.infantry["manouver"]))
								print("Cavalry -    Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(nation.military["cavalry"],  nation.cavalry["attack"], nation.cavalry["defend"], nation.cavalry["manouver"]))
								print("Artillery -  Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(nation.military["artillery"], nation.artillery["attack"], nation.artillery["defend"], nation.artillery["manouver"]))
								print("Fighter -    Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(nation.military["fighter"], nation.fighter["attack"], nation.fighter["defend"], nation.fighter["manouver"]))
								print("Tank -       Num: %.2f   Att: %.2f   Def: %.2f   Man: %s" % \
								(nation.military["tank"], nation.tank["attack"], nation.tank["defend"], nation.tank["manouver"]))
								print("Frigate -    Num: %.2f   Att: %.2f" % (nation.military["frigates"], nation.frigates["attack"]))
								print("Ironclad -   Num: %.2f   Att: %.2f" % (nation.military["iron_clad"], nation.iron_clad["attack"]))
								print("Battleship - Num: %.2f   Att: %.2f" % (nation.military["battle_ship"], nation.battle_ship["attack"]))
								for cb in nation.CB:
									print("Opponent: %s, Province: %s, Action: %s, Time: %s" % (cb.opponent, cb.province, cb.action, cb.time))

								print("Inventory: ##########################################################################################################\n")
								for (k1,v1), (k2,v2) in zip(nation.resources.items(), nation.goods.items()):
									print(" %-12s: %.2f        %-12s: %.2f" % (k1, v1, k2, v2))
								print("\n")
								print("Technologies: ################################################################################################### \n")
								for tech in nation.technologies:
									print(tech, end=" ")
								print("\n")


							if which == "2":
								know = " "
								for k, v in national_comparisons.items():
									print(k, v)
								while know not in national_comparisons.keys():
									know = input("What would you like to know?\n")

								if know == "1":
									print(" Top 10 Nations by Wealth:")
									player_list = players.values()
									wealth = sorted(player_list, key=lambda x: x.resources["gold"], reverse = True)
									wealth = wealth[:10]
									count = 1
									for w in wealth:
										print(" %-2s. %-16s: %.2f" % (count, w.name, w.resources["gold"]))
										count += 1
									print("\n")
									
									print(" Top 10 Nations by Development Level:")
									count = 1
									middle = sorted(player_list, key=lambda x: x.development_level, reverse = True)
									middle = middle[:10]
									for m in middle:
										print(" %-2s. %-16s: %.2f" % (count, m.name, m.development_level))
										count += 1
									print("\n")

									print(" Top 10 Nations by Research:")
									count = 1
									research = sorted(player_list, key=lambda x: x.developments["research"], reverse = True)
									research = research[:10]
									for r in research:
										print(" %-2s. %-16s: %.2f" % (count, r.name, r.developments["research"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Military:")
									count = 1
									officer = sorted(player_list, key=lambda x: x.developments["military"], reverse = True)
									officer = officer[:10]
									for o in officer:
										print(" %-2s. %-16s: %.2f" % (count, o.name, o.developments["military"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Culture:")
									count = 1
									art = sorted(player_list, key=lambda x: x.developments["culture"], reverse = True)
									art = art[:10]
									for a in art:
										print(" %-2s. %-16s: %.2f" % (count, a.name, a.developments["culture"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Government:")
									count = 1
									gov = sorted(player_list, key=lambda x: x.developments["government"], reverse = True)
									gov = gov[:10]
									for g in gov:
										print(" %-2s. %-16s: %.2f" % (count, g.name, g.developments["government"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Management")
									count = 1
									man = sorted(player_list, key=lambda x: x.developments["management"], reverse = True)
									man = man[:10]
									for m in man:
										print(" %-2s. %-16s: %.2f" % (count, m.name, m.developments["management"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Technologies:")
									count = 1
									tech = sorted(player_list, key=lambda x: len(x.technologies), reverse = True)
									tech = tech[:10]
									for t in tech:
										print(" %-2s. %-16s: %.2f" % (count, t.name, len(t.technologies)))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Colonies:")
									count = 1
									col = sorted(player_list, key=lambda x: x.num_colonies, reverse = True)
									col = col[:10]
									for c in col:
										print(" %-2s. %-16s: %.2f" % (count, c.name, c.num_colonies))
										count += 1
									print("\n")

									print(" Top 10 Nations by Population:")
									count = 1
									pop = sorted(player_list, key=lambda x: x.POP, reverse = True)
									pop = pop[:10]
									for p in pop:
										print(" %-2s. %-16s: %.2f" % (count, p.name, p.POP))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Factories:")
									count = 1
									facts = {}
									for k, v in players.items():
										number = 0
										for f, fac in v.factories.items():
											number += fac["number"]
										facts[k] = number
									facts = sorted(facts.items(), key= operator.itemgetter(1), reverse = True) 
									facts = facts[:10]
									for f in facts:
										print(" %-2s. %-16s: %.2f" % (count, f[0], f[1]))
										count +=1
									print("\n")

									print(" Top 10 Nations by Number of Province Developments:")
									count = 1
									developments = {}
									for p, pl in players.items():
										developments[p] = pl.number_developments
									developments = sorted(developments.items(), key= operator.itemgetter(1), reverse = True)
									developments = developments[:10]
									for d in developments:
										print(" %-2s. %-16s: %.2f" % (count, d[0], d[1]))
										count +=1
									print("\n")

								if know == "3":

									print(" Top 10 Food Producers:")
									count = 1
									food = sorted(market.food_production.items(), key= operator.itemgetter(1), reverse = True)
									food = food[:10]
									for f in food:
										print(" %-2s. %-16s: %.2f" % (count, f[0], f[1]))
										count += 1
									print("\n")

									print(" Top 10 Iron Producers:")
									count = 1
									iron = sorted(market.iron_production.items(), key= operator.itemgetter(1), reverse = True)
									iron = iron[:10]
									for i in iron:
										print(" %-2s. %-16s: %.2f" % (count, i[0], i[1]))
										count +=1
									print("\n")

									print(" Top 10 Wood Producers:")
									count = 1
									wood = sorted(market.wood_production.items(), key= operator.itemgetter(1), reverse = True)
									wood = wood[:10]
									for w in wood:
										print(" %-2s. %-16s: %.2f" % (count, w[0], w[1]))
										count +=1
									print("\n")

									print(" Top 10 Cotton Producers:")
									count = 1
									cotton = sorted(market.cotton_production.items(), key= operator.itemgetter(1), reverse = True)
									cotton = cotton[:10]
									for c in cotton:
										print(" %-2s. %-16s: %.2f" % (count, c[0], c[1]))
										count += 1
									print("\n")

									print(" 10 Coal Producers:")
									count = 1
									coal = sorted(market.coal_production.items(), key= operator.itemgetter(1), reverse = True)
									coal = coal[:10]
									for c in coal:
										print(" %-2s. %-16s: %.2f" % (count, c[0], c[1]))
										count += 1
									print("\n")

									print(" Top 10 Gold Producers:")
									count = 1
									gold = sorted(market.gold_production.items(), key= operator.itemgetter(1), reverse = True)
									gold = gold[:10]
									for g in gold:
										print(" %-2s. %-16s: %.2f" % (count, g[0], g[1]))
										count +=1
									print("\n")

									print(" Top 10 Spice Producers:")
									count = 1
									spice = sorted(market.spice_production.items(), key= operator.itemgetter(1), reverse = True)
									spice = spice[:10]
									for s in spice:
										print(" %-2s. %-16s: %.2f" % (count, s[0], s[1]))
										count +=1
									print("\n")

									print(" Top 10 Rubber Producers:")
									count = 1
									rubber = sorted(market.rubber_production.items(), key= operator.itemgetter(1), reverse = True)
									rubber = rubber[:10]
									for r in rubber:
										print(" %-2s. %-16s: %.2f" % (count, r[0], r[1]))
										count +=1
									print("\n")

									print(" Top 10 Oil Producers:")
									count = 1
									oil = sorted(market.oil_production.items(), key= operator.itemgetter(1), reverse = True)
									oil = oil[:10]
									for o in oil:
										print(" %-2s. %-16s: %.2f" % (count, o[0], o[1]))
										count += 1
									print("\n")

									print(" Top 10 Parts Producers:")
									count = 1
									parts = {}
									for p, pl in players.items():
										parts[p] = pl.goods_produced["parts"]
									parts = sorted(parts.items(), key= operator.itemgetter(1), reverse = True)
									parts = parts[:10]
									for p in parts:
										print(" %-2s. %-16s: %.2f" % (count, p[0], p[1]))
										count +=1
									print("\n")

									print(" Top 10 Cannons Producers:")
									count = 1
									cannons = {}
									for p, pl in players.items():
										cannons[p] = pl.goods_produced["cannons"]
									cannons = sorted(cannons.items(), key= operator.itemgetter(1), reverse = True)
									cannons = cannons[:10]
									for c in cannons:
										print(" %-2s. %-16s: %.2f" % (count, c[0], c[1]))
										count +=1
									print("\n")

										
									print(" Top 10 Clothing Producers:")
									count = 1
									clothing = {}
									for p, pl in players.items():
										clothing[p] = pl.goods_produced["clothing"]
									clothing = sorted(clothing.items(), key= operator.itemgetter(1), reverse = True)
									clothing = clothing[:10]
									for c in clothing:
										print(" %-2s. %-16s: %.2f" % (count, c[0], c[1]))
										count +=1
									print("\n")

									print(" Top 10 Paper Producers:")
									count = 1
									paper = {}
									for p, pl in players.items():
										paper[p] = pl.goods_produced["paper"]
									paper = sorted(paper.items(), key= operator.itemgetter(1), reverse = True)
									paper = paper[:10]
									for p in paper:
										print(" %-2s. %-16s: %.2f" % (count, p[0], p[1]))
										count +=1
									print("\n")

									print(" Top 10 Furniture Producers:")
									count = 1
									furniture = {}
									for p, pl in players.items():
										furniture[p] = pl.goods_produced["furniture"]
									furniture = sorted(furniture.items(), key= operator.itemgetter(1), reverse = True)
									furniture = furniture[:10]
									for f in furniture:
										print(" %-2s. %-16s: %.2f" % (count, f[0], f[1]))
										count +=1
									print("\n")

									print(" Top 10 Chemical Producers:")
									count = 1
									chemicals = {}
									for p, pl in players.items():
										chemicals[p] = pl.goods_produced["chemicals"]
									chemicals = sorted(chemicals.items(), key= operator.itemgetter(1), reverse = True)
									chemicals = chemicals[:10]
									for c in chemicals:
										print(" %-2s. %-16s: %.2f" % (count, c[0], c[1]))
										count +=1
									print("\n")

									print(" Top Gear Producers:")
									count = 1
									gear = {}
									for p, pl in players.items():
										gear[p] = pl.goods_produced["gear"]
									gear = sorted(gear.items(), key= operator.itemgetter(1), reverse = True)
									gear = gear[:10]
									for g in gear:
										print(" %-2s. %-16s: %.2f" % (count, g[0], g[1]))
										count +=1
									print("\n")

									print(" Top Radio Producers:")
									count = 1
									radio = {}
									for p, pl in players.items():
										radio[p] = pl.goods_produced["radio"]
									radio = sorted(radio.items(), key= operator.itemgetter(1), reverse = True)
									radio = radio[:10]
									for r in radio:
										print(" %-2s. %-16s: %.2f" % (count, r[0], r[1]))
										count +=1
									print("\n")

									print(" Top Telephone Producers:")
									count = 1
									tele = {}
									for p, pl in players.items():
										tele[p] = pl.goods_produced["telephone"]
									tele = sorted(tele.items(), key= operator.itemgetter(1), reverse = True)
									tele = tele[:10]
									for t in tele:
										print(" %-2s. %-16s: %.2f" % (count, t[0], t[1]))
										count +=1
									print("\n")

									print(" Top Fighter Producers:")
									count = 1
									fighter = {}
									for p, pl in players.items():
										fighter[p] = pl.goods_produced["fighter"]
									fighter = sorted(fighter.items(), key= operator.itemgetter(1), reverse = True)
									fighter = fighter[:10]
									for f in fighter:
										print(" %-2s. %-16s: %.2f" % (count, f[0], f[1]))
										count +=1
									print("\n")

									print(" Top 10 Tank Producers:")
									count = 1
									tank = {}
									for p, pl in players.items():
										tank[p] = pl.goods_produced["tank"]
									tank = sorted(tank.items(), key= operator.itemgetter(1), reverse = True)
									tank = tank[:10]
									for t in tank:
										print(" %-2s. %-16s: %.2f" % (count, t[0], t[1]))
										count +=1
									print("\n")

									print(" Top 10 Auto Producers:")
									count = 1
									auto = {}
									for p, pl in players.items():
										auto[p] = pl.goods_produced["auto"]
									auto = sorted(auto.items(), key= operator.itemgetter(1), reverse = True)
									auto = auto[:10]
									for a in auto:
										print(" %-2s. %-16s: %.2f" % (count, a[0], a[1]))
										count +=1
									print("\n")

								if know == "2":
									print(" Nations by Number of Infantry:")
									count = 1
									infantry = {}
									for p, pl in players.items():
										infantry[p] = pl.military["infantry"]
									infantry = sorted(infantry.items(), key= operator.itemgetter(1), reverse = True)
									infantry = infantry[:10]
									for i in infantry:
										print(" %-2s. %-12s %-2.2f" % (count, i[0], i[1]))
										#print(" %-2s. %s" % (count, i))
										count += 1
									print("\n")

									print(" Nations by Number of Calvary:")
									count = 1
									cavalry = {}
									for p, pl in players.items():
										cavalry[p] = pl.military["cavalry"]
									cavalry = sorted(cavalry.items(), key= operator.itemgetter(1), reverse = True)
									cavalry = cavalry[:10]
									for c in cavalry:
										print(" %-2s. %-12s %-2.2f" % (count, c[0], c[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Artillery:")
									count = 1
									artillery = {}
									for p, pl in players.items():
										artillery[p] = pl.military["artillery"]
									artillery = sorted(artillery.items(), key= operator.itemgetter(1), reverse = True)
									artillery = artillery[:10]
									for a in artillery:
										print(" %-2s. %-12s %-2.2f" % (count, a[0], a[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Frigates:")
									count = 1
									frigates = {}
									for p, pl in players.items():
										frigates[p] = pl.military["frigates"]
									frigates = sorted(frigates.items(), key= operator.itemgetter(1), reverse = True)
									frigates = frigates[:10]
									for f in frigates:
										print(" %-2s. %-12s %-2.2f" % (count, f[0], f[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Ironclads:")
									count = 1
									iron_clad = {}
									for p, pl in players.items():
										iron_clad[p] = pl.military["iron_clad"]
									iron_clad = sorted(iron_clad.items(), key= operator.itemgetter(1), reverse = True)
									iron_clad = iron_clad[:10]
									for i in iron_clad:
										print(" %-2s. %-12s %-2.2f" % (count, i[0], i[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Fighters:")
									count =1 
									fighter = {}
									for p, pl in players.items():
										fighter[p] = pl.military["fighter"]
									fighter = sorted(fighter.items(), key= operator.itemgetter(1), reverse = True)
									fighter = fighter[:10]
									for f in fighter:
										print(" %-2s. %-12s %-2.2f" % (count, f[0], f[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Tanks")
									count =1 
									tank = {}
									for p, pl in players.items():
										tank[p] = pl.military["tank"]
									tank = sorted(tank.items(), key= operator.itemgetter(1), reverse = True)
									tank = tank[:10]
									for t in tank:
										print(" %-2s. %-12s %-2.2f" % (count, t[0], t[1]))
										count += 1
									print("\n")

									print(" Nations by Number of Battleships")
									count =1 
									battle_ship = {}
									for p, pl in players.items():
										battle_ship[p] = pl.military["battle_ship"]
									battle_ship = sorted(battle_ship.items(), key= operator.itemgetter(1), reverse = True)
									battle_ship = battle_ship[:10]
									for bs in battle_ship:
										print(" %-2s. %-12s %-2.2f" % (count, bs[0], bs[1]))
										count += 1
									print("\n")


									print(" Nations by Total Army Strength (Attack):")
									count = 1 
									army_Astrength = {}
									for p, pl in players.items():
										strength = pl.calculate_base_attack_strength()
										army_Astrength[p] = strength
									army_Astrength = sorted(army_Astrength.items(), key= operator.itemgetter(1), reverse = True)
									for ast in army_Astrength:
										print(" %-2s. %-12s %-2.2f" % (count, ast[0], ast[1]))
										count += 1
									print("\n")

									print(" Nations by Total Army Strength (Defend):")
									count = 1 
									army_Dstrength = {}
									for p, pl in players.items():
										strength = pl.calculate_base_defense_strength()
										army_Dstrength[p] = strength
									army_Dstrength = sorted(army_Dstrength.items(), key= operator.itemgetter(1), reverse = True)
									for dst in army_Dstrength:
										print(" %-2s. %-12s %-2.2f" % (count, dst[0], dst[1]))
										count += 1
									print("\n")


									print(" Nations by Total Navy Strength:")
									count = 1 
									navy_strength = {}
									for p, pl in players.items():
										strength = pl.calculate_naval_strength()
										navy_strength[p] = strength
									navy_strength = sorted(navy_strength.items(), key= operator.itemgetter(1), reverse = True)
									for ns in navy_strength:
										print(" %-2s. %-12s %-2.2f" % (count, ns[0], ns[1]))
										count += 1
									print("\n")



						if info_command == "8":
							print("Your Empire has developed the following technologies: \n")
							for t in player.technologies:
								print(t)
							print("You are currently in a position the research the following technologies: \n")
							for k, t in technology_dict.items():
								if(k not in player.technologies and t["requirement"] in player.technologies):
									print(k, t)

						if info_command == "9":
							print("You have land borders with: ")
							for b in player.borders:
								print(b)
							print("\n")
							print("Your Relations with Other Players \n")

							p_relations = [r for r in relations.values() if player.name in r.relata]
							p_relations = deepcopy(p_relations)
						#	print("P-relations:")
						#	for pr in p_relations:
						#		print(pr.relata)
							for i in range(int(len(p_relations)/4) + 1):
						#		print(i)
								k = 0
								relatas = []
								while (i*4) + k < len(p_relations) and k < 4:
									temp = list(p_relations[(i*4)+k].relata)
									if temp[0] == player.name:
										 relatas.append(temp[1])
									else:
										relatas.append(temp[0])
									k += 1
							
								#a = list(p_relations[i].relata)
								#b = list(p_relations[i+1].relata)
								#c = list(p_relations[i+2].relata)
								#d = list(p_relations[i+3].relata)
								#e = list(p_relations[i+4].relata)
								#relatas = [a, b, c, d, e]
								#things =  []
								#for r  in relatas:
									#print("Print r: %s" % (r))
								#	if r[0] == player.name:
								#		 things.append(r[1])
								#	else:
								#		things.append(r[0])
								for j in range(len(relatas)):
									#print("Thing %s" % (things[j]))
									print("%-2s: %-16s: %-3.2f" % ((i*4)+j, relatas[j], p_relations[(i*4)+j].relationship), end = "   ")
								#print("%-16s: %.2f    %-16s: %.2f    %-16s: %.2f    %-16s: %.2f" % (e, p_relations[i].relationship, f, \
								#p_relations[i+1].relationship, g, p_relations[i+2].relationship, h, p_relations[i+3].relationship))
								print("\n")
								#print("".join(list(p_relations[i*5:(i+1)*5]) + p_relations[i*5:(i+1)*5].relationship + "\n"))

						#	for k, v in relations.items():
						#		if player.name in v.relata:
						#			temp = list(v.relata)
									#pprint(vars(v))
						#			if temp[0] == player.name:
	#									print(temp[1], v.relationship)
	#								else:
	#									print(temp[0], v.relationship)
					if command == "2":
						print("How would you like to manage your population? ################################################\n")
						_choices = list(range(1, 4))
						choices = ''.join(str(e) for e in _choices)
						choice = " "
						while (choice not in choices):
							for k, v in manage_pops.items():
								print("%s: %s" % (k,v))
							choice = input()
						if choice == "1":
							player.increase_pop()
						if choice == "2":
							player.increase_middle_class()
						if choice == "3": 
							player.assign_POP()
						if choice =="4":
							player.use_spice_stability()


					if command == "3":
						print("What will be the means of production? \n")
						means = " "
						_choices = list(range(1, 5))
						choices = ''.join(str(e) for e in _choices)
						while (means not in choices):
							for k, v in produce_goods.items():
								print(k, v)
							means = input()
						if means == "1":
							player.craftman_production()
						if means == "2":
							player.factory_production()
						if means == "3":
							chem = " "
							while chem not in use_chemicals.keys():
								for c, chem in use_chemicals.items():
									print(c, chem)
								chem = input()
							if chem == "1":
								if "synthetic_dyes" not in player.technologies:
									print("You need the synthetic_dyes technology to do this \n")
								elif player.goods["chemicals"] < 1:
									print("You do not have enough chemicals \n")
								else:
									amount = input("How many chemicals would you like to convert to dyes? (you have %s chemicals \n" % (player.goods["chemicals"]))
									amount = int(amount)
									if int(amount) > player.goods["chemicals"]:
										print("You do not have enough chemicals for that \n")
									else:
										player.goods["chemicals"] -= amount 
										player.resources["dyes"] += amount
										print("You now have %s dyes and %s chemicals" % (player.resources["dyes"], \
											player.goods["chemicals"]))

							if chem == "2":
								if "fertlizer" not in player.technologies:
									print("You need the fertlizer technology to do this \n")
								elif player.goods["chemicals"] < 1:
									print("You do not have enough chemicals \n")
								else:
									num_farms = 0
									for k, v in player.provinces.items():
										if v.resource == "food":
											num_farms += 1
									print("You have %s farming provinces and %s chemicals \n" % (num_farms, player.goods["chemicals"]))
									_max = min(num_farms, player.goods["chemicals"])
									amount = input("How much food would you like to produce? (max: %s)\n" % (_max) )

									amount = int(amount)
									if(amount > _max):
										print("What is wrong with you anyway? \n")
									else:
										self.resources["food"] += amount
							if chem == "3":
								if "synthetic_rubber" not in player.technologies:
									print ("You need the synthetic rubber technology to do this")
								elif player.resources["oil"] < 2:
									print("You do not have enough oil \n")
								elif player.goods["chemicals"] < 1:
									print("You do not have enough chemicals \n")
								else:
									player.resources["oil"] -= 1
									player.goods["chemiclas"] -= 1
									player.resources["rubber"] += 1
									print("You now have %s rubber and %s oil" % (player.resources["rubber"], \
										player.resources["oil"]))
							if chem == "4":
								if "synthetic_oil" not in player.technologies:
									print ("You need the synthetic oil technology to do this")
								elif player.goods["chemicals"] < 3:
									print("You do not have enough chemicals \n")
								else:
									player.goods["chemicals"] -= 3
									player.resources["oil"] += 1
									rint("You now have %s oil and %s chemicals" % (player.resources["oil"], \
										player.goods["chemicals"]))



					if command == "4":
						print("What sort of item would you like to build? #################################################################################### \n")
						sort = " "
						while (sort not in build.keys()):
							for k, v in build.items():
								print(k, v)
							sort = input()
						if sort == "1":
							player.develop_province()
						elif sort == "2":
							#print("What sort of factory would you like to build? ########### ################################################################## \n")
							#for k, v in build_factory.items():
							#	print(k, v)
							#kind = " "
							#while kind not in build_factory.keys():
							#	kind = input()
							#player.build_factory(build_factory[kind], market)
							player.build_factory(market)
						elif sort == "3":
							player.improve_fortifications()
						elif sort == "4":
							player.build_steam_ship_yard()
						elif sort == "5":
							player.build_unit()

						elif sort == "6":
							player.disband_unit()

					if command == "5":
						for cb in player.CB:
							prov = cb.province
							prov = provinces[prov] 
							if cb.opponent != prov.owner or cb.opponent not in players.keys():
								player.CB.discard(cb)
								del cb
						if len(player.CB) < 1:
							print("You do not currently have a CB against any other player")

						else:
							cb_keys = []
							for cb in player.CB:
								cb_keys.append(cb.province)
						
							action = " "
							while action not in military_action.keys():
								for k, j in military_action.items():
									print(k, j)
								action = input()

							if action == "1":
							
								annex = ""
								while annex not in cb_keys:
									print("Please type in the name of the province associated with the CB:")
									for cb in player.CB:
										print(cb.opponent, cb.province)
									annex = input()
								annex = provinces[annex]
								owner = players[annex.owner]
								if owner.type == "major" and annex.colony == True:
									if player.check_for_border(other):
											print("You may to capture %s by establishing naval domination or by invading %s and taking it as a prize for victory" % (annex.name, other.name))
											landOrSea = " "
											while landOrSea != "l" and landOrSea != "s":
												landOrSea = input("Do you choose land (l) or sea (s)?")
											if landOrSea == "s":
												victor = naval_battle(player, owner, market, relations, owner)
												if victor == player.name:
													gain_province(player, owner, prov, players, market, relations)
												else:
													player.war_after_math(owner, players, relations, annex)

									

									else:
										print("You do not neighbor %s and so you must capture %s by establishing naval \
										dominance" % (owner.name, annex.name))
										victor = naval_battle(player, owner, market, relations, owner)
										if victor == player.name:
											gain_province(player, owner, prov, players, market, relations)
										else:
											player.war_after_math(owner, players, relations, annex)
										
								
								else:
									land = player.check_for_border(owner)
									if land == False:
										print("Since you do not border %s, you must send your army by navy\n" % (other.name))
										transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
										if transport_limit < 4:
											print("Your navy is not sufficient for carrying out an amphibious invasion!")
										else:
											amphib_prelude(player, owner, annex, relations, players)
											player.reputation -= 0.1
									else:
										print("Since we border %s, we may attack by land!" % (owner.name))
										#combat(player, owner, annex, players, market, relations)
										forces = select_ground_forces(player, owner)
										amph_combat(player, owner, forces, prov, players, market, relations)

	
							if action == "2":
								if player.military["fighter"] < 4 or player.military["tank"] < 4:
									print("You must have at least 4 Fighters and 4 Tanks to wage a total war")
								else:
									target = ""
									major_keys = []
									for k, v in players.items():
										if v.type == "major" and v.defeated == False:
											major_keys.append(k)
									if len(major_keys) == 0:
										print("It appears that all other Major Powers have already been defeated")
									elif players[target].name not in player.borders:
										print("You do not share a land border with %s, so you will need to send your military by sea" % (target)) 
										target = players[target]
										amphib_prelude(player, target, "total", players, market, relations)
										
									else:
										print("Since you share a land border with %s, you are free to invade by land" % (target))
										target = players[target]
										forces = ai_select_ground_forces(player, target)
										if forces["infantry"] == 0:
											print("What are you thinking, attacking with no infantry?")
										else:
											forces = ai_select_ground_forces(player, target)
											amph_combat(player, target, forces, "total", players, market, relations)	
										

					if command == "6":
						if player.diplo_action < 1:
								print("You do not have any diplomatic actions \n")
						else:
							print("What action would you like to take? \n")
							for k, v in diplomacy.items():
								print(k, v)
							dip = " "
							_choices = list(range(1, 12))
							choices = ''.join(str(e) for e in _choices)
							while (str(dip) not in choices):
								dip = input()

							if dip == "1":
								print("Please choose a Nation: ########################################################## \n" )
								#for p in players.values():
								for i in range(int(len(players.keys())/5+1)):
									print("  ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
								_other = " "
								while _other not in players.keys():
									_other = input()
								other = players[_other]
								relata = frozenset([player.name, other.name])
								player.diplo_action -=1
								relations[relata].relationship += min(1, 5/(other.POP + 0.001))
								player.reputation += 0.02
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
							
							elif dip == "2":
								print("Please choose a Nation:\n" )
								#for p in players.values():
									#print(p.name)
								for i in range(int(len(players.keys())/5+1)):
									print("  ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
								_other = " "
								while _other not in players.keys():
									_other = input()
								other = players[_other]
								relata = frozenset([player.name, other.name])
								player.diplo_action -=1
								relations[relata].relationship -= min(1, 10/(other.POP + 0.001))
								player.reputation -= 0.02
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))

							elif dip == "3":
								print("Please choose a Nation:\n" )
								for i in range(int(len(players.keys())/5+1)):
									print("  ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
								_other = " "
								while _other not in players.keys():
									_other = input()
								other = players[_other]
								relata = frozenset([player.name, other.name])

								pay = max(2, other.resources["gold"]/10)
								if pay > player.resources["gold"]/5:
									print("You do not have enough gold to bribe %s at this time" % (other.name))
								else:
									relata = frozenset([player.name, other.name])
									relations[relata].relationship += 0.5
									player.resources["gold"] -= pay
									print("Your relation with %s is now %s" % (other.name, relations[relata].relationship))


							elif dip == "4":
								options = []
								key = []
								for o in player.objectives:
									if o in player.provinces.keys():
										continue
									key.append(o)
								for k in key:
									annex = provinces[k]
									other = annex.owner
									other = players[other]
									relata = frozenset({player.name, other.name})
									if len(relata) == 1:
										continue
									if relations[relata].relationship <= -2.5:
										options.append(k)			

								if len(options) < 1:
									print("Your relations are not currently bad enough with any nation to gain a CB \n")
								else:	
									annex = " "
									while annex not in options:
										print("Please choose a province: \n")
										for o in options:
											op = provinces[o]
											print("Name: %s, Owner: %s, Resource: %s, Quality: %s, Culture %s" % \
												(op.name, op.owner, op.resource, op.quality, op.culture))
										annex = input()
									annex = provinces[annex]
									player.diplo_action -= 1
									
									new = CB(player, annex.owner, "annex", annex.name, 5)

									player.CB.add(new)
									print("You are now able to declare war on %s for the province of %s \n" % (new.opponent, new.province))
									player.reputation -= 0.025



							elif dip == "5":
								print("Pick a pair of nations, whose relations you would like to damage:")
								PA = " "
								while PA not in players.keys():
									print("Please choose Nation A:\n" )
									for i in range(int(len(players.keys())/5+1)):
										print("  ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
									print("Please choose Nation A:\n" )
									for i in range(int(len(players.keys())/5+1)):
										print("  ".join(list(players.keys())[i*5:(i+1)*5]) + "\n")
									PA = input()

								PB = " "
								while PB not in players.keys():
									print("Please choose Nation B:\n" )
									for p in players.keys():
										print(p)
									print("Please choose Nation B:\n" )
									PB = input()

								relata = frozenset([PA, PB])
								PA = players[PA]
								PB = players[PB]
								modifier = 4/((PA.POP + PB.POP)/2)
								relations[relata].relationship -= modifier
								print("Relations between %s and %s have been reduced by %s to %s" % \
									(PA.name, PB.name, modifier, relations[relata].relationship))
								player.diplo_action -= 1
								player.reputation -= 0.025



							elif dip == "6":
								other = " "
								while other not in players.keys():
									print("Which nation would you like to destabilize?\n")
									for p, pl in players.items():
										print("%-16s stability: %.2f" % (p, pl.stability))
									other = input()
								amount = 0
								other = players[other]
								if other.type == "old_empire" or other.type == "old_minor":
									amount = random()/2
								else:
									amount = random()/4
								other.stability -= amount
								if other.stability < -3.0:
									other.stability = -3.0
								player.diplo_action -=1
								player.reputation -= 0.033
								relata = frozenset([player.name, other.name])
								relations[relata].relationship -= 0.2
								print("The stability of %s has been reduced by %s and is now %s \n" % (other.name, amount, other.stability ))
						
							elif dip == "7":
								print ("This feature has not yet been implemented \n")

							elif dip == "8":
								print("Would you like to place an embargo on a nation (1) or lift an embargo (2)? \n")
								dec = input()
								options = []
								if dec == "1":
									for k, v in players.items():
										relata = frozenset([player.name, v.name])
										if len(relata) == 1:
										 	continue
										if relations[relata].relationship < -1.5:
											options.append(v.name)
									if len(options) < 1:
										print("You cannot place an embargo on any nation at this time (relations too good \n")
									else:
										ch = " "
										while ch not in options:
											print("On which nation would you like to place a trade embargo? \n")
											for o in options:
												print(o)
											ch = input()
										other = players[ch]
										other.embargo.add(player.name)
										relata = frozenset([player.name, other.name])
										relations[relata].relationship -= 0.25
										player.diplo_action -= 1
										print("%s is no longer able to purchase your resources or goods on the world market" % (other.name))
								if dec == "2":
									for k, v in players.items():
										if player in v.embargo:
											options.append(v.name)
									if len(options) < 1:
										print("You are not currently placing any nation under embargo\n")
									else:
										ch = " "
										while ch not in options:
											print("Which nation do you wish to release from embargo? \n")
											for o in options:
												print(o)
											ch = input()
										other = players[ch]
										player.embargo.discard(other.name)
										player.diplo_action -= 1
										print("You have lifed the trade embargo on %s" % (other.name))


					if command == "7":
						print(" ##################################################################################################################### \n")
						player.research_tech()

					if command == "8":
						choice = input("Would you like to buy (1) or sell (2)? \n")
						if choice == "1":
							market.show_market(player)
							_type = " "
							while _type not in market.market.keys():
								_type = input("What would you like to buy? \n")
							market.buy_item(_type, player, players, market, relations)
						elif choice == "2":
							player.view_inventory()
							_type = " "
							while _type not in market.market.keys():
								_type = input("What would you like to sell? \n")
							market.sell_item(_type, player, players)

					if command == "9":
						print("######################################################################################################### \n ")
						player.use_culture(players)
					if command == "10":
						print("####################################################################################################### \n ")
						check = input("Are you sure you want to end your turn? y/n \n")
						if check == "y":
							player.turn(market)
							break
						else:
							continue
					if command == "11":
						print("Would you like to make a new save? (If you have not created a save for this game yet, you should certainly choose yes) (y/n) \n")
						yn = input()
						if yn == "y":
							create_new_save_game(players, relations, uncivilized_minors, market, provinces)
						if yn == "n":
							save_name = input("Please write in the name of the save file (without file extension) \n")
							save_game(save_name, players, relations, uncivilized_minors, market, provinces)


					if command == "12":
						#print("Saving....\n")
						#save_game(auto_name, players, relations, uncivilized_minors, market, provinces)
						_continue = False
						break

					if command == "h":
						print("\n")
						_help = ""
						while _help not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "r"]:
							print("On what command would you like information?")
							for c in commands:
								print(c)
							print("Return: (r)")
							_help = input()

						if _help == "1":
							print("\n")
							print("Selecting 'Get Information on...' will provide you with a number of options,")
							print("each one providing a category of information on the state of your Empire or the")
							print("state of the Globe")
						if _help == "2":
							print("\n")
							print("Selecting 'Manage POPs' will take you to a few options on managing your Empire's")
							print("population. These include: increasing your population, human development, assigning")
							print("population to gather resources from your provinces or produce goods and giving your")
							print("thankless people spice to keep them happy.")
						if _help == "3":
							print("\n")

							print("Selecting 'Manufacture Goods' will take you to three manufacturing options")
							print("The first it to manufacture goods the old fashioned way, with artisans (not efficient.")
							print("The second is to manufacture goods like civilized people, in a factory.")
							print("The third allows you to convert chemicals into other resources that you may need.")
						if _help == "4":
							print("\n")
							print("Selecting 'Build' takes you to some options on building Empire improvements")
							print("These include, developing provinces (for better resource output),")
							print("building or upgrading factories (for mass production of finished goods),")
							print("improving your fortification (for improved defense strength),")
							print("building/upgrading your shipyard (for producing the most modern ships),")
							print("building military units (for exploiting the globe and keeping the other powers in line),")
							print("and disbanding outdated units.")
						if _help == "5":
							print("\n")
							print("Selecting 'Military Action' will take you to one of two options")
							print("The first is to fight a 'minor' war for a single province")
							print("A cause of war (casus belli) is required to wage a minor war (see Diplomacy)")
							print("The second is to fight a 'Total' war to conquer all the core provinces")
							print("of one of the Major powers.")
							print("Total war be declared on any Major power if you have at least 4 fighters and")
							print("4 tank units (end game).")
						if _help == "6":
							print("\n")
							print("Selecting 'Diplomatic Actions' presents a number of diplomatic actions")
							print("These include improving and damaging relations with other nations,")
							print("gaining a casus belli on an other nation, sabotaging relations between other nations,")
							print("destabilizing other nations, and placing trade embargoes on other nations.")
						if _help == "7":
							print("\n")

							print("Selecting 'Research Technology' will present you with a list of all (if any)")
							print("technologies you can presently research.")
						if _help == "8":
							print("\n")

							print("Selecting 'Trade' will present you with the option to either buy goods")
							print("and resources from the market or place goods and resources onto the market")
						if _help == "9":
							print("\n")
							print("Selecting 'Culture' will present you with various options for spending")
							print("your culture points.")
						if _help == "10":
							print("\n")

							print("I am going to let you figure this one out on your own.")
						if _help == "11":
							print("\n")
 
							print("You will be asked if you wish to make a new save.")
							print("If 'yes', you will be prompted to provide a name for the save file.")
							print("If 'no', your current save file will be used to save the game.")
						if _help == "12":
							print("\n")

							print("Do you really need 'End Game' explained to you?")
		gc.collect()
		
		if AUTO_SAVE == True:
	
			#if market.turn % 2 == 1:

			print("Saving....\n")
			save_game(auto_name, players, relations, market, provinces)

	
		#globe.world_update(players)


	#if turn > 1:
	#player.turn()
