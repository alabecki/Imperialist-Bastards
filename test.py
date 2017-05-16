
#Market Place
import player_class


market_gold = 30

resources = {"food", "cotton", "iron", "wood", "coal", "spice"}
goods = {"parts", "cannons", "paper", "furniture", "clothing", "chemicals"}

market = {
	"food": 3,
	"cotton": 3,
	"iron": 3,
	"wood": 3,
	"coal": 3,
	"spice": 3,

	"parts": 0,
	"clothing": 0,
	"cannons": 0,
	"furniture": 0,
	"paper": 0,
	"chemicals": 0
}

resources_sell_price = {
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

good_sell_price = {
	0: 7,
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

def buy_price(_type):
	if(_type in resources):
		amount = market[_type] + 1
		if(amount < 1):
			price = 10
			if(_type == "spice"):
				price += 1
			return price
		if(amount >= 16):
			price = 1
			if(_type == "spice"):
				price += 1
			return price
		else:
			price = resources_sell_price[amount]
		if(_type == "spice"):
			price += 1
		return price 
	if(_type in goods):
		amount = market[_type] + 1
		if(amount < 1):
			price = 1000
		if(amount >= 19):
			price = 2
			return price
		else:
			price = goods_sell_price[amount]
		return price


def buy_item(_type):
	player = current_player
	price = buy_price(_type)
	if(player.gold < price):
		print("You only have %s gold but %s costs %s gold \n" % (player.gold, _type, price))
		return
	else:
		player.gold -= price
		marker.gold += price
		market[_type] -= 1
		player.resources[_type] += 1
		return
	if(_type in goods):
		amount = market[_type]
		if(amount < 1):
			print("There are currently no %s available on the market\n")
			return
		if(player.gold < price):
			print("You only have %s gold but %s costs %s gold \n" % (player.gold, _type, price))
			return
		else:
			player.gold -= price
			market[_type] -= 1
			if(_type == "chemicals"):
				player.goods["chemicals"] += 2
				return
			else:
				player.goods[_type] += 1
				return

def sell_price(_type):
	if(_type in resources):
		amount = market[_type]
		if(amount < 1):
			price = 6
			if(_type == "spice"):
				price += 1
				return price
		if(amount > 16):
			price = 1
			if(_type == "spice"):
				price += 1
			return price
		else:
			price = resources_sell_price[amount]
		if(_type == "spice"):
			price += 1
		return price 
	if(_type in goods):
		amount = market[_type] 
		if(amount < 1):
			price = 8
		if(amount > 19):
			price = 2
			return price
		else:
			price = goods_sell_price[amount]
		return price

def sell_item(_type):
	player = current_player
	price = sell_price(_type)
	if(market_gold < price):
		print("The market has insufficient gold, try selling something first \n")
		return
	else:
		market_gold -= price
		player.gold += price
		market[_type] += 1
		player.resources[_type] -= 1
		return
	if(_type in goods):
		amount = market[_type]
		if(market_gold < price):
			print("The market has insufficient gold, try selling something first \n")
			return
		else:
			player.gold += price
			market_gold -= price
			market[_type] += 1
			if(_type == "chemicals"):
				player.goods["chemicals"] -= 2
				return
			else:
				player.goods[_type] -= 1
				return


def show_market():
	print("Gold in market: %s \n" % (market_gold))
	for i in market:
		print("%s : amount %s : buy price %s sell price %s \n" % (i, market[i], buy_price(i), sell_price(i)))
	return

