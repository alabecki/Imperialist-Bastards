#Save

import shelve
import jsonpickle
import os
import sys


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

	state = dict()

	#save = shelve.open(file_name, flag = "n", writeback = False)
	for p, player in players.items():
		state[p] = player
	for re, rel in relations.items():
		state[re] = rel
	#state["relations"] = relations
	for p, prov in provinces.items():
		state[prov.name] = prov
	for uc, unciv in uncivilized_minors.items():
		state[uc] = unciv
	state["market"] = market

	with open(file_name, 'w') as save:
		save.write(jsonpickle.encode(state, keys = True, warn = True))

	save.close()
	#save.close()

	#print("%s saved to disk \n" % (file_name))


def load_game(file_name):
	with open(file_name, 'r') as save:
		state = jsonpickle.decode(save.read(), keys = True)

	#save = shelve.open(file_name, writeback = False)
	#state = dict()
	#for k, v in save.items():
	#	state[k] = v
	#save.close()
	#save = shelve.open(file_name, flag = "n", writeback = False)

	return state


