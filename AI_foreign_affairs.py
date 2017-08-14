#AI Foreign Affairs

from AI import*
from combat import*

from player_class import*
from globe import*

import queue as queue
from random import*



def ai_decide_unciv_colonial_war(player, players, uncivilized_minors, provinces):
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 

	if player.type == "old_empire" or player.type =="old_minor":
		return
	print("Col Check 0")
	if player.colonization < 1 + (player.num_colonies * 2) or player.diplo_action < 1 or transport_limit < 4:
		return
	print("Col Check 1")
	priorities = sorted(player.resource_priority, key= player.resource_priority.get, reverse = True) 
	print("Priorities:")
	for r in priorities:
		print(r)
	self_strength = player.calculate_base_attack_strength()
	self_naval_projection_strength = player.ai_naval_projection()
	if self_strength < 3.5:
		return
	print("Col Check 2")

	c_options = set()
	p_options = set()
	for k, unciv in uncivilized_minors.items():
		if unciv.harsh == True and ("medicine" not in player.technologies or "breach_loaded_arms" not in player.technologies):
			continue
		if len(unciv.provinces) >= 1:
			print(unciv.name)
			for prov in unciv.provinces.values():
				if player.check_for_ground_invasion(prov, provinces) == True and self_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
				elif self_naval_projection_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
					
	#for p, pl in players.items():
	#	if pl.type == "old_minor" and len(pl.provinces) >= 1:
	#		old_strength = calculate_base_defense_strength(pl)
	#		for prov in pl.provinces.values():
	#			if player.check_for_ground_invasion(prov, provinces) == True and self_strength > (old_strength * 1.25):
	#				c_options.add(pl)
	#				p_options.add(prov)
	#			elif self_naval_projection_strength >= old_strength * 1.25:
	#				c_options.add(p1)
	#				p_options.add(prov)
	if len(c_options) !=0:
		print("There are some c options!")

		p_target = []
		c_target = []
		for r in priorities:
			print(r)
			for prov in p_options:
				print(prov.name, prov.resource)
				if prov.resource == r:
					for c in c_options:
						if prov.name in c.provinces.keys():
							print("Append: %s: %s" % (c.name, prov.name))
							p_target.append(prov)
							c_target.append(c)

							print("Combat against Unciv!")
							stop = input()
							combat_against_uncivilized(player, c_target[0], p_target[0])				
							player.diplo_action -= 1
							player.reputation -= 0.1
							return

def	decide_rival_target(player, players, market, provinces, relations):

	if len(player.rival_target) > 0 and (len(player.rival_target[0].provinces.keys()) == 0 \
		or player.rival_target[1].name not in player.rival_target[0].provinces.keys() ):
		player.rival_target = []
	if len(player.rival_target) > 0:
		return
	self_strength = player.calculate_base_attack_strength()
	self_naval_projection_strength = player.ai_naval_projection()

	if "mobile_warfare" in player.technologies and player.military["tank"] >= 1:
		option = []
		for o, other in players.items():
			if other.name == player.name:
				continue
			if other.type != "major":
				continue
			if len(other.provinces.keys()) < 1:
				continue
			if other in player.borders and self_strength > other.calculate_base_defense_strength() * 1.2:
				relata = frozenset([player.name, other.name])
				if relations[relata].relationship < 1.75:
					other_strength = calculate_base_defense_strength(other)
					pro_choices = list(other.provinces.values())
					prov = choice(pro_choices)
					player.rival_target = [other, prov]
					return
			else:
				p_navy_str = calculate_naval_strength(player)
				o_navy_str = calculate_naval_strength(other)
				o_def_str = calculate_base_defense_strength(other)
				if p_navy_str > o_navy_str * 1.25 and self_naval_projection_strength > o_def_str * 1.25:
					relata = frozenset([player.name, other.name])
					if relations[relata].relationship < 1.75:
						other_strength = calculate_base_defense_strength(other)
						pro_choices = list(other.provinces.values())
						prov = choice(pro_choices)
						player.rival_target = [other, prov]
					return

	need = set()
	for r, res in player.resources.items():
		if player.resource_base[r] < 1.0 and market.market[r] < 2:
			if r == "oil" and "oil_drilling" not in player.technologies:
				continue
			if r == "rubber" and "electricity" not in player.technologies:
				continue
			need.add(r)
	if len(need) == 0:
		return
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	#c_options = set()
	#p_options = set()
	for k, v in players.items():
		if v.name == player.name:
			continue
		relata = frozenset([player.name, v.name])
		#print(relata)
		other_strength = calculate_base_defense_strength(v)
		if v in player.borders and self_strength > (other_strength * 1.25)\
		or (self_naval_projection_strength > other_strength * 1.5 and transport_limit >= 4):
			for p, pr in v.provinces.items():
				if v.type == "major" and pr.culture == v.culture:
					continue
				if v.type == "major" and v.type != "colony" and player.check_for_ground_invasion(pr, provinces) == False:
					continue
				elif pr.resource in need and relations[relata].relationship < 1.5:
					player.rival_target = [v,  pr]
	if len(player.rival_target) < 1:
		for o, other in players.items():
			if other.name == player.name:
				continue
			relata = frozenset([player.name, other.name])
			if other in player.borders and self_strength > other.calculate_base_defense_strength() * 1.2:
				for p, pr in other.provinces.items():
					if other.type == "major" and pr.culture == other.culture:
						continue
					if other.type == "major" and other.type != "colony" and player.check_for_ground_invasion(pr, provinces) == False:
						continue
					elif relations[relata].relationship < 1.5:
						player.rival_target = [other,  pr]
			else:
				if transport_limit < 4:
					return
				relata = frozenset([player.name, other.name])
				p_navy_str = calculate_naval_strength(player)
				o_navy_str = calculate_naval_strength(other)
				o_def_str = calculate_base_defense_strength(other)
				if p_navy_str > o_navy_str * 1.25 and self_naval_projection_strength > o_def_str * 1.25:
					for p, pr in other.provinces.items():
						if other.type == "major" and pr.culture == other.culture:
							continue
						if other.type == "major" and pr.type != "colony" and player.check_for_ground_invasion(pr, provinces) == False:
							continue
						elif relations[relata].relationship < 1.5:
							player.rival_target = [other,  pr]

	return
					#p_options.add(pr)

def worsen_relations(player, players, relations):
	if player.rival_target == [] or player.diplo_action < 1.5:
		return
	target = player.rival_target[0]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > -2.5:
		player.diplo_action -=1
		relations[relata].relationship -= min(1, 10/(target.POP + 0.001))

def gain_cb(player, players, relations):
	if player.diplo_action < 1.2:
		return
	if player.rival_target == []:
		return
	target = player.rival_target[0]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > -2.5:
		return
	else:
		player.diplo_action -= 1
		player.CB.add(target)



def attack_target(player, players, relations, provinces):
	if len(player.rival_target) < 2:
		return
	if player.diplo_action < 1:
		return
	target = player.rival_target[0]
	print(player.rival_target[0])
	prov = player.rival_target[1]
	print("Target nation: %s" % (target.name))
	print("Target prov: %s" % (prov.name))
	if target.type == "old_empire" or target.type == "old_minor" or prov.type == "colony":
		if player.colonization < 1 + (player.num_colonies) * 2:
			return
	relata = frozenset([player.name, target.name])
	if target not in player.CB:
		return
	annex = player.rival_target[1]
	self_strength = player.calculate_base_attack_strength()
	other_strength = target.calculate_base_defense_strength()
	self_naval_projection_strength = player.ai_naval_projection()
	if target.type == "old_minor" or target.type == "old_empire" or target.type == "civ_minor":
		if target not in player.borders:
			print("Not border")
			if self_naval_projection_strength > other_strength * 1.2:
				amphib_prelude(player, target, annex, players)
				player.reputation -= 0.1
				player.rival_target = []
				if target in player.CB:
					player.CB.remove(target)
				player.diplo_action -= 1.0
				relations[relata].relationship += 1
			else:
				player.rival_target = []

		else:
			print("Border")
			if self_strength > other_strength * 1.2:
				combat(player, target, annex, players)
				player.reputation -= 0.1
				player.rival_target = []
				if target in player.CB:
					player.CB.remove(target)
				player.diplo_action -= 1.0
				relations[relata].relationship += 1

			else:
				player.rival_target = []

	#else:
		#if player.check_for_ground_invasion(annex, provinces): 
		#	self_strength = player.calculate_base_attack_strength()
		#	if self_strength > (other_strength * 1.25):
		#		combat(player, target, annex, players)
		#		player.diplo_action -= 1.0
		#		player.reputation -= 0.25
		#		player.rival_target = []
		#		if target in player.CB:
		#			player.CB.remove(target)
		#	else:
		#		player.rival_target = []

	else:
		sea = calculate_naval_strength(player)/(calculate_naval_strength(target) + 0.1)
		land = self_strength/(other_strength + 0.1)	
		if annex.colony and target in player.borders:
			if sea < 1.25 and land < 1.25:
				player.rival_target = []
				return
			else:
				player.diplo_action -= 1.0
				if land < sea:
					combat(player, target, prov, players)
					player.reputation -= 0.1
					player.rival_target = []
					if target in player.CB:
						player.CB.remove(target)
					relations[relata].relationship += 1

					return
				elif self_naval_projection_strength > other_strength * 1.25:
					victor = naval_battle(player, target, annex)
					if victor == player.name:
						gain_province(player, target, annex, players)
					player.reputation -= 0.1
					player.rival_target = []
					relations[relata].relationship += 1

					if target in player.CB:
						player.CB.remove(target)
					return
		
		elif annex.colony:
			if sea > 1.2 and self_naval_projection_strength > other_strength * 1.25:
				victor = naval_battle(player, target, annex)
				if victor == player.name:
					gain_province(p1, p2, annex, players)
				player.reputation -= 0.1
				player.rival_target = []
				relations[relata].relationship += 1
				if target in player.CB:
					player.CB.remove(target)
				player.diplo_action -= 1.0


		elif target in player.borders and self_strength > other_strength * 1.2:
			combat(player, target, prov, players)
			player.rival_target = []
			relations[relata].relationship += 1
			if target in player.CB:
				player.CB.remove(target)
			player.diplo_action -= 1.0
			player.reputation -= 0.25

		else:
			if calculate_naval_strength(player) > calculate_naval_strength(target) * 1.2 and self_naval_projection_strength > other_strength * 1.2:
				amphib_prelude(player, target, annex, players)
				player.reputation -= 0.25
				player.rival_target = []
				if target in player.CB:
					player.CB.remove(target)
				player.diplo_action -= 1.0
				relations[relata].relationship += 1



def ai_decide_ally_target(player, players, provinces):
	if len(player.allied_target) > 2:
		return
	options = set()
	self_strength = player.calculate_base_defense_strength()
	for k, v in players.items():
		if v in player.borders:
			if self_strength < v.calculate_base_attack_strength():
				options.add(v)
		else:
			navinvade = player.ai_naval_projection()
			if self_strength < navinvade:
				options.add(v)
	if len(options) > 0:
		choice = sample(options, 1)
		player.allied_target.append(choice)
	return

def ai_improve_relations(players, relations):
	if len(player.allied_target) < 1 or player.diplo_action < 1.5:
		return
	choice - sample(player.allied_target, 1)
	relata = frozenset([player.name, choice.name])
	if relations[relata].relationship < 2.5:
		player.diplo_action -=1
		relations[relata].relationship += min(1, 5/(other.POP + 0.001))





def ai_destablize(player, players):
	if player.diplo_action < 2:
		return
	priorities = sorted(player.resource_priority, key=player.resource_priority.get, reverse = True)
	empires = []
	for k, v in players.items():
		if v.type == "old_empire":
			empires.append(v) 
	target = " "
	for r in priorities:
		for emp in empires:
			for p, prov in emp.provinces.items():
				if r == prov.resource and emp.stability > -2.8:
					target = emp
	if target == " ":
		return
	amount = 0
	if target.type == "old_empire" or target.type == "old_minor":
		r = uniform(0,1)
		amount = r/2
	else:
		r = uniform(0,1)
		r/4
		target.stability -= amount
		if target.stability < -3.0:
				target.stability = -3.0
	player.diplo_action -=1
	player.reputation -= 0.1






	
















