#Save

import shelve

from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from AI import*
from human import*


def create_new_save_game(players, relations, uncivilized_minors, market, provinces):
	save_name = input("Please provide a name of the save file \n")
	save_file = shelve.open(save_name)
	save_game(save_name, players, relations, uncivilized_minors, market, provinces)

def save_game(file_name, players, relations, uncivilized_minors, market, provinces):
	save = shelve.open(file_name)

	for p, player in players.items():
		save[player.name] = player


	#save["players"] = players

	save["relations"] = relations

	for p, prov in provinces.items():
		save[prov.name] = prov

	#save["provinces"] = provinces

	for uc, unciv in uncivilized_minors.items():
		save[unciv.name] = unciv
	#save["uncivilized_minors"] = uncivilized_minors

	save["market"] = market


	#save["globe"]

	save.close()

	print("%s saved to disk \n" % (file_name))


def load_game(file_name):
	save = shelve.open(file_name)
	players = dict()
	relations = dict()
	uncivilized_minors = dict()
	provinces = dict()
	market = Market()
	provinces = dict()
	#globe = Globe
	state = dict()


	for k, v in save.items():
		#print(k)
	#	print(type(k))
	#	if type(v) == Player:
	#		print("Player?")
	#		players[v.name] = v
	#	if k == "players":
	#		players = v
	#	elif type(v) == Relation:
	#		relations = v
	#	elif type(v) == Uncivilized_minor:
	#		uncivilized_minors[v.name] = v
	#	elif type(v) == Market:
	#		market = v
	#	elif k == "market":
	#		market = v
	#	elif k == "provinces":
	#		provinces = v
	#	elif k == "uncivilized_minors":
	#		uncivilized_minors = v
	#	elif k == "relations":
	#		relations = v
	#	elif type(v) == Province:
	#		provinces[v.name] = v
		#elif type(v) == Globe:
		#	globe = v
		state[k] = v
	#state = {"players" : players, "relations": relations, "uncivilized_minors": uncivilized_minors, "market": market, "provinces": provinces}
	save.close()
	return state
