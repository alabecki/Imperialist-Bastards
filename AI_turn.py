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


	player.calculate_access_to_goods(market)

	player.calculate_resource_base()
	player.update_priorities(market)
	
	player.assign_priorities_to_provs()

	player.ai_increase_pop(market, relations, players)
	player.ai_increase_pop(market, relations, players)
	player.ai_increase_middle_class(market, relations, players)

	player.AI_reset_POP()
	player.AI_assign_POP()
	player.calculate_resource_production()
	player.calculate_resource_need()
	player.calculate_resource_forecast()
	player.fulfill_needs(market, relations, players)
	player.view_AI_inventory()

	player.early_game(turn, market, relations, players)

	player.use_chemicals()
	ai_decide_unciv_colonial_war(player, players, uncivilized_minors, provinces)
	ai_decide_ally_target(player, players, provinces)
	decide_rival_target(player, players, market, provinces, relations)
	ai_destablize(player, players)
	gain_cb(player, players, relations)
	worsen_relations(player, players, relations)
	attack_target(player, players, relations, provinces)
	ai_improve_relations(player, players, relations)
	ai_bribe(player, players, relations)
	ai_embargo(player, players, relations)
	ai_lift_embargo(player, players, relations)




	player.use_culture(players)

	player.choose_technology()
	player.develop_industry(market, globe, relations, players)

	print("Decide Factory Production:")
	player.ai_decide_factory_productions(market, relations, players)

	#player.AI_set_objective(turn, market)
	player.develop_industry(market, globe, relations, players)
	#player.attempt_objective(market)
	player.decide_build_navy(market)
	player.build_army(market, relations, players)
	player.ai_increase_middle_class(market, relations, players)
	player.develop_industry(market, globe, relations, players)
	player.decide_build_navy(market)


	#if player.AP >= 1:
	#	player.AI_set_objective(turn, market)
	#	player.attempt_objective(market)


	player.AI_sell_surplus(market, players)
	player.check_obsolete()
	player.check_stability(market, relations, players)
	player.use_spice_stability()
	#player.supply_factories_with_material(market)
	
	player.spend_excess_cash(market, players, relations)

			

	player.turn(globe)
