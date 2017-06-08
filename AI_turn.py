#AI Turn
from AI import*
from player_class import*

def AI_turn(player, market, turn):
	print("___________________________________________________________________")
	print("It is now %s turn \n" % (player.name))

	for k, v in player.goods_produced.items():
		player.goods_produced[k] = 0
		print("%s: %s " % (k, v))
	print("___________________________________________________________________")
	player.AI_reset_POP()
	player.AI_assign_POP()
	player.AI_set_objective(turn)
	player.attempt_objective(market)
	#player.ai_choose_build()
	#First, AI tries to fulfill its needs
	player.calculate_resource_production()
	player.calculate_resource_need()
	player.calculate_goods_need()
	player.calculate_resource_forecast()
	player.calculate_goods_forecast()
	player.view_AI_inventory()
	player.fulfill_needs(market)


	player.AI_sell_surplus(market)

	player.choose_technology()

	#player.ai_choose_build()


	player.turn()
