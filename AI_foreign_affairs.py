#AI Foreign Affairs

from AI import*
from combat import*

from player_class import*
from globe import*

import queue as queue
from random import*



def ai_decide_unciv_colonial_war(player, players, uncivilized_minors, provinces):
	if player.rival_target != []:
		return
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 

	if player.type == "old_empire" or player.type =="old_minor":
		return
	if player.colonization < 1 + player.num_colonies or player.diplo_action < 1 or transport_limit < 4 or \
	player.midPOP["bureaucrats"]["number"] < 0.4:
		return
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	priorities = sorted(player.resource_priority, key= player.resource_priority.get, reverse = True) 
	#print("ColPriorities:")
	#for r in priorities:
	#	print(r)
	self_strength = player.calculate_base_attack_strength()
	self_naval_projection_strength = player.ai_naval_projection()
	if self_strength < 3.5:
		return

	c_options = set()
	p_options = set()
	for k, unciv in uncivilized_minors.items():
		if unciv.harsh == True and ("medicine" not in player.technologies or "breach_loaded_arms" not in player.technologies) \
		or player.midPOP["bureaucrats"]["number"] < 0.6:
			continue
		if len(unciv.provinces) >= 1:
			#print(unciv.name)
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
		#print("There are some c options!")

		p_target = []
		c_target = []
		for r in priorities:
			#print(r)
			for prov in p_options:
				#print(prov.name, prov.resource)
				if prov.resource == r:
					for c in c_options:
						if prov.name in c.provinces.keys():
							#print("Append: %s: %s" % (c.name, prov.name))
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
	if len(player.rival_target) > 0 and player.rival_target[0].defeated == True:
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
			if other.type != "major" or other.defeated == True:
				continue
			if len(other.provinces.keys()) < 1:
				continue
			if other in player.borders and self_strength > other.calculate_base_defense_strength() * 1.2:
				relata = frozenset([player.name, other.name])
				if relations[relata].relationship < 1.75:
					other_strength = other.calculate_base_defense_strength()
					pro_choices = list(other.provinces.values())
					prov = choice(pro_choices)
					player.rival_target = [other, prov]
					return
			else:
				p_navy_str = calculate_naval_strength(player)
				o_navy_str = calculate_naval_strength(other)
				o_def_str = other.calculate_base_defense_strength()
				if p_navy_str > o_navy_str * 1.25 and self_naval_projection_strength > o_def_str * 1.25:
					relata = frozenset([player.name, other.name])
					if relations[relata].relationship < 1.75:
						other_strength = other.calculate_base_defense_strength()
						pro_choices = list(other.provinces.values())
						prov = choice(pro_choices)
						player.rival_target = [other, prov]
					return

	need = set()
	for r, res in player.resources.items():
		if player.resource_base[r] < 1.0 and player.supply[r] < 2:
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
		other_strength = v.calculate_base_defense_strength()
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
				o_def_str = other.calculate_base_defense_strength()
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
	if player.rival_target == [] or player.diplo_action < 1.2:
		return
	target = player.rival_target[0]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > -2.5:
		player.diplo_action -=1
		relations[relata].relationship -= min(1, 10/(target.POP + 0.001))
		print("Worsens relations with %s" % (target.name))

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
		print("Gain a CB against %s !!!!!!!!!!!!!!!!!!!!!!!" % (target.name))



def attack_target(player, players, relations, provinces):
	if len(player.rival_target) < 2 or player.diplo_action < 1.0:
		return
	target = player.rival_target[0]
	#print(player.rival_target[0])
	prov = player.rival_target[1]
	#print("Target nation: %s" % (target.name))
	#print("Target prov: %s" % (prov.name))
	if target.type == "old_empire" or target.type == "old_minor" or prov.type == "colony":
		if player.colonization < 1 + (player.num_colonies):
			return
	relata = frozenset([player.name, target.name])
	if target not in player.CB and (target.type == "major" or target.type == "minor"):
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
				war_after_math(player,  target, players, relations)
			else:
				player.rival_target = []

		else:
			print("Border")
			if self_strength > other_strength * 1.2:
				combat(player, target, annex, players)
				war_after_math(player,  target, players, relations)
			else:
				player.rival_target = []

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
					war_after_math(player,  target, players, relations)
					return
				elif self_naval_projection_strength > other_strength * 1.25:
					victor = naval_battle(player, target, players, annex)
					if victor == player.name:
						gain_province(player, target, annex, players)
						war_after_math(player,  target, players, relations)
					return
		
		elif annex.colony:
			if sea > 1.2 and self_naval_projection_strength > other_strength * 1.25:
				victor = naval_battle(player, target, players, annex)
				if victor == player.name:
					gain_province(player, target, annex, players)
				war_after_math(player,  target, players, relations)
				player.reputation -= 0.1



		elif target in player.borders and self_strength > other_strength * 1.2:
			combat(player, target, prov, players)
			war_after_math(player, target, players, relations)
		else:
			if calculate_naval_strength(player) > calculate_naval_strength(target) * 1.2 and self_naval_projection_strength > other_strength * 1.2:
				amphib_prelude(player, target, annex, players)
				war_after_math(player, target, players, relations)


def war_after_math(player, target, players, relations):
	relata = frozenset([player.name, target.name])
	player.rival_target = []
	relations[relata].relationship += 1
	if target in player.CB:
		player.CB.remove(target)
	player.diplo_action -= 1.0
	player.reputation -= 0.1
	for p, pl in players.items():
		if len(set([player.name, p])) == 1 or len(set([target.name, p])) == 1:
			continue
		if relations[frozenset([player.name, p])].relationship < -1.5:
			relations[frozenset([player.name, p])].relationship -= 0.2
		if relations[frozenset([target.name, p])].relationship >= 0 and relations[frozenset([player.name, p])].relationship < 2:
			relations[frozenset([player.name, p])].relationship -= 0.1
		if relations[frozenset([target.name, p])].relationship >= 1:
			relations[frozenset([player.name, p])].relationship -= 0.2 
		if relations[frozenset([target.name, p])].relationship >= 2:
			relations[frozenset([player.name, p])].relationship -= 0.2 
		if pl.type == "AI":
			if pl.rival_target != []:
				if target == pl.rival_target[0]: 
					relations[frozenset([player.name, p])].relationship -= 0.2
			if target in pl.allied_target:
				relations[frozenset([player.name, p])].relationship -= 0.2


	#for r in relations:
	#	re = list(r)
	#	if target.name in re and relations[r].relationship >= 1:
	#		if re[0] == target.name:
	#			o = re[1]
	#		else:
	#			o = re[0]
	#		hurt = frozenset([player.name, o])
	#		relations[hurn].relationship -= 0.2
	#	if target.name in re and relations[r].relationship >= 2:
	#		if re[0] == target.name:
	#			o = re[1]
	#		else:
	#			o = re[0]
	#		hurt = frozenset(player.name, o)
	#		relations[hurn].relationship -= 0.2



def ai_decide_ally_target(player, players, provinces):
	if len(player.allied_target) > 2:
		return
	options = []
	self_strength = player.calculate_base_defense_strength()
	for k, v in players.items():
		if v.name == player.name:
			continue
		if v.type != "major":
			continue
		if v in player.borders:
			if self_strength < v.calculate_base_attack_strength():
				options.append(v)
				#print(v.name)
		else:
			navinvade = player.ai_naval_projection()
			if self_strength < navinvade:
				options.append(v)
				#print(v.name)
	if len(options) > 0:
		pick = choice(options)
		player.allied_target.append(pick)
		print("Adds %s as Ally Target !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (pick.name))

	return

def ai_improve_relations(player, players, relations):
	if len(player.allied_target) < 1 or player.diplo_action < 1.5:
		return
	pick = sample(player.allied_target, 1)
	relata = frozenset([player.name, pick[0].name])
	if relations[relata].relationship < 2.5:
		player.diplo_action -=1
		relations[relata].relationship += min(1, 5/(pick[0].POP + 0.001))
		player.reputation += 0.025
		print("Improves relations with %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (pick[0].name))

def ai_bribe(player, players, relations):
	if player.type != "major" and player.type != "old_empire":
		return
	if player.resources["gold"] < 12:
		return
	tries = 0
	p_relations = [v for v in relations.values() if player.name in v.relata]
	p_relations.sort(key=lambda x: x.relationship, reverse=True)
	for pr in p_relations:
		if relations[pr.relata].relationship > 2.5:
			continue
		if relations[pr.relata].relationship < -1.0:
			continue
		re = list(pr.relata)
		if re[0] == player.name:
			o = re[1]
		else:
			o = re[0]
		other = players[o]
		pay = other.resources["gold"]/10
		if pay > player.resources["gold"]/5:
			continue
		relata = frozenset([player.name, other.name])
		relations[relata].relationship += 0.5
		player.resources["gold"] -= pay
		print("Bribes %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (other.name))
		return
	while tries < 12:
		tries += 1
		pick = choice(list(players.values()))
		if pick.name == player.name:
			continue
		relata = frozenset([player.name, pick.name])

		pay = pick.resources["gold"]/10
		if pay > player.resources["gold"]/4:
			continue
		relations[relata].relationship += 0.5
		player.resources["gold"] -= pay
		print("Bribes %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (pick.name))
		return



def ai_destablize(player, players, relations):
	if player.diplo_action < 2:
		return
	priorities = sorted(player.resource_priority, key=player.resource_priority.get, reverse = True)
	empires = []
	if player.rival_target != []:
		tar = player.rival_target[0]
		if tar.stability > -2.0:
			empires.append(tar)
	for k, v in players.items():
		if v.type == "old_empire" and v.stability > -2.5:
			empires.append(v) 
	target = " "
	for r in priorities:
		for emp in empires:
			for p, prov in emp.provinces.items():
				if r == prov.resource and emp.stability > -2.7 and p != player.name:
					target = emp
	if target == " " or target.name == player.name:
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
	relata = frozenset([player.name, target.name])
	relations[relata].relationship -= 0.2
	print("Destablizes %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (target.name))


def ai_embargo(player, players, relations):
	if player.type != "major" and player.type != "old_empire":
		return
	p_relations = [v for v in relations.values() if player.name in v.relata]
	for pr in p_relations:
		if pr.relationship < -2.35:
			temp = list(pr.relata)
			if temp[0] == player.name:
				o = temp[1]
			else:
				o = temp[0]
			other = players[o]
			if player not in other.embargo:
				other.embargo.append(player)
				relata = frozenset([player.name, other.name])
				relations[relata].relationship -= 0.25
				print("Places embargo on %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (other.name))

def ai_lift_embargo(player, players, relations):
	p_relations = [v for v in relations.values() if player.name in v.relata]
	for o, other in players.items():
		if player in other.embargo:
			relata = frozenset([player.name, other.name])
			if relations[relata].relationship > -1.75:
				other.embargo.remove(player)
				relata = frozenset([player.name, other.name])
				relations[relata].relationship += 0.1
				print("Lifts embargo on %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (other.name))








	
















