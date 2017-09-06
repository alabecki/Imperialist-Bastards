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
	if player.colonization < 1 + player.num_colonies * 1.5 or player.diplo_action < 1 or transport_limit < 4 or \
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

def decide_target(player, players, market, provinces, relations):
	if len(player.rival_target) > 0 and player.rival_target[0].name not in players.keys():
		player.rival_target = []
	if len(player.rival_target) > 0 and (len(player.rival_target[0].provinces.keys()) == 0 \
		or player.rival_target[1].name not in player.rival_target[0].provinces.keys() ):
		player.rival_target = []
	if len(player.rival_target) > 0 and player.rival_target[0].defeated == True:
		player.rival_target = []
	if len(player.rival_target) > 0:
		return
	self_strength = player.calculate_base_attack_strength()
	self_naval_projection_strength = player.ai_naval_projection()
	self_navy_str = calculate_naval_strength(player)
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 

	options = set()
	for obj in player.objectives:
		_object = provinces[obj]
		owner = _object.owner
		if owner == player.name:
			continue
		owner = players[owner]
		if owner.type == "major":
			if player.military["tank"] == 0:
				_object = provinces[obj]
				if owner.culture == _object.culture:
					continue
				elif owner in player.borders and self_strength > owner.calculate_base_defense_strength() * 1.22:
					print("obj 103: %s" % (obj))
					options.add(obj)
				else:
					if transport_limit < 4 or player.government == "despotism":
						return
					owner_navy_str = calculate_naval_strength(owner)
					if self_navy_str > owner_navy_str * 1.25 and self_naval_projection_strength > owner.calculate_base_defense_strength() * 1.22:
						print("obj 110: %s" % (obj))
						options.add(obj)
					else:
						continue

			elif owner in player.borders and self_strength > owner.calculate_base_defense_strength() * 1.22:
				print("obj 116: %s" % (obj))
				options.add(obj)
				continue
			else: 
				if transport_limit < 4 or player.government == "despotism":
					return
				o_navy_str = calculate_naval_strength(owner)
				if self_navy_str > o_navy_str * 1.25 and self_naval_projection_strength > owner.calculate_base_defense_strength() * 1.22:
					print("obj 123: %s" % (obj))
					options.add(obj)
				else:
					continue
		
		elif owner in player.borders and self_strength > owner.calculate_base_defense_strength() * 1.22:
			print("obj 129: %s" % (obj))
			options.add(obj)
		else:
			if transport_limit < 4 or player.government == "despotism":
					return
			o_navy_str = calculate_naval_strength(owner)
			if self_navy_str > o_navy_str * 1.25 and self_naval_projection_strength > owner.calculate_base_defense_strength() * 1.22:
				print("obj 136: %s" % (obj))
				options.add(obj)
			else:
				continue
	if len(options) == 0:
		return
	options_copy = deepcopy(options)
	for opt in options_copy:
		_opt = provinces[opt]
		for pl, play in players.items():
			relata = frozenset([_opt.owner, play.name])
			if len(relata) == 1:
				continue
			if relations[relata].relationship >= 2.6:
				friend = players[play.name]
				friend_power = friend.calculate_base_attack_strength()
				if player in friend.borders and self_strength < friend_power * 1.22:
					roll = random()
					if roll <= 0.62:
						options.discard(opt)
				else:
					friend_navy_str = calculate_naval_strength(friend)
					if friend_navy_str > self_navy_str * 1.22:
						if _opt.colony == True:
							roll = random()
							if roll <= 0.62:
								options.discard(opt)

						elif friend.ai_naval_projection() > player.calculate_base_defense_strength() * 1.22:
							roll = random()
							if roll <= 0.75:
								options.discard(opt)
	if len(options) == 0:
			return

	selection = ""
	for opt in options:
		_opt = provinces[opt]
		if _opt.culture == player.culture:
			selection = opt
			selection = provinces[selection]
			rival = selection.owner
			rival = players[rival]
			player.rival_target = [rival, selection]
			return

	res_priority = sorted(player.resource_priority, key= player.resource_priority.get, reverse = True)
	for res in res_priority:
		for opt in options:
			_opt = provinces[opt]
			if res == _opt.resource:
				owner = _opt.owner
				_owner = players[owner]
				player.rival_target = [_owner, _opt]
				return

				
					



def	decide_rival_target(player, players, market, provinces, relations):
	if len(player.rival_target) > 0 and player.rival_target[0].name not in players.keys():
		player.rival_target = []
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

	
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	#c_options = set()
	#p_options = set()
	res_priority = sorted(player.resource_priority, key= player.resource_priority.get)
	for res in res_priority:
		for k, v in players.items():
			for p, pr in v.provinces.items():
				if res ==  pr.resource:
						other_strength = v.calculate_base_defense_strength()
						relata = frozenset([player.name, v.name])
						if len(relata) == 1:
							continue
						if v in player.borders and self_strength > (other_strength * 1.25)\
						or (self_naval_projection_strength > other_strength * 1.5 and transport_limit >= 4):
							if v.type == "major" and pr.culture == v.culture:
								continue
							if v.type == "major" and v.type != "colony" and player.check_for_ground_invasion(pr, provinces) == False:
								continue
							elif relations[relata].relationship < 1.5:
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
				if transport_limit < 4 or player.government == "despotism":
					return
				if other.check_for_sea_invasion() == False:
					continue
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
	if target.type == "old_minor" or target in player.CB:
		return
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
	prov = player.rival_target[1]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > -2.5 and target.type != "old_minor":
		return
	if target in player.CB:
		return
	else:
		player.diplo_action -= 1
		new = CB(player.name, target.name, "annex", prov.name, 3)
		player.CB.add(new)
		print("Gain a CB against %s !!!!!!!!!!!!!!!!!!!!!!!" % (target.name))


def attack_target(player, players, relations, provinces, market):

	ammo_needed	= player.calculate_army_ammo_needed()

	if player.goods["cannons"] < ammo_needed:
		return

	oil_needed = player.calculate_army_oil_needed()

	if player.resources["oil"] < oil_needed:
		return

	if len(player.CB) <= 0:
		return
	check = False
	cb = " "
	count = 0
	while check == False and count < 16:
		cb = sample(player.CB, 1)
		cb = cb[0]	
		prov = provinces[cb.province]

		if cb.opponent != prov.owner:
			player.CB.discard(cb)
			del cb
			if len(player.CB) <= 0:
				return
			else:
				continue
		if cb.opponent not in players.keys():
			player.CB.discard(cb)
			del cb
			if len(player.CB) <= 0:
				return
			else:
				continue
		target = cb.opponent
		target = players[target]
		if target.just_attacked > 0 or (cb.action == "annex" and player.reputation <= 0.2):
			count += 1
			continue
		else:
			check = True

	target = cb.opponent
	target = players[target]

	if target.just_attacked > 0 or (cb.action == "annex" and player.reputation <= 0.2):
		return
	#print(player.rival_target[0])
	#prov = player.rival_target[1]
	#print("Target nation: %s" % (target.name))
	#print("Target prov: %s" % (prov.name))
	if target.type == "old_empire" or target.type == "old_minor" or prov.type == "colony":
		if player.colonization < 1 + player.num_colonies:
			return

	if (target.type == "major" or target.type == "minor") and cb.action == "annex":
		if player.reputation < 0.5:
			return
 
	self_strength = player.calculate_base_attack_strength()
	other_strength = target.calculate_base_defense_strength()
	self_naval_projection_strength = player.ai_naval_projection()
	if target.type == "old_minor" or target.type == "old_empire" or target.type == "civ_minor":
		if target not in player.borders:
			print("Not border")
			if self_naval_projection_strength > other_strength * 1.2:
				amphib_prelude(player, target, prov, players, market, relations)
				#war_after_math(player,  target, players, relations)
			else:
				player.rival_target = []
		else:
			print("Border")
			if self_strength > other_strength * 1.2:
				combat(player, target, prov, players, market, relations)
				#war_after_math(player, target, players, relations)
			else:
				player.rival_target = []

	else:
		player_naval_strength = calculate_naval_strength(player)
		target_naval_strength = calculate_naval_strength(target)
		cores = target.core_provinces()
		if prov.colony and target in player.borders:
			if player_naval_strength > target_naval_strength * 1.25:
				victor = naval_battle(player, target, market, relations, prov)
				if victor == player.name:
					gain_province(player, target, prov, players, market, relations)
				#	war_after_math(player,  target, players, relations)
					return
			if self_strength > other_strength * 1.22:
				combat(player, target, prov, players, market, relations)
					#	war_after_math(player,  target, players, relations)
				return
			else:
				return
		elif prov not in cores and prov.ocean == True:
			if player_naval_strength > target_naval_strength * 1.25:
				victor = naval_battle(player, target, market, relations, prov)
				if victor == player.name:
					gain_province(player, target, prov, players, market, relations)
				else:
					player.war_after_math(target, players, relations, prov)


		elif target in player.borders and self_strength > other_strength * 1.2:
			combat(player, target, prov, players, market, relations)
			#war_after_math(player, target, players, relations)
		else:
			if calculate_naval_strength(player) > calculate_naval_strength(target) * 1.2 and self_naval_projection_strength > other_strength * 1.2:
				amphib_prelude(player, target, prov, players, market, relations)
				#war_after_math(player, target, players, relations)

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
		player.reputation += 0.02
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
		pay = max(2, other.resources["gold"]/10)
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
			relata = frozenset([player.name, v.name])
			if len(relata) == 2:
				if relations[relata].relationship < 1:
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
		amount = r/4
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
				other.embargo.add(player)
				relata = frozenset([player.name, other.name])
				relations[relata].relationship -= 0.25
				print("Places embargo on %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (other.name))

def ai_lift_embargo(player, players, relations):
	p_relations = [v for v in relations.values() if player.name in v.relata]
	for o, other in players.items():
		if player in other.embargo:
			relata = frozenset([player.name, other.name])
			if relations[relata].relationship > -1.75:
				other.embargo.discard(player)
				relata = frozenset([player.name, other.name])
				relations[relata].relationship += 0.1
				print("Lifts embargo on %s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % (other.name))








	
















