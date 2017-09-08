
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

from historical.Scenario import* 
#sys.path.insert(0, 'C:\Users\Labecki\Documents\Python\game\historical')
#from Scenario import*

# Main Game Loop

run = True
while True:

	print("########################################################################################################### \n")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
	print( "_____________________________Welcome to Imperialist Bastards!_______________________________________________ \n")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
	print("########################################################################################################### \n")
	print(" _____________________________________ Main Menu ___________________________________________ \n")
	print("\n")
	print("______________________________Please select one of the following: ______________________________\n")
	print("---------------------------------- Start a New Game ---(N) --------------------------------------	 \n")
	print("----------------------------- Start Quasi-Historical Scenario (S)--------------------------------     \n")
	print("---------------------------------- Load a Saved Game --(L) --------------------------------------     \n")
	print("------------------------------------- Options ---------(O) --------------------------------------     \n ")
	print("--------------------------------------- Exit ----------(E) --------------------------------------     \n" )
	print("______________________________________________________________________________________________ \n")

	initial = dict()
	selection = " "
	while selection not in ["N", "S", "L", "O", "E"]:
		selection = input()

	if selection == "N":
		initial = start_game()
	elif selection == "S":
		initial = historical()
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

		for k, v in players.items():
			print(k, v)
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

						
	_continue = True
	while(_continue == True):
		
		market.turn +=1
		print("\n Turn: %s \n" % (market.turn))
		#print("Gold in market: %s \n" % (market.gold))
		for k in market.market_keys:
		#for k, v in market.market.items():
			print (k, len(market.market[k]))
		print("Players len: %s " % (len(players.keys())))
		print("Prov len: %s" % (len(provinces.keys())))
		print("Relations len %s" % (len(relations.keys())))
		cont = input()
		order = list(players.keys())
		print("order len %s" % (len(order)))
		shuffle(order)
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

		#		for k, v in player.goods_produced.items():
		#			v = 0

				print("############################################################################################################### \n ")
				print("%s, it is your turn to exploit the globe for the greatness of your nation! \n" % (player.name))
				while(True):
					print(" ######################################################################################################## \n")
					
					player.calculate_access_to_goods(market)
					print("%s, what is your imperial decree? \n" % (player.name))
					print("AP: %s    " % (player.AP))
					for key, value in commands.items():
						print(key, value)
					command = ""
					while (command not in commands.keys()):
						command = input()
					if command == "1":
						print("What would you like to know? ################################################################################\n")
						for key, value in information.items():
							print(key, value)
						info_command = " "
						while info_command not in information.keys():
							info_command = input()
						if info_command == "1":

							print("Currently, your glorious empire has: ###################################################################\n")
									#print("Gold: %s 				Action Points: %s \n" % (player.gold, player.AP))
							print("Stability: %.2f  ______________  Total Population: %.2f\n" % (player.stability, player.POP))
							print("Gold: %.2f  ___________________  Action Points: %.2f \n" % (player.resources["gold"], player.AP))
							print("Diplomatic: %.2f  _____________  Science Points: %.2f \n " % (player.diplo_action, player.research))
							print("Colonization: %.2f  ___________  Reputation: %.2f \n" % (player.colonization, player.reputation))
							print("Number of colonies: %s ______  Col. points needed for next colony: %s "% (player.num_colonies, 1 + player.num_colonies * 1.5))
							print("Lower Class Pops: %.2f  _______  Middle Class Pops: %.2f \n" % (player.numLowerPOP, player.numMidPOP))
							print("Development Points: %.2f  _____ Development Level: %.2f \n" % (player.new_development, player.number_developments))
							print("Free POPs: %.2f  _______________ Culture Points: %.2f" % (player.freePOP, player.culture_points))
							print("Factories:")

							for k, v in player.factories.items():
								print(k,v)
						if info_command == "2":
							print("Province Overview: ######################################################################################## \n")
							for k, province in player.provinces.items():
								print("Name: %-20s 	Resource: %-10s 	Development Level: %s 	Worked?: %s 	Quality: %.2f \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality))
						if info_command == "3":
							print("Population Overview: ####################################################################################### \n")
							print("Total Population: %.2f 	Unassigned Pops: %.2f 	Lower Class Pops: %.2f 	Middle Class Pops: %.2f \n" % \
							(player.POP, player.freePOP, player.numLowerPOP, player.numMidPOP))
							print("Urban Worker Pops: %.2f 	Military Pops: %.2f \n" % (player.proPOP, player.milPOP))
							print("Middle Class POPs: \n")
							for k, v in player.midPOP.items():
								print("%s: %.2f"  % (k, v["number"]))
						if info_command == "4" :
							print("Military Overview: ################################################################################################ \n")
							for k, v in player.military.items():
								print(" %s: %.2f " % (k, v) )

							print("\n")
							print("Infantry, Attack: %s, Defend: %s, Manouver: %s" % (player.infantry["attack"], player.infantry["defend"], player.infantry["manouver"]))
							print("Cavalry, Attack: %s, Defend: %s, Manouver: %s" % (player.cavalry["attack"], player.cavalry["defend"], player.cavalry["manouver"]))
							print("Artillery, Attack: %s, Defend: %s, Manouver: %s" % (player.artillery["attack"], player.artillery["defend"], player.artillery["manouver"]))
							print("Fighter, Attack: %s, Defend: %s, Manouver: %s" % (player.fighter["attack"], player.fighter["defend"], player.fighter["manouver"]))
							print("Tank, Attack: %s, Defend: %s, Manouver: %s" % (player.tank["attack"], player.tank["defend"], player.tank["manouver"]))
							print("Frigate, Attack: %s" % (player.frigates["attack"]))
							print("Ironclad, Attack: %s" % (player.iron_clad["attack"]))
							print("Battleship, Attack: %s" % (player.battle_ship["attack"]))
							print("\n")
							ammo_needed = calculate_ammo_needed(player)
							oil_needed = calculate_oil_needed(player)
							print("Ammo (number of cannons) needed for land combat: %s" % (ammo_needed))
							print("Oil Needed for land combat: %s" % (oil_needed))
							ammo_navy_needed = calculate_ammo_needed_navy(player)
							oil_navy_needed = calculate_oil_needed_navy(player)
							print("Ammo (number of cannons) needed for naval combat: %s" % (ammo_navy_needed))
							print("Oil Needed for naval combat %s" % (oil_navy_needed))


						if info_command == "5":
							print("Inventory: ##########################################################################################################\n")
							for k in market.resources:
							#for k, v in player.resources.items():
								print(" %s: %.2f " % (k, player.resources[k]) )
							#for k, v in player.goods.items():
							for k in market.goods:
								print(" %s: %.2f " % (k, player.goods[k]) )
						if info_command == "6":
							player.view_inventory_production_needs()
						if info_command == "7":
							for k, v in foreign_intelligence.items():
								print (k, v)
							which = input()
							if which == "1":
								for k, v in players.items():
									print(v.name)
								nation = input("Please input the name of the nation you would like to view \n")
								nation = players[nation]
								print("Information Report on %s: ###################################################################\n" % (nation.name))
										#print("Gold: %s 				Action Points: %s \n" % (player.gold, player.AP))
								print("Type: %s ____________________   Culture: %s" % (nation.type, nation.culture))
								print("Stability: %.2f  ____________    Total Population: %.2f\n" % (nation.stability, nation.POP))
								print("Gold: %s  _____________________  Action Points: %.2f \n" % (nation.resources["gold"], nation.AP))
								print("Diplomatic: %.2f  _____________  Science Points: %.2f \n " % (nation.diplo_action, nation.research))
								print("Colonization: %.2f  ___________  Number of Colonies: %s \n " % (nation.colonization, nation.num_colonies))
								print("Government: %s  _____________  Reputation: %.2f \n" % (nation.government, nation.reputation))
								print("Lower Class Pops: %.2f  _______  Middle Class Pops: %.2f \n" % (nation.numLowerPOP, nation.numMidPOP))
								print("Development Points: %.2f  _____  Development Level: %.2f \n" % (nation.new_development, nation.number_developments))
								print("Free POPS: %.2f _______________  ProPops: %.2f\n" % (nation.freePOP, nation.proPOP))
								print("Factories:")


								for k, v in nation.factories.items():
									print(k, v)
								print("Province Overview: ######################################################################################## \n")
								for k, province in nation.provinces.items():
									print("Name: %-20s 	Resource: %-10s 	Development Level: %s 	Worked?: %s 	Quality: %s   Culture: %s \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality, province.culture))
								print("Population Overview: ######################################################################################### \n")
								for k, v in nation.midPOP.items():
									print("%s: %.2f, priority: %.2f \n"  % (k, v["number"], v["priority"]))
								print("Military Overview: ################################################################################################ \n")
								for k, v in nation.military.items():
									print(" %s: %.2f " % (k, v) )
								
								print("\n")
								print("Infantry: Attack: %s, Defense: %s, Manouver: %s" % (nation.infantry["attack"], nation.infantry["defend"], nation.infantry["manouver"]))
								print("Artillery: Attack: %s, Defense: %s, Manouver: %s" % (nation.artillery["attack"], nation.artillery["defend"], nation.artillery["manouver"]))
								print("Cavalry: Attack: %s, Defense: %s, Manouver: %s" % (nation.cavalry["attack"], nation.cavalry["defend"], nation.cavalry["manouver"]))
								print("Fighter: Attack: %s, Defense: %s, Manouver: %s" % (nation.fighter["attack"], nation.fighter["defend"], nation.fighter["manouver"]))
								print("Tank: Attack: %s, Defense: %s, Manouver: %s" % (nation.tank["attack"], nation.tank["defend"], nation.tank["manouver"]))
								print("Frigate: Attack: %s" % (nation.frigate["attack"]))
								print("Ironclad: Attack: %s" % (nation.iron_clad["attack"]))
								print("Battleship: Attack: %s" % (nation.battle_ship["attack"]))
								print("\n")
								print("CBs:")
								for cb in nation.CB:
									print("Opponent: %s, Province: %s, Action: %s, Time: %s" % (cb.opponent, cb.province, cb.action, cb.time))

								print("Inventory: ##########################################################################################################\n")
								for v, k in nation.resources.items():
									print(v, k)
								for v, l in nation.goods.items():
									print(v,k)
								print("\n")
								print("Technologies: ################################################################################################### \n")
								for tech in nation.technologies:
									print(tech, end=" ")


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
										print(" %-2s. %-16s: %s" % (count, w.name, w.resources["gold"]))
										count += 1
									print("\n")
									
									print(" Top 10 Nations by Middle Class:")
									count = 1
									middle = sorted(player_list, key=lambda x: x.numMidPOP, reverse = True)
									middle = middle[:10]
									for m in middle:
										print(" %-2s. %-16s: %s" % (count, m.name, m.numMidPOP))
										count += 1
									print("\n")

									print(" Top 10 Nations by Researchers:")
									count = 1
									research = sorted(player_list, key=lambda x: x.midPOP["researchers"]["number"], reverse = True)
									research = research[:10]
									for r in research:
										print(" %-2s. %-16s: %s" % (count, r.name, r.midPOP["researchers"]["number"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Officers:")
									count = 1
									officer = sorted(player_list, key=lambda x: x.midPOP["officers"]["number"], reverse = True)
									officer = officer[:10]
									for o in officer:
										print(" %-2s. %-16s: %s" % (count, o.name, o.midPOP["officers"]["number"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Artists:")
									count = 1
									art = sorted(player_list, key=lambda x: x.midPOP["artists"]["number"], reverse = True)
									art = art[:10]
									for a in art:
										print(" %-2s. %-16s: %s" % (count, a.name, a.midPOP["artists"]["number"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Bureaucrats:")
									count = 1
									gov = sorted(player_list, key=lambda x: x.midPOP["bureaucrats"]["number"], reverse = True)
									gov = gov[:10]
									for g in gov:
										print(" %-2s. %-16s: %s" % (count, g.name, g.midPOP["bureaucrats"]["number"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Managers")
									count = 1
									man = sorted(player_list, key=lambda x: x.midPOP["managers"]["number"], reverse = True)
									man = man[:10]
									for m in man:
										print(" %-2s. %-16s: %s" % (count, m.name, m.midPOP["managers"]["number"]))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Technologies:")
									count = 1
									tech = sorted(player_list, key=lambda x: len(x.technologies), reverse = True)
									tech = tech[:10]
									for t in tech:
										print(" %-2s. %-16s: %s" % (count, t.name, len(t.technologies)))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Colonies:")
									count = 1
									col = sorted(player_list, key=lambda x: x.num_colonies, reverse = True)
									col = col[:10]
									for c in col:
										print(" %-2s. %-16s: %s" % (count, c.name, c.num_colonies))
										count += 1
									print("\n")

									print(" Top 10 Nations by Population:")
									count = 1
									pop = sorted(player_list, key=lambda x: x.POP, reverse = True)
									pop = pop[:10]
									for p in pop:
										print(" %-2s. %-16s: %s" % (count, p.name, p.POP))
										count += 1
									print("\n")

									print(" Top 10 Nations by Number of Factories:")
									count = 1
									factories = {}
									for k, v in players.items():
										number = 0
										for f, fac in v.factories.items():
											number += fac
										factories[k] = number
									factories = sorted(factories.items(), key= operator.itemgetter(1), reverse = True) 
									factories = factories[:10]
									for f in factories:
										print(" %-2s. %s" % (count, f))
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
										print(" %-2s. %s" % (count, d))
										count +=1
									print("\n")

								if know == "3":

									print(" Top 10 Food Producers:")
									count = 1
									food = sorted(market.food_production.items(), key= operator.itemgetter(1), reverse = True)
									food = food[:10]
									for f in food:
										print(" %-2s. %s" % (count, f))
										count += 1
									print("\n")

									print(" Top 10 Iron Producers:")
									count = 1
									iron = sorted(market.iron_production.items(), key= operator.itemgetter(1), reverse = True)
									iron = iron[:10]
									for i in iron:
										print(" %-2s. %s" % (count, i))
										count +=1
									print("\n")

									print(" Top 10 Wood Producers:")
									count = 1
									wood = sorted(market.wood_production.items(), key= operator.itemgetter(1), reverse = True)
									wood = wood[:10]
									for w in wood:
										print(" %-2s. %s" % (count, w))
										count +=1
									print("\n")

									print(" Top 10 Cotton Producers:")
									count = 1
									cotton = sorted(market.cotton_production.items(), key= operator.itemgetter(1), reverse = True)
									cotton = cotton[:10]
									for c in cotton:
										print(" %-2s. %s" % (count, c))
										count += 1
									print("\n")

									print(" 10 Coal Producers:")
									count = 1
									coal = sorted(market.coal_production.items(), key= operator.itemgetter(1), reverse = True)
									coal = coal[:10]
									for c in coal:
										print(" %-2s. %s" % (count, c))
										count += 1
									print("\n")

									print(" Top 10 Gold Producers:")
									count = 1
									gold = sorted(market.gold_production.items(), key= operator.itemgetter(1), reverse = True)
									gold = gold[:10]
									for g in gold:
										print(" %-2s. %s" % (count, g))
										count +=1
									print("\n")

									print(" Top 10 Spice Producers:")
									count = 1
									spice = sorted(market.spice_production.items(), key= operator.itemgetter(1), reverse = True)
									spice = spice[:10]
									for s in spice:
										print(" %-2s. %s" % (count, s))
										count +=1
									print("\n")

									print(" Top 10 Rubber Producers:")
									count = 1
									rubber = sorted(market.rubber_production.items(), key= operator.itemgetter(1), reverse = True)
									rubber = rubber[:10]
									for r in rubber:
										print(" %-2s. %s" % (count, r))
										count +=1
									print("\n")

									print(" Top 10 Oil Producers:")
									count = 1
									oil = sorted(market.oil_production.items(), key= operator.itemgetter(1), reverse = True)
									oil = oil[:10]
									for o in oil:
										print(" %-2s. %s" % (count, o))
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
										print(" %-2s. %s" % (count, p))
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
										print(" %-2s. %s" % (count, c))
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
										print(" %-2s. %s" % (count, c))
										count +=1
									print("\n")

									print(" Top 10 Paper Producers:")
									count = 1
									paper = {}
									for p, pl in players.items():
										paper[p] = pl.goods_produced["paper"]
									paper = sorted(paper.items(), key= operator.itemgetter(1), reverse = True)
									paper = paper[:10]
									for c in paper:
										print(" %-2s. %s" % (count, c))
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
										print(" %-2s. %s" % (count, f))
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
										print(" %-2s. %s" % (count, c))
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
										print(" %-2s. %s" % (count, g))
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
										print(" %-2s. %s" % (count, r))
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
										print(" %-2s. %s" % (count, t))
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
										print(" %-2s. %s" % (count, f))
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
										print(" %-2s. %s" % (count, t))
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
										print(" %-2s. %s" % (count, a))
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
										print(" %-2s. %s" % (count, i))
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
										print(" %-2s. %s" % (count, c))
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
										print(" %-2s. %s" % (count, a))
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
										print(" %-2s. %s" % (count, f))
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
										print(" %-2s. %s" % (count, i))
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
										print(" %-2s. %s" % (count, f))
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
										print(" %-2s. %s" % (count, t))
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
										print(" %-2s. %s" % (count, bs))
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
										print(" %-2s. %s" % (count, ast))
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
										print(" %-2s. %s" % (count, dst))
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
										print(" %-2s. %s" % (count, ns))
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
							print("Your Relations with Other Players")
							for k, v in relations.items():
								if player.name in v.relata:
									#pprint(vars(v))
									print(v, v.relata, v.relationship)
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
									amount = input("How many farms would you like to improve? \n")
									amount = int(amount)
									if(amount > num_farms or amount > player.goods["chemicals"]):
										print("What is wrong with you anyway? \n")
									else:
										while amount > 0:
											for k, v in player.provinces.items():
												if v.resource == "food":
													v.quality += 0.1
													player.goods["chemicals"] -= 1
													print("%s now has a quality rating of: %s \n" % (v.name, v.quality))
													amount -= 1
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
										print(cb.opponent, cb.action, cb.province, cb.time)
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
													gain_province(player, target, prov, players, market, relations)
												else:
													player.war_after_math(owner, players, relations, annex)

									

									else:
										print("You do not neighbor %s and so you must capture %s by establishing naval \
										dominance" % (owner.name, annex.name))
										victor = naval_battle(player, owner, market, relations, owner)
										if victor == player.name:
											gain_province(player, target, prov, players, market, relations)
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
										forces = select_ground_forces(player, target)
										amph_combat(player, target, forces, prov, players, market, relations)

	
							if action == "2":
								print("This feature is not yet implemented")
			
				
				
					
			
						


				

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
								for p in players.values():
									print(p.name)
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
								for p in players.values():
									print(p.name)
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
								for p in players.values():
									print(p.name)
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
								cb_key = []
								for cb in player.CB:
									cb_key.append(cb.opponent)
								for k, v in players.items():
									if v.type == "major" or v.type == "old_empire":
										relata = frozenset([player.name, v.name])
										if len(relata) == 1:
											continue
										if relations[relata].relationship <= -2.5 and v not in cb_key:
											options.append(v.name)
								if len(options) < 1:
									print("Your relations are not currently bad enough with any nation to gain a CB \n")
								else:	
									other = " "
									while other not in options:
										print("Please choose a nation: \n")
										for o in options:
											print(o)
										other = input()
									other = players[other]
									player.diplo_action -= 1
									p_options = []
									for prov in other.provinces.values():
										if prov.name in player.objectives:
											p_options.append(prov)
									new = CB(player, other.name, "annex", prov.name, 5)

									player.CB.add(other)
									print("You are now able to declare war on %s \n" % (other.name))
									player.reputation -= 0.025



							elif dip == "5":
								print("Pick a pair of nations, whose relations you would like to damage:")
								PA = " "
								while PA not in players.keys():
									print("Please choose Nation A:\n" )
									for p in players.keys():
										print(p)
									print("Please choose Nation A:\n" )
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
										other.embargo.add(player)
										relata = frozenset([player.name, other.name])
										relations[relata].relationship -= 0.25
										player.diplo_action -= 1
										print("%s is no longer able to purchse your resources or goods on the world market" % (other.name))
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
										player.embargo.discard(other)
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
							market.buy_item(_type, player, players, market)
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
		gc.collect()
		
		if AUTO_SAVE == True:
	
			#if market.turn % 2 == 1:

			print("Saving....\n")
			save_game(auto_name, players, relations, market, provinces)

	
		#globe.world_update(players)


	#if turn > 1:
	#player.turn()
