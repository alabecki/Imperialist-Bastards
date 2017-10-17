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
human_player = ""


def AI_turnS(auto_save):
	global players, market, relations, provinces, human_player
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
		app.setButtonBg(p.position, owner.colour)
		app.setButtonFg(p.position, owner.colour)

	app.setMessage("turn_report", market.report)

	player = players[human_player]
	app.setLabel("t1", "Turn:" +  str(market.turn))

	app.setLabel("l4", "%.2f" % round(player.resources["gold"], 2))
	app.setLabel("l5", "%.2f" % round(player.culture_points, 2))
	app.setLabel("l6",  "%.2f" % round(player.POP, 2))
	app.setLabel("l10", "%.2f" % round(player.stability, 2))
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l12", "%.2f" % round(player.freePOP, 2))
	app.setLabel("l16", "%.2f" % round(player.AP, 2))
	app.setLabel("l17", "%.2f" % round(player.research, 2))
	app.setLabel("l18", "%.2f" % round(player.numMidPOP, 2))
	app.setLabel("l22", "%s" % (player.development_level))
	app.setLabel("l23", "%.2f" % round(player.new_development, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.setLabel("l26", player.num_colonies)
	app.setLabel("l27", "%.2f" % round(player.colonization))
	app.setLabel("l28", 1 + round((player.num_colonies * 1.5),2))





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
	global human_player
	human_player = app.getOptionBox("nation")

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
		app.addButton("Onwards!", create_auto_save)
		app.stopSubWindow()
		app.showSubWindow("auto_save_name")
		
	else:
		start_main_screen()

def create_auto_save(btn):
	app.hideSubWindow("auto_save_name")
	global auto_save, players, relations, market, provinces
	auto_save = app.getEntry("auto_save")
	if auto_save != "":
		auto_save = app.getEntry("auto_save")
		auto_save = create_new_save_game(auto_save, players, relations, market, provinces)
	start_main_screen()




def saving(bn):
	global auto_save

	app.hideSubWindow("auto_save_name")
	save_game(auto_save, players, relations, market, provinces)
	app.showSubWindow("saving")

def next_turn(bn):
	global auto_save, human_player
	player = human_player
	#player = app.getOptionBox("nation")
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
	global auto_save, players, human_player, market
	#load_basic_widgets()
	nation = human_player
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
	#app.shrinkImage("l1", 2)
	app.setImageTooltip("l1", "Gold")
	app.addLabel("l2", "Cult Pts:", 3, 1)
	app.addImage("l2", "culture.gif", 3,1)
	#app.shrinkImage("l2", 2)
	app.addLabel("l3", "POP:", 4,1)
	app.addImage("l3", "POP.gif", 4, 1)
	#app.shrinkImage("l3", 2)
	app.addLabel("l4", "%.2f" % round(player.resources["gold"], 2), 2, 2)
	app.addLabel("l5", "%.2f" % round(player.culture_points, 2), 3, 2)
	app.addLabel("l6",  "%.2f" % round(player.POP, 2), 4, 2)
	app.addLabel("l7", "Stability", 2, 3)
	app.addImage("l7", "stability.gif", 2, 3)
	#app.shrinkImage("l7", 2)
	app.addLabel("l8", "Diplomacy",  3, 3)
	app.addImage("l8", "diplo.gif", 3, 3)
	#app.shrinkImage("l8", 2)
	app.addLabel("l9", "FreePOP", 4, 3)
	app.addImage("l9", "freePOP.gif", 4,3)
	#app.shrinkImage("l9", 2)
	app.addLabel("l10", "%.2f" % round(player.stability, 2), 2, 4)
	app.addLabel("l11", "%.2f" % round(player.diplo_action, 2), 3, 4)
	app.addLabel("l12", "%.2f" % round(player.freePOP, 2), 4, 4)
	app.addLabel("l13", "AP", 2, 5)
	app.addImage("l13", "AP.gif", 2, 5)
	#app.shrinkImage("l13", 2)
	app.addLabel("l14", "Scinece Pts", 3, 5)
	app.addImage("l14", "science.gif", 3, 5)
	#app.shrinkImage("l14", 2)
	app.addLabel("l15", "Mid POP", 4, 5)
	app.addImage("l15", "midPOP.gif", 4, 5)
	#app.shrinkImage("l15", 2)
	app.addLabel("l16", "%.2f" % round(player.AP, 2), 2, 6)
	app.addLabel("l17", "%.2f" % round(player.research, 2), 3, 6)
	app.addLabel("l18", "%.2f" % round(player.numMidPOP, 2), 4, 6)
	app.addLabel("l19", "Dev Level", 2, 7)
	app.addImage("l19", "dev_level.gif", 2, 7)
	#app.shrinkImage("l19", 2)
	app.addLabel("l20", "New Industry", 3, 7)
	app.addImage("l20", "new_ind.gif", 3, 7)
	#app.shrinkImage("l20", 2)
	app.addLabel("l21", "Reputation", 4, 7)
	app.addImage("l21", "reputation.gif", 4, 7)
	#app.shrinkImage("l21", 2)
	app.addLabel("l22", "%s" % (player.development_level), 2, 8)
	app.addLabel("l23", "%.2f" % round(player.new_development, 2), 3, 8)
	app.addLabel("l24", "%.2f" % round(player.reputation, 2), 4, 8)

	app.addLabel("l25", "Colonial", 2, 10)
	app.addImage("l25", "flag.gif", 2, 10)
	#app.shrinkImage("l25", 2)
	app.addLabel("l26", player.num_colonies, 2, 11)
	app.addLabel("l27", "%.2f" % round(player.colonization), 2, 12)
	app.addLabel("l28", 1 + round((player.num_colonies * 1.5), 2), 2, 13)


	for i in range(1, 29):
		sz = "l" + str(i)
		app.setLabelHeight(sz, 1)
		app.setLabelWidth(sz, 1)
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
			app.setButtonFg(nm, "blue")			
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
		app.setButtonFg(p.position, colour)


		app.startSubWindow("ai"+ p.position, modal = False)
		app.startLabelFrame("*" + p.name)
		app.setSticky("nesw")
		app.addLabel("*res" + p.name, "Resource: ", 1, 0)
		app.addLabel("*qual"+ p.name, "Quality: ", 2, 0)
		app.addLabel("*dev" + p.name, "Ind. Development: ", 1, 1)
		app.addLabel("*worked" + p.name, "Worked? ", 2, 1)
		app.addLabel("*cult" + p.name, "Culture:", 2, 2)
		app.stopLabelFrame()
		app.stopSubWindow()

		if type(owner) == Human:
			app.startSubWindow("human" + p.position, modal = False)
			app.startLabelFrame("_" + p.name)
			app.setSticky("nesw")
			app.addLabel("res" + p.name, "Resource: ", 1, 0)
			app.addLabel("qual"+ p.name, "Quality: ", 2, 0)
			app.addLabel("dev" + p.name, "Ind. Development: ", 1, 1)
			app.addLabel("worked" + p.name, "Worked? ", 2, 1)
			app.addLabel("cult"+ p.name, "Culture: ", 2, 2 )
			
			app.addButton("Work "+p.name + "?", work_prov)
			
			app.addButton("Free " + p.name + " Pop?", free_prov)
			
			app.addButton("Develop " + p.name, dev_prov)
			
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
	app.stopPanedFrame()

	app.stopPanedFrame()


	app.stopTab()

	app.startTab("Market")
	app.setBg("khaki")


	app.startLabelFrame("Inventory")
	i = 1
	for k, v in player.resources.items():
		if k in ["gold", "/", "//"]:
			continue
		app.addLabel("i_" + k, " ",  i, 0)
		app.addImage("i_" + k, k+".gif", i, 0)
		app.setImageTooltip("i_" + k, k.title())
		app.shrinkImage("i_" + k, 2)
		app.addLabel("i_" + k + "_value", "%.2f" % round(player.resources[k], 2), i, 1)
		app.setLabelRelief(sz, "ridge")
		app.setLabelAlign(sz, "left")
		i = i + 1
	i = 1
	for k, v in player.goods.items():
		app.addLabel("i_" + k, " ", i, 2)
		app.addImage("i_" + k, k +".gif", i, 2)
		app.setImageTooltip("i_" + k, k.title())
		app.shrinkImage("i_" + k, 2)
		app.addLabel("i_" + k + "_value", "%.2f" % round(player.goods[k], 2), i, 3)
		app.setLabelRelief(sz, "ridge")
		app.setLabelAlign(sz, "left")
		i = i + 1
	app.endLabelFrame()

	app.startLabelFrame("Market")
	i = 1
	for r in market.resources:
		if r in ["/", "//", "///"]:
			continue
		app.addLabel(r + "_market", "  supply: %-6.1f (%-6.1f)  price: %-6.1f (%-6.1f)" % \
			(len(market.market[r]), player.supply[r], market.buy_price(r, len(market.market[r])), market.buy_price(r, player.supply[r])), i, 1)
		app.addImage(r + "_market_img", r + ".gif", i, 0)
		app.shrinkImage(r + "_market_img", 2)
		app.addNamedButton("Buy", r + "_buy", buy, i, 4)
		app.setButtonBg(r + "_buy", "red")
		stock = player.supply[r]
		price = market.buy_price(r, stock)
		if player.supply[r] < 1 or (player.resources["gold"] < price):
			app.disableButton(r + "_buy")
		else:
			app.enableButton(r + "_buy")
		app.addNamedButton("Sell", r + "_sell", sell, i, 5)
		app.setButtonBg(r + "_sell", "green")
		if player.resources[r] < 1:
			app.disableButton(r + "_sell")
		else:
			app.enableButton(r + "_sell")
		i = i + 1
	i = 0
	for g in market.goods:
		app.addLabel(g + "_market", "  supply: %-6.1f (%-6.1f)  price: %-6.1f (%-6.1f)" % \
			(len(market.market[g]), player.supply[g], market.buy_price(g, len(market.market[g])), market.buy_price(g, player.supply[g])), i, 8)
		app.addImage(g + "_market_img", g + ".gif", i, 7)
		app.shrinkImage(g + "_market_img", 2)
		app.addNamedButton("Buy", g + "_buy", buy, i, 11)
		app.setButtonBg(g + "_buy", "red")
		stock = player.supply[g]
		price = market.buy_price(g, stock)
		if player.supply[g] < 1 or (player.resources["gold"] < price):
			app.disableButton(g + "_buy")
		else:
			app.enableButton(g + "_buy")
		app.addNamedButton("Sell", g + "_sell", sell, i, 12)
		app.setButtonBg(g + "_sell", "green")
		if player.goods[g] < 1:
			app.disableButton(g + "_sell")
		else:
			app.enableButton(g + "_sell")
		i = i + 1


	app.stopLabelFrame()
	app.stopTab()

	app.stopTabbedFrame()

	app.hideSubWindow("loading new game")

def work_prov(btn):
	global players, human_player
	btn = btn[5:]
	btn = btn[:-1]
	#human = app.getOptionBox("nation")
	human = human_player
	player = players[human]
	player.work_p(btn)
	p = player.provinces[btn]
	app.setLabel("worked" + p.name, "Worked?:" + str(p.worked))
	app.setLabel("l12", player.freePOP)
	app.disableButton("Work "+p.name + "?")
	app.enableButton("Free "+p.name + " Pop?")




def free_prov(btn):
	global players, human_player
	btn = btn[5:]
	btn = btn[:-5]
	human = app.getOptionBox("nation")
	player = players[human_player]
	player.free_p(btn)
	p = player.provinces[btn]
	app.setLabel("worked" + p.name, "Worked?:" + str(p.worked))
	app.setLabel("l12", player.freePOP)
	app.enableButton("Work "+p.name + "?") 
	app.disableButton("Free " + p.name + " Pop?")


def dev_prov(btn):
	global players, human_player
	print("Button before: %s" % (btn))
	btn = btn[7:]
	print("Button after %s" % (btn))
	player = players[human_player]
	human.dev_p(btn)
	p = player.provinces[btn]
	app.setLabel("dev" + p.name, str(p.development_level))
	app.setLabel("l16", player.AP)
	app.setLabel("l23", player.new_development)
	if owner.can_improve_prov(p) == False:
		app.disableButton("Develop " + p.name)
	else:
		app.enableButton("Develop " + p.name)



def press_prov(btn):
	print(btn)
	global players
	global provinces, human_player
	player = players[human_player]
	for p in provinces.values():
		if btn == p.position:
			if p in player.provinces.values():
				show_human_province(p)
			else:
				show_AI_province(p)


def show_human_province(p):
	global human_player
	owner = players[human_player]
	app.showSubWindow("human" + p.position)
	app.setLabel("res" + p.name, "Resource: %s" % (p.resource) )
	app.setLabel("qual"+ p.name, "Quality: %s" % (p.quality))
	app.setLabel("dev" + p.name, "Ind. Development: %s" % (p.development_level))
	app.setLabel("worked" + p.name, "Worked? %s" % (p.worked))
	app.setLabel("cult" + p.name, "Culture: %s" %  (p.culture))


	if p.worked == True or owner.freePOP < 1: 
		app.disableButton("Work "+p.name + "?")
	else:
		app.enableButton("Work "+p.name + "?") 
	if p.worked == False:
		app.disableButton("Free "+p.name + " Pop?")
	else:
		app.enableButton("Free " + p.name + " Pop?")
	if owner.can_improve_prov(p) == False:
		app.disableButton("Develop " + p.name)
	else:
		app.enableButton("Develop " + p.name)

def show_AI_province(p):
	app.showSubWindow("ai"+ p.position)
	app.setLabel("*res" + p.name, "Resource: %s" % (p.resource) )
	app.setLabel("*qual"+ p.name, "Quality: %s" % (p.quality))
	app.setLabel("*dev" + p.name, "Ind. Development: %s" % (p.development_level))
	app.setLabel("*worked" + p.name, "Worked? %s" % (p.worked))
	app.setLabel("*cult" + p.name, "Culture: %s" %  (p.culture))



def show_prov(nm):
	print(nm)
	app.showSubWindow("sub" + nm)


def hide_prov(nm):
	app.hideSubWindow("sub" + nm)

def buy(btn):
	btn = btn[:-5]
	seller_list = getSellers(btn)
	app.changeOptionBox("Sellers", seller_list)
	app.setLabel("item_to_buy", btn)
	app.showSubWindow("chose_seller")

def _buy(btn):
	other = getOptionBox("Sellers")
	_type = getLabel("item_to_buy")
	global human_player, market, players, relations
	buy_item(market, other, _type, human_player, players, relations)
	app.setLabel("i_" + _type + "_value", " %.2f" % round(player.resources[k], 2))



def sell(btn):
	btn = btn[:-6]
	


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

def gui_load_game(btn):
	app.removeAllWidgets()
	save_path = app.openBox(title= "Load Game", dirName= "/Saved Games", fileTypes= None, asFile= True, parent=None)
	#save_path = str(save_path)
	save_path = save_path.name
	state = load_game(save_path)
	initial = compile_loaded_game(state)

	global players, relations, provinces, market
	players = initial["players"]
	relations = initial["relations"]
	provinces = initial["provinces"]
	market = initial["market"]
	human = ""
	for p in players.values():
		if type(p) == Human:
			global human_player
			human_player = p.name
			break
	start_main_screen()

def exit_game(btn):
	sys.exit(0)

def gui_save_game(btn):
	save_path = app.saveBox(title="Save Game", fileName= None, dirName = "/Saved Games", fileExt=".txt", fileTypes=None, asFile=None, parent=None)
	#save_path = save_path.name
	app.showSubWindow("saving")
	print("Saving....\n")
	save_game(save_path, players, relations, market, provinces)
	app.hideSubWindow("saving")




def load_basic_widgets():

	
	#app.playSound("Grand March from Aida.wav", wait=False)

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


app = gui("Imperialist Bastards", "960x600")
app.setFont("10", "arial")
app.setLocation("CENTER")
app.setExpand("all")
app.setBg("khaki", override=False, tint=False)
#app.setGeometry("fullscreen")
app.setImageLocation("Images")
app.setSoundLocation("Sounds")
app.setBgImage("IB.png")
app.growBgImage(2)


fileMenus = ["New Game", "Load Game", "Save", "Save as...", "Exit Game", "Close"]
app.createMenu("Menu")
app.addMenuItem("Menu", "New Game", func = new_game, shortcut=None, underline=-1)
app.addMenuItem("Menu", "Load Game", func = gui_load_game, shortcut = None, underline = -1)
app.addMenuItem("Menu", "Save Game", func= gui_save_game, shortcut = "S", underline = -1)
app.addMenuItem("Menu", "Exit", func = exit_game, shortcut = None, underline = -1)

app.go()