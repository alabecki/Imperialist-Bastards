#AI Turn
from AI import*
from player_class import*
from AI_foreign_affairs import*
from copy import deepcopy


def AI_turn(players, player, market, turn, uncivilized_minors, relations, provinces, globe):
	
	if len(player.provinces.keys()) < 1:
		return
	print("___________________________________________________________________")
	print("It is now %s's turn \n" % (player.name))

	print("___________________________________________________________________")


	player.calculate_resource_base()
	player.update_priorities(market)
	player.assign_priorities_to_provs()

	player.ai_increase_pop(market)
	player.ai_increase_pop(market)
	player.ai_increase_middle_class(market)

	player.AI_reset_POP()
	player.AI_assign_POP()
	player.calculate_resource_production()
	player.calculate_resource_need()
	player.calculate_resource_forecast()
	player.fulfill_needs(market)
	player.view_AI_inventory()

	player.use_chemicals()
	ai_decide_unciv_colonial_war(player, players, uncivilized_minors, provinces)
	ai_decide_ally_target(player, players, provinces)
	decide_rival_target(player, players, market, provinces, relations)
	ai_destablize(player, players)
	gain_cb(player, players, relations)
	worsen_relations(player, players, relations)
	attack_target(player, players, relations, provinces)
	player.use_culture(players)

	player.choose_technology()
	
	print("Decide Factory Production:")
	player.ai_decide_factory_productions(market)

	player.early_game(turn, market)
	#player.AI_set_objective(turn, market)
	player.develop_industry(market, globe)
	#player.attempt_objective(market)
	player.decide_build_navy(market)
	player.build_army(market)
	player.ai_increase_middle_class(market)
	player.develop_industry(market, globe)
	player.decide_build_navy(market)


	#if player.AP >= 1:
	#	player.AI_set_objective(turn, market)
	#	player.attempt_objective(market)


	player.AI_sell_surplus(market)

	player.check_stability(market)
	player.use_spice_stability()
	#player.supply_factories_with_material(market)
	
	player.spend_excess_cash(market)

			

	player.turn(globe)
