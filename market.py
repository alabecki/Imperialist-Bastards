
#Market Place
import player_class

class Market(object):
	def __init__ (self):

		self.gold = 35

		self.resources = ["food", "cotton", "iron", "wood", "coal", "spice", "dyes"]
		self.goods = ["parts", "cannons", "paper", "furniture", "clothing", "chemicals"]

		self.market = {
			"food": 3,
			"cotton": 3,
			"iron": 3,
			"wood": 3,
			"coal": 3,
			"spice": 3,
			"dyes": 3,

			"parts": 0,
			"clothing": 0,
			"cannons": 0,
			"furniture": 0,
			"paper": 0,
			"chemicals": 0
		}

		self.resources_sell_price = {
			0: 5,
			1: 5,
			2: 5,
			3: 4,
			4: 4,
			5: 4,
			6: 4,
			7: 3,
			8: 3,
			9: 3,
			10: 3,
			11: 3,
			12: 2,
			13: 2,
			14: 2,
			15: 2
			#if more than 15 goes to 1
		}

		self.goods_sell_price = {
			1: 7,
			2: 6,
			3: 6,
			4: 6,
			5: 6,
			6: 5,
			7: 5,
			8: 5,
			9: 5,
			10: 5,
			11: 5,
			12: 4,
			13: 4,
			14: 4,
			15: 4,
			16: 3,
			17: 3,
			18: 3
		#if more than 17 -> 1
	}

	def buy_price(self, _type):
		if(_type in self.resources):
			amount = self.market[_type] + 1
			if(amount < 1):
				price = 10
				if(_type == "spice"):
					price += 1
				return price
			elif(amount >= 16):
				price = 1
				if(_type == "spice"):
					price += 1
				return price
			else:
				price = self.resources_sell_price[amount]
			if(_type == "spice"):
				price += 1
			return price
		if(_type in self.goods):
			amount = self.market[_type] + 1
			if(amount < 2):
				price = 1000
			if(amount >= 19):
				price = 2
				return price
			else:
				price = self.goods_sell_price[amount]
			return price


	def total_buy_price(self, _type, amount):
		total = 0
		for i in range(amount):
			total += self.buy_price(_type)
			self.market[_type] -= 1
		return total



	def buy_item(self, _type, player):
		amount = int(input("How many %s do you wish to buy? \n" % (_type)))
		if(_type in self.goods):
			stock = self.market[_type]
			if(stock < amount):
				print("There are currently onlys %s %s available on the market\n " % (stock, _type))
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

	def sell_price(self, _type):
		if(_type in self.resources):
			amount = self.market[_type]
			if(amount < 1):
				price = 6
				if(_type == "spice"):
					price += 1
					return price
			if(amount >= 16):
				price = 1
				if(_type == "spice"):
					price += 1
				return price
			else:
				price = self.resources_sell_price[amount]
			if(_type == "spice"):
				price += 1
			return price
		if(_type in self.goods):
			amount = self.market[_type]
			if(amount < 1):
				price = 8
				return price
			if(amount >= 19):
				price = 2
				return price
			else:
				price = self.goods_sell_price[amount]
			return price

	def total_sell_price(self, _type, amount):
		print("Sell type: %s" % (_type))
		total = 0
		for i in range(amount):
			total += self.sell_price(_type)
			self.market[_type] += 1
		return total

	def sell_item(self, _type, player):
		amount = int(input("How many %s do you wish to sell? \n" % (_type)))
		price = self.total_sell_price(_type, amount)
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
			print("%s : amount %s : buy price %s sell price %s \n" % (i, self.market[i], self.buy_price(i), self.sell_price(i)))
		return
