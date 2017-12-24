
from player_class import Player
from technologies import*
from human import Human
from AI import AI
from minor_classes import*
#from AI_foreign_affairs import*
from random import*
from pprint import pprint
from copy import deepcopy
	
class Battle(object):
	def __init__(self, attacker, defender, prov):
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
		for cb in attacker.CB:
			cb_keys.append(cb)
		for cb in cb_keys:
			if cb.province == prov.name:
				attacker.CB.remove(cb)
				del cb
		if self.winner == attacker.name:
			market.report.append("%s has successfully invaded %s ! \n" % (attacker.name, defender.name))
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
				self.gain_province(players, market, relations)
			else:
				attacker.war_after_math(defender, players, relations, prov)
			loot = attacker.resources["gold"]/3.33
			attacker.resources["gold"] += loot
			defender.resources["gold"] -= loot
			market.report.append("%s loots %s gold from %s \n" % (attacker.name, loot, defender.name))
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
			market.report.append("%s has repelled %s's pitiful invasion! \n" % (p2.name, p1.name))

	def gain_province(self, players, market, relations, provinces):
		prov = provinces[self.prov]
		attacker = players[self.attacker]
		defender = players[self.defender]
		market.report.append("%s has defeated %s for the province of %s \n" % (attacker.name, defender.name, prov.name))
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
			attacker.colonization -= (1 + p1.num_colonies)
			attacker.provinces[prov.name].colony = True
			attacker.num_colonies += 1
		if prov.worked == True:
			attacker.POP += 1
			attacker.numLowerPOP += 1
			defender.POP -= 1
			defender.numLowerPOP -= 1
		if len(defender.provinces.keys()) == 0:
			defender.delete_nation()
			attacker.war_after_math(defender.name, players, relations, prov.name, provinces)
		else:
			attacker.war_after_math(defender.name, players, relations, prov.name, provinces)
			p2_borders = set()
			for k, v in players.items():
				if defender.check_for_border(v) == True:
					p2_borders.add(k)
			defender.borders = p2_borders
		#recalculate borders of nations:
		p1_borders = set()
		for k, v in players.items():
			if attacker.check_for_border(v) == True:
				p1_borders.add(k)
		attacker.borders = p1_borders 
		market.report.append(prov.name + " is now part of " + attacker.name)


class LandBattle(Battle):
	def __init__(self, attacker, defender, prov, *args, **kwargs):
		super(LandBattle, self).__init__(attacker, defender, *args, **kwargs)
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



	def dogFight(self, players):
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

		self.attacker_forces["fighter"] -= min(self.att_fighters_losts, self.attacker_forces["fighter"])
		attacker.military["fighter"] -= min(self.att_fighters_lost, attacker.military["fighter"])
		defender.military["fighter"] -= min(self.def_fighters_lost, defender.military["fighter"])


	def artilleryPhaseLosses(self, players):
		attacker = players[self.attacker]
		defender = players[self.defender]
		artFactor = (self.attacker_forces["artillery"] * attacker.artillery["attack"]) \
		+ (defender.military["artillery"] * defender.artillery["defend"])
		total = calculate_amphib_strength(attacker, self.attacker_forces) + defender.calculate_base_defense_strength()
		return artFactor/total


	def artillery_phase(self, players):
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

		losses = self.artilleryPhaseLosses(players)
		self.att_art_losses = losses * DefArtStrN
		self.def_art_losses = losses * AttArtStrN

		self.attacker_forces = self.distribute_losses_amph(attacker, players, self.att_art_losses)
		self.distribute_losses(defender, players, self.def_art_losses)


	def distribute_losses_amph(self, players, losses):
		num_units = calculate_amphib_num_units(attacker, self.attacker_forces)
		player = players[self.attacker]
		while(losses > 0.5 and num_units >= 0.5):
			loss = uniform(0, 1)
			if loss <= 0.30:
				if(self.attacker_forces["infantry"] >= 0.5):
					self.attacker_forces["infantry"] -= 0.5
					player.military["infantry"] -=0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue
			elif loss > 0.25 and loss <= 0.55:
				if(self.attacker_forces["cavalry"] >= 0.5):
					self.attacker_forces["cavalry"] -= 0.5
					player.military["cavalry"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue

			elif loss > 0.55 and loss <= 0.75:
				if(self.attacker_forces["tank"] >= 0.5):
					player.military["tank"] -= 0.5
					num_units -= 0.5
					self.attacker_forces["tank"] -= 0.5					
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue
			elif loss > 0.75 and loss <= 0.90:
				if(self.attacker_forces["artillery"]):
					player.military["artillery"] -= 0.5
					self.attacker_forces["artillery"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue
			elif loss > 0.90:
				if(self.attacker_forces["fighter"] >= 0.5):
					player.military["fighter"] -= 0.5
					num_units -= 0.5
					self.attacker_forces["fighter"] -= 0.5
					#player.num_units -=0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue

	def distribute_losses(self, players, losses):
		player = players[defender]
		num_units = calculate_number_of_units(player)
		while(losses >= 0.5 and num_units >= 0.5):
			if loss <= 0.30:
				if(player.military["infantry"] >= 0.5):
					player.military["infantry"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue
			elif loss > 0.30 and loss <= 0.55:
				if(player.military["cavalry"] >= 0.5):
					player.military["cavalry"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue
			elif loss > 0.55 and loss <= 0.75:
				if(player.military["tank"] >= 0.5):
					player.military["tank"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue

			elif loss > 0.77 and loss <= 0.9:
				if(player.military["artillery"] >= 0.5):
					player.military["artillery"] -= 0.5
					num_units -= 0.5
					player.POP -= 0.1
					player.milPOP -= 0.1
					player.numLowerPOP -= 0.1
					losses -= 0.5
				else:
					continue

			elif loss > 0.9:
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

	def determine_manouver(self, players):
		AttManRoll = uniform(1, 1.2)
		DefManRoll = uniform(1, 1.2)
		attacker = players[self.attacker]
		defender = players[self.defender]

		AttManouver = ((self.attacker_forces["infantry"] * attacker.infantry["manouver"]) + 
		(self.attacker_forces["cavalry"] * attacker.cavalry["manouver"]) + 	
		(self.attacker_forces["tanks"] * attacker.tanks["manouver"] * self.attacker_oil_penalty)) * AttManRoll
		
		DefManouver = ((defender.military["infantry"] * defender.infantry["manouver"]) +
		(defender.military["cavalry"] * defender.cavalry["manouver"]) +
		(defender.military["tanks"] * defender.tanks["manouver"] * self.defender_oil_penalty)) * DefManRoll

		self.att_manouver = AttManouver/(AttManouver + DefManouver)
		self.def_manouver = DefManouver/(AttManouver + DefManouver)


	def direct_engagement(players):
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
		(self.attacker_forces["cavalry"] * attacker.cavalry["attack"]) + (self.attacker_forces["tank"] * attacker.tank["attack"] * self.att_man_oil_penalty))
		
		DefStr = (self.defender_ammo_penalty * DefRoll * DefMod) * ((defender.military["infantry"] * defender.infantry["defend"]) + 
		(defender.military["cavalry"] * defender.cavalry["defender"]) + (defender.military["tank"] * defender.tank["defend"] * self.def_man_oil_penalty))

		AttStrN = AttStr/(AttStr + DefStr)
		DefStrN = DefStr/(AttStr + DefStr)

		total = calculate_amphib_strength(attacker, self.attacker_forces) + defender.calculate_base_defense_strength()
		losses = total/3

		self.att_eng_losses = losses * DefStrN
		self.def_eng_losses = losses * AttStrN

		self.attacker_forces = self.distribute_losses_amph(attacker, players, self.att_eng_losses)
		self.distribute_losses(defender, players, self.def_eng_losses)


	def landCombat(self, players, market, relations, provinces):
		attacker = players[self.attacker]
		defender = players[self.defender]
		self.initial_attacker_forces = self.attacker_forces
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

		if att_current_makeup["fighter"] > 0.2 and defender.militart["fighter"] > 0.2:
			self.dogFight(players)
		AttRecon = attacker.recon()
		DefRecon = defender.recon()
		self.att_recon = AttRecon/(AttRecon + DefRecon)
		self.def_recon = DefRecon/(AttRecon + DefRecon) 
		#Phase Two: Artillery Barrage 
		self.artillery_phase(players)
		#Phase Three: Manouver 
		self.determine_manouver(players)
		# Phase Three: Engagement
		self.direct_engagment(players)
		if self.calculate_attacker_strength() > defender.calculate_base_defense_strength():
			self.winner = self.attacker
		else:
			self.winner = self.defender		
		self.combat_outcome(players, market, relations, provinces)
		return

	def calculate_attacker_strength(self):
		strength = 0
		for k, v in self.attack_forces.items():
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


class SeaBattle(Battle):
	def __init__(self, attacker, defender, prov, *args, **kwargs):
		super(LandBattle, self).__init__(attacker, defender, *args, **kwargs)
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
		self.initial_attacker_forces["frigates"] = attacker.military["frigates"]
		self.initial_attacker_forces["iron_clad"] = attacker.military["iron_clad"]
		self.initial_attacker_forces["battle_ship"] = attacker.military["battle_ship"]
		self.initial_defender_forces["frigates"] = defender.military["frigates"]
		self.initial_defender_forces["iron_clad"] = defender.military["iron_clad"]
		self.initial_defender_forces["battle_ship"] = defender.military["battle_ship"]
 		market.report.append("A naval battle is being fought between %s and %s !! \n" % (p1.name, p2.name))
		winner = ""
		market.report.append("%s has a fleet size of %s, %s has a fleet size of %s \n" % (p1.name, att_initial_navy, p2.name, def_initial_navy))
		self.attacker_ammo_needed = p1.calculate_ammo_needed_navy()
		self.defender_ammo_needed = p2.calculate_ammo_needed_navy()
		self.attacker_oil_needed = p1.calculate_oil_needed_navy()
		self.defender_oil_needed = p2.calculate_oil_needed_navy()
		market.report.append("%s has naval strength of %s, %s has naval strength of %s \n" % (p1.name, att_str, p2.name, def_str))
		
		p1_roll = uniform(1, 1.2)
		p2_roll = uniform(1, 1.2)
		self.attacker_ammo_penalty = p1.ammo_penalty(self.attacker_ammo_needed)
		self.defender_ammo_penalty = p2.ammo_penalty(self.defender_ammo_needed)
		self.atttacker_oil_penalty = p1.oil_penalty(self.attacker_oil_needed)
		self.defender_oil_penalty = p2.oil_penalty(self.defender_oil_needed)

		att_str = (p1_roll * self.att_ammo_penalty) * ((p1.military["frigates"] * p1.frigates["strength"]) + \
		(p1.military["iron_clad"] * p1.iron_clad["attack"]) + (p1.military["battle_ship"] * p1.battle_ship[attack] \
		 * self.attacker_oil_penalty))

		def_str = (p2_roll * self.defender_ammo_penalt) * ((p2.military["frigates"] * p2.frigates["strength"]) + \
		(p2.military["iron_clad"] * p2.iron_clad["attack"] ) + (p2.military["battle_ship"] * p2.battle_ship[attack] \
		 * self.defender_oil_penalty))

		self.att_str = att_str/(att_str + def_str)
		self.def_str = def_str/(att_str + def_str)

		total_losses = (att_number_units_navy + def_number_units_navy)/3.33
	
		self.att_losses = total_losses * self.def_str
		self.def_losses = total_losses * self.att_str

		market.report.append("%s takes %s losses, %s takes %s losses \n" % (p1.name, self.att_losse, p2.name, self.def_losses))
		att_number_units_navy = distribute_naval_losses(p1, att_losses, att_number_units_navy)
		def_number_units_navy = distribute_naval_losses(p2, def_losses, def_number_units_navy)
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
					p1.war_after_math(p2.name, players, relations, prov, provinces)
				return 
			else:
				p1.stability -= 0.5
				if p1.stability < -3.0:
					p1.stability = -3.0
				p2.stability += 0.5
				if p2.stability > 3.0:
					p2.stability = 3.0
				market.report.append("%s has defeated %s at sea! \n"% (p2.name, p1.name))
				p1.war_after_math(p2.name, players, relations, prov, provinces)
				return 

	