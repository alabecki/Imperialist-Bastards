#AI Turn
from AI import*
from player_class import*
from AI_foreign_affairs import*
from copy import deepcopy


def AI_turn(players, player, market, turn, uncivilized_minors):
	
	if len(player.provinces) < 1:
		return
	print("___________________________________________________________________")
	print("It is now %s's turn \n" % (player.name))

	print("___________________________________________________________________")

	fact_set = deepcopy(player.factories)

	player.update_priorities(market)
	player.assign_priorities_to_provs()

	ai_destablize_empires(player, players)
	ai_decide_colonial_war(player, players, uncivilized_minors)
	player.use_culture(players):

	player.choose_technology()

	player.ai_increase_pop(market)
	player.ai_increase_pop(market)
	player.ai_increase_middle_class(market)
	player.AI_reset_POP()
	player.AI_assign_POP()
	player.calculate_resource_production()
	player.calculate_resource_need()
	player.calculate_resource_forecast()
	player.view_AI_inventory()
	player.fulfill_needs(market)
	
	print("Decide Factory Production:")
	player.ai_decide_factory_productions(market)

	player.AI_set_objective(turn, market)
	player.attempt_objective(market)
	player.early_game(turn, market)
	player.build_army()
	if player.AP >= 1:
		player.AI_set_objective(turn, market)
		player.attempt_objective(market)

	player.use_chemicals()

	player.AI_sell_surplus(market)

	player.check_stability(market)
	player.use_spice_stability()
	#player.supply_factories_with_material(market)
	
	player.spend_excess_cash(market)

	fact2_set = player.factories
	new_fact = [item for item in fact2_set if item not in fact_set]
	print("New factory:")
	for f in new_fact:
		print (f)
		for p in players.items():
			if type(player) == AI:
				if f != "cannons":
					print("Reducing factory priority after someone built one")
					player.build_factory_priority[f] -= 0.2

	player.turn()