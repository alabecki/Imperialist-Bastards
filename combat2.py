#combat2

def amph_combat(p1, p2, p1_forces, prov, players, market, relations):
	print("War has broken out between %s and %s ! \n" % (p1.name, p2.name))
	market.report.append("War has broken out between %s and %s ! \n" % (p1.name, p2.name))
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
		market.report.append("%s has %s units and base attack strength of %s \n" % (p1.name, att_number_units_army, att_str))
		market.report.append("%s has %s units and base defense strength of %s \n" % (p2.name, def_number_units_army, def_str))
		att_manouver = att_manouver * att_manouver_roll
		def_manouver = def_manouver * def_manouver_roll
		# 1 - 1/att_man

		print("%s manouver = %s, %s manouver = %s \n" % (p1.name, att_manouver, p2.name, def_manouver))
		market.report.append("%s manouver = %s, %s manouver = %s \n" % (p1.name, att_manouver, p2.name, def_manouver))
		if( att_manouver * att_manouver_roll) > (def_manouver * def_manouver_roll):
			difference = att_manouver/(def_manouver + 0.001)
			print("%s out-manouvers %s \n" % (p1.name, p2.name))
			market.report.append("%s out-manouvers %s \n" % (p1.name, p2.name))
			att_str = att_str * min( 1.33, difference)


		else:
			print("%s out-manouvers %s \n" % (p2.name, p1.name))
			market.report.append("%s out-manouvers %s \n" % (p2.name, p1.name))
			difference = def_manouver/(att_manouver + 0.001)
			def_str = def_str * min( 1.33, difference)
		print("%s total attack strength: %s, %s total attack strength: %s \n" % (p1.name, att_str, p2.name, def_str))
		market.report.append("%s total attack strength: %s, %s total attack strength: %s \n" % (p1.name, att_str, p2.name, def_str))
		p1a_deficit = p1.goods["cannons"] - att_ammo
		if p1a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p1.name, abs(p1a_deficit)))
			market.report.append("%s has an ammo deficit of %s" % (p1.name, abs(p1a_deficit)))
			penalty = abs(p1a_deficit/ ((att_ammo * 2) + 0.01))
			att_str = att_str * (1 - penalty)
			p1.goods["cannons"] = 0
		else:
			p1.goods["cannons"] -= att_ammo
		
		p2a_deficit = p2.goods["cannons"] - def_ammo
		if p2a_deficit < 0:
			print("%s has an ammo deficit of %s" % (p2.name, abs(p2a_deficit)))
			market.report.append("%s has an ammo deficit of %s" % (p2.name, abs(p2a_deficit)))
			penalty = abs(p2a_deficit/ ((def_ammo * 2) + 0.01))
			def_str = def_str * (1 - penalty)
			p2.goods["cannons"] = 0
		else:
			p2.goods["cannons"] -= def_ammo

		if p1o_deficit < 0:
			print("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
			market.report.append("%s has an oil deficit of %s" % (p1.name, abs(p1o_deficit)))
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
			market.report.append("%s has an oil deficit of %s" % (p2.name, abs(p2o_deficit)))
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
		market.report.append("%s losses: %s,  %s losses: %s \n" % (p1.name, att_losses, p2.name, def_losses))
		att_current_makeup = distribute_losses_amph(p1, att_losses, att_number_units_army, att_current_makeup)
		att_number_units_army = calculate_amphib_num_units(p1, att_current_makeup)
		def_number_units_army = distribute_losses(p2, def_losses, def_number_units_army)
		print("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
		market.report.append("%s has %s units remaining, %s has %s units remaining \n" % (p1.name, att_number_units_army, p2.name, def_number_units_army))
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

	self.attacker = attacker 
		self.defender = defender
		self.current_attacker_forces = []
		self.current_defender_forces = []
		self.current_attacker_strength = 0
		self.current_defender_strength = 0
		self.attack_manouver = 0
		self.defence_manouver = 0
		self.attacker_ammo_deficit = 0
		self.defender_ammo_deficit = 0
		self.attacker_oil_deficit = 0
		self.defender_oil_deficit = 0
		self.attacker_losses = 0
		self.defender_losses = 0





class Battle(object):
	def __init__(self, attacker, defender):
		self.attacker = attacker 
		self.defender = defender
		self.current_attacker_forces = []
		self.attacker_dogfight_roll = 0
		self.defender_dogfight_roll = 0
		self.att_fighters_lost = 0
		self.def_fighters_lost = 0
		self.att_recon = 0
		self.def_recon = 0

	def dogFight(self, players):
		AirAttRoll = uniform(1.0, 1.2)
		AirDefRoll = uniform(1.0, 1.2)
		attacker = players[self.attacker]
		defender = players[self.defender]
		AttOilNeeded = self.current_attacker_forces["fighter"] * attacker.fighter["oil_use"]
		DefOilNeeded = defender.military["fighter"] * defender.fighter["oil_use"]
		AttOilPenalty = attacker.oil_penalty(AttOilNeeded)
		DefOilPenalty = defender.oil_penalty(DefOilNeeded)

		AttAmmoNeeded = self.current_attacker_forces["fighter"] * attacker.fighter["ammo_use"]
		DefAmmoNeeded = defender.military["fighter"] * defender.fighter["ammo_use"]
		AttAmmoPenalty = attacker.ammo_penalty(AttAmmoNeeded)
		DefAmmoPenalty = defender.ammo_penalty(DefAmmoNeeded)

		AttAirStr = self.att_current_makeup["fighter"] * attacker.fighter["manouver"] * attacker.fighter["attack"] * AttRoll * AttAmmoPenalty * AttOilPenalty
		DefAirStr = defender.military["fighter"] * defender.fighter["manouver"] * defender.fighter["attack"] * DefRoll * DefAmmoPenalty * DefOilPenalty
		AttAirStrN = AttAirStr/(AttAirStr + DefAirStr)
		DefAirStrN = DefAirStr/(AttAirStr + DefAirStr)

		if AttAirStrN > DefAirStrN:
			percent_units_lost = 0.5 * (DefAirStrN/AttAirStrN)
		else:
			percent_units_lost = 0.5 * (AttAirStrN/DefAirStrN)

		total_losses = (self.att_current_makeup["fighter"] + defender.military["fighter"]) * percent_units_lost

		self.att_fighters_lost = total_losses * DefAirStrN
		self.def_fighters_lost = total_losses * AttAirStrN

		att_current_makeup["fighter"] -= min(self.att_fighters_losts, att_current_makeup["fighter"])
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
		AttAmmoNeeded = self.current_attacker_forces["artillery"] * attacker.artillery["ammo_use"]
		DefAmmoNeeded = defender.military["artillery"] * defender.artillery["ammo_use"]
		AttAmmoPenalty = attacker.ammo_penalty(AttAmmoNeeded)
		DefAmmoPenalty = defender.ammo_penalty(DefAmmoNeeded)

		AttArtStr = self.attacker_forces["artillery"] * attacker.artillery["attack"] * AttMod * AttAmmoPenalty * AttRoll
		DefArtStr = defender.military["artillery"] * defender.artillery["defend"] + DefMod * DefAmmoPenalty * DefRoll * defender.fortification 

		AttArtStrN = AttArtStr / (AttArtStr + DefArtStr)
		DefArtStrN = DefArtStr / (AttArtStr + DefArtStr)

		losses = self.artilleryPhaseLosses(players)
		self.att_art_losses = losses * DefArtStrN
		self.def_art_losses = losses * AttArtStrN

		self.attacker_forces = self.distribute_losses_amph(attacker, players, self.att_art_losses)
		self.distribute_losses(defender, players, self.def_art_losses)

		calculate_number_of_units(defender)
		calculate_amphib_num_units(attacker, self.attacker_forces)


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


	def landCombat(self, attacker_forces, players, market, relations):
		attacker = players[war.attacker]
		defender = players[war.defender]
		market.report.append("War has broken out between %s and %s ! \n" % (attacker.name, defender.name))
		cont = input()
		#Phase One: Recon
		if att_current_makeup["fighter"] > 0.2 and defender.militart["fighter"] > 0.2:
			dogFight(attacker, defender, att_current_makeup)
		AttRecon = attacker.recon()
		DefRecon = defender.recon()
		self.att_recon = AttRecon/(AttRecon + DefRecon)
		self.def_recon = DefRecon/(AttRecon + DefRecon) 
		#Phase Two: Artillery Barrage 
		self.artillery_phase(players)
		#Phase Three: Manouver 
		self.determine_manouver(players)




			att_manouver = calculate_amphib_man(attacker, att_current_makeup)
			def_manouver = calculate_manouver(defender)

			att_manouver_roll = uniform(1, 1.25)
			def_manouver_roll = uniform(1, 1.25)

