
from player_class import Player
from empire_class import Empire
from technologies import*
from human import Human
from AI import AI
#from AI_foreign_affairs import*

import random
from pprint import pprint
from copy import deepcopy

#
def combat(p1, p2):
	print("War has broken out between %s and %s !!_____________________________ \n" % (p1.name, p2.name))
	cont = input()
	att_initial_army = calculate_number_of_units(p1)
	def_initial_army = calculate_number_of_units(p2)
	while(True):
		att_number_units_army = calculate_number_of_units(p1)
		def_number_units_army = calculate_number_of_units(p2)
		att_str = calculate_base_attack_strength(p1)
		def_str = calculate_base_defense_strength(p2)
		att_ammo = calculate_ammo_needed(p1)
		def_ammo = calculate_ammo_needed(p2)
		att_manouver = calculate_manouver(p1)
		def_manouver = calculate_manouver(p2)
		att_manouver_roll = random.uniform(0, 1)
		def_manouver_roll = random.uniform(0, 1)

		print("%s has %s units and base attack strength of %s \n" % (p1.name, att_number_units_army, att_str))
		print("%s has %s units and base attack strength of %s \n" % (p2.name, def_number_units_army, def_str))

		print("%s manouver = %s, %s manouver = %s \n" % \
		(p1.name, att_manouver + att_manouver_roll, p2.name, def_manouver + def_manouver_roll))
		if( att_manouver + att_manouver_roll) > (def_manouver + def_manouver_roll):
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * 1.20
			if "indirect_fire" in p1.technologies:
				att_str += (p1.military["artillery"] * p1.artillery["attack"]) * 0.5
		else:
			print("%s out-manouvers %s \n" % (p2.name, p1.name))
			def_str = def_str * 1.20
			if "indirect_fire" in p2.technologies:
				def_str += (p2.military["artillery"] * p2.artillery["attack"]) * 0.5
		print("%s total attack strength: %s, %s total attack strength: %s \n" % (p1.name, att_str, p2.name, def_str))
		p1.goods["cannons"] -= att_ammo
		p2.goods["cannons"] =- def_ammo
		att_losses = def_str/3
		def_losses = att_str/3
		print("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_number_units_army = distribute_losses(p1, att_losses, att_number_units_army)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
		done = False
		print("att_initial_army: %s, def_initial_army: %s \n" % (att_initial_army, def_initial_army))
		if(att_number_units_army < att_initial_army * 0.4):
			done = True
		if(def_number_units_army < def_initial_army * 0.3):
			done = True
		if att_number_units_army < 1 or def_number_units_army < 1:
			done = True
		if(done == True):
			if att_number_units_army > def_number_units_army:
				combat_outcome(p1.name, p1, p2)
				return
			else:
				combat_outcome(p2.name, p1, p2)
				return
		else:
			if type(p1) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (p1.name, att_number_units_army, def_number_units_army))
				if(cont == "n"):
					print("%s has given up the assult in %s and has retreated \n" % (p1.name, p2.name))
					return
			if type(p1) == AI:
				att_str = calculate_base_attack_strength(p1)
				def_str = calculate_base_defense_strength(p2)
				if att_str * 0.85 < def_str:
					return


def calculate_number_of_units(player):
	count = 0
	count += player.military["infantry"] + player.military["cavalry"] + player.military["artillery"] + player.military["irregulars"]
	return count

def calculate_base_attack_strength(p1):
	strength = 0.0
	strength += p1.military["infantry"] * p1.infantry["attack"]
	strength += p1.military["cavalry"] * p1.cavalry["attack"]
	strength += p1.military["artillery"] * p1.artillery["attack"]
	return strength

def calculate_base_defense_strength(p2):
	strength = 0.0
	strength += p2.military["irregulars"] * p2.irregulars["defend"]
	strength += p2.military["infantry"] * p2.infantry["defend"]
	strength += p2.military["cavalry"] * p2.cavalry["defend"]
	strength += p2.military["artillery"] * p2.artillery["defend"]
	strength = strength * p2.fortification
	return strength

def calculate_ammo_needed(p):
	ammo_needed = 0.0
	ammo_needed += p.military["infantry"] * p.infantry["ammo_use"]
	ammo_needed += p.military["cavalry"] * p.cavalry["ammo_use"]
	ammo_needed += p.military["artillery"] * p.artillery["ammo_use"]
	return ammo_needed

def calculate_manouver(p):
	manouver = 0.0
	manouver += p.military["infantry"] * p.infantry["manouver"]
	manouver += p.military["artillery"] * p.infantry["manouver"]
	manouver += p.military["cavalry"] * p.infantry["manouver"]
	manouver = manouver * (1 + p.midPOP["officers"]["number"]/p.milPOP)
	return manouver

def distribute_losses(player, losses, num_units):
	while(losses > 0.5 and num_units >= 0.5):
		print("Losses %s , num_units %s \n" % (losses, num_units))
		if(player.military["irregulars"] >= 0.5):
			player.military["irregulars"] -= 0.5
			num_units -= 0.5
			#player.num_units -=0.5
			player.POP -= 0.075
			player.milPOP -= 0.075
			player.numLowerPOP -= 0.075
			losses -= 0.5
		loss = random.uniform(0, 1)
		if loss <= 0.4:
			if(player.military["infantry"] >= 0.5):
				player.military["infantry"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
			else:
				continue
		elif loss > 0.4 and loss <= 0.8:
			if(player.military["cavalry"] >= 0.5):
				player.military["cavalry"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
			else:
				continue
		elif loss >= 0.8:
			if(player.military["artillery"] >= 0.5):
				player.military["artillery"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
			else:
				continue
	return num_units


def distribute_losses_amph(player, losses, num_units, current_makeup):
	while(losses > 0.5 and player.number_units >= 0):
		loss = random.uniform(0, 1)
		if loss <= 0.4:
			if(current_makeup[0] > 0.5):
				player.military["infantry"] -=0.5
				current_makeup[0] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
		if loss > 0.4 and loss <= 0.8:
			if(current_makeup[1] > 0.5):
				player.military["cavalry"] -= 0.5
				current_makeup[1] -= 0.5
				#player.num_units -=0.5
				#def_losses -= 1
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
		if loss > 0.8:
			if(current_makeup[2] > 0.5):
				player.military["artillery"] -= 0.5
				current_makeup[2] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.075
				player.milPOP -= 0.075
				player.numLowerPOP -= 0.075
				losses -= 0.5
	return current_makeup

def combat_outcome(winner, p1, p2):
	if winner == p1.name:
		print("%s has sucessfuly invaded %s ! \n" % (p1.name, p2.name))
		p1.stability += 1
		if p1.stability > 3:
			p1.stability = 3
		p1.CB.discard(p2.name)
		if(p2.type == "empire" or p2.type == "old_minor"):
			old_empire_defeat(p1, p2)
		loot = p2.resources["gold"]/2.0
		p1.resources["gold"] += loot
		p2.resources["gold"] -= loot
		print("%s loots %s gold from %s \n" % (p1.name, loot, p2.name))
		return
	elif winner == p2.name:
		p1.stability -= 1
		if p1.stability < -3.0:
			p1.stability = -3.0
		p2.stability += 1
		if p1.stability > 3.0:
			p1.stability = 3.0
		print("%s has repelled %s's pitiful invasion! \n" % (p1.name, p2.name))
		if type(p2) == Human:
			cont = input("Does %s wish to (1) remain at war with %s, or to make a white pease? " % (p2.name, p1.name))
			if(cont == "1"):
				return
			if(cont == "2"):
				if type(p1) == Human:
					res = input("Does %s accept %s's offer of a white pease? (y/n) \n" % (p2.name))
					if(res == "y"):
						Print("The war between %s and %s has ended in a white pease \n" % (p1.name, p2.name))
						p1.CB.remove(p2.name)
		else:
			Print("The war between %s and %s has ended in a white pease \n" % (p1.name, p2.name))
			p1.CB.remove(p2.name)


def old_empire_defeat(p1, p2):
	win_name = p1.name
	loss_name = p2.name
	annex = " "
	if type(p1) == Human:
		print("%s has defeated the Old Empre (or Old_minor) %s and may now claim one of her provinces \n" % (win_name, loss_name))
		for k, p in p2.provinces.items():
			pprint (vars(p))
		annex = input("Please type in the name of the province you would like to take \n")
	if type(p1) == AI:
		priorities = sorted(p1.resource_priority, key= p1.resource_priority.get, reverse = True) 
		for r in priorities:
			for p, prov in p2.provinces.items():
						if r == prov.resource:
							annex = p 
	new = deepcopy(p2.provinces[annex])
	p1.provinces[new.name] = new
	p1.provinces[new.name].type = "colony"
	p1.provinces[new.name].worked = True
	p2.provinces.pop(annex)
	p1.POP += 1
	p1.numLowerPOP += 1
	p1.reputation -= 0.1
	p1.colonization -= 1
	p1.num_colonies += 1
	p2.POP -= 1
	p2.numLowerPOP -= 1
	p2.stability -= 0.5
	if p2.stability < -3.0:
		p2.stability = -3.0
	if len(p2.provinces) == 0:
		print("%s no longer exists as a nation!")

	print(annex + " is now part of " + p1.name)


def combat_against_uncivilized(player, unciv):
	print("The nation of %s is attacking %s !__________________________________________________" % (player.name, unciv.name))
	cont = input()
	if type(player) == Human:
		amount = naval_transport(player)
	if type(player) == AI:
		amount = ai_transport_units(player)

	player_initial_army = sum(amount)
	player_initial_makeup = amount
	player_current_makeup = amount
	unciv_initial_army = unciv.number_irregulars

	while(True):
		player_number_units_army = sum(player_current_makeup)
		player_str = player_current_makeup[0] * player.infantry["attack"] + player_current_makeup[1] * player.cavalry["attack"] + player_current_makeup[2] * player.artillery["attack"]
		player_ammo = player_current_makeup[0] * player.infantry["ammo_use"] + player_current_makeup[1] * player.cavalry["ammo_use"] + player_current_makeup[2] * player.artillery["ammo_use"]
		player_manouver = player_current_makeup[0] * player.infantry["manouver"] + player_current_makeup[1] * player.cavalry["manouver"] + player_current_makeup[2] * player.artillery["manouver"]
		player_manouver = player_manouver * (1 + player.midPOP["officers"]["number"]/player.milPOP)
		unciv_strength = unciv.number_irregulars * 0.65
		player_manouver_roll = random.uniform(0, 1)
		unciv_manouver_roll = random.uniform(0, 1)

		print("%s has %s units with a total attack strength of %s \n" % (player.name, player_initial_army, player_str))
		print("%s has %s units with a total attack strength of %s \n" % (unciv.name, unciv.number_irregulars, unciv_strength ))
		if(player_manouver + player_manouver_roll > 1.5 + unciv_manouver_roll):
			player_str = player_str * 1.20
			if "indirect_fire" in player.technologies:
				player_str += (player_current_makeup[2] * player.artillery["attack"]) * 0.5
		else:
			unciv_strength  = unciv_strength * 1.20
		player.goods["cannons"] -= player_ammo
		print("Player modified att str: %s \n" % (player_str))
		print("unciv modified att str %s \n" % (unciv_strength))
		player_losses = unciv_strength/3.0
		unciv_losses = player_str/3.0
		print("Player losses: %s \n" % (player_losses))
		print("unciv losses %s \n" % (unciv_losses))

		player_current_makeup = distribute_losses_amph(player, player_losses, player_number_units_army, player_current_makeup)
		player_number_units_army = sum(player_current_makeup)
		unciv.number_irregulars -= unciv_losses
		player_str = player_current_makeup[0] * player.infantry["attack"] + player_current_makeup[1] * player.cavalry["attack"] + player_current_makeup[2] * player.artillery["attack"]
		print("Player units remaining: %s. Player Stength: %s \n" % (player_number_units_army, player_str) )
		print("Unciv remaining: %s. Unciv Strenthg: %s \n" % (unciv.number_irregulars, unciv.number_irregulars * 0.65) )
		done = False
		if(player_number_units_army < player_initial_army * 0.4):
			done = True
		if(unciv.number_irregulars < unciv_initial_army * 0.4):
			done = True
		if(done == True):
			if player_number_units_army > unciv.number_irregulars:
				print("%s is now in the hands of %s \n" % (unciv.name, player.name))
				for k, prov in unciv.provinces.items():
					player.provinces[k] = prov
					player.provinces[k].type = "colony"
					player.provinces[k].worked = False
				player.colonization -= 1
				player.num_colonies +=1
				print("%s is now in possession of %s, which produces %s \n" % (player.name, prov.name, prov.resource))
				unciv.provinces.clear()
				return
			else:
				print("%s's attept to take %s has ended in failure, what an embarresment! \n" % (player.name, unciv.name))
				player.stability -= 0.5
				if p1.stability < -3.0:
					p1.stability = -3.0
				unciv.number_irregulars += 1
				return
		else:
			if type(player) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (player.name, str(player_number_units_army), str(number_irregulars)))
				if(cont == "n"):
					return
			if type(player) == AI:
				player_str = player_current_makeup[0] * player.infantry["attack"] + player_current_makeup[1] * player.cavalry["attack"] + player_current_makeup[2] * player.artillery["attack"]
				unciv_strength = unciv.number_irregulars * 0.65
				if player_str * 0.85 < unciv_strength:
					return


def amph_combat(p1, p2, p1_forces):
	att_initial_army = sum(p1_forces)
	att_initial_makeup = p1_forces
	att_current_makeup = p1_forces
	def_initial_army = calculate_number_of_units(p2)
	while(True):
		def_number_units_army = calculate_number_of_units(p2)
		att_number_units_army = sum(att_current_makeup)
		att_str = att_current_makeup[0] * p1.infantry["attack"] + att_current_makeup[1] * p1.cavalry["attack"] + att_current_makeup[2] * p1.artillery["attack"]
		def_str = calculate_base_defense_strength(p2)
		att_ammo = att_current_makeup[0] * p1.infantry["ammo_use"] + att_current_makeup[1] * p1.cavalry["ammo_use"] + att_current_makeup[2] * p1.artillery["ammo_use"]
		def_ammo = calculate_ammo_needed(p2)
		att_manouver = att_current_makeup[0] * p1.infantry["manouver"] + att_current_makeup[1] * p1.cavalry["manouver"] + att_current_makeup[2] * p1.artillery["manouver"]
		att_manouver = att_manouver * (1 + p1.midPOP["officers"]["number"]/p1.milPOP)
		def_manouver = calculate_manouver(p2)
		att_manouver_roll = random.uniform(0, 1)
		def_manouver_roll = random.uniform(0, 1)

		print("%s has %s units and base attack strength of %s \n" % (p1.name, att_number_units_army, att_str))
		print("%s has %s units and base attack strength of %s \n" % (p2.name, def_number_units_army, def_str))

		print("%s manouver = %s, %s manouver = %s \n" % (p1.name, att_manouver + att_manouver_roll, p2.name, def_manouver + def_manouver_roll))

		if( att_manouver + att_manouver_roll) > (def_manouver + def_manouver_roll):
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * 1.20
			if "indirect_fire" in p1.technologies:
				att_str += (att_current_makeup[2] * p1.artillery["attack"]) * 0.5
		else:
			print("%s out-manouvers %s \n" % (p2.name, p1.name))
			def_str = def_str * 1.20
			if "indirect_fire" in p2.technologies:
				def_str += (p2.military["artillery"] * p2.artillery["attack"]) * 0.5

		print("%s total attack strength: %s, %s total attack strength: %s \n" % (p1.name, att_str, p2.name, def_str))
		p1.goods["cannons"] -= att_ammo
		p2.goods["cannons"] =- def_ammo
		att_losses = def_str/3
		def_losses = att_str/3

		print("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_current_makeup = distribute_losses_amph(p1, att_losses, att_number_units_army, att_current_makeup)
		att_number_units_army = sum(att_current_makeup)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
		done = False
		if(att_number_units_army < att_initial_army * 0.4):
			done = True
		if(def_number_units_army < def_initial_army * 0.3):
			done = True
		if(done == True):
			if att_number_units_army > def_number_units_army:
				combat_outcome(p1.name, p1, p2)
				return
			else:
				combat_outcome(p2.name, p1, p2)
				return
		else:
			if type(p1) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (p1.name, att_number_units_army, def_number_units_army))
				if(cont == "n"):
					break
			if type(p1) == AI:
				player_str = player_current_makeup[0] * player.infantry["attack"] + player_current_makeup[1] * player.cavalry["attack"] + player_current_makeup[2] * player.artillery["attack"]
				def_str = calculate_base_defense_strength(p2)
				if player_str * 0.85 < def_str:
					return


def naval_transport(p1):
	transport_limit = int((p1.military["frigates"] * 2) + (p1.military["iron_clad"] *2))
	correct = False
	print("check")
	print("Your transport capacity is %s" % (transport_limit))
	while correct == False:
		amount = input("How many do you want to send of each of the following? \
		infantry, cavalry, and artillery (three numbers seprated by a space each) \n").split()
		amount = [int(x) for x in amount]
		if sum(amount) > transport_limit:
			print("The amount you specified exceeds your capacity \n")
		elif amount[0] > p1.military["infantry"] or amount[1] > p1.military["cavalry"] or amount[2] > p1.military["artillery"]:
			print("You do not have have that many units \n")
		else:
			correct = True
	return amount


def ai_transport_units(player):
	transport_limit = int((player.military["frigates"] * 2) + (player.military["iron_clad"] *2))
	forces = [0, 0, 0]
	for i in range(transport_limit):
		flag = False
		tries = 0
		while flag == False and tries < 12:
			type = random.choice(["infantry", "cavalry", "artillery"])
			if type == "infantry":
				if player.military["infantry"] - forces[0] >= 1:
					forces[0] += 1
					flag = True
			if type == "cavalry":
				if player.military["cavalry"] - forces[1] >= 1:
					forces[1] += 1
					flag = True
			if type == "artillery":
				if player.military["artillery"] - forces[2] >= 1:
					forces[2] += 1
					flag = True
			tries += 1
	return forces


def calculate_number_of_ships(player):
	count = 0
	count += player.military["frigates"] + player.military["iron_clad"]
	return count

def calculate_naval_strength(player):
	count = 0
	count += player.military["frigates"] * player.frigates["attack"] + random.uniform(0, 1)
	count +=  player.military["iron_clad"] * player.iron_clad["attack"]
	count = count * (1 + player.midPOP["officers"]["number"]/((player.milPOP) *2))
	return count



def distribute_naval_losses(player, losses, num_units):
	while(losses > 0.5 and num_units >= 0.1):
		while(player.military["frigates"] > 0.1 and losses > 0.5):
		#	print("Losses %s, num_units %s \n" % (losses, num_units))
			player.military["frigates"] -=0.5
			player.POP -= 0.075
			player.milPOP -= 0.075
			player.numLowerPOP -= 0.075
			num_units -= 0.5
			losses -= 0.5
		while(player.military["iron_clad"] >= 0.1 and losses > 0.5):
			player.military["iron_clad"] -= 0.5
			player.POP -= 0.075
			player.milPOP -= 0.075
			player.numLowerPOP -= 0.075
			num_units -= 0.5
			losses -= 0.5
	return num_units

def calculate_ammo_needed_navy(player):
	amount = 0
	amount += player.military["frigates"] * player.frigates["ammo_use"]
	amount += player.military["iron_clad"] * player.iron_clad["ammo_use"]
	return amount


def naval_battle(p1, p2):
	print("Naval Battle!!!!__________________________________________________________________________________")
	winner = ""
	att_initial_navy = calculate_number_of_ships(p1)
	def_initial_navy = calculate_number_of_ships(p2)
	print("%s has a fleet size of %s, %s has a fleet size of %s \n" % (p1.name, att_initial_navy, p2.name, def_initial_navy))
	while(True):
		att_number_units_navy = calculate_number_of_ships(p1)
		def_number_units_navy = calculate_number_of_ships(p2)
		def_ammo = calculate_ammo_needed_navy(p1)
		att_ammo = calculate_ammo_needed_navy(p2)
		att_str = calculate_naval_strength(p1)
		def_str = calculate_naval_strength(p2)
		print("%s has naval strength of %s, %s has naval strength of %s \n" % (p1.name, att_str, p2.name, def_str))
		p1.goods["cannons"] -= att_ammo
		p2.goods["cannons"] -= def_ammo
		att_losses = def_str/4
		def_losses = att_str/4
		print("%s takes %s losses, %s takes %s losses \n" % (p1.name, att_losses, p2.name, def_losses))
		att_number_units_navy = distribute_naval_losses(p1, att_losses, att_number_units_navy)
		def_number_units_navy = distribute_naval_losses(p2, def_losses, def_number_units_navy)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_navy, p2.name, def_number_units_navy))
		if(att_number_units_navy < att_initial_navy * 0.4):
			print("%s had defeated %s at sea! \n"% (p2.name, p1.name))
			winner = p2.name
			return winner
		elif(def_number_units_navy <= def_initial_navy * 0.4):
			print("%s had defeated %s at sea! \n" % (p1.name, p2.name))
			winner = p1.name
			return winner
		else:
			if type(p1) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (p1.name, att_number_units_navy, def_number_units_navy))
				if(cont == "n"):
					return p2.name
				if cont == "y":
					continue
			if type(p2) == AI:
				att_str = calculate_naval_strength(p1)
				def_str = calculate_naval_strength(p2)
				if att_str * 86 < def_str:
					return p2.name
				else:
					continue


