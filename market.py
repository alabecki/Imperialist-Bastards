
#Market Place
import player_class

class Market(object):
	def __init__ (self):

		self.gold = 3000

		self.resources = ["food", "cotton", "iron", "wood", "coal", "spice", "dyes", "rubber", "oil"]
		self.goods = ["parts", "cannons", "paper", "furniture", "clothing", "chemicals", "gear", "radio", "telephone", "fighter", "tank", "auto"]

		

		self.market = {
			"food": [],
			"cotton": [],
			"iron": [],
			"wood": [],
			"coal": [],
			"spice": [],
			"dyes": [],
			"rubber": [],
			"oil": [],
			"gold": [],

			"parts": [],
			"clothing": [],
			"cannons": [],
			"furniture": [],
			"paper": [],
			"chemicals": [],
			#"frigates": 0,
			#"iron_clad": 0,
			#"battle_ship": 0,
			"gear": [],
			"radio": [],
			"telephone": [],
			"fighter": [],
			"tank": [],
			"auto": []
		}

		self.global_factories = {

	
			"parts": 0,
			"clothing": 0,
			"furniture": 0,
			"paper": 0,
			"cannons": 0,
			"chemicals": 0,
			"gear": 0,
			"radio": 0,
			"telephone": 0,
			"fighter": 0,
			"auto": 0,
			"tank": 0
		}

		self.resources_sell_price = {
			1: 7,
			2: 7,
			3: 6,
			4: 6,
			5: 6,
			6: 6,
			7: 6,
			8: 5,
			9: 5,
			10: 5,
			11: 5,
			12: 5,
			13: 4,
			14: 4,
			15: 4,
			16: 4,
			17: 4,
			18: 3,
			19: 3,
			20: 3,
			21: 3,
			22: 3,
			23: 2,
			24: 2,
			25: 2,
			26: 2,
			27: 2,
			28: 2,
			#if more than 15 goes to 1
		}

		self.goods_sell_price = {
			1: 9,
			2: 9,
			3: 8,
			4: 8,
			5: 8,
			6: 8,
			7: 8,
			8: 7,
			9: 7,
			10: 7,
			11: 7,
			12: 7,
			13: 6,
			14: 6,
			15: 6,
			16: 6,
			17: 6,
			18: 5,
			19: 5,
			20: 5,
			21: 5,
			22: 5,
			23: 4,
			24: 4,
			25: 4,
			26: 4,
			27: 4,
			28: 3,
			29: 3,
			30: 3,


		#if more than 17 -> 1
	}

	#def buy_price(self, _type):
	#	if(_type in self.resources):
	#		amount = self.market[_type] - 1
	#		if(amount < 1):
	#			price = 100000
	#			return price
	#		elif(amount >= 29):
	#			price = 1
	#			return price
	#		else:
	#			price = self.resources_sell_price[amount]
	#		return price
	#	if(_type in self.goods):
	#		amount = self.market[_type]
	#		if(amount < 1):
	#			price = 10000
	#			return price
	#		if(amount >= 31):
	#			price = 2
	#			return price
	#		else:
	#			price = self.goods_sell_price[amount]
	#		return price


	def total_buy_price(self, _type, amount):
		print("Check")
		total = 0
		for i in range(amount):
			total += self.buy_price(_type)
			self.market[_type] -= 1
		return total



	def buy_item(self, _type, player):
		amount = int(input("How many %s do you wish to buy? \n" % (_type)))
		stock = self.market[_type]
		if(stock < amount):
			print("There are currently only %s %s available on the market\n " % (stock, _type))
			return
		else:
			price = self.total_buy_price(_type, amount)
			ok = input("%s %s will cost %s gold, is this okay? (y/n) \n" % (amount, _type, price ))
			if ok == "n":
				self.market[_type] += amount
				return
			else:
				if(player.resources["gold"] < price):
					print("You only have %s gold but %d %s costs %s gold \n" % (player.resources["gold"], amount,  _type, price))
					return
				else:
					player.resources["gold"] -= price
					self.gold += price
					#self.market[_type] -= amount
					if _type in self.resources:
						player.resources[_type] += amount
						print("You now have %s %s and %s gold \n" % (player.resources[_type], _type, player.resources["gold"]))
					else:
						if(_type == "chemicals"):
							player.goods["chemicals"] += 2*amount
							print("You now have %s %s and %s gold \n" % (player.goods[_type], _type, player.resources["gold"]))
							return
						else:
							player.goods[_type] += amount
							print("You now have %s %s and %s gold \n" % (player.goods[_type], _type, player.resources["gold"]))
							return

	


	def buy_price(self, kind, supply):
		#amount = self.calculate_access_to_good(player, kind)
		if(kind in self.resources):
			#amount = len(self.market[kind]) 
			if(supply < 1):
				price = 100000
				return price
			elif(supply > 28 and supply <= 32):
				price = 1
				return price
			elif(supply > 32):
				price = 0
				return price
			else:
				price = self.resources_sell_price[supply]
				return price
		if(kind in self.goods):
			#amount = self.market[kind]
			#print("Amount in Market: %s" % (amount))
			if supply < 1:
				return 100000
			mod = 1
			if kind == "radio" or kind == "telephone":
				print("Type is radio or telephone")
				mod = 1.25
			if kind == "fighter":
				mod = 4.75
			if kind == "tank":
				mod =  6.5
			if kind == "frigates" or kind == "iron_clad":
				mod = 3.2
			if kind == "auto":
				mod = 3.5
			
			if(supply < 1):
				price = 10 * mod
				return price
			if(supply >= 21 and supply < 26):
				price = 2 * mod
				return price
			if(supply >= 26 and supply <= 30):
				price = 1 * mod
				return price
			if(supply > 30):
				price = 0.5 * mod
				return price
			else:
				price = self.goods_sell_price[supply] * mod
			return price 

	#def sell_price(self, _type):
	#	if(_type in self.resources):
	#		amount = self.market[_type] 
	#		if(amount < 1):
	#			price = 7
	#			return price
	#		elif(amount > 21 and amount <= 26):
	#			price = 1
	#			return price
	#		elif(amount > 26):
	#			price = 0
	#			return price
	#		else:
	#			price = self.resources_sell_price[amount]
	#			return price
	#	if(_type in self.goods):
	#		amount = self.market[_type]
	#		#print("Amount in Market: %s" % (amount))
	#		mod = 1
	#		if _type == "radio" or _type == "telephone":
	#			print("Type is radio or telephone")
	#			mod = 1.25
	#		if _type == "fighter":
	#			mod = 3
	#		if _type == "tank":
	#			mod =  5.5
	#		if _type == "frigates" or _type == "iron_clad":
	#			mod = 3.2
	#		if _type == "auto":
	#			mod = 2.5
			
	#		if(amount < 1):
	#			price = 10 * mod
	#			return price
	#		if(amount >= 21 and amount < 26):
	#			price = 2 * mod
	#			return price
	#		if(amount >= 26 and amount <= 30):
	#			price = 1 * mod
	#			return price
	#		if(amount > 30):
	#			price = 0.5 * mod
	#			return price
	#		else:
	#			price = self.goods_sell_price[amount] * mod
	#		return price 

	def total_sell_price(self, _type, amount):  #Will need to redo when returnig to human
		print("Sell type: %s" % (_type))
		total = 0
		for i in range(amount):
			total += self.sell_price(_type)
			self.market[_type] += 1
		return total

	def sell_item(self, _type, player):  #Will need to redo when returnig to human
		amount = int(input("How many %s do you wish to sell? \n" % (_type)))
		price = self.total_sell_price(_type, amount)
		if price == 0:
			print("The market cannot buy any more of that resiurce at this time \n")
			return
		ok = input("Selling %s %s will make you %s gold, is this okay? (y/n) \n" % (amount, _type, price ))
		if ok == "n":
			self.market[_type] += amount
			return
		else:
			if(self.gold < price):
				print("The market has insufficient gold, try buying something first \n")
				return
			else:
				self.gold -= price
				player.resources["gold"] += price
				#self.market[_type] += amount
				if(_type in self.resources):
					player.resources[_type] -= amount
					print("You now have %s gold and %s %s \n" % (player.resources["gold"], player.resources[_type], _type))
					return
				elif(_type in self.goods):
					if _type == "chemicals":
						player.goods["chemicals"] -= 2 * amount
					else:
						player.goods[_type] -= amount
					print("You now have %s gold and %s %s \n" % (player.resources["gold"], player.goods[_type], _type))
					player.new_development += amount * 0.1
					return





	def show_market(self):
		print("Gold in market: %s \n" % (self.gold))
		for i in self.market:
			print("%s : amount %s price %s \n" % (i, len(self.market[i]), self.buy_price(i, len(self.market[i])) ))
		return
