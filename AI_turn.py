# Turn
from AI import*
from player_class import*
from AI_foreign_affairs import*
from copy import deepcopy


def AI_turn(players, player, market, relations, provinces):
	
	if len(player.provinces.keys()) < 1:
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("%s has only one province!!!" % (player.name))
		return

	if type(player) == Human:
		return
	print("___________________________________________________________________")
	print("It is now %s's turn \n" % (player.name))

	print("___________________________________________________________________")

	if player.reputation < 0.65:
		player.reputation += player.midPOP["artists"]["number"] * 0.1


	player.AP += 1
	print("AP = %s" % (player.AP))


	player.calculate_access_to_goods(market)

	player.calculate_resource_base()
	player.update_priorities(market)



	player.calculate_resource_production()
	player.calculate_resource_need()
	player.calculate_resource_forecast()
	player.fulfill_needs(market, relations, players)
	player.view_AI_inventory()

	player.ai_increase_pop(market, relations, players)
	player.ai_increase_pop(market, relations, players)

	player.AI_reset_POP()
	player.AI_assign_POP()


	player.early_game(market, relations, players)
	player.ai_increase_middle_class(market, relations, players)


	player.assign_priorities_to_provs()
	
	player.choose_technology()

	player.develop_industry(market, relations, players)

	player.decide_build_navy(market, relations, players)

	print("Decide Factory Production!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:")
	player.ai_decide_factory_productions(market, relations, players)
	player.develop_industry(market, relations, players)

	player.build_army(market, relations, players)


	player.use_chemicals(market, relations, players)
	#attack_target(player, players, relations, provinces, market)
	decide_target(player, players, market, provinces, relations)
	worsen_relations(player, players, relations, provinces)
	gain_cb(player, players, relations)
	attack_target(player, players, relations, provinces, market)
	ai_bribe(player, players, relations)
	ai_decide_ally_target(player, players, provinces)



	count = 0
	while player.diplo_action >= 2 and count < 4:
		if player.rival_target == [] or len(player.CB) < 2:
			worsen_relations(player, players, relations, provinces)
		if len(player.embargo) > 0:
			improve = sample(player.embargo, 1)
			improve = improve[0]

			relata = frozenset({player.name, improve.name})
			player.diplo_action -=1
			if relata in relations.keys():
				relations[relata].relationship += min(1, 5/(improve.POP + 0.001))
				player.reputation += 0.02
			print("Improves relations with %s by %s" % (improve.name, min(1, 5/(improve.POP + 0.001))))

		damage_relations(player, players, relations)
		ai_improve_relations(player, players, relations)
		ai_destablize(player, players, relations)
		count += 1
	ai_embargo(player, players, relations)
	ai_lift_embargo(player, players, relations)


	player.use_culture(players)
	
	#player.AI_set_objective(turn, market)
	player.develop_industry(market, relations, players)
	#player.attempt_objective(market)

	player.ai_increase_middle_class(market, relations, players)
	player.develop_industry(market, relations, players)
	player.decide_build_navy(market, relations, players)


	#if player.AP >= 1:
	#	player.AI_set_objective(turn, market)
	#	player.attempt_objective(market)


	player.AI_sell_surplus(market, players)
	player.check_obsolete()
	player.check_stability(market, relations, players)
	player.use_spice_stability()
	#player.supply_factories_with_material(market)
	
	player.spend_excess_cash(market, players, relations)

			

	player.turn(market)
