#AI Foreign Affairs

from AI import*
from combat import*
from random import random
from player_class import*

import queue as queue


def calculate_base_attack_strength(p1):
	strength = 0.0
	strength += p1.military["infantry"] * p1.infantry["attack"]
	strength += p1.military["cavalry"] * p1.cavalry["attack"]
	strength += p1.military["artillery"] * p1.artillery["attack"]
	strength += p1.military["tank"] * p1.tank["attack"]
	strength += p1.military["fighter"] * p1.fighter["attack"]
	return strength


def calculate_base_defense_strength(p2):
	strength = 0.0
	strength += p2.military["irregulars"] * p2.irregulars["defend"]
	strength += p2.military["infantry"] * p2.infantry["defend"]
	strength += p2.military["cavalry"] * p2.cavalry["defend"]
	strength += p2.military["artillery"] * p2.artillery["defend"]
	strength += p2.military["tank"] * p2.tank["defend"]
	strength += p2.military["fighter"] * p2.fighter["defend"]
	strength = strength * p2.fortification
	return strength

def ai_decide_unciv_colonial_war(player, uncivilized_minors, rough_uncivilized_minors, provinces):
	if player.type == "old_empire" or player.type =="old_minor":
		return
	if player.colonization < 1 + (player.num_colonies * 2) or player.diplo_action < 1 or transport_limit < 4:
		return

	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	priorities = sorted(player.resource_priority, key= player.resource_priority.get, reverse = True) 
	self_strength = calculate_base_attack_strength(player)
	self_naval_projection_strength = ai_naval_projection(player)
	if self_strength < 3.5:
		return

	c_options = set()
	p_options = set()
	for k, unciv in uncivilized_minors.items():
		if unciv.harsh == True and ("medicine" in player.technologies or "breach_loaded_arms" in player.technologies):
			continue
		if len(unciv.provinces) >= 1:
			for prov in unciv.provinces.values():
				if player.check_for_ground_invasion(prov, provinces) == True and self_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
				elif self_naval_projection_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
					
	for p, pl in players.items():
		if pl.type == "old_minor" and len(pl.provinces) >= 1:
			old_strength = calculate_base_defense_strength(pl)
			for prov in pl.provinces.values():
				if player.check_for_ground_invasion(prov, provinces) == True and self_strength > (old_strength * 1.25):
					c_options.add(pl)
					p_options.add(prov)
				elif self_naval_projection_strength >= old_strength * 1.25:
					c_options.add(p1)
					p_options.add(prov)
	if len(c_options) !=0:
		p_target = ""
		c_target = ""
		for r in priorities:
			for prov in p_options:
				if prov.resource == r:
					for c in c_options:
						if prov in c.provinces:
							p_target = prov
							c_target = c


		combat_against_uncivilized(player, c_target, p_target)				
		player.diplo_action -= 1
		player.reputation -= 0.1
		return

def	decide_on_next_target(player, players, market, provinces, relations):
	if len(player.target) > 0:
		return
	need = set()
	for r, res in self.resources.items():
		if self.resource_base[r] < 1.0 and market.market[r] < 2:
			if r == "oil" and "oil_drilling" not in player.technologies:
				continue
			if r == "rubber" and "electricity" not in player.technologies:
				continue
			need.add(r)
	if len(need) == 0:
		return
	self_strength = calculate_base_attack_strength(player)
	self_naval_projection_strength = ai_naval_projection(player)
	#c_options = set()
	#p_options = set()
	for k, v in players.items():
		other_strength = calculate_base_defense_strength(v)
		if player.check_for_ground_invasion(prov, provinces) == True and self_strength > (other_strength * 1.25)\
		or self_naval_projection_strength > other_strength * 1.25:
			for p, pr in v.provinces:
				if v.type == "major" and pr.culture == v.culture:
					continue
				if v.type == "major" and v.type != colony and player.check_for_ground_invasion(pr, provinces) == False:
					continue
				elif pr.resource in need and relations[player.name, v.name].relationship < 1.25:
					player.rival_target = [v,  pr]
					return
					#p_options.add(pr)

def worsen_relations(player, players, relations):
	if player.rival_target == []:
		return
	target = player.rival_target[0]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > 2.5:
		player.diplo_action -=1
		relations[relata].relationship -= min(1, 10/(other.POP + 0.001))

def attack_target(player, players, relations):
	if player.rival_target == []:
		return
	target = player.rival_target[0]
	relata = frozenset([player.name, target.name])
	if relations[relata].relationship > -2.5:
		return
	annex = player.rival_target[1]
	self_strength = calculate_base_attack_strength(player)
	other_strength = calculate_base_defense_strength(target)
	self_naval_projection_strength = ai_naval_projection(player)
	if target.type == "old_minor" or target.type == "old_empire":
		land = player.check_for_border(target)
		if land == False:
			amphib_prelude(player, target, annex)
			player.reputation -= 0.1
		else:
			combat(player, other, annex)
			player.reputation -= 0.1
	else:
		if player.check_for_ground_invasion(annex, provinces): 
			self_strength = calculate_base_attack_strength(player)
			if self_strength > (other_strength * 1.2):
				combat(player, target, annex)
				player.diplo_action -= 1.0
				player.reputation -= 0.25
		else:
			sea = calculate_naval_strength(player)/calculate_naval_strength(target)
			land = self_strength/other_strength	
			if annex.colony and player.check_for_border(other):
				if sea < 1.18 and land < 1.18:
					return
				else:
					if land < sea:
						combat(player, target, prov)
					else:
						naval_battle(player, target, prov)
					player.reputation -= 0.2
			else:
				if sea > 1.2:
					naval_battle(player, target, prov)
					player.reputation -= 0.2


		
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
			tries += 1
	return forces


def ai_naval_projection(player):
	forces = ai_transport_units(player)
	strength = 0
	for k, v in forces.items():
		att = 0
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


def ai_destablize_empires(player, players):
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
					target = emp.name
	if target == " ":
		return
	amount = random.random()/1.5
	players[target].stability -= amount
	if players[target].stability < -3.0:
		players[target].stability = -3.0
	player.diplo_action -=1
	player.reputation -= 0.1




	
















