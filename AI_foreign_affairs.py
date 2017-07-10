#AI Foreign Affairs

from AI import*
from combat import*
from random import random
from player_class import*

from queue import queue


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

def ai_decide_unciv_colonial_war(player, uncivilized_minors, rough_uncivilized_minors):
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
	for k, unciv in rough_uncivilized_minors.items():
		if len(unciv.provinces) >= 1:
			for prov in unciv.provinces.values():
				if check_for_ground_invasion(player, prov) == True and self_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
				elif self_naval_projection_strength >= 4:
					c_options.add(unciv)
					p_options.add(prov)
					
	if "medicine" in player.technologies and "breach_loaded_arms" in player.technologies:
		for k, unciv in rough_uncivilized_minors.items():
			if len(unciv.provinces) >= 1:
				for prov in unciv.provinces.values():
					if check_for_ground_invasion(player, prov) == True and self_strength >= 5:
						c_options.add(unciv)
						p_options.add(prov)
					elif self_naval_projection_strength >= 4:
						c_options.add(unciv)
						p_options.add(prov)
	for p, pl in players.items():
		if pl.type == "old_minor" and len(pl.provinces) >= 1:
			old_strength = calculate_base_defense_strength(pl)
			for prov in pl.provinces.values():
				if check_for_ground_invasion(player, prov) == True and self_strength > (old_strength * 1.25):
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

def	decide_on_resource_motivated_invasion(player, market):
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
	c_options = set()
	p_options = set()
	for k, v in players.items():
		other_strength = calculate_base_defense_strength(v)
		if check_for_ground_invasion(player, prov) == True and self_strength > (other_strength * 1.25)\
		or self_naval_projection_strength > other_strength * 1.25:
			for p, pr in v.provinces:
				if pr.resource in need:
					c_options.add(v)
					p_options.add(pr)
	if len(c_options) < 1:
		return
	if 

		forces = ai_transport_units(player)					
		amph_combat(player, target, forces)
		player.diplo_action -= 1.0
		player.reputation -= 0.1
		return
		
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


def b_borders_a(p1, p2):
	bBa = set()
	for v1 in p1.provinces.values():
		for v2 in p2.provinces.values():
			if abs(v1.x - v2.x) <= 1 and abs(v1.y - v2.y) <= 1:
				bBa.add(v2)
	return bBa


	
def core_provinces(player):
	core = []
	consider = Queue(100)
	first = player.provinces[player.capital]
	consider.put(first):
	while len.consider >= 1:
		thing = get(consider):
		for p in player.provinces.values():
			if abs(thing.x - p.x) <= 1 and abs(thing.y - p.y) <= 1:
				if p not in core:
					consider.put(p)
			core.append(thing)
	return core

def check_for_ground_invasion(p1, prov):
	core = core_provinces(p1)
	for c in core: 
		if abs(core.x - prov.x) <= 1 and abs(core.y - prov.y) <= 1:
			return True
	return False
















