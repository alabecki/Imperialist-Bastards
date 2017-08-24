
from player_class import Player
from technologies import*
from human import Human
from AI import AI

#from AI_foreign_affairs import*

from random import*
from pprint import pprint
from copy import deepcopy




#
def combat(p1, p2, prov, players):
	print("War has broken out between %s and %s !!_____________________________ \n" % (p1.name, p2.name))
	cont = input()
	att_initial_army = calculate_number_of_units(p1)
	def_initial_army = calculate_number_of_units(p2)
	while(True):
		att_number_units_army = calculate_number_of_units(p1)
		def_number_units_army = calculate_number_of_units(p2)
		att_str = p1.calculate_base_attack_strength()
		def_str = p2.calculate_base_defense_strength()
		att_ammo = calculate_ammo_needed(p1)
		def_ammo = calculate_ammo_needed(p2)
		att_oil = calculate_oil_needed(p1)
		def_oil = calculate_oil_needed(p2)
		att_manouver = calculate_manouver(p1)
		def_manouver = calculate_manouver(p2)
		att_manouver_roll = uniform(0, 1)
		def_manouver_roll = uniform(0, 1)

		p1o_deficit = p1.resources["oil"] - att_oil
		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = calculate_oil_manouver(p1)
			temp = abs(p1o_deficit/((att_oil * 1.5) + 0.01))
			penalty = base * (1 - temp)
			att_manouver -=  penalty

		p2o_deficit = p2.resources["oil"] - def_oil
		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = calculate_oil_manouver(p2)
			temp = abs(p2o_deficit/((def_oil * 1.5) + 0.01))
			penalty = base * (1 - temp)
			att_manouver -=  penalty

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

		p1a_deficit = p1.goods["cannons"] - att_ammo
		if p1a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p1.name, abs(p1a_deficit)))
			penalty = abs(p1a_deficit/((att_ammo * 2) + 0.01))
			att_str = att_str * (1 - penalty)
			p1.goods["cannons"] = 0
		else:
			p1.goods["cannons"] -= att_ammo

		p2a_deficit = p2.goods["cannons"] - def_ammo
		if p2a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p2.name, abs(p2a_deficit)))
			penalty = abs(p2a_deficit/((def_ammo * 2) + 0.1))
			def_str = def_str * (1 - penalty)
			p2.goods["cannons"] = 0
		else:
			p2.goods["cannons"] -= def_ammo

		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = calculate_oil_def(p1)
			temp = abs(p1o_deficit/((att_oil *2) + 0.01))
			penalty = base * (1 - temp)
			att_str -= penalty
			p1.resources["oil"] = 0
		else:
			p1.resources["oil"] -= att_oil

		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = calculate_oil_def(p2)
			temp = abs(p2o_deficit/(def_oil *2))
			penalty = base * (1 - temp)
			def_str -= penalty
			p2.resources["oil"] = 0
		else:
			p2.resources["oil"] -= def_oil

	
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
				combat_outcome(p1.name, p1, p2, prov, players)
				return
			else:
				combat_outcome(p2.name, p1, p2, prov, players)
				return
		else:
			if type(p1) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (p1.name, att_number_units_army, def_number_units_army))
				if(cont == "n"):
					print("%s has given up the assult in %s and has retreated \n" % (p1.name, p2.name))
					return
			if type(p1) == AI:
				att_str = p1.calculate_base_attack_strength()
				def_str = p2.calculate_base_defense_strength()
				if att_str * 0.85 < def_str:
					return


def calculate_number_of_units(player):
	count = 0
	count += player.military["infantry"] + player.military["cavalry"] + player.military["artillery"] + \
	 player.military["irregulars"] + player.military["tank"] + player.military["fighter"]
	return count



def calculate_ammo_needed(p):
	ammo_needed = 0.0
	ammo_needed += p.military["infantry"] * p.infantry["ammo_use"]
	ammo_needed += p.military["cavalry"] * p.cavalry["ammo_use"]
	ammo_needed += p.military["artillery"] * p.artillery["ammo_use"]
	ammo_needed += p.military["tank"] * p.cavalry["ammo_use"]
	ammo_needed += p.military["fighter"] * p.artillery["ammo_use"]
	print("Ammo Needed for %s: %s" % (p.name, ammo_needed))

	return ammo_needed

def calculate_oil_needed(p):
	oil_needed = 0.0
	oil_needed += p.military["tank"] * p.tank["oil_use"]
	oil_needed += p.military["fighter"] * p.fighter["oil_use"]
	print("Oil Needed for %s: %s" % (p.name, oil_needed))
	return oil_needed

def calculate_manouver(p):
	manouver = 0.0
	manouver += p.military["infantry"] * p.infantry["manouver"]
	manouver += p.military["cavalry"] * p.infantry["manouver"]
	manouver += p.military["tank"] * p.infantry["manouver"]
	manouver += p.military["fighter"] * p.infantry["manouver"]
	manouver = manouver * (1 + p.midPOP["officers"]["number"])
	return manouver

def calculate_oil_manouver(p):
	manouver = 0.0
	manouver += p.military["tank"] * p.infantry["manouver"]
	manouver += p.military["fighter"] * p.infantry["manouver"]
	manouver = manouver * (1 + p.midPOP["officers"]["number"])
	return manouver

def calculate_oil_att(p):
	strength = 0.0
	strength += p.military["tank"] * p.tank["attack"]
	strength += p.military["fighter"] * p.fighter["attack"]
	return strength

def calculate_oil_def(p):
	strength = 0.0
	strength += p.military["tank"] * p.tank["defend"]
	strength += p.military["fighter"] * p.fighter["defend"]
	return strength


def distribute_losses(player, losses, num_units):
	while(losses > 0.5 and num_units >= 0.5):
		print("Losses %s , num_units %s \n" % (losses, num_units))
		if(player.military["irregulars"] >= 0.5):
			player.military["irregulars"] -= 0.5
			num_units -= 0.5
			#player.num_units -=0.5
			player.POP -= 0.1
			player.milPOP -= 0.1
			player.numLowerPOP -= 0.1
			losses -= 0.5
		loss = uniform(0, 1)
		if loss <= 0.25:
			if(player.military["infantry"] >= 0.5):
				player.military["infantry"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
		elif loss > 0.25 and loss <= 0.5:
			if(player.military["cavalry"] >= 0.5):
				player.military["cavalry"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
		elif loss > 0.5 and loss <= 0.7:
			if(player.military["tank"] >= 0.5):
				player.military["tank"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue

		elif loss > 0.7 and loss <= 0.85:
			if(player.military["artillery"] >= 0.5):
				player.military["artillery"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.2
				losses -= 0.5
			else:
				continue

		elif loss > 0.85:
			if(player.military["fighter"] >= 0.5):
				player.military["fighter"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
	return num_units


def distribute_losses_amph(player, losses, num_units, current_makeup):
	while(losses > 0.5 and num_units >= 0.5):
	
		loss = uniform(0, 1)
		if loss <= 0.25:
			if(current_makeup["infantry"] >= 0.5):
				player.military["infantry"] -=0.5
				current_makeup["infantry"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
		elif loss > 0.25 and loss <= 0.5:
			if(current_makeup["cavalry"] >= 0.5):
				player.military["cavalry"] -= 0.5
				num_units -= 0.5
				current_makeup["cavalry"] -= 0.5
				#player.num_units -=0.5
				#def_losses -= 1
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue

		elif loss > 0.5 and loss <= 0.7:
			if(current_makeup["tank"] >= 0.5):
				player.military["tank"] -= 0.5
				num_units -= 0.5
				current_makeup["tank"] -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
		elif loss > 0.7 and loss <= 0.85:
			if(current_makeup["artillery"] >= 0.5):
				player.military["artillery"] -= 0.5
				current_makeup["artillery"] -= 0.5
				num_units -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
		elif loss > 0.85:
			if(current_makeup["fighter"] >= 0.5):
				player.military["fighter"] -= 0.5
				num_units -= 0.5
				current_makeup["fighter"] -= 0.5
				#player.num_units -=0.5
				player.POP -= 0.1
				player.milPOP -= 0.1
				player.numLowerPOP -= 0.1
				losses -= 0.5
			else:
				continue
	return current_makeup

def combat_outcome(winner, p1, p2, prov, players):
	if winner == p1.name:
		print("%s has sucessfuly invaded %s ! \n" % (p1.name, p2.name))
		p1.stability += 0.5
		if p1.stability > 3:
			p1.stability = 3
		p1.CB.discard(p2)
		#print(prov.name)
		#if p2.type == "major" or p2.type == "old_empire":
		#	resolve_major_conflict()

		#for p, pr in p2.provinces.items():
		#	print(p, pr.name)
		if prov.name in p2.provinces.keys():
			gain_province(p1, p2, prov, players)
		else:
			print("PROV was not FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		loot = p2.resources["gold"]/2.0
		p1.resources["gold"] += loot
		p2.resources["gold"] -= loot
		print("%s loots %s gold from %s \n" % (p1.name, loot, p2.name))
		if p2.type == "major" and p1.military["tank"] > 0 and prov.culture == p2.culture:
			p2.defeated == True
			print("%s has been defeated by %s! " % (p2.name, p1.name))
		if p2 in p1.CB:
			p1.CB.remove(p2)
		return
	elif winner == p2.name:
		p1.stability -= 0.5
		if p1.stability < -3.0:
			p1.stability = -3.0
		p2.stability += 0.5
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
						p1.CB.remove(p2)
		else:
			print("The war between %s and %s has ended in a white pease \n" % (p1.name, p2.name))
			if p2.name in p1.CB:
				p1.CB.remove(p2)


def gain_province(p1, p2, prov, players):
	win_name = p1.name
	loss_name = p2.name
	print("%s has defeated %s for the province of %s \n" % (win_name, loss_name, prov.name))
	#new = deepcopy(p2.provinces[prov.name])
	p1.provinces[prov.name] = prov
	if type(p1) == AI:
		p1.resource_base[prov.resource] += prov.quality
		p1.ai_modify_priorities_from_province(p1.provinces[prov.name].resource)
	
	#p1.provinces[new.name].type = "old"
	p1.provinces[prov.name].worked = True
	p2.provinces.pop(prov.name)
	if p2.capital == prov.name and len(p2.provinces.keys()) > 0:
		opts = list(p2.provinces.keys())
		ch = choice(opts)
		p2.capital = ch

	if p2.type == "old_empire" or p2.type == "old_minor" or prov.colony == True:
		p1.colonization -= 1 + (p1.num_colonies * 2)
		p1.provinces[prov.name].colony == True
		p1.num_colonies += 1
	if prov.worked == True:
		p1.POP += 1
		p1.numLowerPOP += 1
		p2.POP -= 1
		p2.numLowerPOP -= 1
	p1.reputation -= 0.1
	#p1.num_colonies += 1
	p1.stability -= 0.15
	if p1.stability < -3.0:
		p1.stability = -3.0
	
	p2.stability -= 0.25
	if p2.stability < -3.0:
		p2.stability = -3.0
	if len(p2.provinces.keys()) == 0:
		print("%s no longer exists as a nation!")
	#recalculate borders of nations:
	p1_borders = set()
	for k, v in players.items():
		if p1.check_for_border(v) == True:
			p1_borders.add(v)
	p1.borders = p1_borders 
	if len(p2.provinces.keys()) != 0:
		p2_borders = set()
		for k, v in players.items():
			if p2.check_for_border(v) == True:
				p2_borders.add(v)
		p2.borders = p2_borders 


	print(str(prov) + " is now part of " + p1.name)


def calculate_amphib_num_units(player, current_makeup):
	number = 0
	for k, v in current_makeup.items():
		number += v
	return number

def calculate_amphib_strength(player, forces):
	strength = 0
	for k, v in forces.items():
		if k == "infantry":
			strength += forces[k] * player.infantry["attack"]
		if k == "cavalry":
			strength += forces[k] * player.cavalry["attack"]
		if k == "artillery":
			strength += forces[k] * player.artillery["attack"]
		if k == "tank":
			strength += forces[k] * player.tank["attack"]
		if k == "fighter":
			strength += forces[k] * player.fighter["attack"]
	return strength

def calculate_amphib_ammo(player, current_makeup):
	ammo = 0
	for k, v in current_makeup.items():
		if k == "infantry":
			ammo += current_makeup[k] * player.infantry["ammo_use"]
		if k == "cavalry":
			ammo += current_makeup[k] * player.cavalry["ammo_use"]
		if k == "artillery":
			ammo += current_makeup[k] * player.artillery["ammo_use"]
		if k == "tank":
			ammo += current_makeup[k] * player.tank["ammo_use"]
		if k == "fighter":
			ammo += current_makeup[k] * player.fighter["ammo_use"]
	return ammo

def calculate_amphib_man(player, current_makeup):
	manouver = 0
	for k, v in current_makeup.items():
		if k == "infantry":
			manouver += current_makeup[k] * player.infantry["manouver"]
		if k == "cavalry":
			manouver += current_makeup[k] * player.cavalry["manouver"]
		if k == "artillery":
			manouver += current_makeup[k] * player.artillery["manouver"]
		if k == "tank":
			manouver += current_makeup[k] * player.tank["manouver"]
		if k == "fighter":
			manouver += current_makeup[k] * player.fighter["manouver"]
	manouver = manouver * (1 + player.midPOP["officers"]["number"]/2)
	return manouver

def calculate_amphib_oil(player, current_makeup):
	oil = 0
	for k, v in current_makeup.items():
		if k == "tank":
			oil += current_makeup[k] * player.tank["oil_use"]
		if k == "fighter":
			oil += current_makeup[k] * player.fighter["oil_use"]
	return oil

def oil_amph_unit_str(player, current_makeup):
	amount = 0
	for k, v in current_makeup.items():
		if k == "tank":
			amount = current_makeup[k] * player.tank["attack"]
		if k == "fighter":
			amount = current_makeup[k] * player.fighter["attack"]
	return amount  

def oil_amph_unit_man(player, current_makeup):
	amount = 0
	for k, v in current_makeup.items():
		if k == "tank":
			amount = current_makeup[k] * player.tank["manouver"]
		if k == "fighter":
			amount = current_makeup[k] * player.fighter["manouver"]
	return amount  



def combat_against_uncivilized(player, unciv, cprov = ""):
	print("The nation of %s is attacking %s !__________________________________________________" % (player.name, unciv.name))
	cont = input()
	forces = {}
	if type(player) == Human:
		forces = naval_transport(player)
	if type(player) == AI:
		forces = player.ai_transport_units()

	player_initial_army = calculate_amphib_num_units(player, forces)
	player_initial_makeup = forces
	player_current_makeup = forces
	unciv_initial_army = unciv.number_irregulars

	while(True):
		player_number_units_army = calculate_amphib_num_units(player, player_current_makeup)
		player_str = calculate_amphib_strength(player, player_current_makeup)
		player_ammo = calculate_amphib_ammo(player, player_current_makeup)
		player_manouver = calculate_amphib_man(player, player_current_makeup)
		player_oil = calculate_amphib_oil(player, player_current_makeup)
		print("Oil amount %s" % (player_oil))
		print("player oil %s" % (player.resources["oil"]))

		unciv_strength = unciv.number_irregulars * 0.65
		player_manouver_roll = uniform(0, 1)
		unciv_manouver_roll = uniform(0, 1)
		o_deficit = player.resources["oil"] - player_oil
		print("deficit %s" % (o_deficit))
		if o_deficit < 0:
			print("%s has an oil deficit of %s" % (player.name, abs(o_deficit)))
			base = oil_amph_unit_man(player, player_current_makeup)
			temp = abs(o_deficit/(player_oil * 1.5))
			penalty = base * (1 - temp)
			player_manouver -=  penalty

		print("%s has %s units with a total attack strength of %s \n" % (player.name, player_number_units_army, player_str))
		print("%s has %s units with a total attack strength of %s \n" % (unciv.name, unciv.number_irregulars, unciv_strength ))
		if(player_manouver + player_manouver_roll > 1.5 + unciv_manouver_roll):
			player_str = player_str * 1.20
			if "indirect_fire" in player.technologies:
				player_str += (player_current_makeup["artillery"] * player.artillery["attack"]) * 0.5
		else:
			unciv_strength  = unciv_strength * 1.20
		
		a_deficit = player.goods["cannons"] - player_ammo
		if a_deficit < 0:
			print("%s has an ammo deficit of %s" % (player.name, abs(a_deficit)))
			penalty = abs(a_deficit/ (player_ammo * 2))
			player_str = player_str * (1 - penalty)
			player.goods["cannons"] = 0
		else:
			player.goods["cannons"] -= player_ammo

		if o_deficit < 0:
			print("%s has an oil deficit of %s" % (player.name, abs(o_deficit)))
			base = oil_amph_unit_str(player, player_current_makeup)
			temp = abs(o_deficit/(player_oil *2))
			penalty = base * (1 - temp)
			player_str -= penalty
			player.resources["oil"] = 0
		else:
			player.resources["oil"] -= player_oil

		print("Player modified att str: %s \n" % (player_str))
		print("unciv modified att str %s \n" % (unciv_strength))
		player_losses = unciv_strength/3.0
		unciv_losses = player_str/3.0
		print("Player losses: %s \n" % (player_losses))
		print("unciv losses %s \n" % (unciv_losses))

		player_current_makeup = distribute_losses_amph(player, player_losses, player_number_units_army, player_current_makeup)
		player_number_units_army = calculate_amphib_num_units(player, player_current_makeup)
		unciv.number_irregulars -= unciv_losses
		player_str = calculate_amphib_strength(player, player_current_makeup)
		print("Player units remaining: %s. Player Stength: %s \n" % (player_number_units_army, player_str) )
		print("Unciv remaining: %s. Unciv Strenthg: %s \n" % (unciv.number_irregulars, unciv.number_irregulars * 0.65) )
		done = False
		if(player_number_units_army < player_initial_army * 0.4):
			done = True
		if(unciv.number_irregulars < unciv_initial_army * 0.4):
			done = True
		if(done == True):
			if player_number_units_army > unciv.number_irregulars:
				print("%s has defeated %s for the province of %s \n" % (player.name, unciv.name, cprov.name))
				#print("What provinces does Unciv have?")
				#for p, prov in unciv.provinces.items():
				#	print(p, prov.name)
				new = deepcopy(unciv.provinces[cprov.name])
				
				player.provinces[new.name] = new
				#p1.provinces[new.name].type = "old"
				player.provinces[new.name].worked = False
				player.provinces[new.name].colony = True
				player.provinces[new.name].type = "uncivilized"
				player.POP += 1
				player.freePOP +=1
				player.numLowerPOP += 1
				player.resources["gold"] += 3


				unciv.provinces.pop(cprov.name)
				if type(player) == AI:
					player.resource_base[new.resource] += int(new.quality)
					player.ai_modify_priorities_from_province(player.provinces[new.name].resource)
				player.reputation -= 0.1
				player.colonization -= 1 + (player.num_colonies * 2)
				player.num_colonies += 1
				player.stability -= 0.1
				if player.stability < -3.0:
					player.stability = -3.0
				return
			else:
				print("%s's attept to take %s has ended in failure, what an embarresment! \n" % (player.name, unciv.name))
				player.stability -= 0.5
				if player.stability < -3.0:
					player.stability = -3.0
				unciv.number_irregulars += 1
				return
		else:
			if type(player) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (player.name, str(player_number_units_army), str(number_irregulars)))
				if(cont == "n"):
					return
			if type(player) == AI:
				player_str =  calculate_amphib_strength(player, player_current_makeup)
				unciv_strength = unciv.number_irregulars * 0.65
				if player_str * 0.85 < unciv_strength:
					return


def amph_combat(p1, p2, p1_forces, prov, players):
	print("War has broken out between %s and %s !! _____________________________ \n" % (p1.name, p2.name))
	cont = input()
	att_initial_army = calculate_amphib_num_units(p1, p1_forces)
	att_initial_makeup = p1_forces
	att_current_makeup = p1_forces
	def_initial_army = calculate_number_of_units(p2)
	while(True):
		def_number_units_army = calculate_number_of_units(p2)
		att_number_units_army = calculate_amphib_num_units(p1, p1_forces)
		att_str = calculate_amphib_strength(p1, p1_forces)
		def_str = p2.calculate_base_defense_strength()
		att_ammo = calculate_amphib_ammo(p1, p1_forces)
		att_oil = calculate_amphib_oil(p1, p1_forces)
		def_ammo = calculate_ammo_needed(p2)
		def_oil = calculate_oil_needed(p2)
		att_manouver = calculate_amphib_man(p1, p1_forces)
		def_manouver = calculate_manouver(p2)
		att_manouver_roll = uniform(0, 1)
		def_manouver_roll = uniform(0, 1)

		p1o_deficit = p1.resources["oil"] - att_oil
		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = oil_amph_unit_man(p1, p1_forces)
			temp = abs(p1o_deficit/(att_oil * 1.5))
			penalty = base * (1 - temp)
			att_manouver -=  penalty

		p2o_deficit = p2.resources["oil"] - def_oil
		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = calculate_oil_manouver(p2)
			temp = abs(p2o_deficit/(def_oil * 1.5))
			penalty = base * (1 - temp)
			att_manouver -=  penalty

		print("%s has %s units and base attack strength of %s \n" % (p1.name, att_number_units_army, att_str))
		print("%s has %s units and base attack strength of %s \n" % (p2.name, def_number_units_army, def_str))

		print("%s manouver = %s, %s manouver = %s \n" % (p1.name, att_manouver + att_manouver_roll, p2.name, def_manouver + def_manouver_roll))

		if( att_manouver + att_manouver_roll) > (def_manouver + def_manouver_roll):
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * 1.20
			if "indirect_fire" in p1.technologies:
				att_str += (att_current_makeup["artillery"] * p1.artillery["attack"]) * 0.5
		else:
			print("%s out-manouvers %s \n" % (p2.name, p1.name))
			def_str = def_str * 1.20
			if "indirect_fire" in p2.technologies:
				def_str += (p2.military["artillery"] * p2.artillery["attack"]) * 0.5

		print("%s total attack strength: %s, %s total attack strength: %s \n" % (p1.name, att_str, p2.name, def_str))
		p1a_deficit = p1.goods["cannons"] - att_ammo
		if p1a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p1.name, abs(p1a_deficit)))
			penalty = abs(p1a_deficit/ ((att_ammo * 2) + 0.01))
			att_str = att_str * (1 - penalty)
			p1.goods["cannons"] = 0
		else:
			p1.goods["cannons"] -= att_ammo
		
		p2a_deficit = p2.goods["cannons"] - def_ammo
		if p2a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p2.name, abs(p2a_deficit)))
			penalty = abs(p2a_deficit/ ((def_ammo * 2) + 0.01))
			def_str = def_str * (1 - penalty)
			p2.goods["cannons"] = 0
		else:
			p2.goods["cannons"] -= def_ammo

		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = oil_amph_unit_str(p1, p1_forces)
			temp = abs(p1o_deficit/((att_oil *2) + 0.01))
			penalty = base * (1 - temp)
			att_str -= penalty
			p1.resources["oil"] = 0
		else:
			p1.resources["oil"] -= att_oil

		p2o_deficit = p2.resources["oil"] - def_oil
		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = calculate_oil_def(p2)
			temp = abs(p2o_deficit/((def_oil *2) + 0.01))
			penalty = base * (1 - temp)
			def_str -= penalty
			p2.resources["oil"] = 0
		else:
			p2.resources["oil"] -= def_oil

		att_losses = def_str/3
		def_losses = att_str/3
		if att_losses > att_number_units_army:
			temp = att_losses = att_number_units_army
			def_losses -= temp
		if def_losses > def_number_units_army:
			temp = def_losses - def_number_units_army
			att_losses -= temp
		done = False
		if att_losses < 0.52 and def_losses < 0.52:
			done = True
		print("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_current_makeup = distribute_losses_amph(p1, att_losses, att_number_units_army, att_current_makeup)
		att_number_units_army = calculate_amphib_num_units(p1, att_current_makeup)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
		done = False

		if(att_number_units_army <= att_initial_army * 0.6):
			done = True
		if(def_number_units_army <= def_initial_army * 0.5):
			done = True
		if done == True:
			if att_number_units_army > def_number_units_army:
				combat_outcome(p1.name, p1, p2, prov, players)
				return
			else:
				combat_outcome(p2.name, p1, p2, prov, players)
				return
		else:
			if type(p1) == Human:
				cont = input("%s, you currently have %s units, the enemy has %s units, would you like to continue the assult? (y,n)" \
				% (p1.name, att_number_units_army, def_number_units_army))
				if(cont == "n"):
					break
			if type(p1) == AI:
				att_str = calculate_amphib_strength(p1, p1_forces)
				def_str = p2.calculate_base_defense_strength()
				if att_str * 0.85 < def_str:
					return


def naval_transport(player):
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	forces = {
		"infantry": 0,
		"cavalry": 0,
		"artillery": 0,
		"tank": 0,
		"fighter": 0
	}
	if type(player) == Human:
		number = 0
		correct = False
		print("Your transport capacity is %s" % (transport_limit))
		for k, v in forces.items():
			while correct == False:
				amount = input("How many %s would you like to send? (you have %s)" % (k, v))
				if number + amount > transport_limit:
					print("The amount you specified exceeds your capacity \n")
					continue
				elif amount > player.military[v]:
					print("You only have %s %s" (v, k))
					continue
				else:
					forces[k] = amount
					correct = True
	if type(player) == AI:
		for v in range(int(transport_limit)):
			tries = 0
			while tries < 40:
				_type = choice(["infantry", "cavalry", "artillery", "tank", "fighter"])
				if (player.military[_type] - forces[_type]) >= 1:
					print("Load %s " % (_type))
					forces[_type] += 1
					break
				tries += 1
	print("forces:")
	for j, k in forces.items():
		print(j, k)
	return forces


def ai_transport_units(player):
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	forces = {
		"infantry": 0,
		"cavalry": 0,
		"artillery": 0,
		"tank": 0,
		"fighter": 0
	}
	number = 0
	for v in range(int(transport_limit)):
		tries = 0
		while tries < 32:
			_type = choice(["infantry", "cavalry", "artillery", "tank", "fighter"])
			if player.military[_type] - forces[_type] >= 1:
				forces[_type] += 1
				break
			tries += 1

	return forces


def calculate_number_of_ships(player):
	count = 0
	count += player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]
	return count

def calculate_naval_strength(player):
	count = 0
	count += player.military["frigates"] * player.frigates["attack"]
	count +=  player.military["iron_clad"] * player.iron_clad["attack"]
	count +=  player.military["battle_ship"] * player.battle_ship["attack"]
	return count


def distribute_naval_losses(player, losses, num_units):
	limit = 0
	while(losses > 0.2 and num_units >= 0.2):
		while(player.military["frigates"] > 0.2 and losses > 0.2):
		#	print("Losses %s, num_units %s \n" % (losses, num_units))
			player.military["frigates"] -=0.5
			player.POP -= 0.1
			player.milPOP -= 0.1
			player.numLowerPOP -= 0.1
			num_units -= 0.5
			losses -= 0.5
			limit += 1
			if limit > 20:
				break
		while(player.military["iron_clad"] >= 0.2 and losses > 0.2):
			player.military["iron_clad"] -= 0.25
			player.POP -= 0.05
			player.milPOP -= 0.05
			player.numLowerPOP -= 0.05
			num_units -= 0.25
			losses -= 0.5
			limit += 1
			if limit > 30:
				break
		while(player.military["battle_ship"] >= 0.2 and losses > 0.2):
			player.military["battle_ship"] -= 0.125
			player.POP -= 0.025
			player.milPOP -= 0.025
			player.numLowerPOP -= 0.025
			num_units -= 0.125
			losses -= 0.5
			limit += 1
			if limit > 40:
				break
		limit += 1
		if limit > 60:
			return num_units
	return num_units

def calculate_ammo_needed_navy(player):
	amount = 0
	amount += player.military["frigates"] * player.frigates["ammo_use"]
	amount += player.military["iron_clad"] * player.iron_clad["ammo_use"]
	amount += player.military["battle_ship"] * player.battle_ship["ammo_use"]
	print("Oil Needed for %s: %s" % (player.name, amount))

	return amount

def calculate_oil_needed_navy(player):
	amount = player.military["battle_ship"] * player.battle_ship["oil_use"]
	print("Oil Needed for %s: %s" % (player.name, amount))
	return amount


def naval_battle(p1, p2, prov = " "):
	print("A naval battle is being fought between %s and %s !!_____________________________ \n" % (p1.name, p2.name))
	cont = input()
	winner = ""
	att_initial_navy = calculate_number_of_ships(p1)
	def_initial_navy = calculate_number_of_ships(p2)
	print("%s has a fleet size of %s, %s has a fleet size of %s \n" % (p1.name, att_initial_navy, p2.name, def_initial_navy))
	while(True):
		att_number_units_navy = calculate_number_of_ships(p1)
		def_number_units_navy = calculate_number_of_ships(p2)
		att_ammo = calculate_ammo_needed_navy(p1)
		def_ammo = calculate_ammo_needed_navy(p2)
		att_oil = calculate_oil_needed_navy(p1)
		def_oil = calculate_oil_needed_navy(p2)
		att_str = calculate_naval_strength(p1)
		def_str = calculate_naval_strength(p2)
		print("%s has naval strength of %s, %s has naval strength of %s \n" % (p1.name, att_str, p2.name, def_str))
		p1a_deficit = p1.goods["cannons"] - att_ammo
		if p1a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p1.name, abs(p1a_deficit)))
			penalty = abs(p1a_deficit/ ((att_ammo * 2) + 0.1))
			att_str = att_str * max((1 - penalty), 0.3)
			p1.goods["cannons"] = 0
		else:
			p1.goods["cannons"] -= att_ammo

		p2a_deficit = p2.goods["cannons"] - def_ammo
		if p2a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p2.name, abs(p2a_deficit)))
			penalty = abs(p2a_deficit/ ((def_ammo * 2) + 0.1))
			att_str = def_str * max((1 - penalty), 0.3)
			p2.goods["cannons"] = 0
		else:
			p2.goods["cannons"] -= def_ammo

		p1o_deficit = p1.resources["oil"] - att_oil
		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = p1.military["battle_ship"] * p1.battle_ship["oil_use"]
			temp = abs(p1o_deficit/((att_oil *2) + 0.1))
			#penalty = base * max((1 - temp), 0.25)

			att_str = att_str * max(1 - temp, 0.3)
			p1.resources["oil"] = 0
		else:
			p1.resources["oil"] -= att_oil

		p2o_deficit = p2.resources["oil"] - def_oil
		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = p2.military["battle_ship"] * p2.battle_ship["oil_use"]
			temp = abs(p2o_deficit/(def_oil *2))
			#penalty = base * max((1 - temp), 0.3)
			#def_str - penalty
			def_str = def_str * max(1 - temp, 0.3)

			p2.resources["oil"] = 0
		else:
			p2.resources["oil"] -= def_oil
		print("Attack str: %s" % (att_str))
		print("Defense str: %s " % (def_str))

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
			if prov in p2.provinces:
				gain_province(p1, p2, prov, players)
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

def amphib_prelude(player, other, annex, players):
	amount = naval_transport(player)
	if type(other) == Human:
		print("That dastardly %s is sending an armada filled with soldiers to your homeland! \n" % (player.name))
		print("His navy has %s frigates and %s ironclads. Your navy has %s frigates and %s ironclads" \
			% (player.military["frigates"], (player.military["iron_clad"]), other.military["frigates"], other.military["iron_clad"] ))
		inter = ""
		while inter != "y" and inter != "n":
			inter = input("Do you wish to send your army to intercept? (y/n)")
		if inter == "n":
			print("We will meet the enemy on the ground! \n")
			amph_combat(player, other, amount, players)
		else:
			print("Let us stop them in their tracks! \n")
			result = naval_battle(player, other)
			if result == other.name:
				print("%s attempts to sail his army to %s has failed\n" % (player.name, other.name))
			elif result == player.name:
				print("%s has sailed his navy to %s and is about to invade! \n" % (player.name, other.name))
				amph_combat(player, other, amount, annex, players)
	elif calculate_naval_strength(other) >= calculate_naval_strength(player):
		result = naval_battle(player, other)
		if result == other.name:
			print("%s attempts to sail his army to %s has failed\n" % (player.name, other.name))
		elif result == player.name:
			print("%s has sailed his navy to %s and is about to invade! \n" % (player.name, other.name))
			amph_combat(player, other, amount, annex, players)
	else:
		amph_combat(player, other, amount, annex, players)

	

