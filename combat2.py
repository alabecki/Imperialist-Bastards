
from player_class import Player
from technologies import*
from human import Human
from AI import AI
from minor_classes import*
#from AI_foreign_affairs import*
from random import*
from pprint import pprint
from copy import deepcopy

def delete_nation(attacker, defender, players, market, relations):
	attacker = players[attacker]
	defender = players[defender]
	print("%s no longer exists as a nation!" % (defender.name))
	market.report.append("%s no longer exists as a nation!" % (defender.name))
	for k, v in defender.resources.items():
		attacker.resources[k] += v
	for k, v in defender.goods.items():
		attacker.goods[k] += v
	for k, v in market.market.items():
		for i in v:
			if i.owner == defender.name:
				if k in attacker.resources.keys():
					attacker.resources[k] += 1
				if k in attacker.goods.keys():
					attacker.goods[k] +=1
				market.market[k].remove(i)
			#	print("removed %s %s"% (i.owner, i.kind))
				del i
	attacker.POP += 1
	attacker.numLowerPOP += 1
	attacker.freePOP += 1
	relkeys = list(relations.keys())
	for r in relkeys:
		if defender.name in relations[r].relata:
			del relations[r]
	for pl in players.values():
		if type(pl) == AI:
			if defender.name in pl.sphere_targets:
				pl.sphere_targets.remove(defender.name)
			if defender.name in pl.allied_target:
				pl.allied_targets.remove(defender.name)
			if pl.rival_target != []:
				if defender.name == pl.rival_target[0]:
					pl.rival_target = []
		if defender.name in pl.objectives:
				pl.objectives.remove(defender.name)
		if defender.name in pl.embargo:
			pl.embargo.remove(defender.name)


def war_after_math(player, target, players, relations, prov, provinces, market):
	print("War Aftermath")
	prov = provinces[prov]
	player = players[player]
	target = players[target]
	if player.culture == prov.culture:
		player.reputation += 0.15
		player.stability += 0.2
	#if target in self.CB:
	#	self.CB.remove(target)
	if target.type == "old_minor":
		player.reputation -= 0.1

		player.stability += 0.1
	if target.type == "old_empire":
		player.reputation -= 0.15
		player.stability += 0.1
	if (target.type == "minor" or target.type == "major") and player.military["tank"] == 0:
		player.reputation -= 0.3
		for pl, play in players.items():
			if play.type == "major" and player.name != pl:
				relations[frozenset([player.name, pl])].relationship -= 0.2

	for p, pl in players.items():
		if len(set([player.name, p])) == 1 or len(set([target.name, p])) == 1:
			continue
		if relations[frozenset([player.name, p])].relationship < -1.5:
			relations[frozenset([player.name, p])].relationship -= 0.1
		if relations[frozenset([target.name, p])].relationship >= 0 and relations[frozenset([player.name, p])].relationship < 1.5:
			relations[frozenset([player.name, p])].relationship -= 0.1
		if relations[frozenset([target.name, p])].relationship >= 1:
			relations[frozenset([player.name, p])].relationship -= 0.15 
		if relations[frozenset([target.name, p])].relationship >= 2:
			relations[frozenset([player.name, p])].relationship -= 0.15
		if relations[frozenset([target.name, p])].relationship >= 2.7:
			if pl.type == "major" or pl.type == "minor":
				if relations[frozenset([player.name, p])].relationship < 2:
					new = CB(p, player.name, "annex", prov.name, 5)
					pl.CB["opponent"] = new
					pl.CB[new.opponent] = new
				else:
					relations[frozenset([player.name, p])].relationship -= 1

	if type(pl) == AI:
		if pl.rival_target != []:
			if target == pl.rival_target[0]: 
				relations[frozenset([player.name, p])].relationship -= 0.15
		if target in pl.allied_target:
			relations[frozenset([player.name, p])].relationship -= 0.2

	if len(target.provinces.keys()) == 0:
		delete_nation(player.name, target.name, players, market, relations)
	else:
		p2_borders = set()
		for k, v in players.items():
			if target.check_for_border(v, players) == True:
				p2_borders.add(k)
		target.borders = p2_borders
	if player.reputation < 0:
			player.reputation = 0

	
class Battle(object):
	def __init__(self, ID, attacker, defender, prov):
		self.ID = ID
		self.attacker = attacker 
		self.defender = defender
		self.prov = prov
		self.winner = ""
		self.initial_attacker_forces = {}
		self.initial_defender_forces = {}

		self.attacker_ammo = 0
		self.defender_ammo = 0
		self.attacker_ammo_needed = 0
		self.defender_ammo_needed = 0
		self.attacker_ammo_penalty = 0
		self.defender_ammo_penalty = 0

		self.attacker_oil = 0
		self.defender_oil = 0
		self.attacker_oil_needed = 0
		self.defender_oil_needed = 0
		self.attacker_oil_penalty = 0
		self.defender_oil_penalty = 0

	def combat_outcome(self, players, market, relations, provinces):
		if self.prov == "total":
		#	self.resolve_total_war(players, market, relations)
			return
		attacker = players[self.attacker]
		defender = players[self.defender]
		prov = provinces[self.prov]
		if type(attacker) == AI:
			attacker.rival_target = []
		relata = frozenset([attacker.name, defender.name])
		attacker.rival_target = []
		relations[relata].relationship += 1
		cb_keys = []
		for cb in attacker.CB.keys():
			cb_keys.append(cb)
		for cb in cb_keys:
			if attacker.CB[cb].province == prov.name:
					if cb in attacker.CB.keys():
						del attacker.CB[cb]
		if self.winner == attacker.name:
			market.report.append("%s has successfully invaded %s ! \n" % (attacker.name, defender.name))
			print("%s has successfully invaded %s ! \n" % (attacker.name, defender.name))
			#maybe gain stability with Nationalism
			defender.just_attacked = 3
			if defender.number_developments >= 2:
				opts = []
				for pr, province in defender.provinces.items():
					if province.development_level >= 1:
						opts.append(province)
				if len(opts) >= 1:
					selection = choice(opts)
					selection.development_level -= 1
			if prov.name in defender.provinces.keys():
				self.gain_province(players, market, relations, provinces)
			loot = attacker.resources["gold"]/3
			attacker.resources["gold"] += loot
			defender.resources["gold"] -= loot
			market.report.append("%s loots %.2f gold from %s \n" % (attacker.name, loot, defender.name))
			war_after_math(attacker.name, defender.name, players, relations, prov.name, provinces, market)
			if defender.type == "major" and attacker.military["tank"] > 0 and prov.culture == defender.culture:
				defender.defeated == True
				market.report.append("%s has been defeated by %s! " % (defender.name, attacker.name))
		elif self.winner == defender.name:
			attacker.stability -= 0.5
			if attacker.stability < -3.0:
				attacker.stability = -3.0
			defender.stability += 0.5
			if defender.stability > 3.0:
				defender.stability = 3.0
			market.report.append("%s has repelled %s's pitiful invasion! \n" % (defender.name, attacker.name))

	def gain_province(self, players, market, relations, provinces):
		prov = provinces[self.prov]
		attacker = players[self.attacker]
		defender = players[self.defender]
		war_after_math(attacker.name, defender.name, players, relations, prov.name, provinces, market)
		market.report.append("%s has defeated %s for the province of %s \n" % (attacker.name, defender.name, prov.name))
		print("%s has defeated %s for the province of %s \n" % (attacker.name, defender.name, prov.name))
		if prov.culture == defender.culture or prov.type == "civilized":
			if defender.development_level > 2:
				defender.development_level -= 1
				possibilities = []
				for d, dev in defender.developments.items():
					if dev > 0:
						possibilities.append(d)
				loss = choice(possibilities)
				defender.developments[loss] -= 1
		prov.owner = attacker.name
		print("%s is now owned by %s" % (prov.name, attacker.name))
		#new = deepcopy(p2.provinces[prov.name])
		attacker.number_developments += prov.development_level 
		#maybe add an option for sorchered earth 
		defender.number_developments -= prov.development_level
		attacker.provinces[prov.name] = prov
		if type(attacker) == AI:
			attacker.resource_base[prov.resource] += prov.quality
			attacker.ai_modify_priorities_from_province(attacker.provinces[prov.name].resource)
		if type(defender) == AI:
			defender.resource_base[prov.resource] -= prov.quality
		p2_core = defender.core_provinces() 
		#p1.provinces[new.name].type = "old"
		if prov in p2_core:
			#print(prov)
			p2_core.remove(prov)
		defender.provinces.pop(prov.name)
		p2_core = list(p2_core)
		if prov.name in defender.capital:
			#print(prov.name + "is old capital of" + p2.name)
			defender.capital.remove(prov.name)
		if len(defender.provinces.keys()) > 0 and len(defender.capital) == 0:
			if len(p2_core) > 0:
				ch = choice(p2_core)
			#	print("New Capital: %s" % (ch.name))
				defender.capital.add(ch.name)
			else:
				ch = choice(list(defender.provinces.keys()))
				defender.capital.add(ch)
		if prov.colony == True:
			defender.num_colonies -= 1
			defender.colonization += (1 + defender.num_colonies)
		if defender.type == "old_empire" or defender.type == "old_minor" or prov.colony == True:
			attacker.colonization -= (1 + attacker.num_colonies)
			attacker.provinces[prov.name].colony = True
			attacker.num_colonies += 1
		if prov.worked == True:
			attacker.POP += 1
			attacker.numLowerPOP += 1
			defender.POP -= 1
			defender.numLowerPOP -= 1
		p1_borders = set()
		for k, v in players.items():
			if attacker.check_for_border(v, players) == True:
				p1_borders.add(k)
		attacker.borders = p1_borders 
		market.report.append(prov.name + " is now part of " + attacker.name)
		print(prov.name + " is now part of " + attacker.name)


class LandBattle(Battle):
	def __init__(self, ID, attacker, defender, prov, *args, **kwargs):
		super(LandBattle, self).__init__(ID, attacker, defender, prov, *args, **kwargs)
		self.attacker_forces = {}
		
		self.attacker_dogfight_roll = 0
		self.defender_dogfight_roll = 0
		self.att_fighters_lost = 0
		self.def_fighters_lost = 0
		self.att_recon = 0
		self.def_recon = 0
		self.att_art_losses = 0
		self.def_art_losses = 0
		self.att_manouver = 0
		self.def_manouver = 0
		self.att_eng_losses = 0
		self.def_eng_losses = 0
		self.winner = ""


	def dogFight(self, players, market):
		AirAttRoll = uniform(1.0, 1.2)
		AirDefRoll = uniform(1.0, 1.2)
		attacker = players[self.attacker]
		defender = players[self.defender]
		
		AttAirStr = self.attacker_forces["fighter"] * attacker.fighter["manouver"] * attacker.fighter["attack"] * AttRoll * self.attacker_ammo_penalty * self.attacker_oil_needed
		DefAirStr = defender.military["fighter"] * defender.fighter["manouver"] * defender.fighter["attack"] * DefRoll * self.defender_ammo_penalty * self.defender_oil_penalty
		AttAirStrN = AttAirStr/(AttAirStr + DefAirStr)
		DefAirStrN = DefAirStr/(AttAirStr + DefAirStr)

		if AttAirStrN > DefAirStrN:
			percent_units_lost = 0.5 * (DefAirStrN/AttAirStrN)
		else:
			percent_units_lost = 0.5 * (AttAirStrN/DefAirStrN)

		total_losses = (self.attacker_forces["fighter"] + defender.military["fighter"]) * percent_units_lost

		self.att_fighters_lost = total_losses * DefAirStrN
		self.def_fighters_lost = total_losses * AttAirStrN
		market.report.append("Def Fighter Losees %s" % (self.att_fighters_lost))
		market.report.append("Att Fighter Losses %s" % (self.att_fighter_losses))

		self.attacker_forces["fighter"] -= min(self.att_fighters_losts, self.attacker_forces["fighter"])
		attacker.military["fighter"] -= min(self.att_fighters_lost, attacker.military["fighter"])
		defender.military["fighter"] -= min(self.def_fighters_lost, defender.military["fighter"])


	def artilleryPhaseLosses(self, players):
		attacker = players[self.attacker]
		defender = players[self.defender]
		artFactor = (self.attacker_forces["artillery"] * attacker.artillery["attack"]) \
		+ (defender.military["artillery"] * defender.artillery["defend"])
		total = attacker.calculate_amphib_strength(self.attacker_forces) + defender.calculate_base_defense_strength()
		return artFactor/total


	def artillery_phase(self, players, market):
		AttRoll = uniform(1, 1.2)
		DefRoll = uniform(1, 1.2)
		AttMod = 1.0
		DefMod = 1.0
		attacker = players[self.attacker]
		defender = players[self.defender]
		if self.att_recon > self.def_recon:
			AttMod += (self.att_recon - self.def_recon)
		else:
			DefMod += (self.def_recon - self.att_recon)
		AttArtStr = self.attacker_forces["artillery"] * attacker.artillery["attack"] * AttMod * self.attacker_ammo_penalty * AttRoll
		DefArtStr = defender.military["artillery"] * defender.artillery["defend"] + DefMod * self.defender_ammo_penalty * DefRoll * defender.fortification 

		AttArtStrN = AttArtStr / (AttArtStr + DefArtStr)
		DefArtStrN = DefArtStr / (AttArtStr + DefArtStr)

		#losses = self.artilleryPhaseLosses(players)
		total = attacker.calculate_amphib_strength(self.attacker_forces) + defender.calculate_base_defense_strength()
		artFactor = (self.attacker_forces["artillery"] * attacker.artillery["attack"])/total
		num_units = self.calculate_amphib_num_units(players) + defender.calculate_number_of_units()
		self.att_art_losses = artFactor * DefArtStrN * num_units * 0.5
		self.def_art_losses = artFactor * AttArtStrN * num_units * 0.5
		market.report.append("Def Art Losees %s" % (self.def_art_losses))
		market.report.append("Att Art Losses %s" % (self.att_art_losses))

		self.distribute_losses_amph(players, self.att_art_losses)
		self.distribute_losses(players, self.def_art_losses)

	def calculate_amphib_num_units(self, players):
		player = players[self.attacker]
		number = 0
		for k, v in self.attacker_forces.items():
			number += v
		return number

	def distribute_losses_amph(self, players, losses):
		player = players[self.attacker]
		count = 0
		num_units = self.calculate_amphib_num_units(players)
		while(losses >= 0.25 and num_units >= 0.5 and count < 64):
			count += 1
			pick = uniform(0, 1)
			print("att loss pick %.2f" % pick)
			num_units -= 0.25
			player.POP -= 0.05
			player.milPOP -= 0.05
			player.numLowerPOP -= 0.05
			losses -= 0.25
			if pick <= 0.30:
				if(self.attacker_forces["infantry"] >= 0.25):
					self.attacker_forces["infantry"] -= 0.25
					player.military["infantry"] -=0.25
				else:
					continue
			elif pick > 0.25 and pick <= 0.55:
				if(self.attacker_forces["cavalry"] >= 0.25):
					self.attacker_forces["cavalry"] -= 0.25
					player.military["cavalry"] -= 0.25
				else:
					continue
			elif pick > 0.55 and pick <= 0.75:
				if(self.attacker_forces["tank"] >= 0.25):
					player.military["tank"] -= 0.25
					self.attacker_forces["tank"] -= 0.25					
				else:
					continue
			elif pick > 0.77 and pick <= 0.90:
				if(self.attacker_forces["artillery"]):
					player.military["artillery"] -= 0.25
					self.attacker_forces["artillery"] -= 0.25
				else:
					continue
			elif pick > 0.90:
				if(self.attacker_forces["fighter"] >= 0.25):
					player.military["fighter"] -= 0.25
					self.attacker_forces["fighter"] -= 0.25
				else:
					continue

	def distribute_losses(self, players, losses):
		player = players[self.defender]
		num_units = player.calculate_number_of_units()
		count = 0
		while(losses >= 0.25 and num_units >= 0.5 and count < 64):
			count += 1
			pick = uniform(0, 1)
			num_units -= 0.25
			player.POP -= 0.05
			player.milPOP -= 0.05
			player.numLowerPOP -= 0.05
			losses -= 0.25
			print("def loss pick %.2f" % pick)
			if pick <= 0.30:
				if player.military["infantry"] >= 0.25:
					player.military["infantry"] -= 0.25
				else:
					continue
			elif pick > 0.30 and pick <= 0.55:
				if player.military["cavalry"] >= 0.25:
					player.military["cavalry"] -= 0.25
				else:
					continue
			elif pick > 0.55 and pick <= 0.77:
				if player.military["tank"] >= 0.25:
					player.military["tank"] -= 0.25
				else:
					continue

			elif pick > 0.77 and pick <= 0.9:
				if(player.military["artillery"] >= 0.25):
					player.military["artillery"] -= 0.25
				else:
					continue

			elif pick > 0.9:
				if(player.military["fighter"] >= 0.25):
					player.military["fighter"] -= 0.25
				else:
					continue
		return num_units

	def determine_manouver(self, players):
		AttManRoll = uniform(1, 1.2)
		DefManRoll = uniform(1, 1.2)
		attacker = players[self.attacker]
		defender = players[self.defender]

		AttManouver = ((self.attacker_forces["infantry"] * attacker.infantry["manouver"]) + 
		(self.attacker_forces["cavalry"] * attacker.cavalry["manouver"]) + 	
		(self.attacker_forces["tank"] * attacker.tank["manouver"] * self.attacker_oil_penalty)) * AttManRoll
		
		DefManouver = ((defender.military["infantry"] * defender.infantry["manouver"]) +
		(defender.military["cavalry"] * defender.cavalry["manouver"]) +
		(defender.military["tank"] * defender.tank["manouver"] * self.defender_oil_penalty)) * DefManRoll

		self.att_manouver = AttManouver/(AttManouver + DefManouver)
		self.def_manouver = DefManouver/(AttManouver + DefManouver)


	def direct_engagement(self, players, market):
		attacker = players[self.attacker]
		defender = players[self.defender]
		AttRoll = uniform(1, 1.2)
		DefRoll = uniform(1, 1.2)
		AttMod = 1
		DefMod = 1
		if self.att_manouver > self.def_manouver:
			AttMod += (self.att_manouver - self.def_manouver)
		else:
			DefMod += (self.def_manouver - self.att_manouver)

		AttStr = (self.attacker_ammo_penalty * AttRoll * AttMod) * ((self.attacker_forces["infantry"] * attacker.infantry["attack"]) + 
		(self.attacker_forces["cavalry"] * attacker.cavalry["attack"]) + (self.attacker_forces["tank"] * attacker.tank["attack"] * self.attacker_oil_penalty))
		
		DefStr = (self.defender_ammo_penalty * DefRoll * DefMod) * ((defender.military["infantry"] * defender.infantry["defend"]) + 
		(defender.military["cavalry"] * defender.cavalry["defend"]) + (defender.military["tank"] * defender.tank["defend"] * self.defender_oil_penalty))

		AttStrN = AttStr/(AttStr + DefStr)
		DefStrN = DefStr/(AttStr + DefStr)

		artFactor = (self.attacker_forces["artillery"] * attacker.artillery["attack"]) + (defender.military["artillery"] * defender.artillery["defend"])
		total = attacker.calculate_amphib_strength(self.attacker_forces) + defender.calculate_base_defense_strength()
		losses = (total - artFactor)/total 
		num_units = self.calculate_amphib_num_units(players) + defender.calculate_number_of_units()

		self.att_eng_losses = losses * DefStrN * num_units * 0.25
		self.def_eng_losses = losses * AttStrN * num_units * 0.25
		market.report.append("Def engagement losses: %.2f" % self.def_eng_losses)
		market.report.append("Att engagement losses: %.2f" % self.att_eng_losses)

		self.distribute_losses_amph(players, self.att_eng_losses)
		self.distribute_losses(players, self.def_eng_losses)


	def landCombat(self, players, market, relations, provinces):
		attacker = players[self.attacker]
		defender = players[self.defender]
		self.initial_attacker_forces = self.attacker_forces
		self.initial_attacker_forces["infantry"] = self.attacker_forces["infantry"]
		self.initial_attacker_forces["cavalry"] = self.attacker_forces["cavalry"]
		self.initial_attacker_forces["artillery"] = self.attacker_forces["artillery"]
		self.initial_attacker_forces["fighter"] = self.attacker_forces["fighter"]
		self.initial_attacker_forces["tank"] = self.attacker_forces["tank"]
		
		self.initial_defender_forces["infantry"] = defender.military["infantry"]
		self.initial_defender_forces["cavalry"] = defender.military["cavalry"]
		self.initial_defender_forces["artillery"] = defender.military["artillery"]
		self.initial_defender_forces["fighter"] = defender.military["fighter"]
		self.initial_defender_forces["tank"] = defender.military["tank"]
		market.report.append("War has broken out between %s and %s ! \n" % (attacker.name, defender.name))
		self.attacker_ammo = attacker.goods["cannons"]
		self.defender_ammo = defender.goods["cannons"]
		self.attacker_ammo_needed = attacker.calculate_amphib_ammo(self.attacker_forces)
		self.defender_ammo_needed = defender.calculate_land_ammo_needed()
		self.attacker_ammo_penalty = attacker.ammo_penalty(self.attacker_ammo_needed)
		self.defender_ammo_penalty = defender.ammo_penalty(self.defender_ammo_needed)

		self.attacker_oil = attacker.resources["oil"]
		self.defender_oil = defender.resources["oil"]
		self.attacker_oil_needed = attacker.calculate_amphib_oil(self.attacker_forces)
		self.defender_oil_needed = defender.calculate_oil_needed()
		self.attacker_oil_penalty = attacker.oil_penalty(self.attacker_oil_needed)
		self.defender_oil_penalty = defender.oil_penalty(self.defender_oil_needed)

		if self.attacker_forces["fighter"] > 0.2 and defender.military["fighter"] > 0.2:
			self.dogFight(players, market)
		AttRecon = attacker.recon()
		DefRecon = defender.recon()
		self.att_recon = AttRecon/(AttRecon + DefRecon)
		self.def_recon = DefRecon/(AttRecon + DefRecon) 
		#Phase Two: Artillery Barrage 
		self.artillery_phase(players, market)
		#Phase Three: Manouver 
		self.determine_manouver(players)
		# Phase Three: Engagement
		self.direct_engagement(players, market)
		if self.calculate_attacker_strength(players) > defender.calculate_base_defense_strength():
			self.winner = self.attacker
		else:
			self.winner = self.defender		
		self.combat_outcome(players, market, relations, provinces)
		return

	def calculate_attacker_strength(self, players):
		strength = 0
		player = players[self.attacker]
		for k, v in self.attacker_forces.items():
			if k == "infantry":
				strength += v * player.infantry["attack"]
			if k == "cavalry":
				strength += v * player.cavalry["attack"]
			if k == "artillery":
				strength += v * player.artillery["attack"]
			if k == "tank":
				strength += v * player.tank["attack"]
			if k == "fighter":
				strength += v * player.fighter["attack"]
		return strength


class SeaBattle(Battle):
	def __init__(self, ID, attacker, defender, prov, *args, **kwargs):
		super(SeaBattle, self).__init__(ID, attacker, defender, prov, *args, **kwargs)
		self.att_losses = 0
		self.def_losses = 0
		self.winner = ""

	
	def naval_battle(self, players, market, relations, provinces):
		p1 = players[self.attacker]
		p2 = players[self.defender]
		self.attacker_ammo = p1.goods["cannons"]
		self.defender_ammo = p2.goods["cannons"]
		self.attacker_oil = p1.resources["oil"]
		self.defender_oil = p2.resources["oil"]
		self.initial_attacker_forces["frigates"] = p1.military["frigates"]
		self.initial_attacker_forces["iron_clad"] = p1.military["iron_clad"]
		self.initial_attacker_forces["battle_ship"] = p1.military["battle_ship"]
		self.initial_defender_forces["frigates"] = p2.military["frigates"]
		self.initial_defender_forces["iron_clad"] = p2.military["iron_clad"]
		self.initial_defender_forces["battle_ship"] = p2.military["battle_ship"]
		att_number_units_navy = p1.calculate_number_of_ships()
		def_number_units_navy = p2.calculate_number_of_ships()

		market.report.append("A naval battle is being fought between %s and %s !! \n" % (p1.name, p2.name))
		winner = ""
		market.report.append("%s has a fleet size of %s, %s has a fleet size of %s \n" % (p1.name, att_number_units_navy, p2.name, def_number_units_navy))
		self.attacker_ammo_needed = p1.calculate_ammo_needed_navy()
		self.defender_ammo_needed = p2.calculate_ammo_needed_navy()
		self.attacker_oil_needed = p1.calculate_oil_needed_navy()
		self.defender_oil_needed = p2.calculate_oil_needed_navy()
		
		p1_roll = uniform(1, 1.2)
		p2_roll = uniform(1, 1.2)
		self.attacker_ammo_penalty = p1.ammo_penalty(self.attacker_ammo_needed)
		self.defender_ammo_penalty = p2.ammo_penalty(self.defender_ammo_needed)
		self.atttacker_oil_penalty = p1.oil_penalty(self.attacker_oil_needed)
		self.defender_oil_penalty = p2.oil_penalty(self.defender_oil_needed)


		att_str = (p1_roll * self.attacker_ammo_penalty) * ((p1.military["frigates"] * p1.frigates["attack"]) + \
		(p1.military["iron_clad"] * p1.iron_clad["attack"]) + (p1.military["battle_ship"] * p1.battle_ship["attack"] \
		 * self.attacker_oil_penalty))

		def_str = (p2_roll * self.defender_ammo_penalty) * ((p2.military["frigates"] * p2.frigates["attack"]) + \
		(p2.military["iron_clad"] * p2.iron_clad["attack"] ) + (p2.military["battle_ship"] * p2.battle_ship["attack"] \
		 * self.defender_oil_penalty))
		market.report.append("%s has naval strength of %s, %s has naval strength of %s \n" % (p1.name, att_str, p2.name, def_str))

		self.att_str = att_str/(att_str + def_str)
		self.def_str = def_str/(att_str + def_str)

		total_losses = (att_number_units_navy + def_number_units_navy)/3.33
	
		self.att_losses = total_losses * self.def_str
		self.def_losses = total_losses * self.att_str

		market.report.append("%s takes %s losses, %s takes %s losses \n" % (p1.name, self.att_losses, p2.name, self.def_losses))
		att_number_units_navy = distribute_naval_losses(p1, self.att_losses, att_number_units_navy)
		def_number_units_navy = distribute_naval_losses(p2, self.def_losses, def_number_units_navy)
		market.report.append("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_navy, p2.name, def_number_units_navy))
		
		att_str_remaining = p1.calculate_naval_strength()
		def_str_remaining = p2.calculate_naval_strength()

		if att_str_remaining > def_str_remaining:
			market.report.append("%s has defeated %s at sea! \n" % (p1.name, p2.name))
			self.winner = p1.name
			if self.prov in p2.provinces.keys():
				p1.stability -= 0.5
				if p1.stability < -3.0:
					p1.stability = -3.0
				p2.stability += 0.5
				if p2.stability > 3.0:
					p2.stability = 3.0
				self.gain_province(players, market, relations, provinces)
				war_after_math(p1.name, p2.name, players, relations, self.prov, provinces, market)
			return 
		else:
			p1.stability -= 0.5
			if p1.stability < -3.0:
				p1.stability = -3.0
			p2.stability += 0.5
			if p2.stability > 3.0:
				p2.stability = 3.0
			market.report.append("%s has defeated %s at sea! \n"% (p2.name, p1.name))
			war_after_math(p1.name, p2.name, players, relations, self.prov, provinces, market)
			return 



def distribute_naval_losses(player, losses, num_units):
	limit = 0
	while(losses >= 0.25 and num_units >= 0.25 and limit < 128):
		limit += 1
		losses -= 0.25
		while(player.military["frigates"] >= 0.25 and losses >= 0.25):
		#	print("Losses %s, num_units %s \n" % (losses, num_units))
			player.military["frigates"] -= 0.25
			player.POP -= 0.05
			player.milPOP -= 0.05
			player.numLowerPOP -= 0.05
			num_units -= 0.25
		while(player.military["iron_clad"] >= 0.125 and losses > 0.125):
			player.military["iron_clad"] -= 0.125
			player.military["frigates"] -= 0.25
			player.POP -= 0.125
			player.milPOP -= 0.125
			player.numLowerPOP -= 0.125
			num_units -= 0.125
		while(player.military["battle_ship"] >= 0.0625 and losses > 0.0625):
			player.military["battle_ship"] -= 0.0625
			player.POP -= 0.0625
			player.milPOP -= 0.0625
			player.numLowerPOP -= 0.0625
			num_units -= 0.0625
			losses -= 0.0625
	return num_units
	