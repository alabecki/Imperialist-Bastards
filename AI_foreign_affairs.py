#AI Foreign Affairs

from AI import*
from combat import*
from random import random
from player_class import*


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

def ai_decide_colonial_war(player, players, uncivilized_minors):
	if player.type == "old_empire" or player.type =="old_minor":
		return
	transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
	priorities = sorted(player.resource_priority, key= player.resource_priority.get, reverse = True) 
	if player.colonization < (1 + player.num_colonies) or player.diplo_action < 1 or transport_limit < 4:
		return
	self_strength = calculate_base_attack_strength(player)
	self_naval_projection_strength = ai_naval_projection(player)
	if self_strength < 3.5:
		return
	count = 0
	for k, unciv in uncivilized_minors.items():
		if len(unciv.provinces) >= 1:
			count += 1
	if count != 0:
		target = " "
		for r in priorities:
			for u, unciv in uncivilized_minors.items():
				for p, prov in unciv.provinces.items():
					if r == prov.resource:
						target = unciv
		combat_against_uncivilized(player, target)				
		player.diplo_action -= 1
		player.reputation -= 0.1
		return
	minors = dict()
	for p, pl in players.items():
		if pl.type == "old_minor" and len(pl.provinces) >= 1:
			minors[p] = pl
	if len(minors) >= 1 and transport_limit >= 6 and self_naval_projection_strength >= 6:
		for r in priorities:
			for u, minor in minors.items():
				for p, prov in minor.provinces.items():
					if r == prov.resource:
						target = minor
		forces = ai_transport_units(player)					
		amph_combat(player, target, forces)
		player.diplo_action -= 1.0
		player.reputation -= 0.1
		return
	if transport_limit >= 8:
		empires = []
		for k, v in players.items():
			if v.type == "old_empire" and len(v.provinces) >= 1:
				empires.append(v)
		options = []
		for e in empires: 
			defence = calculate_base_defense_strength(e)
			if self_naval_projection_strength * 0.80 > defence:
				options.append(e)
		if len(options) < 1:
			return
		else:
			target = " "
			for r in priorities:
				for opt in options:
					for p, prov in opt.provinces.items():
						if r == prov.resource:
							target = opt
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
	
	






