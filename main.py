
#!/usr/bin/env python3

#/usr/bin/python3

from pprint import pprint
from random import*
from itertools import product, combinations
import sys
import shelve
import operator

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

	selection = " "
	while selection not in ["N", "S", "L", "O", "E"]:
		selection = input()

	if selection == "N":
		initial = start_game()
	elif selection == "S":
		initial = historical()
	elif selection == "L":
		name = input("What is the name of the save that you want to load? \n")
		state = load_game(name)
		#players = initial["players"]
		#print("Players:")
		players = dict()
		provinces = dict()
		relations = dict()
		uncivilized_minors = dict()
		market = Market 
		for k, v in state.items():
			if type(v) == AI or type(v) == Human:
				players[k] = v
			if type(v) == Province:
				provinces[k] = v
			if k == "relations":
				relations = v
			if k == "market":
				market = v
			if k == "provinces":
				provinces = v
		print("Players:")
		for k in players.keys():
			print(k)
		initial = {"players": players, "provinces": provinces, "relations": relations, "market": market, "uncivilized_minors": uncivilized_minors}

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
	uncivilized_minors = initial["uncivilized_minors"]
	market = initial["market"]
	#globe = initial["globe"]


	turn = 0
	_continue = True
	while(_continue == True):
		turn +=1
		print("\n Turn: %s \n" % (turn))
		#print("Gold in market: %s \n" % (market.gold))
		for k, v in market.market.items():
			print (k, len(v))
		print("Players len: %s " % (len(players)))
		cont = input()
		order = list(players.keys())
		print("order len %s" % (len(order)))
		shuffle(order)
		for o in order:
			if type(players[o]) == AI:
				AI_turn(players, players[o], market, turn, uncivilized_minors, relations, provinces)
			else:
				player = players[o]


		#for player in players.values():
		#	if type(player) == AI:
		#		AI_turn(players, player, market, turn)
		#	if type(player) == Human:

		#		for k, v in player.goods_produced.items():
		#			v = 0

				print("################################################################################################################### \n ")
				print("%s, it is your turn to exploit the globe for the greatness of your nation! \n" % (player.name))
				while(True):
					print(" ############################################################################################################ \n")
					
					player.calculate_access_to_goods(market)
					print("%s, what is your imperial decree? \n" % (player.name))
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
							print("Stability: %s  ______________  Total Population: %s\n" % (player.stability, player.POP))
							print("Gold: %s  ___________________  Action Points: %s \n" % (player.resources["gold"], player.AP))
							print("Diplomatic: %s  _____________  Science Points: %s \n " % (player.diplo_action, player.research))
							print("Colonization: %s  ___________  Reputation: %s \n" % (player.colonization, player.reputation))
							print("Lower Class Pops: %s  _______  Middle Class Pops: %s \n" % (player.numLowerPOP, player.numMidPOP))
							print("Development Points: %s  _____ Development Level: %s \n" % (player.new_development, player.number_developments))
							print("Free POPs: %s  _______________ Culture Points: %s" % (player.freePOP, player.culture_points))
							print("Factories:")
							for k, v in player.factories.items():
								print(k,v)
						if info_command == "2":
							print("Province Overview: ######################################################################################## \n")
							for k, province in player.provinces.items():
								print("Name: %-20s 	Resource: %-10s 	Development Level: %s 	Worked?: %s 	Quality: %s \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality))
						if info_command == "3":
							print("Population Overview: ####################################################################################### \n")
							print("Total Population: %s 	Unassigned Pops: %s 	Lower Class Pops: %s 	Middle Class Pops: %s \n" % \
							(player.POP, player.freePOP, player.numLowerPOP, player.numMidPOP))
							print("Urban Worker Pops: %s 	Military Pops: %s \n" % (player.proPOP, player.milPOP))
							print("Middle Class POPs: \n")
							for k, v in player.midPOP.items():
								print("%s: %s, priority: %s \n"  % (k, v["number"], v["priority"]))
						if info_command == "4" :
							print("Military Overview: ################################################################################################ \n")
							for k, v in player.military.items():
								print(" %s: %s " % (k, v) )
						if info_command == "5":
							print("Inventory: ##########################################################################################################\n")
							for k, v in player.resources.items():
								print(" %s: %s " % (k, v) )
							for k, v in player.goods.items():
								print(" %s: %s " % (k, v) )
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
								print("Stability: %s  ______________  Total Population: %s\n" % (nation.stability, nation.POP))
								print("Gold: %s  ___________________  Action Points: %s \n" % (nation.resources["gold"], nation.AP))
								print("Diplomatic: %s  _____________  Science Points: %s \n " % (nation.diplo_action, nation.research))
								print("Colonization: %s  ___________  Number of Colonies: %s \n " % (nation.colonization, nation.num_colonies))
								print("Government: %s  _____________  Reputation: %s \n" % (nation.government, nation.reputation))
								print("Lower Class Pops: %s  _______  Middle Class Pops: %s \n" % (nation.numLowerPOP, nation.numMidPOP))
								print("Development Points: %s  _____  Development Level: %s \n" % (nation.new_development, nation.number_developments))
								print("Free POPS: %s _______________  ProPops: %s\n" % (nation.freePOP, nation.proPOP))
								print("Factories:")
								for k, v in nation.factories.items():
									print(k, v)
								print("Province Overview: ######################################################################################## \n")
								for k, province in nation.provinces.items():
									print("Name: %-20s 	Resource: %-10s 	Development Level: %s 	Worked?: %s 	Quality: %s   Culture: %s \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality, province.culture))
								print("Population Overview: ######################################################################################### \n")
								for k, v in nation.midPOP.items():
									print("%s: %s, priority: %s \n"  % (k, v["number"], v["priority"]))
								print("Military Overview: ################################################################################################ \n")
								for k, v in nation.military.items():
									print(" %s: %s " % (k, v) )
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
									print(v.relationship)
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
							while chem not in use_chemicals:
								for c in use_chemicals:
									print(c)
								chem = input()
							if chem == "1":
								if "synthetic_dyes" not in player.technologies:
									print("You need the synthetic_dyes technology to do this \n")
								elif players.goods["chemicals"] < 1:
									print("You do not have enough chemicals \n")
								else:
									amount = input("How many chemicals would you like to convert to dyes? (you have %s chemicals \n" % (player.goods["chemicals"]))
									if int(amount) > player.goods["chemicals"]:
										print("You do not have enough chemicals for that \n")
									else:
										player.goods["chemicals"] -= amount * 2
										player.resources["dyes"] += amount
										print("You now have %s dyes and %s chemicals" % (player.resources["dyes"], \
											player.goods["chemicals"]))

							if chem == "2":
								if "fertlizer" not in player.technologies:
									print("You need the fertlizer technology to do this \n")
								elif players.goods["chemicals"] < 1:
									print("You do not have enough chemicals \n")
								else:
									num_farms = 0
									for k, v in player.provinces.items():
										if v.resource == "food":
											num_farms += 1
									print("You have %s farming provinces and %s chemicals \n" % (num_farms, player.goods["chemicals"]))
									amount = input("How many farms would you like to improve? \n")
									if(amount > num_farms or amount > player.goods["chemicals"]):
										print("What is wrong with you anyway? \n")
									else:
										while amount > 0:
											for k, v in player.provinces.items():
												if v.resource == "food":
													v.quality += 0.12
													player.goods["chemicals"] -= 1
													print("%s now has a quality rating of: %s \n" % (v.name, v.quality))
								if chem == "3":
									if "synthetic_rubber" not in technologies:
										print ("You need the synthetic rubber technology to do this")
									elif players.goods["chemicals"] < 4:
										print("You do not have enough chemicals \n")
									else:
										player.goods["chemicals"] -= 5
										player.resources["rubber"] += 1
										rint("You now have %s rubber and %s chemicals" % (player.resources["rubber"], \
											player.goods["chemicals"]))
								if chem == "4":
									if "synthetic_oil" not in technologies:
										print ("You need the synthetic oil technology to do this")
									elif players.goods["chemicals"] < 4:
										print("You do not have enough chemicals \n")
									else:
										player.goods["chemicals"] -= 5
										player.resources["oil"] += 1
										rint("You now have %s oil and %s chemicals" % (player.resources["oil"], \
											player.goods["chemicals"]))



					if command == "4":
						print("What sort of item would you like to build? #################################################################################### \n")
						for k, v in build.items():
							print(k, v)
						sort = " "
						_choices = list(range(1, 6))
						choices = ''.join(str(e) for e in _choices)
						while (str(sort) not in choices):
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

					if command == "5":
						for k, j in military_action.items():
							print(k, j)
						action = " "
						_choices = list(range(1, 4))
						choices = ''.join(str(e) for e in _choices)
						while (str(action) not in choices):
							action = input()

						#War on Uncivilized Nation
						if action == "1":
							if player.diplo_action < 1:
								print("You do not have any diplomatic points")
							elif player.colonization < 1 + (player.num_colonies * 2):
								print("You do not have enough colonization points")
							else:
								options = set()
								print("On what uncivilized nation would you like to declare war? \n")
								for k, v in uncivilized_minors.items():
									if unciv.harsh == True and ("medicine" in player.technologies or "breach_loaded_arms" in player.technologies):
										continue
									if len(unciv.provinces) < 1:
										continue
									print(v.name)
									options.add(v.name)
									other = " "
									while other not in options:
										other = input()
									other = uncivilized_minors[other]
									print("Which province would you like to take (there is likely only 1 option:")
									for p in other.provinces.values():
										print(p)
									annex = " "
									while annex not in other.provinces.keys():
										annex = input()
									annex = other.provinces[annex]
									land = check_for_border(player, other)
									if land == False:
										print("Since you do not border %s, you must send your army by navy\n" % (other.name))
										amphib_prelude(player, other, annex)
										player.reputation -= 0.1
									else:
										print("Since we border %s, we may attack by land!" % (other.name))
										combat(player, other, annex)
										player.reputation -= 0.1

						#War on old_minor or old_empire
						if action == "2":
							if player.diplo_action < 1:
								print("You do not have any diplomatic points")
							elif player.colonization < 1 + (player.num_colonies * 2):
								print("You do not have enough colonization points")
							else:
								options = set()
								for p, pl in players.items():
									if pl.type == "old_minor":
										options.add(pl)
								if len(options) == 0:
									print("All old world minor nations have already been taken!!")
								else:
									other = " "
									while other not in options:
										print("On what old world minor power would you like to declare war? \n")
										other = input()
									other = players[other]
									annex = " "
									while annex not in other.provinces.keys():
										print("Which province do you seek to annex?\n")
										for p, prov in other.provinces.items():
											print(p.name, p.resources, p.quality)
										annex = input()
									annex = other.provinces[annex]
									land = player.check_for_border(other)
									if land == False:
										print("Since you do not border %s, you must send your army by navy\n" % (other.name))
										amphib_prelude(player, other, annex)
										player.reputation -= 0.1
									else:
										print("Since we border %s, we may attack by land!" % (other.name))
										combat(player, other, annex)
										player.reputation -= 0.1
						
						if action == "3":
							if player.diplo_action < 1:
								print("You do not have any diplomatic points")
							elif player.colonization < 1 + (player.num_colonies * 2):
								print("You do not have enough colonization points")
							else:
								options = set()
								for p, pl in players.items():
									if pl.type == "old_empire" and pl in player.CB:
										options.add(pl)
								if len(options) == 0:
									print("You do not have a CB on an Old World Empire at this time")
								else:
									other = " "
									while other not in options:
										print("On what old world empire would you like to declare war? \n")
										other = input()
									other = players[other]
									annex = " "
									while annex not in other.provinces.keys():
										print("Which province do you seek to annex?\n")
										for p, prov in other.provinces.items():
											print(p.name, p.resources, p.quality)
										annex = input()
									annex = other.provinces[annex]
									land = player.check_for_border(other)
									if land == False:
										print("Since you do not border %s, you must send your army by navy\n" % (other.name))
										amphib_prelude(player, other, annex)
										player.reputation -= 0.1
									else:
										print("Since we border %s, we may attack by land!" % (other.name))
										combat(player, other, annex)
										player.reputation -= 0.1

						#War on Modern Nation
						if action == "4":
							c_options = set()
							print("One which Major Power do you intend wage a colonial war?\n")
							for k, v in players.items():
								if v.type == "major":
									if v.num_colonies > 0 and v in player.CB:
										c_options.add(v.name)

							if len(c_options) == 0:
								print("There are currently no major powers on whom you may wage a colonial war \n")
							else:
								other = " "
								while other not in c_options:
									print("On which Modern nation do you intend wage a colonial war?\n")
									other = input()
								p_options = set()
								print("The following provinces are colonies belonging to %s" % (other.name))
								for prov in other.provinces.values():
									if prov.colony == True and prov.ocean == True:
										print(prov.name, prov.resources, prov.quality)
										p_options.add(prov.name)
							
								if player.check_for_border(other) and annex.colony:
									print("You may either try to capture %s by establishing naval domination or by \
										invading %s and taking it as a prize for victory")
									landOrSea = " "
									while landOrSea != "l" and landOrSea != "s":
										landOrSea = input("Do you choose land (l) or sea (s)?")
									if landOrSea == "s":
										naval_battle(player, other, annex)
										player.reputation -= 0.2
									else:
										combat(player, other, annex)
								elif annex.colony:
									print("You do not neighbor %s and so you must capture %s by establishing naval \
									dominance" % (other.name, annex.name))
									naval_battle(player, other, annex)
									player.reputation -= 0.2

						if action == "5":
							a_options = set()
							print("On which Major Power do you intend wage a colonial war?\n")
							for k, v in players.items():
								if v.type == "major":
									non_national = False
									for p, prov in v.provinces.items():
										if prov.culture != v.culture:
											non_national = True
									if non_national == True and v in player.CB:
										a_options.add(v.name)
							if len(c_options) == 0:
								print("There are currently no major powers on whom you may wage a minor war \n")
							else:
								other = " "
								while other not in a_options:
									print("On which Modern nation do you intend wage a minor war?\n")
									other = input()
								p_options = set()
								if player.check_for_border(other):
									for prov in other.provinces.values():
										if prov.culure != other.culture and player.check_for_ground_invasion(prov, provinces):
											print(prov.name, prov.resources, prov.quality)
											p_options.add(prov.name)
								annex = " "
								while annex not in p_options:
									print("The following are neighboring provinces that you may annex: \n")
									for p in p_options:
										print(p)
									annex = input()
								annex = other.provinces[annex]
								if check_for_border(player, other) and player.check_for_ground_invasion(annex, provinces):
									print("You may seek to capture neighboring %s from %s by land!" % (annex.name, other.name))
									combat(player, other, annex)
									player.reputation -= 0.3

						if action == "6":
							if player.military["tanks"] < 1:
								print("Great Wars can only be waged once you have Tanks in your military")
							else:
								options = set()
								for k, v in players.items():
									if v.type == "major" and v in player.CB:
										options.add(v)
								if len(options) == 0:
									print("You cannot currently wage war on a Major Power")
								else:
									other = " "
									while o not in options:
										print("On which Major Power would you like wage a Great War?")
										for o in options:
											print(o)
										other = input()
									land = check_for_border(player, other)
									if land == False:
										print("Since you do not border %s, you must send your army by navy\n" % (other.name))
										amphib_prelude(player, other, annex)
										player.reputation -= 0.1
									else:
										print("Since we border %s, we may attack by land!" % (other.name))
										combat(player, other, annex)
										player.reputation -= 0.1

				

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
								player.reputation += 0.025
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
							
							elif dip == "2":
								print("Please choose a Nation:\n" )
								for p in players.values():
									print(p.name)
								_other = " "
								while _other not in player.keys():
									_other = input()
								other = players[_other]
								relata = frozenset([player.name, other.name])
								player.diplo_action -=1
								relations[relata].relationship -= min(1, 10/(other.POP + 0.001))
								player.reputation -= 0.025
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
								player.diplo_action -=1


							elif dip == "3":
								options = []
								for k, v in players.items():
									if v.type == "major" or v.type == "old_empire":
										relata = frozenset([player.name, v.name])
										if relata.relationship <= -2.5:
											options.append(v)
								if len(options) < 1:
									print("Your relations are not currently bad enough with any nation to gain a CB \n")
								other = " "
								while other not in options:
									print("Please choose a nation: \n")
									for o in options:
										print(options)
										other = input()
								player.diplo_action -= 1
								player.CB.add(other)
								print("You are now able to declare war on %s \n" % (other))
								player.reputation -= 0.025


							elif dip == "4":
								print("Pick a pair of nations, whose relations you would like to damage:")
								print("Please choose Nation A:\n" )
								for p in players.values():
									print(p.name)
								PA = " "
								while PA not in player.keys():
									PA = input()
								print("Pick a pair of nations, whose relations you would like to damage:")
								print("Please choose Nation A:\n" )
								for p in players.values():
									print(p.name)
									PB = " "
									while PB not in player.keys():
										PB = input()
								relata = frozenset([PA, PB])
								PA = players[PA]
								PB = players[PB]
								modifier = 4/((PA.POP + PB.POP)/2)
								relations[relata].relationship -= modifier
								print("Relations between %s and %s have been reduced by %s to %s" % \
									(PA.name, PB.name, modifier, relations[relata].relationship))
								player.diplo_action -= 1


							elif dip == "5":
								other = " "
								while other not in players.keys():
									print("Which nation would you like to destabilize?\n")
									for p, pl in players.items():
										print("%s: stability: %" % (p, pl.stability))
										other = input()
								amount = 0
								if other.type == "old_empire" or other.type == "old_minor":
									amount = random()/2
								else:
									amount = random()/4
								other.stability -= amount
								if other.stability < -3.0:
									other.stability = -3.0
								player.diplo_action -=1
								player.reputation -= 0.1
								relata = frozenset([player.name, other.name])
								relations[relata].relationship -= 0.2
								print("The stability of %s has been reduced by %s and is now %s \n" % (other.name, amount, other.stability ))
						
							elif dip == "6":
								print ("This feature has not yet been implemented \n")

							elif dip == "7":
								print("Would you like to place an embargo on a nation (1) or lift an embargo (2)? \n")
								dec = input()
								options = []
								if dec == "1":
									for k, v in players.items():
										relata = frozenset([player.name, v.name])
										if relation[relata].relationship < -1.5:
											options.append(v)
									if len(options) < 1:
										print("You cannot place an embargo on any nation at this time (relations too good \n")
									else:
										ch = " "
										while ch not in options:
											print("On which nation would you like to place a trade embargo? \n")
											ch = input()
											other = players[ch]
											other.embargo.add(player)
											relata = frozenset(player.name, other.name)
											relations[relata].relationship -= 0.25
											player.diplo_action -= 1
								if dec == "2":
									for k, v in player.items():
										if player in v.embargo:
											option.append(v)
									if len(options) < 1:
										print("You are not currently placing any nation under embargo\n")
									else:
										ch = " "
										while ch not in options:
											print("Which nation do you wish to release from embargo? \n")
											ch = input()
										other = layers[ch]
										player.discard(other)
										player.diplo_action -= 1


					if command == "7":
						print(" ##################################################################################################################### \n")
						player.research_tech()

					if command == "8":
						choice = input("Would you like to buy (1) or sell (2)? \n")
						if choice == "1":
							market.show_market()
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
						_continue = False
						break
		#globe.world_update(players)


	#if turn > 1:
	#player.turn()
