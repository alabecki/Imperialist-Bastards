#Back Up

def increase_pop(self):
  if(self.POP_increased > 1.0):
    print("You have already increased your population as much as possible this turn \n")
    return
  if(self.POP_increased == 1.0):
    if(self.goods["chemicals"] < 2):
      print("You need chemicals in order to increase your population again")
      return
    elif(self.goods["clothing"] < 1.0):
      print("You do not have enough clothing to increase your population \n")
      return
    else:
      self.POP += 1.0
      self.freePOP += 1.0
      self.goods["chemicals"] -= 2.0
      self.goods["clothing"] -= 1.0
      print("Your nation now has a population of %s with %s free POPS \n" % (self.POP), self.freePOP)
      return
  elif(self.resources["food"] < 1.0):
    print("You do not have enough food to increase your population \n")
    return
  elif(self.goods["clothing"] < 1.0):
    print("You do not have enough clothing to increase your population \n")
    return
  else:
    self.POP += 1.0
    self.freePOP += 1.0
    self.resources["food"] -= 1.0
    self.goods["clothing"] -= 1.0
    print("Your nation now has a population of %s with %s free POPS \n" % (self.POP), self.freePOP)
    return



    	def increase_middle_class(self):
    		if(self.freePOP < 1.0):
    			print("You do not have any free POPs")
    			return
    		elif(self.resources["food"] < 1.0):
    			print("You do not have any food \n")
    			return
    		elif(self.goods["furniture"] < 1.0):
    			print("You do not have any furniture \n")
    			return
    		elif(self.resources["spice"] < 1.0):
    			print("You do not have any spice \n")
    			return
    		_type = input("What kind of middle class POP would you like to create?: researchers generals  \
    			spies artists \n")
    		if(self.midPOP[_type] > 0.9):
    			print("You have already created as many %s a permitted \n")
    			return
    		if(self.midPOP[_type] < 2.0):
    			self.resources["spice"] -= 1.0
    			self.goods["furniture"] -= 1.0
    			self.numMidPOP += 0.2
    			self.midPOP[_type] += 0.2
    			self.freePOP -= 0.2
    			print("You now have %s %s and a total of %s middle class POPS \n" % (self.midPOP[_type], _type, self.midPOP["total"]))
    			return
    		else:
    			print("Since this will be a level 3 middle class POP, it will also cost 1 clothing \n")
    			if(self.goods["clothing"] < 1.0):
    				print("You do not have any clothing \n")
    				return
    			else:
    				self.resources["spice"] -= 1.0
    				self.goods["furniture"] -= 1.0
    				self.goods["clothing"] -= 1.0
    				self.midPOP["total"] += 1.0
    				self.midPOP["researchers"] += 1.0
    				self.freePOP -= 1
    				print("You now have %s %s and a total of %s middle class POPS \n" % (self.midPOP[_type], _type, self.midPOP[total]))
    				return


def attempt_objective(self, market):
    print("Attempting objective: - %s" % (self.objective))
    print("Has %s New Development Points \n" % (self.new_development))
    print("Has %s AP \n" % (str(self.AP)))
    if self.objective == 0:
      return
    if self.AP >= 1:
      if self.objective == 1:
        print("Wants to build frigate")
        flag = True
        if self.goods["cannons"] < 2:
          print("Wants cannons")
          decision = self.ai_decide_on_good("cannons", market)
          if decision != "buy":
            flag = False
          self.ai_obtain_good("cannons", decision, market)
        if self.resources["wood"] < 1:
          get = self.ai_buy("wood", 1, market)
          if get == "fail":
            flag = False
        if self.resources["cotton"] < 1:
          get = self.ai_buy("cotton", 1, market)
          if get == "fail":
            flag = False
        if self.freePOP < 0.2 and self.proPOP < 2:
          flag = False
        if self.freePOP < 0.2 and self.proPOP >= 2:
          self.proPOP -= 1
          self.freePOP += 1
        if flag == False:
            print("Cannot produce this this round")
            return
        else:
          self.ai_build_frigates()
          return
      if self.objective == 2:
        print("Wants to build factory")
        flag = True
        if self.goods["parts"] < 1:
          print("Wants machine parts")
          decision = self.ai_decide_on_good("parts", market)
          if decision != "buy":
            flag = False
          self.ai_obtain_good("parts", decision, market)
          #print("Flag: %s" % (flag))
        if self.resources["iron"] < 1:
          print("Wants to get iron")
          get = self.ai_buy("iron", 1, market)
          if get == "fail":
            flag = False
        if flag == False:
          return
        else:
          #priorities = (sorted(self.build_factory_priority.keys(), key=lambda x:x[1], reverse=True ))
          priorities = sorted(self.build_factory_priority, key=self.build_factory_priority.get, reverse = True)
        
          options = self.ai_factory_options()
          for o in options:
            for p in priorities:
              if p in options:
                self.ai_build_build_factory(p, market)
                return
      if self.objective == 4:
        print("Wants to improve province")
        flag = True
        if self.goods["parts"] < 1:
          print("Wants parts")
          decision = self.ai_decide_on_good("parts", market)
          if decision != "buy":
            flag = False
          self.ai_obtain_good("parts", decision, market)
        if self.resources["iron"] < 0.5:
          print("Wants iron")
          get = self.ai_buy("iron", 1, market)
          if get == "fail":
            flag = False
        if self.resources["wood"] < 1:
          print("Wants wood")
          get = self.ai_buy("wood", 1, market)
          if get == "fail":
            flag = False
        if flag == False:
          return
        else:
          #priorities = (sorted(self.improve_province_priority.items(), key=lambda x:x[1], reverse=True ))
          #print("priorities")
          priorities = sorted(self.improve_province_priority, key=self.improve_province_priority.get, reverse = True)
          #for p in priorities:
          # print(p)
          options = self.ai_improve_province_options()
          #print("options")
          #for o in options:
          # print (o)
          for p in priorities:
            if p in options:
            # print("Checking for %s province" % (p))
              if p == "improve_fortifications" and self.goods["cannons"] >= 1.5:
                self.ai_improve_fortifications()
                return
              elif p == "food":
                self.ai_develop_province("food")
                return
              if p == "iron":
                self.ai_develop_province("iron")
                return
              if p == "coal":
                self.ai_develop_province("coal")
                return
              if p == "wood":
                self.ai_develop_province("wood")
                return
              if p == "cotton":
                self.ai_develop_province("cotton")
                return
              if p == "gold":
                self.ai_develop_province("gold")
                return
              if p == "spice":
                self.ai_develop_province("spice")
                return
              if p == "dyes":
                self.ai_develop_province("dyes")
                return
              if p == "build_steam_ship_yard":
                self.ai_build_steam_ship_yard()
                return
      if self.objective == 3:
        print("Wants to build army")
        flag = True
        if self.goods["cannons"] < 2:
          print("Wants to get cannons")
          decision = self.ai_decide_on_good("cannons", market)
          if decision != "buy":
            print("Cannot acquire cannons this turn")
            return
          self.ai_obtain_good("cannons", decision, market)
          if flag  == False:
            print("cannot acquire cannons")
            return
        if self.freePOP < 0.2 and self.proPOP < 2:
          print("No people to raise army")
          return
        if self.freePOP < 0.2:
          self.proPOP -= 1
          self.freePOP += 1
        #priorities = (sorted(self.military_priority(), key=lambda x:x[1], reverse=True ))
        if "professional_armies" not in self.technologies:
          self.ai_build_irregulars()
        else:
          print("About to build army:...")
          priorities = sorted(self.military_priority, key=self.military_priority.get, reverse = True)
          for p in priorities:
            if p == "infantry":
              self.ai_build_infantry()
              return
            if p == "cavalry" and self.resources["food"] > 1:
              self.ai_build_cavalry()
              return
            if p == "artillery" and self.goods["cannons"] > 2:
              self.ai_build_artillery()
              return
            if p == "irregulars":
              self.ai_build_irregulars()
              return
            if p == "iron_clad":
              if "iron_clad" in self.technologies and self.goods["parts"] >= 1 and self.resources["iron"] >= 1 and self.steam_ship_yard == True:
                self.ai_build_ironclad()
                return
            #if p == "frigates":
            # if(self.resources["wood"] >= 1 and self.resources["cotton"] >= 1 and self.goods["cannons"] >= 1 and "iron_clad" not in self.technologies and self.freePOP >= 0.15):
            #   self.ai_build_frigates()
            #   return
      if self.objective == 5:
        flag = True
        if self.goods["cannons"] < 1.5:
          print("Wants cannons")
          decision = self.ai_decide_on_good("cannons", market)
          if decision != "buy":
            flag = False
          self.ai_obtain_good("cannons", decision, market)
        if self.resources["iron"] < 1:
          get = self.ai_buy("wood", 1, market)
          if get == "fail":
            flag = False
        if self.goods["parts"] < 1:
          decision = self.ai_decide_on_good("parts", market)
          if decision != "buy":
            flag = False
          self.ai_obtain_good("parts", decision, market)
        if self.freePOP < 0.2 and self.proPOP < 2:
          flag = False
        if self.freePOP < 0.2 and self.proPOP >= 2:
          self.proPOP -= 1
          self.freePOP += 1
        if flag == False:
            print("Cannot produce this this round")
            return        flag == False
            self.ai_obtain_good("cannons", decision, market)










        def AI_set_objective(self, turn, market):
    self.objective = 0
    print("Set AI Objective:")
    if self.military["frigates"] < 2 and "professional_armies" in self.technologies and "iron_clad" not in self.technologies:
      self.objective = 1
      return
    army = self.num_army_units()
    if army < self.numLowerPOP/2 and (self.freePOP > 0.2 or self.proPOP > 2):
      self.objective = 3
      return
    if self.new_development >= 1:
      opt = self.ai_improve_province_options()
      for o in opt:
        if len(opt) > 1 and "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1 :
          #print("Able to develop provice or build factory")
          if len(self.factories) >= self.number_developments and len(self.factories) >= 1:
            self.objective = 4
          else:
            pick = uniform(0, 1)
            if pick >=  0.35:
              self.objective = 2
              return
            else:
              self.objective = 4
              return
      if len(opt) > 1:
        self.objective = 4
        return
      if "high_pressure_steam_engine" in self.technologies and len(self.ai_factory_options()) >= 1:
        self.objective = 2
        return
    if self.military["frigates"] < 2 and "iron_clad" not in self.technologies:
      self.objective = 1
      return
    if self.try_middle_class(market) == True:
      self.try_middle_class(market)
      self.ai_increase_middle_class(market)
      self.objecive = 0
      return
    if self.military["frigates"] < 4 and self.num_colonies >= 1:
      if "iron_clad" not in self.technologies or self.steam_ship_yard == False:
        self.objective = 1
        return
      else:
        self.objective = 5
    if self.number_units < self.numLowerPOP:
      self.objective = 3
      return
    if "iron_clad" in self.technologies and self.military["iron_clad"] < self.num_colonies:
      self.objective = 3
      return
    else:
      self.ai_increase_middle_class(market)
      self.objective = 0
      return




  def determine_middle_class_need(self):
    requirement = ["paper"]
    if self.numMidPOP >= 2 and self.numMidPOP < 3:
      requirement = ["paper", "clothing"]
    if self.numMidPOP >= 3 and self.numMidPOP < 4:
      requirement = ["paper", "paper", "clothing"]
    if self.numMidPOP >= 4 and self.numMidPOP < 5:
      requirement = ["paper", "paper", "clothing", "furniture"]
    if self.numMidPOP >= 5 and self.numMidPOP < 6:
      requirement = ["paper", "paper", "clothing", "furniture", "chemicals"]
    if self.numMidPOP >= 6 and self.numMidPOP < 7:
      requirement = ["paper", "paper", "clothing", "furniture", "chemicals", "radio"]
    if self.numMidPOP >= 7 and self.numMidPOP < 8:
      requirement = ["paper", "paper", "clothing", "furniture", "chemicals", "radio", "telephone"]
    if self.numMidPOP > 8:
      requirement = ["paper", "paper", "clothing", "furniture", "chemicals", "radio", "telephone", "auto"]
    print("Mid class requirments:")
    for r in requirement:
      print(r)
    return requirement

  def check_mid_requirement(self, requirement):
    if self.resources["spice"] < 1:
      return False
    for r in requirement:
      if self.goods[r] < 1: 
        return False
    if self.numMidPOP >= 3 and self.goods["paper"] < 2:
      return False
    if self.freePOP < 0.5 and self.proPOP < 2:
      return False
    return True



    def determine_cost_increase_develop(self):
    if self.numMidPOP == 0:
      requirment = []
    if self.numMidPOP == 1:
      requirement = ["paper"]
    if self.numMidPOP == 2:
      requirement = ["furniture"]
    if self.numMidPOP == 3:
      requirement = ["paper"]
    if self.numMidPOP == 4:
      requirement = ["furniture"]
    if self.numMidPOP == 5:
      requirement = ["paper", "clothing"]
    if self.numMidPOP == 6:
      requirement = ["paper", "furniture"]
    if self.numMidPOP == 7:
      requirement = ["paper", "clothing"]
    if self.numMidPOP > 7 and self.numMidPOP <= 9
      requirement = ["paper", "furniture", "clothing"]
    if self.numMidPOP == 10:
      requirement = ["chemicals", "paper", "furniture"]
    if self.numMidPOP == 11:
      requirement = ["chemicals", "paper", "clothing"]
    if self.numMidPOP == 12:
      requirement = ["chemicals", "clothing", "furniture"]
    if self.numMidPOP == 13:
      requirement = ["paper", "furniture", "clothing"]
    if self.numMidPOP == 14:
      requirement = ["radio", "chemicals", "paper"]
    if self.numMidPOP == 15:
      requirement = ["radio", "funiture", "parts", "clothing"]
    if self.numMidPOP == 16:
      requirement = ["radio", "paper", "paper", "chemicals"]
    if self.numMidPOP == 17:
      requirement = ["telephone", "paper", "clothing", "parts"]
    if self.numMidPOP == 18:
      requirement = ["telephone", "radio", "furniture", "paper"]
    if self.numMidPOP == 19:
      requirement = ["telephone", "radio", "clothing", "paper"]
    if self.numMidPOP == 20:
      requirement = ["auto", "furniture", "paper", "chemicals"]
    if self.numMidPOP == 21:
      requirement = ["auto", "telephone", "clothing", "paper", "spice"]
    if self.numMidPOP == 22:
      requirement = ["auto", "radio", "spice", "furniture", "chemicals"]
    if self.numMidPOP == 23:
      requirement = ["auto", "telephone", "paper", "spice", "clothing"]
    if self.numMidPOP > 23:
      requirement = ["auto", "radio", "telephone", "spice", "paper", "clothing", "chemicals", "furniture"]



        if action == "1":
              if player.diplo_action < 1:
                print("You do not have any diplomatic points")
              elif player.colonization < 1 + (player.num_colonies * 1.5):
                print("You do not have enough colonization points")
              else:
                options = set()
                print("On what uncivilized nation would you like to declare war? \n")
                for uc, unciv in uncivilized_minors.items():
                  if unciv.harsh == True and ("medicine" in player.technologies or "breach_loaded_arms" in player.technologies):
                    continue
                  if len(unciv.provinces) < 1:
                    continue
                  print(unciv.name)
                  options.add(unciv.name)
                  other = " "
                  while other not in options:
                    other = input()
                  other = uncivilized_minors[other]
                  print("Which province would you like to take (there is likely only 1 option:")
                  for p in other.provinces.values():
                    print(p)
                  annex = " "
                  while annex not in other.provinces.keys():
                    annex = input()
                  annex = other.provinces[annex]
                  land = check_for_border(player, other)
                  if land == False:
                    print("Since you do not border %s, you must send your army by navy\n" % (other.name))
                    transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
                    if transport_limit < 4:
                      print("Your navy is not sufficient for carrying out an amphibious invasion!")
                    else:
                      amphib_prelude(player, other, market, relations, annex)
                      player.reputation -= 0.1
                  else:
                    print("Since we border %s, we may attack by land!" % (other.name))
                    combat(player, other, annex, market, relations)
                    player.reputation -= 0.1

            #War on old_minor or old_empire
            if action == "2":
              if player.colonization < 1 + (player.num_colonies * 1.5):
                print("You do not have enough colonization points")
              else:
                options = set()
                for cb in player.CB:
                  opponent = cb.opponent
                  opponent = players[opponent]
                  if opponent.type == "old_minor":
                    if len(opponent.provinces.keys()) != 0 and opponent.just_attacked <= 0:
                      options.add(cb)
                if len(options) == 0:
                  print("You do not currently have a CB on any old world minors")
                  return
                else:
                  other = " "
                  while other not in options:
                    print("For which province would you like to declare war? \n")
                    for o in options:
                      print(o.opponent + ": " o.province)
                  annex = input()
                  other = annex.owner
                  other = players[other]
                  annex = " "                 
                  land = player.check_for_border(other)
                  if land == False:
                    print("Since you do not border %s, you must send your army by navy\n" % (other.name))
                    transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
                    if transport_limit < 4:
                      print("Your navy is not sufficient for carrying out an amphibious invasion!")
                    else:
                      amphib_prelude(player, other, annex, relations, players)
                      player.reputation -= 0.1
                  else:
                    print("Since we border %s, we may attack by land!" % (other.name))
                    combat(player, other, annex, market, relations)
                    player.reputation -= 0.1
            
            if action == "3":
              if player.diplo_action < 1:
                print("You do not have any diplomatic points")
              elif player.colonization < 1 + (player.num_colonies * 1.5):
                print("You do not have enough colonization points")
              else:
                cb_keys = []
                for cb in player.CB:
                  cb_keys.append(cb.opponent)
                options = set()
                for p, pl in players.items():
                  if pl.type == "old_empire" and pl in cb_keys and pl.just_attacked <= 0:
                    options.add(pl.name)
                if len(options) == 0:
                  print("You do not have a CB on an Old World Empire at this time")
                else:
                  other = " "
                  while other not in options:
                    print("On what old world empire would you like to declare war? \n")
                    for o in options:
                      print(o)
                    other = input()
                  other = players[other]
                  annex = " "
                  while annex not in other.provinces.keys():
                    print("Which province do you seek to annex?\n")
                    for p, prov in other.provinces.items():
                      print(prov.name, prov.resource, prov.quality)
                    annex = input()
                  annex = other.provinces[annex]
                  land = player.check_for_border(other)
                  if land == False:
                    print("Since you do not border %s, you must send your army by navy\n" % (other.name))
                    amphib_prelude(player, other, annex, market, relationsplayers)
                    player.reputation -= 0.1
                  else:
                    print("Since we border %s, we may attack by land!" % (other.name))
                    combat(player, other, annex, market, relations)
                    player.reputation -= 0.1

            #War on Modern Nation
            if action == "4":
              c_options = set()
              cb_keys = []
              for cb in player.CB:
                cb_keys.append(cb.opponent)
              print("One which Major Power do you intend wage a colonial war?\n")
              for k, v in players.items():
                if v.type == "major":
                  if v.num_colonies > 0 and v in cb_keys and pl.just_attacked <= 0:
                    c_options.add(v.name)

              if len(c_options) == 0:
                print("There are currently no major powers on whom you may wage a colonial war \n")
              else:
                other = " "
                while other not in c_options:
                  print("On which Modern nation do you intend wage a colonial war?\n")
                  for co in c_options:
                    print(co)
                  other = input()
                p_options = set()
                other = players[other]
                for prov in other.provinces.values():
                  #print(prov.name, prov.colony)
                  #if prov.colony == True:
                    #print(prov.name, prov.resources, prov.quality)
                  p_options.add(prov.name)
                annex = " "
                while annex not in p_options:
                  print("The following provinces are colonies belonging to %s" % (other.name))
                  for po in p_options:
                    print(po)
                  annex = input()
                annex = provinces[annex]
                if player.check_for_border(other):
                  print("You may to capture %s by establishing naval domination or by invading %s and taking it as a prize for victory" % (annex.name, other.name))
                  landOrSea = " "
                  while landOrSea != "l" and landOrSea != "s":
                    landOrSea = input("Do you choose land (l) or sea (s)?")
                  if landOrSea == "s":
                    naval_battle(player, other, market, relations, annex)
                    player.reputation -= 0.2
                  else:
                    combat(player, other, annex, players, market , relations)
                else:
                  print("You do not neighbor %s and so you must capture %s by establishing naval \
                  dominance" % (other.name, annex.name))
                  naval_battle(player, other, market, relations, annex)
                  player.reputation -= 0.2

            if action == "5":
              a_options = set()
              cb_keys = []
              for cb in player.CB:
                cb_keys.append(cb.opponent)
              print("On which Major Power do you intend wage a minor war?\n")
              for k, v in players.items():
                if v.type == "major":
                  non_national = False
                  for p, prov in v.provinces.items():
                    if prov.culture != v.culture:
                      non_national = True
                  if non_national == True and v in cb_keys and pl.just_attacked <= 0:
                    a_options.add(v.name)
              if len(a_options) == 0:
                print("There are currently no major powers on whom you may wage a minor war \n")
              else:
                other = " "
                while other not in a_options:
                  print("On which Modern nation do you intend to wage a minor war?\n")
                  for ao in a_options:
                    print(ao)
                  other = input()
                p_options = set()
                other = players[other]
                if player.check_for_border(other):
                  for prov in other.provinces.values():
                    if prov.culture != other.culture and player.check_for_ground_invasion(prov, provinces):
                      print(prov.name, prov.resource, prov.quality)
                      p_options.add(prov.name)
                annex = " "
                while annex not in p_options:
                  print("The following are neighboring provinces that you may annex: \n")
                  for p in p_options:
                    print(p)
                  annex = input()
                annex = other.provinces[annex]
                if player.check_for_border(other) and player.check_for_ground_invasion(annex, provinces):
                  print("You may seek to capture neighboring %s from %s by land!" % (annex.name, other.name))
                  combat(player, other, annex, players, market, relations)
                  player.reputation -= 0.3

            if action == "6":
              cb_keys = []
              for cb in player.CB:
                cb_keys.append(cb.opponent)
              if player.military["tank"] < 1:
                print("Great Wars can only be waged once you have Tanks in your military")
              else:
                options = set()
                for k, v in players.items():
                  if v.type == "major" and v in cb_keys:
                    options.add(v.name)
                if len(options) == 0:
                  print("You cannot currently wage war on a Major Power")
                else:
                  other = " "
                  while other not in options:
                    print("On which Major Power would you like wage a Great War?")
                    for o in options:
                      print(o)
                    other = input()
                  other = players[other]
                  land = player.check_for_border(other)

                  annex = ""
                  for p, prov in other.provinces.items():
                    if prov.name == other.capital:
                      annex = prov

                  if land == False:
                    print("Since you do not border %s, you must send your army by navy\n" % (other.name))
                    transport_limit = (player.military["frigates"] + player.military["iron_clad"] + player.military["battle_ship"]) * 2 
                    if transport_limit < 4:
                      print("Your navy is not sufficient for carrying out an amphibious invasion!")
                    else:
                      amphib_prelude(player, other, market, relations, annex)
                      player.reputation -= 0.1
                  else:
                    print("Since we border %s, we may attack by land!" % (other.name))
                    combat(player, other, annex, players, market, relations)
                    player.reputation -= 0.1