
#Market Place
from random import*

import player_class
from minor_classes import*


class Market(object):
	def __init__ (self):

		self.turn = 0

		self.defeated = []

		self.resources = ["food", "cotton", "iron", "wood", "coal", "spice", "dyes", "rubber", "oil", "/", "//", "///"]
		self.goods = ["parts", "cannons", "paper", "furniture", "clothing", "chemicals", "gear", "radio", "telephone", "fighter", "tank", "auto"]

		self.landBattle = 0
		self.seaBattle = 0 

		self.market_keys = ["food", "cotton", "iron", "wood", "coal", "spice", "dyes", "rubber", "oil", "parts", "cannons", "paper", "furniture", "clothing", "chemicals", "gear", "radio", "telephone", "fighter", "tank", "auto"]

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
			"auto": [],
			"/": [],
			"//": [],
			"///": [],
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
			31: 2,
			32: 2,
			32: 2,
			33: 2
	}

	food_production = dict()
	cotton_production = dict()
	wood_production = dict()
	gold_production = dict()
	coal_production = dict()
	iron_production = dict()
	spice_production = dict()
	rubber_production = dict()
	oil_production = dict()

	report = []

	market_report = " "

	def total_buy_price(self, _type, amount, supply):
		total = 0
		for i in range(amount):
			total += self.buy_price(_type, supply)
			supply -= 1
		return total

	def getSellers(self, _type, player):
		seller_list = []
		for i in self.market[_type]:
			pl = i.owner
			if i.owner in player.embargo:
				continue
			seller_list.append(i.owner)
		return seller_list

	def buy_item(self, other, _type, player, players, relations):			
		for i in self.market[_type]:
			#print("Owner: %s, Other: %s" % (i.owner.name, buy_from))
			if i.owner == other:
				#print("Removing item...%s" % (i.owner))
				self.market[_type].remove(i)
				del i
				break
		other = players[other]
		price = self.buy_price(_type, player.supply[_type])
		player.resources["gold"] -= price
		other.resources["gold"] += price
		other.new_development +=  0.2
		#self.market[_type].remove(s)
		player.supply[_type] -= 1
		relations[frozenset({other.name, player.name})].relationship + 0.015
		if _type in self.resources:
			player.resources[_type] += 1
		else:
			player.goods[_type] +=1
			other.new_development +=  0.2

		player.calculate_access_to_goods(self)


	def buy_price(self, kind, supply):
		#amount = self.calculate_access_to_good(player, kind)
		if(kind in self.resources):
			#amount = len(self.market[kind]) 
			if(supply < 1):
				price = 1000
				return price
			elif(supply > 28 and supply <= 33):
				price = 1
				return price
			elif(supply > 33):
				price = 0
				return price
			else:
				price = self.resources_sell_price[supply]
				return price
		if(kind in self.goods):
			#amount = self.market[kind]
			#print("Amount in Market: %s" % (amount))
			if supply < 1:
				return 1000
			mod = 1
			if kind == "clothing":
				mod = 1.2
			if kind == "radio" or kind == "telephone":
				mod = 1.25
			if kind == "fighter":
				mod = 4.75
			if kind == "tank":
				mod =  6.5
			if kind == "frigates" or kind == "iron_clad":
				mod = 3.2
			if kind == "auto":
				mod = 3.5
			if supply > 33:
				return 1 * mod
			
			price = self.goods_sell_price[supply] * mod
			return price 



	def sell_item(self, kind, player, players):  #Will need to redo when returnig to human

		#player = players[player]
		st = random()
		ID = player.name + str(st)
		new = MarketItem(ID, kind, player.name)
		self.market[kind].append(new)
		if kind in player.resources.keys():
			player.resources[kind] -= 1
		else:
			player.goods[kind] -= 1
	


	def show_market(self, player):
		print("Market _____________________________________________________________________________________________")
		for k1,k2 in zip(self.resources, self.goods):
			print( " %-12s: amount: %-6.1f (%-6.1f)  price: %-6.1f (%-6.1f)      %-12s: amount: %-6.1f (%-6.1f)  price: %-6.1f (%-6.1f)" % \
			(k1, len(self.market[k1]), player.supply[k1], self.buy_price(k1, len(self.market[k1])), self.buy_price(k1, player.supply[k1]), \
			k2, len(self.market[k2]), player.supply[k2], self.buy_price(k2, len(self.market[k2])), self.buy_price(k2, player.supply[k2]) ))
		#for i in self.market_keys:
		#	print("%s : amount %s price %s \n" % (i, player.supply[i], self.buy_price(i, player.supply[i]) ))
		print("_____________________________________________________________________________________________________")
		return
