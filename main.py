
#!/usr/bin/env python3

from pprint import pprint
from random import*
from itertools import product, combinations
import sys
import shelve

from name_generator import*

from cheat import*
from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from combat import*
#from naval import*
from empire_class import*
from Old_Minor_Class import*
from commands import*
from start import*
from save import*
from AI import*
from human_turn import*
from AI_turn import*
from Scenario import*

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
	if selection == "S":
		initial = historical()
	elif selection == "L":
		name = input("What is the name of the save that you want to load? \n")
		initial = load_game(name)
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


	turn = 0
	_continue = True
	while(_continue == True):
		turn +=1
		print("\n Turn: %s \n" % (turn))
		print("Gold in market: %s \n" % (market.gold))
		for k, v in market.market.items():
			print (k, v)
		print("Players len: %s " % (len(players)))
		cont = input()
		order = list(players.keys())
		print("order len %s" % (len(order)))
		shuffle(order)
		for o in order:
			if type(players[o]) == AI:
				AI_turn(players, players[o], market, turn, uncivilized_minors)
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
							print("Free POPs: %s  _______________ Culture Points: %s" % (player.freePOP, player.culture))
							print("Factories:")
							for f in player.factories:
								print(f)
						if info_command == "2":
							print("Province Overview: ######################################################################################## \n")
							for k, province in player.provinces.items():
								print("Name: %s 	Resource: %s 	Development Level: %s 	Worked?: %s 	Quality: %s \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality))
						if info_command == "3":
							print("Population Overview: ######################################################################################### \n")
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
								print("Colonization: %s  ___________  Reputation: %s \n" % (nation.colonization, nation.reputation))
								print("Lower Class Pops: %s  _______  Middle Class Pops: %s \n" % (nation.numLowerPOP, nation.numMidPOP))
								print("Development Points: %s  _____ Development Level: %s \n" % (nation.new_development, nation.number_developments))
								print("Free POPS: %s ________________ProPops: %s\n" % (nation.freePOP, nation.proPOP))
								print("Factories:")
								for f in nation.factories:
									print(f)
								print("Province Overview: ######################################################################################## \n")
								for k, province in nation.provinces.items():
									print("Name: %s 	Resource: %s 	Development Level: %s 	Worked?: %s 	Quality: %s   Culture: \n" % \
									(province.name, province.resource, province.development_level, province.worked, province.quality, province.culture))
								print("Population Overview: ######################################################################################### \n")
								for k, v in nation.midPOP.items():
									print("%s: %s, priority: %s \n"  % (k, v["number"], v["priority"]))
								print("Military Overview: ################################################################################################ \n")
								for k, v in nation.military.items():
									print(" %s: %s " % (k, v) )
								print("Inventory: ##########################################################################################################\n")
								if type(nation) == "human":
									nation.view_inventory_production_needs()
								if type(nation) == "AI":
									nation.view_AI_inventory()

						if info_command == "8":
							print("Your Empire has developed the following technologies: \n")
							for t in player.technologies:
								print(t)
							print("You are currently in a position the research the following technologies: \n")
							for k, t in technology_dict.items():
								if(k not in player.technologies and t["requirement"] in player.technologies):
									print(k, t)

						if info_command == "9":
							print("You have land borders with: %s \n" % (player.borders))
							for k, v in relations.items():
								if player.name in v.relata:
									pprint(vars(v))
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
								for k1, v1 in use_chemicals:
									print(k1, k1)
								chem = input()
							if chem == "1":
								if "synthetic_dyes" not in player.technologies:
									print("You need the synthetic_dyes technology to do this \n")
								elif players.goods["chemicals"] < 2:
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
							print("What sort of factory would you like to build? ########### ################################################################## \n")
							for k, v in build_factory.items():
								print(k, v)
							kind = " "
							while kind not in build_factory.keys():
								kind = input()
							player.build_factory(build_factory[kind], market)
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
								print("On what old nation or empire would you like to declare war? \n")
								print("(Only those with whom your relations are sufficietly bad will be displayed)\n")
								count = 0
								for k, v in players.items():
									if v.type == "old_empire" or v.type == "old_minor":
										relata = frozenset([player.name, v.name])
										if relations[relata].relations < -2.5:
											options.add(v)
								if count == 0:
									print("There are no old nations on which you can declare war at this time \n")
								else:
									other = " "
									while other not in options:
										print("On what old nation or empire would you like to declare war? \n")
										other = input()
									other = players[other]
									print("Which provice do you seek to annex?\n")
									for p, prov in other.provinces.items():
										print(p.name, p.resources, p.quality)
									annex = " "
									while annex not in other.provinces.keys():
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
						if action == "3":
							c_options = set()
							print("One which Modern nation do you intend to declare war?\n")
							for k, v in players.items():
								if v.type == "major" or v.type == "civ_minor":
									relata = frozenset([player.name, v.name])
									if relations[relata].relations < -2.5:
										print(v.name)
										c_options.add(v.name)
							other = " "
							while other not in c_options:
								other = input()

							check = False
							p_options = set()
							print("The following provices (if any) are colonies belonging to %s" % (other.name))
							for prov in other.provinces.values():
								if prov.colony == True and prov.ocean == True:
									print(prov.name, prov.resources, prov.quality)
									p_options.add(prov.name)
							if player.check_for_border(other):
								print("The following (if any) are neigbouring provices that you may annex: \n")
								for prov in other.provinces.values():
									if prov.culure != other.culture and player.check_for_ground_invasion(prov, provinces):
										print(prov.name, prov.resources, prov.quality)
										p_options.add(prov.name)
							if len(p_options) < 1:
								print("%s does not have any provinces that can be annexed in war \n")
							else:
								annex = " "
								while annex not in p_options:
									annex = input()
								annex = other.provinces[annex]
								if check_for_border(player, other) and player.check_for_ground_invasion(annex, provinces):
									print("You may seek to capture neighbouring %s from %s by land!" % (annex.name, other.name))
									combat(player, other, annex)
									player.reputation -= 0.3
								elif player.check_for_border(other) and annex.colony:
									print("You may either try to capture %s by establishing naval dominaition or by \
										invadint %s and taking it as a prize for vicotry")
									landOrSea = " "
									while landOrSea != "l" and landOrSea != "s":
										landOrSea = input("Do you choose land (l) or sea (s)?")
									if landOrSea == "s":
										naval_battle(player, other, annex)
										player.reputation -= 0.2
									else:
										combat(player, other, annex)
								elif annex.colony:
									print("You do not neighbour %s and so you must capture %s by establishing naval \
									dominance" % (other.name, annex.name))
									amphib_prelude(player, other, annex)
									player.reputation -= 0.2

				

					if command == "6":
						print("Please choose a Nation: ###################################################################################################### \n" )
						for p in players.values():
							print(p.name)
						_other = " "
						while _other not in player.keys():
							_other = input()
						other = players[_other]
						relata = frozenset([player.name, other.name])
							#for e in old_empires
								#print(e.name)
						print("What action would you like to take? \n")
						for k, v in diplomacy.items():
							print(k, v)
						dip = " "
						_choices = list(range(1, 12))
						choices = ''.join(str(e) for e in _choices)
						while (str(dip) not in choices):
							dip = input()

						if dip == "1":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							else:
								player.diplo_action -=1
								relations[relata].relationship += min(1, 5/(other.POP + 0.001))
								player.reputation += 0.05
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
						elif dip == "2":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							else:
								player.diplo_action -=1
								relations[relata].relationship -= min(1, 10/(other.POP + 0.001))
								player.reputation -= 0.05
								print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
								player.diplo_action -=1
						elif dip == "3":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							elif relations[relata].relationship > -2.5:
								print("Your relations with %s are not bad enough yet, they are %s but must be less than -2 \n"\
								% (other.name, relations[relata].relationship))
							else:
								player.CB.add(other.name)
								print("You have gained a CB against %s, you may now declare war against it when you please! \n" % (other.name))
								player.diplo_action -=1
								player.reputation -= 0.05
						elif dip == "4":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							elif relations[relata].relationship < 1:
								print("Your relations with %s are not good enough yet, they are %s but must be at least 1 \n"\
								% (other.name, relations[relata].relationship))
							else:
								player.diplo_action -= 1.0
								player.reputation += 0.05
								relations[relata].non_aggression =True
								print("You now have a non-aggression pact with %s \n" % (other.name))
						elif dip == "5":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							elif relations[relata].relationship < 2:
								print("Your relations with %s are not good enough yet, they are %s but must be at least 2 \n"\
								% (other.name, relations[relata].relationship))
							else:
								player.diplo_action -= 1.0
								player.reputation += 0.05
								relations[relata].defensive_alliance = True

						elif dip == "6":
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							elif relations[relata].relationship < 3:
								print("Your relations with %s are not good enough yet, they are %s but must be at least 3 \n"\
								% (other.name, relations[relata].relationship))
							else:
								player.diplo_action -= 1.0
								player.reputation += 0.05
								relations[relata].full_alliance = True

						elif(dip == "7"):
							if player.diplo_action < 1:
								print("You do not have any dioplomatic actions \n")
							else:
								amount = 0
								if other.type == "old_empire" or other.type == "old_minor":
									amount = random()/1.5
								else:
									amount = random()/3
								other.stability -= amount
								if other.stability < -3.0:
									other.stability = -3.0
								player.diplo_action -=1
								player.reputation -= 0.1
								print("The stability of %s has been reduced by %s and is now %s \n" % (other.name, amount, other.stability ))
						else:
								print ("This feathre has not been added yet \n")
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
							market.buy_item(_type, player)
						elif choice == "2":
							player.view_inventory()
							_type = " "
							while _type not in market.market.keys():
								_type = input("What would you like to sell? \n")
							market.sell_item(_type, player)

					if command == "9":
						print("######################################################################################################### \n ")
						player.use_culture()
					if command == "10":
						print("####################################################################################################### \n ")
						check = input("Are you sure you want to end your turn? y/n \n")
						if check == "y":
							player.turn()
							break
						else:
							continue
					if command == "11":
						print("Would you like to make a new save? (If you have not created a save for this game yet, you should certainly choose yes) (y/n) \n")
						yn = input()
						if yn == "y":
							create_new_save_game(players, relations, uncivilized_minors, market)
						if yn == "n":
							save_name = input("Please write in the name of the save file (without file extension) \n")
							save_game(file_name, players, relations, uncivilized_minors, market)

					if command == "12":
						_continue = False
						break

	#if turn > 1:
		#player.turn()
