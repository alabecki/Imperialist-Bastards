
from player_class import Player
from technologies import*
from human import Human
from AI import AI
from minor_classes import*

#from AI_foreign_affairs import*

from random import*
from pprint import pprint
from copy import deepcopy




#
def combat(p1, p2, prov, players, market, relations):
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
		att_manouver_roll = uniform(1, 1.25)
		def_manouver_roll = uniform(1, 1.25)

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
		print("%s has %s units and base defense strength of %s \n" % (p2.name, def_number_units_army, def_str))

		print("%s manouver = %s, %s manouver = %s \n" % \
		(p1.name, att_manouver * att_manouver_roll, p2.name, def_manouver * def_manouver_roll))
		if( att_manouver * att_manouver_roll) > (def_manouver * def_manouver_roll):
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * 1.20
			if "indirect_fire" in p1.technologies:
				att_str += (p1.military["artillery"] * p1.artillery["attack"]) * 0.2
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


		temp = max(1, att_number_units_army * 0.25) 
		

		loss_mod = max(0.1, att_str/temp)


		att_losses = def_str/loss_mod
		def_losses = att_str/loss_mod

		print("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_number_units_army = distribute_losses(p1, att_losses, att_number_units_army)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
		done = False
		print("att_initial_army: %s, def_initial_army: %s \n" % (att_initial_army, def_initial_army))
		if(att_number_units_army < att_initial_army * 0.42):
			done = True
		if(def_number_units_army < def_initial_army * 0.35):
			done = True
		if att_number_units_army < 1 or def_number_units_army < 1:
			done = True
		if(done == True):
			if att_number_units_army > def_number_units_army:
				combat_outcome(p1.name, p1, p2, prov, players, market, relations)
				return
			else:
				combat_outcome(p2.name, p1, p2, prov, players, market, relations)
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
	#print("Ammo Needed for %s: %s" % (p.name, ammo_needed))

	return ammo_needed

def calculate_oil_needed(p):
	oil_needed = 0.0
	oil_needed += p.military["tank"] * p.tank["oil_use"]
	oil_needed += p.military["fighter"] * p.fighter["oil_use"]
	#print("Oil Needed for %s: %s" % (p.name, oil_needed))
	return oil_needed

def calculate_manouver(p):
	manouver = 0.0
	manouver += p.military["infantry"] * p.infantry["manouver"]
	manouver += p.military["cavalry"] * p.cavalry["manouver"]
	manouver += p.military["tank"] * p.tank["manouver"]
	manouver += p.military["fighter"] * p.fighter["manouver"]
	#manouver = manouver * (1 + p.midPOP["officers"]["number"])
	manouver = manouver * (1 + p.developments["military"]/5)
	return manouver

def calculate_oil_manouver(p):
	manouver = 0.0
	manouver += p.military["tank"] * p.tank["manouver"]
	manouver += p.military["fighter"] * p.fighter["manouver"]
	#manouver = manouver * (1 + p.midPOP["officers"]["number"])
	manouver = manouver * (1 + p.developments["military"]/5)

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
	while(losses >= 0.5 and num_units >= 0.5):
		#print("Losses %s , num_units %s \n" % (losses, num_units))
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


def resolve_total_war(winner, p1, p2, prov, players, market, relations):
	if winner == p1.name:
		p1.reputation -= 0.5
		print("%s has sucessfuly invaded %s ! \n" % (p1.name, p2.name))
		if p2.number_developments >= 4:
			opts = []
			for pr, province in p2.provinces.items():
				if province.development_level >= 1:
					opts.append(province)
			if len(opts) >= 5:
				amount = int(len(opts)/3)
				for i in range(amount):
					selection = choice(opts)
					if selection.development_level >= 1:
						selection.development_level -= 1
						print("As a result of the war, the development level of %s has been reduced to %s" % (selection.name, selection.development_level))
			
		num_resist = 0
		for p, pr in p2.provinces.items():
			if pr.culture != p1.culture and pr.culture == p2.culture:
				num_resist += 1

		num_resist = int(num_resist)
		for i in range(num_resist):
			p1.stability -= 0.2
			if p1.stability < -3:
				p1.stability = -3
			unit_types = ["infantry", "cavalry", "artillery", "tank", "fighter"]
			kind = choice(unit_types)
			if p1.military[kind] > 2:
				p1.military[kind] -= 0.04
				p1.milPOP -= 0.04
				p1.POP -= 0.04
			print("A %s unit belogning to %s has been damaged by %s resistance fighters!" % (kind, p1.name, p2.name))

		for r, res in p2.resources.items():
			if p1.resources[r] >= 3:
				p1.resources[r] += (p2.resources[r] - 2)
				p2.resources[r] = 2
		for g, good in p2.goods.items():
			if p1.goods[g] >= 3:
				p1.goods[g] += (p2.goods[g] -2)
				p2.goods[g] = 2
	
		for pl in players.values():
			sphere_target_copy = deepcopy(pl.sphere_targets)
			for st in sphere_target_copy:
				if st == p2.name:
					pl.sphere_targets.remove(st)
		capital = p2.capital
		for c in capital:
			print(c)
			p1.capital.add(c)
		core = p2.core_provinces()
		p2.capital = set()
		for p, pr in p2.provinces.items():
			if pr in core:
				p1.provinces[p] = pr
				p1.number_developments += pr.development_level
				pr.owner = p1.name 
				if type(p1) == AI:
					p1.resource_base[pr.resource] += pr.quality
					p1.ai_modify_priorities_from_province(p1.provinces[pr.name].resource)


		core_keys = []
		for c in core:
			core_keys.append(c.name)
		for ck in core_keys:
			print("%s has lost %s" % (p2.name, ck))
			p2.number_developments -= p2.provinces[ck].development_level
			p2.provinces.pop(ck)
			p2.resource_base[pr.resource] -= pr.quality

		#if p2.development_level >= 4:

		#if p2.numMidPOP >= 2:
		#	for p, pl in players.items():
		#		if pl.type == "major" and pl.stability > 0 and pl.name != p1.name:
		#			profs = list(p1.midPOP.keys())
		#			refuge = choice(profs)
		#			pl.midPOP[refuge]["number"] += 0.2
		#			pl.numMidPOP += 0.2
		#			p1.POP += 0.2
		#			p2.midPOP[refuge]["number"] -= 0.2
		#			p2.numMidPOP -= 0.2
		#			p2.POP -= 0.2
		#			print("A %s has fled from %s to %s" % (refuge, p2.name, pl.name))

		remains = (len(p2.provinces.keys()) * 1.2)

		p1.POP += (p2.POP - remains)
		p1.numLowerPOP += (p2.POP - remains)
		p2.POP = remains
		p2.numLowerPOP = remains
		#for k, v in p1.midPOP.items():
		#	p1.midPOP[k]["number"] += p2.midPOP[k]["number"]
		#	p1.numMidPOP += p2.midPOP[k]["number"]
		#	p1.POP += p2.midPOP[k]["number"]
		#	p2.numMidPOP -= p2.midPOP[k]["number"]
		#	p2.POP -= p2.midPOP[k]["number"]
		#	p2.midPOP[k]["number"] = 0
		

		for p, pl in players.items():
			
			if len(set([p1.name, p])) == 1 or len(set([p2.name, p])) == 1:
				continue
			if relations[frozenset([p2.name, p])].relationship < 1.5:
				relations[frozenset([p1.name, p])].relationship -= 1
			if relations[frozenset([p1.name, p])].relationship < 2.5:
				relations[frozenset([p1.name, p])].relationship -= 1
			if relations[frozenset([p2.name, p])].relationship < 1.5:
				relations[frozenset([p1.name, p])].relationship -= 1

		#recalculate borders of nations:
		p1_borders = set()
		for k, v in players.items():
			if p1.check_for_border(v) == True:
				p1_borders.add(k)
		p1.borders = p1_borders
		print("%s has lost a total war to %s" % (p2.name, p1.name))
		pause = input()

		p2_borders = set()
		if len(p2.provinces.keys()) >= 1:
			opts = list(p2.provinces.keys())
			ch = choice(opts)
			p2.capital.add(ch)
			p2_borders = set()
			for k, v in players.items():
				if p2.check_for_border(v) == True:
					p2_borders.add(k)
				p2.borders = p2_borders
		

		p2.defeated = True

		if len(p2.provinces.keys()) == 0:
			print("%s no longer exists as a nation!" % (p2.name))
	
			for k, v in market.market.items():
				for i in v:
					if i.owner == p2.name:
						if k in p1.resources.keys():
							p1.resources[k] += 1
						if k in p1.goods.keys():
							p1.goods[k] +=1
						market.market[k].remove(i)
						del i
			pause = input()
			relkeys = list(relations.keys())
			for r in relkeys:
				if p2.name in relations[r].relata:
					del relations[r]
			for pl in players.values():
				if type(pl) == AI:
					if p2.name in pl.sphere_targets:
						pl.sphere_targets.remove(p2.name)
					if p2 in pl.allied_target:
						pl.allied_target.remove(p2)
					if pl.rival_target != []:
						if p2.name == pl.rival_target[0].name:
							pl.rival_target = []
				if p2.name in pl.objectives:
					pl.objectives.remove(p2.name)
				if p2.name in pl.embargo:
					pl.embargo.remove(p2.name)	
				#sphere_target_copy = deepcopy(pl.sphere_targets)
				#for st in sphere_target_copy:
					#if st == p2.name:
			#			pl.sphere_targets.remove(st)
		
			del players[p2.name]
 	

	elif winner == p2.name:
		p1.stability -= 1
		if p1.stability < -3.0:
			p1.stability = -3.0
		p2.stability += 1
		if p1.stability > 3.0:
			p1.stability = 3.0
		print("%s has repelled %s's pitiful invasion! \n" % (p2.name, p1.name))
		print("Will we soon see a counter invasion from %s ?" %  (p2.name))
							


def combat_outcome(winner, p1, p2, prov, players, market, relations):

	if prov == "total":
		resolve_total_war(winner, p1, p2, prov, players, market, relations)
		return
	if type(p1) == AI:
		p1.rival_target = []
	relata = frozenset([p1.name, p2.name])
	p1.rival_target = []
	relations[relata].relationship += 1
	#cb_copy = deepcopy(p1.CB)


	cb_keys = []
	for cb in p1.CB:
		cb_keys.append(cb)

	for cb in cb_keys:
		if cb.province == prov.name:
			print("CB discharged: %s %s" % (cb.province, cb.opponent))
			p1.CB.remove(cb)
			del cb

	if winner == p1.name:
		
		print("%s has sucessfuly invaded %s ! \n" % (p1.name, p2.name))
		#p1.stability += 0.5
		#if p1.stability > 3:
		#	p1.stability = 3
		#maybe gain stability with Nationalism
		p2.just_attacked = 3

		if p2.number_developments >= 2:
			opts = []
			for pr, province in p2.provinces.items():
				if province.development_level >= 1:
					opts.append(province)
			if len(opts) >= 1:
				selection = choice(opts)
				selection.development_level -= 1
				print("As a result of the war, the development level of %s has been reduced to %s" % (selection.name, selection.development_level))

	
		if prov.name in p2.provinces.keys():
			gain_province(p1, p2, prov, players, market, relations)
		else:
			p1.war_after_math(p2, players, relations, prov)

		loot = p2.resources["gold"]/3.33
		p1.resources["gold"] += loot
		p2.resources["gold"] -= loot
		print("%s loots %s gold from %s \n" % (p1.name, loot, p2.name))
		if p2.type == "major" and p1.military["tank"] > 0 and prov.culture == p2.culture:
			p2.defeated == True
			print("%s has been defeated by %s! " % (p2.name, p1.name))
	
	elif winner == p2.name:
		p1.stability -= 0.5
		if p1.stability < -3.0:
			p1.stability = -3.0
		p2.stability += 0.5
		if p1.stability > 3.0:
			p1.stability = 3.0
		print("%s has repelled %s's pitiful invasion! \n" % (p2.name, p1.name))
		print("The war between %s and %s has ended in a white pease \n" % (p1.name, p2.name))
			

def gain_province(p1, p2, prov, players, market, relations):
	win_name = p1.name
	loss_name = p2.name
	print("%s has defeated %s for the province of %s \n" % (win_name, loss_name, prov.name))
	if prov.culture == p2.culture or prov.type == "civilized":
		#if p2.numMidPOP >= 1.0:
		#	num_prov = len(p2.provinces.keys())
		#	mid_keys = list(p2.midPOP.keys())
		#	amount = int((p2.numMidPOP/num_prov) * 8)
		#	for i in range(amount):
		#		switch = choice(mid_keys)
		#		p1.midPOP[switch]["number"] += 0.2
		#		p1.numMidPOP += 0.2
		#		p1.POP += 0.2
		#		p2.midPOP[switch]["number"] -= 0.2
		#		p2.numMidPOP -= 0.2
		#		p2.POP -= 0.2
		#		print("%s has lost a %s to %s" % (p2.name, switch, p1.name))
		if p2.development_level > 2:
			p2.development_level -= 1
			possibilities = []
			for d, dev in p2.developments.items():
				if dev > 0:
					possibilities.append(d)
			loss = choice(possibilities)
			p2.developments[loss] -= 1

	pause = input()
	prov.owner = p1.name
	#new = deepcopy(p2.provinces[prov.name])
	p1.number_developments += prov.development_level 
	#maybe add an option for sorchered earth 
	p2.number_developments -= prov.development_level
	p1.provinces[prov.name] = prov
	if type(p1) == AI:
		p1.resource_base[prov.resource] += prov.quality
		p1.ai_modify_priorities_from_province(p1.provinces[prov.name].resource)
	if type(p2) == AI:
		p2.resource_base[prov.resource] -= prov.quality
	p2_core = p2.core_provinces() 
	#p1.provinces[new.name].type = "old"
	if prov in p2_core:
		p2_core.remove(prov)
	p2.provinces.pop(prov.name)
	p2_core = list(p2_core)
	if prov.name in p2.capital:
		print(prov.name + "is old capital of" + p2.name)
		p2.capital.remove(prov.name)
	if len(p2.provinces.keys()) > 0 and len(p2.capital) == 0:
		if len(p2_core) > 0:
			ch = choice(p2_core)
			print("New Capital: %s" % (ch.name))
			p2.capital.add(ch.name)
		else:
			ch = choice(list(p2.provinces.keys()))
			p2.capital.add(ch)
	if prov.colony == True:
		p2.num_colonies -= 1
		p2.colonization += 1 + p1.num_colonies
	if p2.type == "old_empire" or p2.type == "old_minor" or prov.colony == True:
		p1.colonization -= (1 + p1.num_colonies)
		p1.provinces[prov.name].colony = True
		p1.num_colonies += 1
	if prov.worked == True:
		p1.POP += 1
		p1.numLowerPOP += 1
		p2.POP -= 1
		p2.numLowerPOP -= 1
	p1.stability -= 0.15
	if p1.stability < -3.0:
		p1.stability = -3.0
	
	p2.stability -= 0.25
	if p2.stability < -3.0:
		p2.stability = -3.0
	if len(p2.provinces.keys()) == 0:
		print("%s no longer exists as a nation!" % (p2.name))
		p1.war_after_math(p2, players, relations, prov)
		for k, v in p2.resources.items():
			p1.resources[k] += v
		for k, v in p2.goods.items():
			p1.goods[k] += v
		for k, v in market.market.items():
			for i in v:
				if i.owner == p2.name:
					if k in p1.resources.keys():
						p1.resources[k] += 1
					if k in p1.goods.keys():
						p1.goods[k] +=1
					market.market[k].remove(i)
					print("removed %s %s"% (i.owner, i.kind))
					del i
		pause = input()
		relkeys = list(relations.keys())
		for r in relkeys:
			if p2.name in relations[r].relata:
				del relations[r]
		for pl in players.values():
			if type(pl) == AI:
				if p2.name in pl.sphere_targets:
					pl.sphere_targets.remove(p2.name)
				if p2 in pl.allied_target:
					pl.allied_targets.remove(p2)
				if pl.rival_target != []:
					if p2.name == pl.rival_target[0].name:
						pl.rival_target = []
			if p2.name in pl.objectives:
					pl.objectives.remove(p2.name)
			if p2.name in pl.embargo:
				pl.embargo.remove(p2.name)
	
		del players[p2.name]
	else:
		p1.war_after_math(p2, players, relations, prov)
		p2_borders = set()
		for k, v in players.items():
			if p2.check_for_border(v) == True:
				p2_borders.add(k)
		p2.borders = p2_borders
	#recalculate borders of nations:
	p1_borders = set()
	for k, v in players.items():
		if p1.check_for_border(v) == True:
			p1_borders.add(k)
	p1.borders = p1_borders 

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
	num_units = 0
	manouver = 0
	for k, v in current_makeup.items():
		num_units += current_makeup[k]
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

	#manouver = manouver * (1 + player.midPOP["officers"]["number"]/2)
	#manouver = manouver/(num_units + 0.001)
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


def select_ground_forces(player, target):

	forces = {
		"infantry": 0,
		"cavalry": 0,
		"artillery": 0,
		"tank": 0,
		"fighter": 0
	}
	number = 0
	for k, v in forces.items():
		correct = False
		while correct == False:
			print("How many %s would you like to send? (you have %s)" % (k, player.military[k]))
			print("%s has %s %s" % (target.name, target.military[k], k))
			amount = input()
			amount = int(amount)
			if amount > player.military[k]:
				print("You only have %s %s" %(v, k))
				continue
			else:
				forces[k] = amount
				number += amount
				correct = True
	return forces



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
		#print("Oil amount %s" % (player_oil))
		#print("player oil %s" % (player.resources["oil"]))

		unciv_strength = unciv.number_irregulars * 0.65
		player_manouver_roll = uniform(0, 1)
		unciv_manouver_roll = uniform(0, 1)
		o_deficit = player.resources["oil"] - player_oil
		#print("deficit %s" % (o_deficit))
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
				player.colonization -= (1 + player.num_colonies) 
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


def amph_combat(p1, p2, p1_forces, prov, players, market, relations):
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


		att_manouver_roll = uniform(1, 1.25)
		def_manouver_roll = uniform(1, 1.25)



		p1o_deficit = p1.resources["oil"] - att_oil
		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			base = oil_amph_unit_man(p1, p1_forces)
			temp = abs(p1o_deficit/((att_oil * 1.5) + 0.01))
			penalty = base * (1 - temp)
			att_manouver -=  penalty

		p2o_deficit = p2.resources["oil"] - def_oil
		if p2o_deficit < 0:
			print("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
			base = calculate_oil_manouver(p2)
			temp = abs(p2o_deficit/(def_oil * 1.5) + 0.01)
			penalty = base * (1 - temp)
			att_manouver -=  penalty

		att_manouver = att_manouver * (((p1.developments["military"]) + 0.1)/((att_number_units_army) + 0.001))
		def_manouver = def_manouver * (((p2.developments["military"])+ 0.1)/((def_number_units_army) + 0.001))

		print("%s has %s units and base attack strength of %s \n" % (p1.name, att_number_units_army, att_str))
		print("%s has %s units and base defense strength of %s \n" % (p2.name, def_number_units_army, def_str))
		att_manouver = att_manouver * att_manouver_roll
		def_manouver = def_manouver * def_manouver_roll

		print("%s manouver = %s, %s manouver = %s \n" % (p1.name, att_manouver, p2.name, def_manouver))
		
		if( att_manouver * att_manouver_roll) > (def_manouver * def_manouver_roll):
			difference = att_manouver/(def_manouver + 0.001)
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * min( 1.33, difference)


		else:
			print("%s out-manouvers %s \n" % (p2.name, p1.name))
			difference = def_manouver/(att_manouver + 0.001)
			def_str = def_str * min( 1.33, difference)
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


		temp = max(1, att_number_units_army * 0.333) 
		

		loss_mod = att_str/temp


		att_losses = def_str/(loss_mod + 0.001)
		def_losses = att_str/(loss_mod + 0.001)

		if att_losses > att_number_units_army:
			temp = att_losses = att_number_units_army
			def_losses -= temp
		if def_losses > def_number_units_army:
			temp = def_losses - def_number_units_army
			att_losses -= temp
		
		done = False

		if att_losses < 0.50 and def_losses < 0.50:
			done = True

		print("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_current_makeup = distribute_losses_amph(p1, att_losses, att_number_units_army, att_current_makeup)
		att_number_units_army = calculate_amphib_num_units(p1, att_current_makeup)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))

		att_now = calculate_amphib_strength(p1, p1_forces)
		def_now = p2.calculate_base_defense_strength()
		if att_now >= def_now * 2 or def_now >= att_now * 2:
			done = True 

		if(att_number_units_army < att_initial_army * 0.45):
			done = True
		if(def_number_units_army < def_initial_army * 0.38):
			done = True
		if att_number_units_army < 1 or def_number_units_army < 1:
			done = True
		if done == True:	
			if att_number_units_army > def_number_units_army:
				combat_outcome(p1.name, p1, p2, prov, players, market, relations)
				return
			else:
				combat_outcome(p2.name, p1, p2, prov, players, market, relations)
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


def naval_transport(player, target):
	forces = {
		"infantry": 0,
		"cavalry": 0,
		"artillery": 0,
		"tank": 0,
		"fighter": 0
	}
	if player.military["infantry"] < 1:
		return forces
	forces["infantry"] += 1
	transport_limit = ((player.military["frigates"] + player.military["iron_clad"]) * 2 + player.military["battle_ship"] * 3) 
	if type(player) == Human:
		number = 0
		print("Your transport capacity is %s" % (transport_limit))
		for k, v in forces.items():
			correct = False
			while correct == False:
				amount = input("How many %s would you like to send? (you have %s)" % (k, player.military[k]))
				amount = int(amount)
				if number + amount > transport_limit:
					print("The amount you specified exceeds your capacity \n")
					continue
				elif amount > player.military[k]:
					print("You only have %s %s" %(v, k))
					continue
				else:
					forces[k] = amount
					number += amount
					correct = True
	if type(player) == AI:
		target_strength = target.calculate_base_defense_strength()
		#print("Target strength: %s" % (target_strength))
		self_strength = 0
		number_units = player.num_army_units()
		tries = 0
		number = 0
		while (self_strength < (target_strength * 2) and number_units > 0.99 and tries < 128 and number <= transport_limit):
			pick = choice(["infantry", "artillery", "cavalry", "fighter", "tank"])
			if (player.military[pick] - forces[pick]) >= 1:
			#	print("Adds %s " % (pick))
				forces[pick] += 1
				if pick == "infantry":
					self_strength += player.infantry["attack"]
				elif pick == "cavalry":
					self_strength += player.cavalry["attack"]
				elif pick == "artillery":
					self_strength += player.artillery["attack"]
				elif pick == "tank":
					self_strength += player.tank["attack"]
				elif pick == "fighter":
					self_strength += player.fighter["attack"]
				tries += 1
				number_units -= 1
				#print("Tries: %s" % (tries))
				number += 1
			else:
				tries += 1

	return forces




		#for v in range(int(transport_limit)):
		#	tries = 0
		#	while tries < 52:
		#		_type = choice(["infantry", "cavalry", "artillery", "tank", "fighter"])
		#		if (player.military[_type] - forces[_type]) >= 1:
		#			print("Load %s " % (_type))
		#			forces[_type] += 1
		#			break
		#		tries += 1
	print("forces:")
	for j, k in forces.items():
		print(j, k)
	return forces


def ai_transport_units(player, target):
	target_strength = target.calculate_base_defense_strength()
#	print("Target strength: %s" % (target_strength))
	self_strength = 0
	tries = 0
	number_units = player.num_army_units()
	transport_limit = ((player.military["frigates"] + player.military["iron_clad"]) * 2 + player.military["battle_ship"] * 3) 
	forces = {
		"infantry": 0,
		"cavalry": 0,
		"artillery": 0,
		"tank": 0,
		"fighter": 0
	}
	number = 0

	while (self_strength < (target_strength * 2) and number_units > 0.99 and tries < 128 and number <= transport_limit):
		pick = choice(["infantry", "artillery", "cavalry", "fighter", "tank"])
		if (player.military[pick] - forces[pick]) >= 1:
		#	print("Adds %s " % (pick))
			forces[pick] += 1
			if pick == "infantry":
				self_strength += player.infantry["attack"]
			elif pick == "cavalry":
				self_strength += player.cavalry["attack"]
			elif pick == "artillery":
				self_strength += player.artillery["attack"]
			elif pick == "tank":
				self_strength += player.tank["attack"]
			elif pick == "fighter":
				self_strength += player.fighter["attack"]
			tries += 1
			number_units -= 1
			print("Tries: %s" % (tries))
			number += 1
		else:
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
	#print("Oil Needed for %s: %s" % (player.name, amount))

	return amount

def calculate_oil_needed_navy(player):
	amount = player.military["battle_ship"] * player.battle_ship["oil_use"]
	#print("Oil Needed for %s: %s" % (player.name, amount))
	return amount


def naval_battle(p1, p2, market, relations, prov = " "):
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

		temp = max(1, att_number_units_navy * 0.25) 
		loss_mod = att_str/(temp + 0.001)
		att_losses = def_str/(loss_mod + 0.001)
		def_losses = att_str/(loss_mod + 0.001)

	

		print("%s takes %s losses, %s takes %s losses \n" % (p1.name, att_losses, p2.name, def_losses))
		att_number_units_navy = distribute_naval_losses(p1, att_losses, att_number_units_navy)
		def_number_units_navy = distribute_naval_losses(p2, def_losses, def_number_units_navy)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_navy, p2.name, def_number_units_navy))
		done = False
		if att_losses < 0.50 and def_losses < 0.50:
			done = True
		if(att_number_units_navy < att_initial_navy * 0.43):
			done = True
		if(def_number_units_navy < def_initial_navy * 0.35):
			done = True
		if att_number_units_navy < 1 or def_number_units_navy < 1:
			done = True
		if(done == True):
			if att_number_units_navy > def_number_units_navy:
				print("%s had defeated %s at sea! \n" % (p1.name, p2.name))
				winner = p1.name
				if prov in p2.provinces:
					gain_province(p1, p2, prov, players, market, relations)
				return winner
			else:
				print("%s had defeated %s at sea! \n"% (p2.name, p1.name))
				winner = p2.name
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

def amphib_prelude(player, other, annex, players, market, relations):
	amount = naval_transport(player, other)
	if amount["infantry"] == 0:
		return
	if type(other) == Human:
		print("That dastardly %s is sending an armada filled with soldiers to your homeland! \n" % (player.name))
		print("His navy has %s frigates and %s ironclads. Your navy has %s frigates and %s ironclads" \
			% (player.military["frigates"], (player.military["iron_clad"]), other.military["frigates"], other.military["iron_clad"] ))
		inter = ""
		while inter != "y" and inter != "n":
			inter = input("Do you wish to send your army to intercept? (y/n)")
		if inter == "n":
			print("We will meet the enemy on the ground! \n")
			amph_combat(player, other, amount, players, market, relations)
		else:
			print("Let us stop them in their tracks! \n")
			result = naval_battle(player, other, market, relations)
			if result == other.name:
				print("%s attempts to sail his army to %s has failed\n" % (player.name, other.name))
			elif result == player.name:
				print("%s has sailed his navy to %s and is about to invade! \n" % (player.name, other.name))
				amph_combat(player, other, amount, annex, players, market)
	elif calculate_naval_strength(other) >= calculate_naval_strength(player):
		result = naval_battle(player, other, market, relations)
		if result == other.name:
			print("%s attempts to sail his army to %s has failed\n" % (player.name, other.name))
			return
		elif result == player.name:
			print("%s has sailed his navy to %s and is about to invade! \n" % (player.name, other.name))
			amph_combat(player, other, amount, annex, players, market, relations)
			return
	else:
		amph_combat(player, other, amount, annex, players, market, relations)

	

