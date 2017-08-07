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