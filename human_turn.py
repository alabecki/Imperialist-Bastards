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
from commands import*
from start import*
from save import*
from AI import*

def human_turn(player, cont):

	print("################################################################################################################### \n ")
	print("%s, it is your turn to exploit the globe for the greatness of your nation \n" % (player.name))
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
					for k, v in players:
						print(v.name)
					nation = input("Please input the name of the nation you would like to view \n")
					nation = players[nation]
					print("Information Report on %s: ###################################################################\n" % (nation.name))
							#print("Gold: %s 				Action Points: %s \n" % (player.gold, player.AP))
					print("Stability: %s  ______________  Total Population: %s\n" % (nation.stability, nation.POP))
					print("Gold: %s  ___________________  Action Points: %s \n" % (nation.resources["gold"], nation.AP))
					print("Diplomatic: %s  _____________  Science Points: %s \n " % (nation.diplo_action, nation.research))
					print("Colonization: %s  ___________  Reputation: %s \n" % (nation.colonization, nation.reputation))
					print("Lower Class Pops: %s  _______  Middle Class Pops: %s \n" % (nation.numLowerPOP, nation.numMidPOP))
					print("Development Points: %s  _____ Development Level: %s \n" % (nation.new_development, nation.number_developments))
					print("Factories:")
					for f in nation.factories:
						print(f)
					print("Province Overview: ######################################################################################## \n")
					for k, province in nation.provinces.items():
						print("Name: %s 	Resource: %s 	Development Level: %s 	Worked?: %s 	Quality: %s \n" % \
						(province.name, province.resource, province.development_level, province.worked, province.quality))
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
			player.assign_POP()
		if command == "3":
			print("What will be the means of production? #######################################################################################  \n")
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
				if "synthetic_dyes" not in player.technologies:
					print("You need the synthetic_dyes technology to do this \n")
				elif players.goods["chemicals"] < 1:
					print("You do not have enough chemicals \n")
				else:
					amount = input("How many chemicals would you like to convert to dyes? (you have %s chemicals \n" % (player.goods["chemicals"]))
					if int(amount) > player.goods["chemicals"]:
						print("You do not have enough chemicals for that \n")
					else:
						player.goods["chemicals"] -= amount
						player.resources["dyes"] += amount
			if means == "4":
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
									v.quality += 0.15
									player.goods["chemicals"] -= 1
									print("%s now has a quality rating of: %s \n" % (v.name, v.quality))
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
				player.build_factory(build_factory[kind])
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
			if action == "1":
				print("On what nation would you like to declare war? ############################################################################## \n")
				for k , v1 in players.items():
					print(v1.name)
				other = " "
				while other not in player.keys():
					other = input()
				other = players[other]
				if(other.name not in player.CB):
					print("You do not have a casus belli againt %s \n" % (other.name))
				else:
					if(other.name in player.borders):
						print("Since you border %s, you may attack directly by land \n" % (other.name))
						combat(player, other)
						player.reputation -= 0.2
					else:
						print("Since you do not border %s, you must send your army by navy\n" % (other.name))
						amount = naval_transport(player)
						if other.human == "human":
							print("That dasterdly %s is sending an armarda filled with soliders to your homeland! \n" % (player.name))
							print("His navy has %s frigates and %s ironclads. Your navy has %s frigates and %s ironclads" \
								% (player.military["frigates"], (player.military["iron_clad"]), other.military["frigates"], other.military["iron_clad"] ))
							inter = ""
							while inter != "y" and inter != "n":
								inter = input("Do you wish to send your army to intercept? (y/n)")
							if inter == "n":
								print("We will meet the enemy on the ground! \n")
								amph_combat(player, other, amount)
							else:
								print("Let us stop them in their tracks! \n")
								result = naval_battle(player, other)
								if result == other.name:
									print("%s attemps to sail his army to %s has failed\n" % (player.name, other.name))
								elif result == player.name:
									print:("%s has sailed his navy to %s and is about to invade! \n" % (player.name, other.name))
									amph_combat(player, other, amount)
			if action == "2":
				print("On what nation would you like to declare a colonial war? ####################################################################  \n")
				for k in players.keys():
					print(k)
				other = " "
				while other not in players.keys():
					other = input()
				if(other not in player.CB):
					print("You do not have a causu belli againt %s \n" % (other))
				elif(player.colonization < 1.0 + player.num_colonies):
					print("You do not have enough colonization point to add a new colony \n")
				if players[other].num_colonies < 1:
					print(other + " does not have any colonies :(  \n")
				else:
					options = []
					for k, v in other.provinces.itesm():
						if v.type == "colony":
							print(k, v.resource, v.quality)
							options.append(k)
					take = ""
					while take not in options:
						take = input("which colony will you attempt to take? \n")
					winner = naval_transport(player, players[other])
					player.reputation -= 0.1
					if winner == player.name:
						print("You have defeated " + other + "and " + take + "is now part of your empire! \n")
						player.provinces[take] = players[other].provinces[take]
						players[other].provinces.pop(take)
						player.provinces[take].type = "colony"
						player.colonization -= 1 + player.num_colonies
						player.num_colonies += 1
						player.stability += 1
						player.reputation -= 0.2
						player.relations["CB"].delete(other)
						if(player.provinces[take].worked == True):
							player.POP += 1
							player.numLowClass += 1
							players[other].POP -= 1
							players[other].numLowClass -= 1

					else:
						print("You have lost at sea against " + other + "! \n")
						player.stability -= 1
						players[other].stability += 1
						player.relations["CB"].delete(other)

			if action == "3":
				if(player.colonization < 1.0 + player.num_colonies):
					print("You do not have enough colonization points to get a new colony ####################################################### \n")
				else:
					for k, unciv in uncivilized_minors.items():
						print(unciv.name)
					print("On what minor uncivilized nation would you like to wage war? \n")
					other = " "
					while other not in uncivilized_minors.keys():
						other = input()
					combat_against_uncivilized(player, uncivilized_minors[other])
					player.reputation -= 0.1

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
					relations[relata].relationship +=1
					player.reputation += 0.05
					print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
			elif dip == "2":
				if player.diplo_action < 1:
					print("You do not have any dioplomatic actions \n")
				else:
					player.diplo_action -=1
					relations[relata].relationship -= 2
					player.reputation -= 0.05
					print("Your relation with %s is now %s " % (other.name, relations[relata].relationship))
					player.diplo_action -=1
			elif dip == "3":
				if player.diplo_action < 1:
					print("You do not have any dioplomatic actions \n")
				elif relations[relata].relationship > -2:
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
					amount = random.random()/2
					other.stability -= amount
					player.diplo_action -=1
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
			print(" ######################################################################################################################### \n ")
			player.setMiddleClassPriorities()
		if command == "10":
			print("####################################################################################################################### \n ")
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
