#Save

import jsonpickle
import simplejson as json
import os
import sys


from player_class import*
from minor_classes import*
from market import Market
from technologies import*
from AI import*
from human import*



def create_new_save_game(game_name, players, relations, market, provinces):
	jsonpickle.set_preferred_backend('simplejson')
	#save_name = input("Please provide a name of the save file \n")
	cur_path = os.path.dirname(__file__)
	save_path = os.path.join(cur_path, game_name)
	#save_path = os.path.relpath('../Saved Games/' + game_name, cur_path)
	

	#save_file = shelve.open(save_name)
	save_game(save_path, players, relations, market, provinces)
	return save_path
	

def save_game(save_path, players, relations, market, provinces):

	state = dict()
	jsonpickle.set_preferred_backend('simplejson')

	#save = shelve.open(file_name, flag = "n", writeback = False)
	for p, player in players.items():
		state[p] = player
	for re, rel in relations.items():
		state[re] = rel
	#state["relations"] = relations
	for p, prov in provinces.items():
		state[prov.name] = prov
	#for uc, unciv in uncivilized_minors.items():
	#	state[uc] = unciv
	state["market"] = market
	with open(save_path, 'w') as save:
		save.write(jsonpickle.encode(state, keys = True, warn = True))

	save.close()
	#save.close()

	#print("%s saved to disk \n" % (file_name))


def load_game(save_path):
	jsonpickle.set_preferred_backend('simplejson')
	
	#cur_path = os.path.dirname(__file__)
	#save_path = os.path.relpath('..\\Save Game\\' + file_name, cur_path)

	with open(save_path, 'r') as save:
		state = jsonpickle.decode(save.read(), keys = True)

	#print("State:")
	#for s in state:
	#	print(s)
	

	#save = shelve.open(file_name, writeback = False)
	#state = dict()
	#for k, v in save.items():
	#	state[k] = v
	#save.close()
	#save = shelve.open(file_name, flag = "n", writeback = False)

	return state

def compile_loaded_game(state):
	players = dict()
	provinces = dict()
	relations = dict()
	#uncivilized_minors = dict()
	market = Market 
	for k, v in state.items():
		if type(v) == AI or type(v) == Human:
			players[k] = v
		if type(v) == Province:
			provinces[k] = v
		if type(v) == Relation:
			relations[k] = v
		if k == "relations":
			relations = v
		if k == "market":
			market = deepcopy(v)
		if k == "provinces":
			provinces = v
	copy_state = deepcopy(list(state.keys()))
	for k in copy_state:
		del state[k]
	del state
	del copy_state

	initial = {"players": players, "provinces": provinces, "relations": relations, "market": market}
	return initial


