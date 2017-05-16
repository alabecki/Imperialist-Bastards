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
    		if(self.midPOP[_type] > 3.0):
    			print("You have already created as many %s a permitted \n")
    			return
    		if(self.midPOP[_type] < 2.0):
    			self.resources["spice"] -= 1.0
    			self.goods["furniture"] -= 1.0
    			self.midPOP["total"] += 1.0
    			self.midPOP[_type] += 1.0
    			self.freePOP -= 1.0
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
