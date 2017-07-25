#Save

import shelve

from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from empire_class import*
from Old_Minor_Class import*


def create_new_save_game(players, relations, uncivilized_minors, market):
	save_name = input("Please provide a name of the save file \n")
	save_file = shelve.open(save_name)
	save_game(save_name, players, relations, uncivilized_minors, market)

def save_game(file_name, players, relations, uncivilized_minors, market):
	save = shelve.open(file_name)

	for p, player in players.items():
		save[player.name] = player

	save["relations"] = relations

	for p, prov in provinces.items():
		save[prov.name] = prov

	for uc, unciv in uncivilized_minors.items():
		save[unciv.name] = unciv

	save["market"] = market

	save["globe"]

	save.close()


def load_game(file_name):
	save = shelve.open(file_name)
	players = dict()
	relations = dict()
	uncivilized_minors = dict()
	market = Market()

	for k, v in save.items():
		if type(v) == Player:
			players[v.name] = v
		elif type(v) == Relation:
			relations = v
		elif type(v) == Uncivilized_minor:
			uncivilized_minors[v.name] = v
		elif type(v) == Market:
			market = v
	state = {"players" : players, "relations": relations, "uncivilized_minors": uncivilized_minors, "market": market}
	save.close()
	return state
