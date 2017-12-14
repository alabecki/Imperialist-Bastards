import sys
import operator
import gc
import os
from appJar import gui

from gui_main.py import*
from player_class import*
from human import*

initial = dict()

def menuPress(command):
	if command == "New Game":
		first_choice = command
		#start_main_screen()
	elif command == "Load Game":
		app.openBox(title= "Load Game", dirName="game", fileTypes= None, asFile=True, parent=None)
		#name = input("What is the name of the save that you want to load? \n")
		print("Loading %s" % (name))
		state = load_game(name)
		#players = initial["players"]
		#print("Players:")
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
	elif command == "Save":
		save_game(auto_name, players, relations, market, provinces)
	elif command == "Save as...":
		print("Please provide a name for the save")
		name = input()
		save_game(name, players, relations, market, provinces)
	elif command == "Exit Game":
		sys.exit(0)
	elif command == "Close":
		return



def gameChoice(name):
	if name == "Semi-Historical":
		initial = historical()

	if name == "Fictional":
		initial = balance()


def start_main_screen():
	name = player.name
	color = "green"
	app.startFrame("info")
	app.setFrameHeight("info", 4)
	app.setFrameBg("info", "Khaki")
	app.setExpand("none")
	app.setFont(10)

	app.addLabel("l0", name, 1, 1, 3)
	app.getLabelWidget("l0").config(font="Times 14 bold underline")
	app.setLabelFg("l0", color)
	
	app.addLabel("l1", "Gold:", 2, 1)
	app.addImage("l1", "coins.png", 2, 1)
	app.shrinkImage("l1", 2)
	app.setImageTooltip("l1", "Gold")
	app.addLabel("l2", "Cult Pts:", 3, 1)
	app.addImage("l2", "culture.png", 3,1)
	app.shrinkImage("l2", 2)
	app.addLabel("l3", "POP:", 4,1)
	app.addImage("l3", "POP.png", 4, 1)
	app.shrinkImage("l3", 2)
	app.shrinkImage("l3", 2)
	app.addLabel("l4", "%.2f" % round(player.resources["gold"], 2), 2, 2)
	app.addLabel("l5", "%.2f" % round(player.culture_points, 2), 3, 2)
	app.addLabel("l6",  "%.2f" % round(player.POP, 2), 4, 2)
	app.addLabel("l7", "Stability", 2, 3)
	app.addImage("l7", "stability.png", 2, 3)
	app.shrinkImage("l7", 2)
	app.addLabel("l8", "Diplomacy",  3, 3)
	app.addImage("l8", "diplo.png", 3, 3)
	app.shrinkImage("l8", 2)
	app.addLabel("l9", "FreePOP", 4, 3)
	app.addImage("l9", "freePOP.png", 4,3)
	app.shrinkImage("l9", 2)
	app.addLabel("l10", "%.2f" % round(player.stability, 2), 2, 4)
	app.addLabel("l11", "%.2f" % round(player.diplo_points, 2), 3, 4)
	app.addLabel("l12", "%.2f" % round(player.freePOP, 2), 4, 4)
	app.addLabel("l13", "AP", 2, 5)
	app.addImage("l13", "AP.png", 2, 5)
	app.shrinkImage("l13", 2)
	app.addLabel("l14", "Scinece Pts", 3, 5)
	app.addImage("l14", "science.png", 3, 5)
	app.shrinkImage("l14", 2)
	app.addLabel("l15", "Mid POP", 4, 5)
	app.addImage("l15", "midPOP.png", 4, 5)
	app.shrinkImage("l15", 2)
	app.addLabel("l16", "%.2f" % round(player.AP, 2), 2, 6)
	app.addLabel("l17", "%.2f" % round(player.midPOP, 2), 3, 6)
	app.addLabel("l18", "%.2f" % round(player.freePOP, 2), 4, 6)
	app.addLabel("l19", "Dev Level", 2, 7)
	app.addImage("l19", "dev_level.png", 2, 7)
	app.shrinkImage("l19", 2)
	app.addLabel("l20", "New Industry", 3, 7)
	app.addImage("l20", "new_ind.png", 3, 7)
	app.shrinkImage("l20", 2)
	app.addLabel("l21", "Reputation", 4, 7)
	app.addImage("l21", "reputation.png", 4, 7)
	app.shrinkImage("l21", 2)
	app.addLabel("l22", "%.2f" % (player.development_level, 2), 8)
	app.addLabel("l23", "%.2f" % round(player.new_development, 2), 3, 8)
	app.addLabel("l24", "%.2f" % round(player.reputation, 2), 4, 8)

	app.addLabel("l25", "Colonial", 2, 10)
	app.addImage("l25", "flag.png", 2, 10)
	app.shrinkImage("l25", 2)
	app.addLabel("l26", player.num_colonies, 2, 11)
	app.addLabel("l27", int(player.colonization), 2, 12)
	app.addLabel("l28", 1 + (player.num_colonies * 1.5), 2, 13)


	for i in range(1, 29):
		sz = "l" + str(i)
		app.setLabelHeight(sz, 1)
		app.setLabelWidth(sz, 4)
		app.setLabelRelief(sz, "ridge")
	app.stopFrame()


	app.startFrame("map")
	app.setFrameHeight("map", 18)
	app.setFrameWidth("map", 30)

	app.startScrollPane("map_scroll")
	app.setExpand("none")

	for i in range(1, 25):
		for j in range(1, 33):
			nm = str(i)+ " " + str(j)
			app.addLabel(nm, "", i, j)
			app.setLabelHeight(nm, 2)
			app.setLabelWidth(nm, 3)
			app.setLabelBg(nm, "blue")
			app.setLabelRelief(nm, "ridge")
		#	app.getLabelWidget(nm).config(font= "Times 6")
	app.stopScrollPane()
	app.stopFrame()

	app.startFrame("links")
	app.setFrameHeight("links", 4)

	app.stopFrame()
