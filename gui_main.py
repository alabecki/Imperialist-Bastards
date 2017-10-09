from appJar import gui

from pprint import pprint
from random import*
from itertools import product, combinations
import sys
import operator
import gc
import os

from name_generator import*
from player_class import*
from human import*
from minor_classes import*
from market import Market
from technologies import*
from combat import*
from start import*
from save import*
from AI import*
from human_turn import*
from AI_turn import*
from globe import*
#from GUI_functions import*
#import Scenarios.historical.Scenario 
#import Scenarios.BalanceScenario.Scenario
from Scenarios.historical.Scenario import* 
from Scenarios.BalanceScenario.Scenario import*




auto_save = ""
initial = dict()
players = dict()
market = dict()
provinces = dict()
relations = dict()


def AI_turnS(auto_save):
	global players, market, relations, provinces
	market.report = []
	market.turn +=1
	order = list(players.keys())
	shuffle(order)
	for k, v in market.market.items():
		for i in v:
			if i.owner not in players.keys():
				market.market[k].remove(i)
				del i
	for o in order:
		if o not in players.keys():
			continue
		if type(players[o]) == AI:
			AI_turn(players, players[o], market, relations, provinces)
		else:
			for k in players[o].goods_produced.keys():
				players[o].goods_produced[k] = 0
	gc.collect()
	
	if auto_save != "":

		#if market.turn % 2 == 1:
		app.showSubWindow("saving")
		print("Saving....\n")
		save_game(auto_save, players, relations, market, provinces)
		app.hideSubWindow("saving")
	for p in provinces.values():
		temp = p.owner
		owner = players[temp]
		app.setLabelBg(p.position, owner.colour)
		app.setLabelOverFunction(p.position, [show_prov, hide_prov])
		app.setLabel("name" + p.position, "Name: " + p.name + "  Owner: " + p.owner)
		app.setLabel("res" + p.position, "Resource: " + p.resource + "  Qual: " + str(p.quality))
		app.setLabel("dev" + p.position, "Development: " + str(p.development_level))
	app.setMessage("turn_report", market.report)

	human = app.getOptionBox("nation")
	player = players[human]
	app.setLabel("t1", "Turn:" +  str(market.turn))
	app.setLabel("l4", player.resources["gold"])
	app.setLabel("l5",  player.culture_points)
	app.setLabel("l6",  player.POP,)
	app.setLabel("l10", player.stability)
	app.setLabel("l11", player.diplo_action)
	app.setLabel("l12", player.freePOP)
	app.setLabel("l16", player.AP)
	app.setLabel("l17", player.research)
	app.setLabel("l18", player.numMidPOP)
	app.setLabel("l22", player.development_level)
	app.setLabel("l23", player.new_development)
	app.setLabel("l24", player.reputation)
	app.setLabel("l26", player.num_colonies)
	app.setLabel("l27", player.colonization)
	app.setLabel("l28", 1 + (player.num_colonies * 1.5))






def scen_press(btn):
	scen = app.getRadioButton("Scen")
	print("scen: %s" % (scen))
	app.hideSubWindow("Scenario_Choice")
	app.showSubWindow("Choose_Type")

def nation_type_press(btn):
	nation_type = app.getRadioButton("nation_type")
	print("__nation_type: %s" % (nation_type))
	app.hideSubWindow("Choose_Type")
	#app.showSubWindow("Choose_Nation")
	modern_major = []
	modern_minors = []
	old_empires = []
	old_minors = []
	scen = app.getRadioButton("Scen")
	print("__game type: %s" % (scen))
	if scen == "Semi-Historical":
		modern_major = ["England", "France", "Russia", "Germany", "Austria", "Italy", "Ottoman", "Spain", "Netherlands"]
		modern_minors = ["Denmark", "Sweden", "Portugal", "Two Sicilies", "Switzerland", "Saxony", \
		"Bavaria", "NorthGermany", "Papal States"]
		old_empires = ["China", "India", "Japan", "Persia"]
		old_minors = ["Korea", "Egypt", "Algeria", "Morocco", "Kazakhstan", "Philippines", "Dai Nam", "Siam", "Malaysia", \
		"Brunei", "Tunisia", "Libya", "Nejd", "Afghanistan", "Bengal", "Hyderabad", "Burma", "Cambodia", "Sulawesi", "Java"]
	if scen == "Fictional":
		modern_major = ["Bambaki", "Hyle", "Trope", "Sidero", "Isorropia", "Karbouno"]
		modern_minors = ["Situs", "Hythen", "Intero", "Kora", "Southo", "Cindra", "Estos", "Lian", "Bulgo" ]
		old_minors = ["Kaygree", "Kish", "Rabus", "Sparko", "Argos", "Mancha", "Gelder", "Porta", "Norra", \
		"Wego", "Arbaca", "Egaro"]	

	if nation_type == "Major Power":
		nation_type = modern_major
	if nation_type == "Minor Power":
		nation_type = modern_minors
	if nation_type == "Old Empire":
		nation_type = old_empires
	if scen != "None": 
		app.startSubWindow("Choose_Nation", modal = True)
		app.addLabelOptionBox("nation", nation_type)
		app.addButton("OK", nation_press)
		app.stopSubWindow()
		app.showSubWindow("Choose_Nation")
	#human_nation = app.getOptionBox("nation")

def nation_press(btn):
	player = app.getOptionBox("nation")
	scen = app.getRadioButton("Scen")
	global initial

	print("Human Nation %s" % (player))
	app.hideSubWindow("Choose_Nation")
	if scen == "Semi-Historical":
		initial = historical(player)
		print("Initial set_____________________________")
	if scen == "Fictional":
		initial = balance(player)
	global players
	global provinces
	global relations
	global market
	players = initial["players"]
	provinces = initial["provinces"]
	relations = initial["relations"]
	market = initial["market"]
	#player = players[player]
	print("(90 - Player: %s" % (player))
	#app.showSubWindow("auto_save?")
	ask_auto_save()


def ask_auto_save():
	app.startSubWindow("auto_save?", modal = True)
	app.addLabel("auto?", "Would you like to turn Auto Save on?")
	app.addRadioButton("?auto_save?", "Yes")
	app.addRadioButton("?auto_save?", "No")
	app.addButton("Ok then..", get_auto_save_name)
	app.stopSubWindow()

	app.showSubWindow("auto_save?")



def get_auto_save_name(bn):
	app.hideSubWindow("auto_save?")
	temp = app.getRadioButton("?auto_save?")
	if temp == "Yes":
		app.startSubWindow("auto_save_name", modal = True)
		app.addLabel("ask save name", "Please enter a name for your saved game:")
		app.addEntry("auto_save")
		app.addButton("Onwards!", saving)
		app.stopSubWindow()
		app.showSubWindow("auto_save_name")
		
	else:
		start_main_screen()



def saving(bn):
	global auto_save
	app.hideSubWindow("auto_save_name")
	app.startSubWindow("saving", modal = True)
	auto_save = app.getEntry("auto_save")
	if auto_save != "" and auto_save != None:
		save_game(auto_save, players, relations, market, provinces)
	app.addLabel("saveing label", "Saving Game ...")
	app.stopSubWindow()
	app.showSubWindow("saving")
	start_main_screen()

def next_turn(bn):
	global auto_save
	player = app.getOptionBox("nation")
	global players
	player = players[player]
	gains = player.turn(market)
	show_player_gains(gains)
	app.showSubWindow("player_gains")
	app.showSubWindow("AI turn")
	AI_turnS(auto_save)
	app.hideSubWindow("AI turn")

def show_player_gains(gains):
	app.setLabel("RG", "Research Gain: %s" % (gains[0]))
	app.setLabel("CG", "Culture Gain: %s" % (gains[1]))
	app.setLabel("CPG", "Colonization Point Gain: %s" % (gains[2]))
	app.setLabel("DPG", "Diplomatic Point Gain: %s" % gains[3])
	app.showSubWindow("player_gains")



def start_main_screen():
	global auto_save
	global players
	global market
	nation = app.getOptionBox("nation")
	player = players[nation]
	#app.hideSubWindow("auto_save_name")
	if auto_save != "":
		app.hideSubWindow("saving")
	app.showSubWindow("loading new game")
	#app.playSound("Grand March from Aida.wav", wait=False)
	
	app.startTabbedFrame("GameGUI")
	
	app.startTab("MainTab")
	app.setPadding(2)
	#app.setExpand("none")

	app.startPanedFrameVertical("info")
	app.setBg("khaki")
	#app.startFrame("info")
	#app.setExpand("all")
	#app.setFrameHeight("info", 20)
	
	#app.setExpand("none")
	app.setFont(10)

	app.addLabel("l0", player.name, 1, 1, 2)
	app.getLabelWidget("l0").config(font="Times 15 bold underline")
	app.setLabelFg("l0", player.colour)

	app.addLabel("t1", "Turn:" +  str(market.turn), 1, 4)
	app.getLabelWidget("l0").config(font="Times 15 bold underline")

	

	
	app.addLabel("l1", "Gold:", 2, 1)
	app.addImage("l1", "coins.gif", 2, 1)
	app.shrinkImage("l1", 2)
	app.setImageTooltip("l1", "Gold")
	app.addLabel("l2", "Cult Pts:", 3, 1)
	app.addImage("l2", "culture.gif", 3,1)
	app.shrinkImage("l2", 2)
	app.addLabel("l3", "POP:", 4,1)
	app.addImage("l3", "POP.gif", 4, 1)
	app.shrinkImage("l3", 2)
	app.shrinkImage("l3", 2)
	app.addLabel("l4", player.resources["gold"], 2, 2)
	app.addLabel("l5",  player.culture_points, 3, 2)
	app.addLabel("l6",  player.POP, 4, 2)
	app.addLabel("l7", "Stability", 2, 3)
	app.addImage("l7", "stability.gif", 2, 3)
	app.shrinkImage("l7", 2)
	app.addLabel("l8", "Diplomacy",  3, 3)
	app.addImage("l8", "diplo.gif", 3, 3)
	app.shrinkImage("l8", 2)
	app.addLabel("l9", "FreePOP", 4, 3)
	app.addImage("l9", "freePOP.gif", 4,3)
	app.shrinkImage("l9", 2)
	app.addLabel("l10", player.stability, 2, 4)
	app.addLabel("l11", player.diplo_action, 3, 4)
	app.addLabel("l12", player.freePOP, 4, 4)
	app.addLabel("l13", "AP", 2, 5)
	app.addImage("l13", "AP.gif", 2, 5)
	app.shrinkImage("l13", 2)
	app.addLabel("l14", "Scinece Pts", 3, 5)
	app.addImage("l14", "science.gif", 3, 5)
	app.shrinkImage("l14", 2)
	app.addLabel("l15", "Mid POP", 4, 5)
	app.addImage("l15", "midPOP.gif", 4, 5)
	app.shrinkImage("l15", 2)
	app.addLabel("l16", player.AP, 2, 6)
	app.addLabel("l17", player.research, 3, 6)
	app.addLabel("l18", player.numMidPOP, 4, 6)
	app.addLabel("l19", "Dev Level", 2, 7)
	app.addImage("l19", "dev_level.gif", 2, 7)
	app.shrinkImage("l19", 2)
	app.addLabel("l20", "New Industry", 3, 7)
	app.addImage("l20", "new_ind.gif", 3, 7)
	app.shrinkImage("l20", 2)
	app.addLabel("l21", "Reputation", 4, 7)
	app.addImage("l21", "reputation.gif", 4, 7)
	app.shrinkImage("l21", 2)
	app.addLabel("l22", player.development_level, 2, 8)
	app.addLabel("l23", player.new_development, 3, 8)
	app.addLabel("l24", player.reputation, 4, 8)

	app.addLabel("l25", "Colonial", 2, 10)
	app.addImage("l25", "flag.gif", 2, 10)
	app.shrinkImage("l25", 2)
	app.addLabel("l26", player.num_colonies, 2, 11)
	app.addLabel("l27", player.colonization, 2, 12)
	app.addLabel("l28", 1 + (player.num_colonies * 1.5), 2, 13)

	for i in range(1, 29):
		sz = "l" + str(i)
		app.setLabelHeight(sz, 2)
		app.setLabelWidth(sz, 2)
		app.setLabelRelief(sz, "ridge")
		app.setLabelAlign(sz, "left")


	app.addLabel
	app.addButton("turn", next_turn, 2, 16, 2)
	app.setButtonBg("turn", "dark green")
	app.setSticky("w")
	app.setPadding(2, 2)
	app.setInPadding(2,2)
	
	#app.startFrame("map")
	app.startPanedFrameVertical("map")
	

	app.startScrollPane("map_scroll")
	app.setExpand("all")

	#app.setFrameHeight("map", 18)
	
	#app.setSticky("sw")

	app.setExpand("all")

	#app.setExpand("none")
	global provinces

	for i in range(1, 19):
		for j in range(1, 33):
			nm = str(i)+ " " + str(j)
			#app.addLabel(nm, "", i, j)
			app.addButton(nm, press_prov, i, j)
			app.setButtonHeight(nm, 2)
			app.setButtonWidth(nm, 4)
			app.setButtonBg(nm , "blue")			
			#app.setLabelRelief(nm, "ridge")
			#app.setLabelHeight(nm, 2)
			#app.setLabelWidth(nm, 4)
			#app.setLabelBg(nm, "blue")
			#app.setLabelRelief(nm, "ridge")
			
	
	for p in provinces.values():
		temp = p.owner
		owner = players[temp]
		colour = owner.colour
		#print(p.name, p.owner, p.position, colour)
		#app.setLabelBg(p.position, colour)
		#app.setLabelOverFunction(p.position, [show_prov, hide_prov])
		#app.startSubWindow("sub" + p.position, modal = False)
		app.setButtonBg(p.position, colour)

		app.startSubWindow("ai"+ p.position, modal = False)
		app.addLabel("ai_name" + p.position, "Name: " + p.name + "  Owner: " + p.owner)
		app.addLabel("ai_res" + p.position, "Resource: " + p.resource + "  Qual: " + str(p.quality))
		app.addLabel("ai_dev" + p.position, "Development: " + str(p.development_level))
		app.stopSubWindow()
		if type(owner) == Human:
			app.startSubWindow("human" + p.position, modal = False)
			app.startLabelFrame("_" + p.name)
			app.setSticky("nesw")
			app.addLabel("res" + p.name, "Resource: ", 0, 1)
			app.addLabel("res_val" + p.name, p.resource, 0, 2)
			app.addLabel("qual"+ p.name, "Quality: ", 0, 3)
			app.addLabel("qual_val" + p.name, str(p.quality), 0, 4)
			app.addLabel("dev" + p.name, "Ind. Development: ", 1, 1)
			app.addLabel("dev_val" + p.name, str(p.development_level), 1, 2)
			app.addLabel("worked" + p.name, "Worked? ", 1, 3)
			app.addLabel("worked_val" + p.name, str(p.worked), 1, 4)
			app.addLabel("h_res" + p.position, "Resource: " + p.resource + "  Qual: " + str(p.quality), 2, 1)
			app.addLabel("h_dev" + p.position, "Development: " + str(p.development_level) + " Worked?: " + str(p.worked), 2, 2)
			
			app.addButton("Work "+p.name + "?", work_prov)
			if p.worked == True or owner.freePOP < 1: 
				app.disableButton("Work "+p.name + "?")
			else:
				app.enableButton("Work "+p.name + "?") 
			app.addButton("Free " + p.name + " Pop?", free_prov)
			if p.worked == False:
				app.disableButton("Free "+p.name + " Pop?")
			else:
				app.enableButton("Free " + p.name + " Pop?")
			app.addButton("Develop " + p.name, dev_prov)
			if owner.can_improve_prov(p) == False:
				app.disableButton("Develop " + p.name)
			else:
				app.enableButton("Develop " + p.name)
			app.stopLabelFrame()
			app.stopSubWindow()

			
	app.stopScrollPane()
	app.stopPanedFrame()
	app.startPanedFrameVertical("report_pane")
	app.startScrollPane("report")
	app.setBg("goldenrod3")

	app.setScrollFrameHeight("report", 16)
	app.setSticky("ne")
	app.addMessage("turn_report", "Report")
	app.setExpand("all")
	app.stopScrollPane()
	app.stopPannedFrame()

	app.stopPanedFrame()


	app.stopTab()


	app.stopTabbedFrame()

	app.hideSubWindow("loading new game")

def work_prov(btn):
	global players
	btn = btn[5:]
	btn = btn[:-1]
	human = app.getOptionBox("nation")
	player = players[human]
	player.work_p(btn)
	p = player.provinces[btn]
	app.setLabel("worked_val" + p.name, p.worked)
	app.setLabel("l12", player.freePOP)



def free_prov(btn):
	global players
	btn = btn[5:]
	btn = btn[:-1]
	human = app.getOptionBox("nation")
	player = players[human]
	player.free_p(btn)
	p = player.provinces[btn]
	app.setLabel("worked_val" + p.name, p.worked)
	app.setLabel("l12", player.freePOP)



def dev_prov(btn):
	global players
	btn = btn[5:]
	btn = btn[:-1]
	human = app.getOptionBox("nation")
	player = players[human]
	human.dev_p(btn)
	p = player.provinces[btn]
	app.setLabel("dev_val" + p.name, str(p.development_level))
	app.setLabel("l16", player.AP)
	app.setLabel("l23", player.new_development)







def press_prov(btn):
	global players
	global provinces
	human = app.getOptionBox("nation")
	player = players[human]
	for p in provinces.values():
		if btn == p.position:
			if p in player.provinces.values():
				app.showSubWindow("human" + p.position)
			else:
				app.showSubWindow("ai"+ p.position)

def show_prov(nm):
	print(nm)
	app.showSubWindow("sub" + nm)


def hide_prov(nm):
	app.hideSubWindow("sub" + nm)
	



def new_game(btn):
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



app = gui("IB", "960x600")
app.setFont("10", "arial")
app.setLocation("CENTER")
app.setExpand("all")
#app.setGeometry("fullscreen")

app.setImageLocation("Images")
app.setSoundLocation("Sounds")
app.setBgImage("Colonialism.png")
fileMenus = ["New Game", "Load Game", "Save", "Save as...", "Exit Game", "Close"]
app.createMenu("Menu")
app.addMenuItem("Menu", "New Game", func = new_game, shortcut=None, underline=-1)

app.playSound("Grand March from Aida.wav", wait=False)

app.startSubWindow("loading new game", modal = False)
app.addLabel("nload", " Please wait while the game world is loaded... ")
app.setLabelInPadding("nload", [2, 2])
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



app.go()