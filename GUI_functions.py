import sys
import operator
import gc
import os
from appJar import gui

from player_class import*
from human import*


def load_basic_widgets():
	#app.playSound("Grand March from Aida.wav", wait=False)
	app.startSubWindow("loading new game", modal = False)
	app.addLabel("nload", " Please wait while the game world is loaded... ")
	app.stopSubWindow()

	app.startSubWindow("Scenario_Choice", modal=True)
	app.addLabel("Scenario_Choice", "Which Scenario Would You Like to Play?")
	app.addRadioButton("Scen", "None")
	app.addRadioButton("Scen", "Semi-Historical")
	app.addRadioButton("Scen", "Fictional")
	#app.setRadioButton("Scen", "None", callFunction = True)
	#app.setRadioButtonFunction("Scen", gameChoice)   # call this funciton, whenever the RadioButton changes
	#app.setRadioButtonChangeFunction("Scen", gameChoice)
	app.addButton("Cont", scen_press)
	app.stopSubWindow()

	app.startSubWindow("Choose_Type", modal= True)
	app.addRadioButton("nation_type", "Major Power")
	app.addRadioButton("nation_type", "Minor Power")
	app.addRadioButton("nation_type", "Old Empire")
	app.addButton("Cont.", nation_type_press)
	app.stopSubWindow()


	app.startSubWindow("AI turn")
	app.addLabel("processing", "Please wait while the AI turns are processed" )
	app.stopSubWindow()

	app.startSubWindow("player_gains", modal = False)
	dummy = 0
	app.addLabel("RG", "Research Gain:")
	app.addLabel("CG", "Culture Gain:")
	app.addLabel("CPG", "Colonization Point Gain:")
	app.addLabel("DPG", "Diplomatic Point Gain:")
	app.stopSubWindow()


	app.startSubWindow("diplomacy", modal = False)
	app.startLabelFrame("dip")
	app.addLabel("other_player", "Relations with: ")
	app.addLabel("curr_relation", "Current Relations: ")
	app.stopLabelFrame()
	app.stopSubWindow()


	app.startSubWindow("saving", modal = True)
	app.addLabel("saveing label", "Saving Game ...")
	app.stopSubWindow()

	app.startSubWindow("chose_seller", modal = True)
	app.startLabelFrame("From whom you would like to buy?")
	app.addLabel("item_to_buy", "")
	app.addLabelOptionBox("Sellers", [""])
	app.addNamedButton("Select", "seller_select", _buy)
	app.stopLabelFrame()
	app.stopSubWindow()

	app.startSubWindow("chose_dev_type", modal = True)
	app.addLabel("ask_dev_type", "In what area will you develop your nation?")
	app.addOptionBox("get_dev_type", [])
	app.addNamedButton("Select", "dev_select", increase_dev_level)
	app.stopSubWindow()

	app.startSubWindow("choose doctrine", modal = True)
	app.addLabel("Please choose a military doctrine for your glorious army!")
	app.addOptionBox("get_mil_doct", [])
	app.addNamedButton("Select", "doct_select", acquire_doctrine)
	app.stopSubWindow()

	app.startSubWindow("amount_to_man", modal = True)
	app.addLabel("amnt_to_make", "How many would you like to produce?")
	app.addOptionBox("amount_to_man", [])
	app.addNamedButton("OK", "amount_good_select", manifacture_good_2)
	app.stopSubWindow()

	app.startSubWindow("Province to Integrate", modal = True)
	app.addLabel("prov_to_integrate", "Which Province would you like to culturally integrate?")
	app.addOptionBox("prov_to_int", [])
	app.addNamedButton("OK", "prov_to_integrate", integrate_culture_2)
	app.stopSubWindow()

	#app.startSubWindow("chem_growth", modal = True)
	#app.yesNoBox("chem_for_growth", "Increasing Your Pop again this turn will require 1 chemical", parent= None)
	#app.stopSubWindow()

def start_game_tread():
	app.thread(start_main_screen)
	print("Game should have started now \n")

def exit_game(btn):
	sys.exit(0)

def gui_save_game(btn):
	save_path = app.saveBox(title="Save Game", fileName= None, dirName = "/Saved Games", fileExt=".txt", fileTypes=None, asFile=None, parent=None)
	#save_path = save_path.name
	app.showSubWindow("saving")
	print("Saving....\n")
	save_game(save_path, players, relations, market, provinces)
	app.hideSubWindow("saving")

def player_type(_type):
	if kind == "Modern Major":
		print("Which Great Power will player " + str(i) + " control? \n")
		app.startSubWindow("nation_choice", modal = True)
		app.addLabelOptionBox("great powers", modern_major)
		app.setLabelOptionFunction("great_powers", select_great_power)
		app.stopSubWindow()

	if kind == "Modern Minor":
		print("Which Minor Modern nation will player " + str(i) + " control? \n")
		app.startSubWindow("nation_choice", modal = True)
		app.addLabelOptionBox("minor powers", modern_minors)
		app.setLabelOptionFunction("minor_powers", select_minor_power)
		app.stopSubWindow()

	if kind == "Old Empire":
		print("This feature is not yet implemented") 


def new_game(btn):
	load_basic_widgets()
	app.showSubWindow("Scenario_Choice")


def menuPress(command):
	if command == "New Game":
		first_choice = command
		print("first choice is new game")
		app.startSubWindow("Scen_Choice", modal=True)
		app.directoryBox(title= "Choose Scenario", dirName= "Scenarios", parent= "Scen_Choice")	
		app.addRadioButton("Scen", "Semi-Historical")
		app.addRadioButton("Scen", "Fictional")
		app.setRadioButtonFunction("Scen", gameChoice)   # call this funciton, whenever the RadioButton changes
		app.stopSubWindow()
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
		save_game(auto_save, players, relations, market, provinces)
	elif command == "Save as...":
		print("Please provide a name for the save")
		name = input()
		save_game(name, players, relations, market, provinces)
	elif command == "Exit Game":
		sys.exit(0)
	elif command == "Close":
		return
def good_material(_type):
	if _type in ["parts", "cannons"]:
		return ["iron", "coal"]
	if _type == "clothing":
		return ["cotton", "dyes"]
	if _type == "furniture":
		return ["wood", "cotton"]
	if _type == "paper":
		return []

def get_auto_save_name(bn):
	app.hideSubWindow("auto_save?")
	temp = app.getRadioButton("?auto_save?")
	if temp == "Yes":
		app.startSubWindow("auto_save_name", modal = True)
		app.addLabel("ask save name", "Please enter a name for your saved game:")
		app.addEntry("auto_save")
		app.addButton("Onwards!", create_auto_save)
		app.stopSubWindow()
		app.showSubWindow("auto_save_name")
	else:
		start_main_screen()
		#start_game_tread()

def ask_auto_save():
	app.startSubWindow("auto_save?", modal = True)
	app.addLabel("auto?", "Would you like to turn Auto Save on?")
	app.addRadioButton("?auto_save?", "Yes")
	app.addRadioButton("?auto_save?", "No")
	app.addButton("Ok then..", get_auto_save_name)
	app.stopSubWindow()

	app.showSubWindow("auto_save?")
