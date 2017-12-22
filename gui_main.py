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
from market import*
from technologies import*
from combat import*
from start import*
from save import*
from AI import*
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
PRODUCE = ""
OTHER = ""

manufacture = {
	"parts": {"iron": 0.67, "coal": 0.33},
	"cannons": {"iron": 0.67, "coal": 0.33},
	"paper": {"wood": 1.0},
	"clothing": {"cotton": 0.9, "dyes": 0.3},
	"furniture": {"wood": 0.67, "cotton": 0.33},
	"chemicals": {"coal": 1},
	"gear": {"rubber": 0.6, "iron": 0.2, "coal": 0.2},
	"radio": {"gear": 0.85, "wood": 0.15},
	"telephone": {"gear": 0.85, "wood": 0.15},
	"fighter": {"wood": 1, "gear": 1, "parts": 1, "cannons": 1.0},   # 2.5 
	"auto": {"rubber": 0.5, "gear": 1.0, "parts": 1.0, "iron": 0.5},		#2
	"tank": {"iron": 1.5, "cannons": 1.5, "rubber": 0.5, "gear": 1, "parts": 1}, 
	}

def update_gui():
	global players, human_player, market
	player = players[human_player]
	update_main_tab()
	update_market_tab()
	update_production_tab() 
	update_tech_tab()
	update_culture_tab()
	update_military_tab()
	#update_diplomacy_tab()

def update_market_tab():
	global players, human_player, market
	player = players[human_player]
	for k, v in player.resources.items():
		if k in ["gold", "/", "//"]:
			continue
		app.setLabel("i_" + k + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources[k]), len(market.market[k]), player.supply[k], \
			market.buy_price(k, len(market.market[k])), market.buy_price(k, player.supply[k])))

	for k, v in player.goods.items():
		app.setLabel("i_" + k + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods[k]), len(market.market[k]), player.supply[k], \
			market.buy_price(k, len(market.market[k])), market.buy_price(k, player.supply[k])))
	update_buy_button()
	update_sell_button() 

def update_main_tab():
	global players, human_player, market
	player = players[human_player]
	#Update Main Tab (except map)
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
	app.setLabel("l27", player.num_colonies)
	app.setLabel("l28", "%.2f / %.2f" % (round(player.colonization), 1 + round(player.num_colonies * 1.5)))
	
	if player.check_development() == False:
		app.disableButton("Develop")
	else:
		app.enableButton("Develop")

	if(player.POP_increased > 1):
		app.disableButton("POP UP")
	elif player.POP_increased == 1 and player.goods["chemicals"] < 1:
		app.disableButton("POP UP")
	elif player.resources["food"] < 1 or player.goods["clothing"] < 1:
		app.disableButton("POP UP")
	else:
		app.enableButton("POP UP")

	for p in player.provinces.keys():
		if player.check_if_prov_can_be_dev(p):
			if player.AP >= 1 and player.goods["parts"] >= 1 and player.resources["wood"] > 1:
				app.enableButton("Develop " + p)
			else:
				app.disableButton("Develop " + p)
		else:
			app.disableButton("Develop " + p)

def update_production_tab():
	global players, human_player, market
	player = players[human_player]
	if player.freePOP < 1:
		app.disableButton("add_pro_pop")
	else:
		app.enableButton("add_pro_pop")
	if player.proPOP < 1:
		app.disableButton("remove_pro_pop")
	else:
		app.enableButton("remove_pro_pop")
	update_production_gui()

def update_tech_tab():
	global players, human_player, market
	player = players[human_player]
	stab_rounds = round(player.stability * 2) / 2
	research_per_turn = 0.25 + ((player.developments["research"] + player.developments["management"]/6) * \
	government_map[player.government] * stability_map[stab_rounds])
	app.setLabel("research_status", "      Current Research Points: %s    Research Points Per Turn: %s      "  % (round(player.research, 2), round(research_per_turn, 2)))
	for k, v in technology_dict.items():
		if k in player.technologies:
			app.setLabelBg("tech_"+ k, "dark orange")
			app.disableButton("res_" + k)
		if k not in player.technologies:
			app.setLabelBg("tech_"+ k, "gold3")
			#tech = btn[4:]
			if  technology_dict[k]["requirement"] <= player.technologies and player.development_level >= technology_dict[k]["min_mid"] \
			and  technology_dict[k]["cost"] <= player.research:
				app.enableButton("res_" + k)
			else:
				app.disableButton("res_" + k)

def update_culture_tab():
	global players, human_player, market
	player = players[human_player]

	app.setLabel("num_officers", "%.2f" % player.developments["military"])
	app.setLabel("num_scientists", "%.2f" % player.developments["research"])
	app.setLabel("num_artists", "%.2f" % player.developments["culture"])	
	app.setLabel("num_bureaucrats", "%.2f" % player.developments["government"])
	app.setLabel("num_managers", "%.2f" % player.developments["management"])

	if player.culture_points < 1:
		app.disableButton("Increase Stability")
		app.disableButton("Export Culture")
	else:
		app.enableButton("Increase Stability")
		app.enableButton("Export Culture")	
	if player.culture_points < 1 or player.diplo_action < 1:
		app.disableButton("Improve Reputation")
	else:
		app.enableButton("Improve Reputation")
	others = player.check_for_non_accepted_cultures()
	if len(others) == 0 or player.culture_points < 1:
		app.disableButton("Integrate Culture")
	else:
		app.enableButton("Integrate Culture")
	if player.resources["spice"] < 1 or player.stability >= 3:
		app.disableButton("Consume Spice")
	else:
		app.enableButton("Consume Spice")


def update_diplomacy_tab():
	global players, human_player, relations
	player = players[human_player]
	count = 1
	for k, v in players.items():
		if k == player.name:
			continue
		relata = frozenset([player.name, k])
		app.setLabel("relations_with_" + k, "Relations: %.2f" % relations[relata].relationship)

		if player.diplo_action < 1 or relations[relata].relationship >= 3.0:
			app.disableButton("imp_rel_w" + k)
		else:
			app.enableButton("imp_rel_w" + k)
		if player.diplo_action < 1 or relations[relata].relationship <= - 3.0:
			app.disableButton("dmg_rel_w" + k)
		else:
			app.enableButton("dmg_rel_w" + k)
		if player.diplo_action < 1 or relations[relata].relationship >= -2.5:
			app.disableButton("CB_" + k)
		else:
			app.enableButton("CB_" + k)
		for cb in player.CB:
			if cb.opponent == k:
				app.disableButton("CB_" + k)

		if player.diplo_action < 1 or players[k].stability <= - 3.0:
			app.disableButton("destab" + k)
		else:
			app.enableButton("destab" + k)
		if player.resources["gold"] < 2.0 or relations[relata].relationship >= 3.0 or players[k].type == "major":
			app.disableButton("bribe" + k)
		else:
			app.enableButton("bribe" + k)
		if player.diplo_action < 1:
			app.disableButton("sab_rel" + k)
		else:
			app.enableButton("sab_rel" + k)
		if player.diplo_action < 1 or (player.name not in players[k].embargo and relations[relata].relationship > -1.5):
			app.disableButton("embargo" + k)
		else:
			app.enableButton("embargo" + k)
		count += 1


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
		#start_game_tread()

def create_auto_save(btn):
	app.hideSubWindow("auto_save_name")
	global auto_save, players, relations, market, provinces
	auto_save = app.getEntry("auto_save")
	if auto_save != "":
		auto_save = app.getEntry("auto_save")
		auto_save = create_new_save_game(auto_save, players, relations, market, provinces)
	#start_main_screen()
	start_game_tread()


def saving(bn):
	global auto_save

	app.hideSubWindow("auto_save_name")
	save_game(auto_save, players, relations, market, provinces)
	app.showSubWindow("saving")

def next_turn(bn):
	global auto_save, players, human_player
	#player = app.getOptionBox("nation")
	player = players[human_player]
	gains = player.turn(market)
	show_player_gains(gains)
	app.showSubWindow("player_gains")
	app.showSubWindow("AI turn")
	turn_thread()
	#AI_turnS(auto_save)
	app.hideSubWindow("AI turn")

def turn_thread():
	global auto_save
	app.thread(AI_turnS, auto_save)

def show_player_gains(gains):
	app.setLabel("RG", "Research Gain: %s" % (gains[0]))
	app.setLabel("CG", "Culture Gain: %s" % (gains[1]))
	app.setLabel("CPG", "Colonization Point Gain: %s" % (gains[2]))
	app.setLabel("DPG", "Diplomatic Point Gain: %s" % gains[3])
	app.showSubWindow("player_gains")


def start_main_screen():
	global auto_save, players, human_player, market, relations
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
	app.addImage("player_flag", player.name + ".gif", 1, 1)
	app.addLabel("l0", player.name, 1, 2, 2)
	app.getLabelWidget("l0").config(font="Times 15 bold underline")
	app.setLabelFg("l0", player.colour)

	app.addLabel("t1", "Turn:" +  str(market.turn), 1, 5)
	app.setLabelBg("t1", "peru")
	app.getLabelWidget("t1").config(font="Times 13 bold underline")


	app.addLabel("l1", "Gold:", 2, 1)
	app.addImage("l1", "coins.gif", 2, 1)
	#app.shrinkImage("l1", 2)
	app.setImageTooltip("l1", "Gold")
	app.addLabel("l2", "Cult Pts:", 3, 1)
	app.addImage("l2", "culture.gif", 3,1)
	app.setImageTooltip("l2", "Culture Points")
	#app.shrinkImage("l2", 2)
	app.addLabel("l3", "POP:", 4,1)
	app.addImage("l3", "POP.gif", 4, 1)
	app.setImageTooltip("l3", "Population")
	#app.shrinkImage("l3", 2)
	app.addLabel("l4", "%.2f" % round(player.resources["gold"], 2), 2, 2)
	app.addLabel("l5", "%.2f" % round(player.culture_points, 2), 3, 2)
	app.addLabel("l6",  "%.2f" % round(player.POP, 2), 4, 2)
	
	app.addLabel("l7", "Stability", 2, 3)
	app.addImage("l7", "stability.gif", 2, 3)
	app.setImageTooltip("l7", "Stability")
	#app.shrinkImage("l7", 2)
	app.addLabel("l8", "Diplomacy",  3, 3)
	app.addImage("l8", "diplo.gif", 3, 3)
	app.setImageTooltip("l8", "Diplomatic Points")
	#app.shrinkImage("l8", 2)
	app.addLabel("l9", "FreePOP", 4, 3)
	app.addImage("l9", "freePOP.gif", 4,3)
	app.setImageTooltip("l9", "Free POPs")

	#app.shrinkImage("l9", 2)
	app.addLabel("l10", "%.2f" % round(player.stability, 2), 2, 4)
	app.addLabel("l11", "%.2f" % round(player.diplo_action, 2), 3, 4)
	app.addLabel("l12", "%.2f" % round(player.freePOP, 2), 4, 4)
	app.addLabel("l13", "AP", 2, 5)
	app.addImage("l13", "AP.gif", 2, 5)
	app.setImageTooltip("l13", "Action Points")
	#app.shrinkImage("l13", 2)
	app.addLabel("l14", "Scinece Pts", 3, 5)
	app.addImage("l14", "science.gif", 3, 5)
	app.setImageTooltip("l14", "Science Points")

	#app.shrinkImage("l14", 2)
	app.addLabel("l15", "Mid POP", 4, 5)
	app.addImage("l15", "midPOP.gif", 4, 5)
	app.setImageTooltip("l15", "Middle POP")

	#app.shrinkImage("l15", 2)
	app.addLabel("l16", "%.2f" % round(player.AP, 2), 2, 6)
	app.addLabel("l17", "%.2f" % round(player.research, 2), 3, 6)
	app.addLabel("l18", "%.2f" % round(player.numMidPOP, 2), 4, 6)

	app.addLabel("l19", "Dev Level", 2, 7)
	app.addImage("l19", "dev_level.gif", 2, 7)
	app.setImageTooltip("l19", "Development Level")
	#app.shrinkImage("l19", 2)
	app.addLabel("l20", "New Industry", 3, 7)
	app.addImage("l20", "new_ind.gif", 3, 7)
	app.setImageTooltip("l20", "New Industry")
	#app.shrinkImage("l20", 2)
	app.addLabel("l21", "Reputation", 4, 7)
	app.addImage("l21", "reputation.gif", 4, 7)
	app.setImageTooltip("l21", "Reputation")

	#app.shrinkImage("l21", 2)
	app.addLabel("l22", "%s" % (player.development_level), 2, 8)
	app.addLabel("l23", "%.2f" % round(player.new_development, 2), 3, 8)
	app.addLabel("l24", "%.2f" % round(player.reputation, 2), 4, 8)

	app.addLabel("l25", "Colonial", 2, 10)
	app.addImage("l25", "flag.gif", 2, 10)
	app.setImageTooltip("l25", "Number of Colonies")
	
	app.addLabel("l26", "col_points", 3, 10)
	app.addImage("l26", "ship.gif", 3, 10)
	app.setImageTooltip("l26", "Colonial Points")
	app.shrinkImage("l26", 2)
	
	app.addLabel("l27", player.num_colonies, 2, 11)
	app.addLabel("l28", "%.2f / %.2f" % (round(player.colonization), 1 + round(player.num_colonies * 1.5)), 3, 11)

	for i in range(1, 29):
		sz = "l" + str(i)
		app.setLabelHeight(sz, 1)
		app.setLabelWidth(sz, 1)
		app.setLabelRelief(sz, "ridge")
		app.setLabelAlign(sz, "left")

	#app.addButton("Next Turn", next_turn, 2, 15)
	app.addImageButton("New Turn", next_turn, "turn.gif", 2, 15)
	app.setButtonTooltip("New Turn", "Next Turn")
	#app.setButtonBg("Next Turn", "dark green")
	app.setSticky("w")
	#app.setPadding(2, 2)
	#app.setInPadding(2,2)

	#app.addButton("POP UP", increase_population, 3, 15)
	#app.setButtonBg("POP UP", "orange")
	app.addImageButton("POP UP", increase_population, "pop_growth.gif", 3, 15)
	app.setButtonTooltip("POP UP", "Increase Population")
	if(player.POP_increased > 1):
		app.disableButton("POP UP")
	if player.POP_increased == 1.0 and player.goods["chemicals"] < 1:
		app.disableButton("POP UP")
	if player.resources["food"] < 1 or player.goods["clothing"] < 1:
		app.disableButton("POP UP")
	else:
		app.enableButton("POP UP")

	#app.addButton("Develop", dev_type, 4, 15)
	app.addImageButton("Develop", dev_type, "develop.gif", 4, 15)
	app.setButtonTooltip("Develop", "Increase Development Level")
	#app.setPadding(2, 2)
	#app.setInPadding(2,2)
	#app.setButtonBg("Develop", "dark violet")
	if player.check_development() == False:
		app.disableButton("Develop")
	else:
		app.enableButton("Develop")

	app.startPanedFrameVertical("map")
	
	app.startScrollPane("map_scroll")
	app.setExpand("all")
	app.setStretch("all")
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
		
	for p in provinces.values():
		temp = p.owner
		owner = players[temp]
		colour = owner.colour

		app.setButtonBg(p.position, colour)
		app.setButtonFg(p.position, colour)

		app.startSubWindow("ai"+ p.position, modal = False)
		app.setPadding([10, 10])
		app.startLabelFrame("*" + p.name)
		app.setSticky("nesw")
		app.addLabel(p.name, "Owner: ", 1, 0)
		print(owner.name)
		app.addImage(p.name, owner.name + ".gif", 1, 1)
		app.addLabel("*res" + p.name, "Resource: ", 2, 0)
		app.addLabel("*qual"+ p.name, "Quality: ", 3, 0)
		app.addLabel("*dev" + p.name, " Ind. Development: ", 2, 1)
		app.addLabel("*worked" + p.name, "Worked? ", 3, 1)
		app.addLabel("*cult" + p.name, "Culture:", 3, 2)
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
			
			#app.addButton("Work "+p.name + "?", work_prov)
			app.addImageButton("Work " + p.name +"?", work_prov, "work.gif", 3, 0)
			app.setButtonTooltip("Work " + p.name +"?", "Work " + p.name +"?")

			#app.addButton("Free " + p.name + " Pop?", free_prov)
			app.addImageButton("Free " + p.name + " Pop?", free_prov, "red_x.gif", 3, 1)
			app.setButtonTooltip("Free " + p.name + " Pop?", "Free " + p.name + " Pop?")
			
			app.addImageButton("Develop " + p.name, dev_prov, "train_tracks.gif", 3, 2)
			app.setButtonTooltip("Develop " + p.name, "Develop " + p.name)
			#app.addButton("Develop " + p.name, dev_prov)
			
			app.stopLabelFrame()
			app.stopSubWindow()
	
	app.stopScrollPane()
	app.stopPanedFrame()

	app.startPanedFrameVertical("report_pane")
	app.startScrollPane("report")
	app.setBg("goldenrod3")

	app.setSticky("ne")
	app.addMessage("turn_report", "Report")
	app.setStretch("all")
	app.stopScrollPane()
	app.stopPanedFrame()

	app.stopPanedFrame()

	app.stopTab()
	#######################################################################################################
	app.startTab("Market")

	app.setStretch("all")
	app.startPanedFrameVertical("market pan")
	app.startScrollPane("Market_Scroll")
	app.setBg("khaki")

	app.startLabelFrame("Inventory and Market")
	app.setStretch("none")
	app.setSticky("nw")

	i = 1

	app.addLabel("resources_", "Invent  |   Market   |   Price", 0, 1, 3, 1)
	for k, v in player.resources.items():
		if k in ["gold", "/", "//"]:
			continue
		app.addLabel("i_" + k, " ",  i, 0,)
		app.setLabelBg("i_" + k, "blue")
		app.addImage("i_" + k, k+".gif", i, 0)
		app.setImageTooltip("i_" + k, k.title())
		app.shrinkImage("i_" + k, 2)
		app.setLabelWidth("i_" + k, 1)
		app.addLabel("i_" + k + "_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources[k]), len(market.market[k]), player.supply[k], \
				market.buy_price(k, len(market.market[k])), market.buy_price(k, player.supply[k])), i, 1)
		app.setLabelRelief("i_" + k + "_value", "ridge")
		app.setLabelAlign("i_" + k + "_value", "left")
		app.addImageButton(k + "_buy", buy, "buy.gif", i, 5)
		#app.addNamedButton("Buy", k + "_buy", buy, i, 5)
		#app.setButtonBg(k + "_buy", "red")
		stock = player.supply[k]
		price = market.buy_price(k, stock)
		if player.supply[k] < 1 or (player.resources["gold"] < price):
			app.disableButton(k + "_buy")
		else:
			app.enableButton(k + "_buy")
		app.addImageButton(k + "_sell", sell, "sell.gif", i, 6)
		#app.addNamedButton("Sell", k + "_sell", sell, i, 6)
		#app.setButtonBg(k + "_sell", "green")
		if player.resources[k] < 1:
			app.disableButton(k + "_sell")
		else:
			app.enableButton(k + "_sell")
		i = i + 1
	i = 1
	app.addLabel("goods_", "Invent  |   Market   |   Price", 0, 9, 4, 1)
	for k, v in player.goods.items():
		app.addLabel("blank_" + k, "   ", i, 7)
		app.addLabel("i_" + k, " ", i, 8, 1, 1)
		app.addImage("i_" + k, k +".gif", i, 8, 1, 1)
		app.setImageTooltip("i_" + k, k.title())
		app.shrinkImage("i_" + k, 2)
		app.setLabelWidth("i_" + k, 1)
		app.addLabel("i_" + k + "_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods[k]), len(market.market[k]), player.supply[k], \
			market.buy_price(k, len(market.market[k])), market.buy_price(k, player.supply[k])), i, 9)
		app.setLabelRelief("i_" + k + "_value", "ridge")
		app.setLabelAlign("i_" + k + "_value", "left")
		app.addImageButton(k + "_buy", buy, "buy.gif", i, 13)
		#app.addNamedButton("Buy", k + "_buy", buy, i, 13)
		#app.setButtonBg(k + "_buy", "red")
		stock = player.supply[k]
		price = market.buy_price(k, stock)
		if player.supply[k] < 1 or (player.resources["gold"] < price):
			app.disableButton(k + "_buy")
		else:
			app.enableButton(k + "_buy")
		app.addImageButton(k + "_sell", sell, "sell.gif", i, 14)
		#app.addNamedButton("Sell", k + "_sell", sell, i, 14)
		#app.setButtonBg(k + "_sell", "green")
		if player.goods[k] < 1:
			app.disableButton(k + "_sell")
		else:
			app.enableButton(k + "_sell")
		i = i + 1
	app.stopLabelFrame()

	app.stopScrollPane()

	app.startPanedFrameVertical("market_report_pane")
	app.startScrollPane("market_report")
	app.setBg("goldenrod3")

	app.setSticky("ne")
	app.addMessage("turn_market_report", "Market Report")
	app.setStretch("all")
	app.stopScrollPane()
	app.stopPanedFrame()
	app.stopPanedFrame()

	app.stopTab()
	#######################################################################################################
	app.startTab("Production")
	app.setBg("gainsboro")
	app.setExpand("all")
	app.startScrollPane("Production")			

	app.startLabelFrame("Urban Workers")
	app.addLabel("num_urban_workers", "Number of Urban Workers %s" % (player.proPOP), 1, 1)
	app.addIconButton("add_pro_pop", add_pro_pop, "ARROW-4-UP", 1, 2)
	if player.freePOP < 1:
		app.disableButton("add_pro_pop")
	else:
		app.enableButton("add_pro_pop")
	app.addIconButton("remove_pro_pop", remove_pro_pop, "ARROW-4-DOWN", 1, 3)
	if player.proPOP < 1:
		app.disableButton("remove_pro_pop")
	else:
		app.enableButton("remove_pro_pop")
	app.stopLabelFrame()

	i = 2
	fact_options = player.factory_optons()
	app.startLabelFrame("Manufacture Goods")
	app.addLabel("production_"," Fact. Type     Level  Used?    Upgrade    Invent. Can Prod. Producing  Produce", 1, 0, 9)
	for f in player.goods.keys():
		app.addLabel("p_" + f, " ", i, 0, 1, 1)
		app.addImage("p_" + f, f +".gif", i, 0, 1, 1)
		app.shrinkImage("p_" + f, 2)
		app.setImageTooltip("p_" + f, f.title())
		app.addLabel("level_" + f, player.factories[f]["number"], i, 1, 1, 1)
		app.addLabel("used_" + f, player.factories[f]["used"], i, 2, 1, 1)
		app.addImageButton("upgrade_" + f, build_fact, "upgrade2.gif", i, 3, 1, 1)
		app.setButtonTooltip("upgrade_" + f, "Upgrade " + f)
		#app.addNamedButton("Upgrade", "upgrade_" + f, build_fact, i, 3, 1, 1)
		#app.setButtonBg("upgrade_" + f, "dark olive green")
		if f not in fact_options:
			app.disableButton("upgrade_" + f)
		else:
			enableButton("upgrade_" + f)
		app.addLabel("iamount_" + f, player.goods[f], i, 4, 1, 1)
		app.addLabel("producing_" + f, player.goods_produced[f], i, 6, 1, 1)
		app.addLabel("abprod_" + f, player.amount_can_manif(f), i, 5, 1, 1)
		app.addImageButton("produce_" + f, manifacture_good_1, "build.gif", i, 7, 1, 1)
		app.setButtonTooltip("produce_" + f, "Produce " + f)
		#app.addNamedButton("Produce", "produce_" + f, manifacture_good_1, i, 7, 1, 1)
		#app.setButtonBg("produce_" + f, "orange red")
		if player.amount_can_manif(f) < 1:
			app.disableButton("produce_" + f)
		else:
			app.enableButton("produce_" + f)
		i += 1
	#app.stopLabelFrame()

	#app.startLabelFrame("Infrastructure")

	app.addImage("fort", "fort.gif", 1, 9, 3, 3)
	app.addLabel("upgrade_fortification", "Fortification Level: %.2f" % player.fortification, 2, 12, 2, 1)
	#app.addNamedButton("Upgrade", "upgrade_fort", upgrade_fort, 2, 14, 1)
	app.addImageButton("upgrade_fort", upgrade_fort, "upgrade.gif", 2, 14, 1)
	app.setButtonTooltip("upgrade_fort", "Upgrade Fortifications")

	app.addImage("shipyard", "shipyard.gif", 4, 9, 3, 3)
	app.addLabel("upgrade_shipyard", "shipyard Level: %d" % player.shipyard, 5, 12, 2, 1)
	#app.addNamedButton("Upgrade", "upgrade_shipyard", upgrade_shipyard, 5, 14, 1)
	app.addImageButton("upgrade_shipyard", upgrade_shipyard, "upgrade.gif", 5, 14, 1)
	app.setButtonTooltip("upgrade_shipyard", "Upgrade shipyard")
	if player.goods["cannons"] < 1 or player.AP < 1 or (player.fortification >= 1.1 and "cement" \
		not in player.technologies) or player.fortification >= 1.2:
		app.disableButton("upgrade_fort")
	else:
		app.enableButton("upgrade_fort")
	
	if player.AP < 1 or player.new_development < 1 or player.resources["wood"] < 1 or player.goods["parts"] < 1:
		app.disableButton("upgrade_shipyard")
	elif player.shipyard == 1 and "ironclad" not in player.technologies:
		app.disableButton("upgrade_shipyard")
	elif player.shipyard == 2 and oil_powered_ships not in player.technologies:
		app.disableButton("upgrade_shipyard")
	else:
		app.enableButton("upgrade_shipyard")


	if player.AP < 1 or player.new_development < 1 or player.resources["wood"] < 1 or player.goods["parts"] < 1:
		app.disableButton("upgrade_shipyard")
	else:
		app.enableButton("upgrade_shipyard")
	#app.stopLabelFrame()

	#app.startLabelFrame("Chemical Conversion")
	app.addImage("chemical_frame", "chemical_conversion.gif", 8, 9, 2, 4)	
	app.addButton("Synthetic Dyes", synthetic_dyes, 8, 13, 2)
	app.addButton("Fertilize Soil", fertilize_soil, 9, 13, 3)
	app.addButton("Synthetic Rubber", synthetic_rubber, 10, 13, 3)
	app.addButton("Synthetic Oil", synthetic_oil, 11, 13, 3)
	#app.addImage("chemical_frame", "chemical_conversion.gif", 1, 5)
	#app.stopLabelFrame()

	if "synthetic_dyes" not in player.technologies or player.goods["chemicals"] < 1:
		app.disableButton("Synthetic Dyes")
	else:
		app.enableButton("Synthetic Dyes")
	if "fertilizer" not in player.technologies or player.goods["chemicals"] < 1:
		app.disableButton("Fertilize Soil")
	else:
		app.enableButton("Fertilize Soil")
	if "synthetic_rubber" not in player.technologies or player.goods["chemicals"] < 1 or player.goods["oil"] < 1:
		app.disableButton("Synthetic Rubber")
	else:
		app.enableButton("Synthetic Rubber")
	if "synthetic_oil" not in player.technologies or player.goods["chemicals"] < 3:
		app.disableButton("Synthetic Oil")
	else:
		app.enableButton("Synthetic Oil")
	
	app.stopLabelFrame()
	app.stopScrollPane()
	app.stopTab()
	######################################################################################################
	app.startTab("Technology")
	app.setExpand("all")
	app.setBg("chartreuse")
	app.startScrollPane("technologies")
	#app.startPanedFrame("tech_divider")
	app.startLabelFrame("Research Status")
	stab_rounds = round(player.stability * 2) / 2
	research_per_turn = 0.25 + ((player.developments["research"] + player.developments["management"]/6) * \
		government_map[player.government] * stability_map[stab_rounds])
	app.addLabel("research_status", "      Current Research Points: %.2f    Research Points Per Turn: %.2f      "  % (round(player.research, 2), round(research_per_turn, 2)), 1, 1, 8, 2)
	app.stopLabelFrame()

	#app.startScrollPane("technologies")
	app.startLabelFrame("Technology List")
	#app.addImage()
	app.add
	row = 1
	for k, v in technology_dict.items():
		app.addLabel("tech_" + k, "%s: requires: %s, cost: %.2f, min dev: %d" % \
		 (k, v["requirement"], v["cost"], v["min_mid"]), row, 1, 6, 1)
		app.addImageButton("sel_" + k, select_technology, "report.gif", row, 7, 1, 1)
		app.addImageButton("res_" + k, research_technology, "research.gif", row, 8, 1, 1)
		app.setButtonTooltip("sel_" + k, "Get Description")
		app.setButtonTooltip("res_" + k, "Research " + k)
		#app.addNamedButton("Select", "sel_" + k, select_technology, row, 7, 1, 1)
		#app.addNamedButton("Research", "res_" + k, research_technology,  row, 8, 1, 1)
		if k not in player.technologies:
			app.setLabelBg("tech_"+ k, "gold3")
			if  technology_dict[k]["requirement"] <= player.technologies and player.development_level >= technology_dict[k]["min_mid"] \
			and  technology_dict[k]["cost"] <= player.research:
				app.enableButton("res_" + k)
			else:
				app.disableButton("res_" + k)
		else:
			app.setLabelBg("tech_"+ k, "dark orange")
			app.disableButton("res_" + k)
		row += 1
	app.stopLabelFrame()
	app.stopScrollPane()
	#app.startPanedFrame("Tech Descriptions")
	
	app.startLabelFrame("  ")
	app.setSticky("nw")
	app.addImage("tech_image", "default_tech_pic.gif", 1, 1)
	app.setSticky("ne")
	app.startLabelFrame("Technology Description")
	app.addMessage("tech_description", "    Technology Descriptions go here    ", 1, 2)
	app.setMessageBg("tech_description", "DarkSeaGreen1")
	app.stopLabelFrame()
	app.stopLabelFrame()
	#app.stopScrollPane()

	app.stopTab()
	####################################################################################################
	app.startTab("Culture")
	app.setExpand("none")
	app.setBg("MediumOrchid2")

	app.startLabelFrame("Demographics:")
	app.addImage("officers", "officer.gif", 0, 0)
	app.setImageTooltip("officers", "Officers")
	app.addLabel("num_officers", "%.2f" % player.developments["military"], 1, 0)
	app.addImage("scientists", "scientist.gif", 0, 1)
	app.setImageTooltip("scientists", "Scientists")
	app.addLabel("num_scientists", "%.2f" % player.developments["research"], 1, 1)
	app.addImage("artists", "artist.gif", 0, 2)
	app.setImageTooltip("artists", "Artists")
	app.addLabel("num_artists", "%.2f" % player.developments["culture"], 1, 2)
	app.addImage("bureaucrats", "bureaucrat.gif", 0, 3)
	app.setImageTooltip("bureaucrats", "Bureaucrats")
	app.addLabel("num_bureaucrats", "%.2f" % player.developments["government"], 1, 3)
	app.addImage("managers", "manager.gif", 0, 4)
	app.setImageTooltip("managers", "Managers")
	app.addLabel("num_managers", "%.2f" % player.developments["management"], 1, 4)
	app.stopLabelFrame()

	app.startLabelFrame("Cost For Next Development Level")
	requirements = player.determine_middle_class_need()
	for r in requirements:
		count = 1
		ID = uniform(2, 3)*count
		img = r + ".gif"
		app.addImage(ID, img, 1, count)
		app.shrinkImage(ID, 2)
		count += 1
	app.stopLabelFrame()
	
	app.startLabelFrame("Culture Commands")
	app.addImage("culture_tab", "culture_tab.gif", 1, 0, 1, 5)
	app.addButton("Increase Stability", increase_stability, 1, 2, 3)
	app.addButton("Improve Reputation", improve_reputation, 2, 2, 3)
	app.addButton("Integrate Culture", integrate_culture, 3, 2, 3)
	app.addButton("Export Culture", export_culture, 4, 2, 3)
	app.addButton("Consume Spice", consume_spice, 5, 2, 3)
	app.stopLabelFrame()


	if player.culture_points < 1:
		app.disableButton("Increase Stability")
		app.disableButton("Export Culture")
	else:
		app.enableButton("Increase Stability")
		app.enableButton("Export Culture")	
	if player.culture_points < 1 or player.diplo_action < 1:
		app.disableButton("Improve Reputation")
	else:
		app.enableButton("Improve Relations")
	others = player.check_for_non_accepted_cultures()
	if len(others) == 0 or player.culture_points < 1:
		app.disableButton("Integrate Culture")
	else:
		app.enableButton("Integrate Culture")
	if player.resources["spice"] < 1 or player.stability >= 3:
		app.disableButton("Consume Spice")
	else:
		app.enableButton("Consume Spice")
	app.stopTab()

	#######################################################################################################
	app.startTab("Military")
	app.setBg("OrangeRed2")
	app.setStretch("all")
	app.startScrollPane("military")

	app.startLabelFrame("Total Strength")
	attack = player.calculate_base_attack_strength()
	defense = player.calculate_base_defense_strength()
	naval = player.calculate_naval_strength()
	app.addLabel("total_attack_str", "Land Attack Strength: %.2f" % (attack), 1, 1)
	app.addLabel("total_defense_str", "Land Defense Strength: %.2f" % (defense), 1, 2)
	app.addLabel("total_naval_str", "Naval Strength: %.2f" % (naval), 1, 3)
	app.stopLabelFrame()

	app.startLabelFrame("Casus Belli")
	app.addLabelOptionBox("CB List:", [" "])
	app.stopLabelFrame()

	app.startLabelFrame("Claims")
	count = 1
	for obj in player.objectives:
		if obj not in player.provinces.keys():
			ID = uniform(1,2) * count
			obj = provinces[obj]	
			app.addLabel(ID, "%s: %s %.2f" % (obj.name, obj.resource, obj.quality), count, 1)		
			app.addImage(ID, obj.owner + ".gif", count, 2)
			app.setImageTooltip(ID, obj.owner)
			count += 1
	app.stopLabelFrame()

	app.startLabelFrame("Army")
	row = 1
	app.addLabel("army_breakdown", " Type          Number     Att.       Def.   Man.    AmmoUse   OilUse", 0, 0, 9, 1)
	for k in player.military.keys():
		if k == "irregulars":
			continue
		
		elif k in ["frigates", "iron_clad", "battle_ship"]:
			continue
		else:
			app.addLabel("build_" + k, "", row, 0, 1)
			app.addImage("build_" + k, k +".gif", row, 0, 1)
			app.shrinkImage("build_" + k, 2)
			app.setImageTooltip("build_" + k, k.title())
			app.addLabel("num_" + k, player.military[k], row, 1, 1)
			app.setLabelRelief("num_" + k, "sunken")
			if k == "irregulars":
				app.addLabel("att_" + k, player.irregulars["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.irregulars["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.irregulars["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.irregulars["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.irregulars["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				#app.addNamedButton(" Build ", "build_" + k, build_army, row, 7, 1)
				if player.freePOP < 0.2 or player.goods["cannons"] < 1:
					app.disableButton("build_" + k)

			if k == "infantry":
				app.addLabel("att_" + k, player.infantry["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.infantry["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.infantry["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.infantry["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.infantry["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				#app.addNamedButton("Build", "build_" + k, build_army, row, 7, 1)
				if player.freePOP < 0.2 or player.goods["cannons"] < 1.5:
					app.disableButton("build_" + k)
				else:
					app.enableButton("build_"+ k)

			if k == "cavalry":
				app.addLabel("att_" + k, player.cavalry["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.cavalry["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.cavalry["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.cavalry["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.cavalry["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				#app.addNamedButton("Build", "build_" + k, build_army, row, 7, 1)
				if player.freePOP < 0.2 or player.goods["cannons"] < 1.5 or player.resources["food"] < 2:
					app.disableButton("build_" + k)
				else:
					app.enableButton("build_"+ k)
			if k == "artillery":
				app.addLabel("att_" + k, player.artillery["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.artillery["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.artillery["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.artillery["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.artillery["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				if player.freePOP < 0.2 or player.goods["cannons"] < 2.5:
					app.disableButton("build_" + k)
				else:
					app.enableButton("build_"+ k)

			if k == "tank":
				app.addLabel("att_" + k, player.tank["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.tank["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.tank["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.tank["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.tank["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				if player.freePOP < 0.2 or player.goods[k] < 1:
					app.disableButton("build_" + k)
				else:
					app.enableButton("build_"+ k)

			if k == "fighter":
				app.addLabel("att_" + k, player.fighter["attack"], row, 2, 1)
				app.addLabel("def_" + k, player.fighter["defend"], row, 3, 1)
				app.addLabel("man_" + k, player.fighter["manouver"], row, 4, 1)
				app.addLabel("ammo_use_" + k, player.fighter["ammo_use"], row, 5, 1)
				app.addLabel("oil_use_" + k, player.fighter["oil_use"], row, 6, 1)
				app.addImageButton("build_" + k, build_army, "add.gif", row, 7, 1)
				app.setButtonTooltip("build_" + k, "Build " + k)
				if player.freePOP < 0.2 or player.goods[k] < 1:
					app.disableButton("build_" + k)
				else:
					app.enableButton("build_"+ k)
			#app.addNamedButton("Disband", "disband_" + k, disband_army, row, 8, 1)
			app.addImageButton("disband_" + k, disband_army, "red_x.gif", row, 8, 1)
			app.setButtonTooltip("disband_" + k, "Disband " + k)
			if player.military[k] < 1:
				app.disableButton("disband_" + k)
			else:
				app.enableButton("disband_" + k)
			row += 1
	app.stopLabelFrame()

	app.startLabelFrame("Navy")
	row = 1
	app.addLabel("navy_breakdown", "  Type        Number     Att.      HP     AmmoUse     OilUse", 0, 0, 8)

	for k in player.military.keys():
		if 	k not in ["frigates", "iron_clad", "battle_ship"]:
				continue
		else:
			app.addLabel("build_" + k, " ", row, 0, 1, 1)
			app.addImage("build_" + k, k +".gif", row, 0, 1, 1)
			app.shrinkImage("build_" + k, 2)
			app.setImageTooltip("build_" + k, k.title())
			app.addLabel("num_" + k, player.military[k], row, 1, 1, 1)
			app.setLabelRelief("num_" + k, "sunken")
		if k == "frigates":
			app.addLabel("att_" + k, player.frigates["attack"], row, 2, 1, 1)
			app.addLabel("HP_" + k, player.frigates["HP"], row, 3, 1, 1)
			app.addLabel("ammo_use_" + k, player.frigates["ammo_use"], row, 4, 1, 1)
			app.addLabel("oil_use_" + k, player.frigates["oil_use"], row, 5, 1, 1)
			#app.addNamedButton("Build", "build_" + k, build_army, row, 6, 1, 1)
			app.addImageButton("build_" + k, build_army, "add.gif", row, 6, 1, 1)
			app.setButtonTooltip("build_" + k, "Build " + k)

			if player.shipyard < 1 or player.AP < 1 or player.resources["wood"] < 1 or player.goods["cannons"] < 1.5 or player.resources["cotton"] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_" + k)
		if k == "iron_clad":
			app.addLabel("att_" + k, player.iron_clad["attack"], row, 2, 1, 1)
			app.addLabel("HP_" + k, player.iron_clad["HP"], row, 3, 1, 1)
			app.addLabel("ammo_use_" + k, player.iron_clad["ammo_use"], row, 4, 1, 1)
			app.addLabel("oil_use_" + k, player.iron_clad["oil_use"], row, 5, 1, 1)
			#app.addNamedButton("Build", "build_" + k, build_army, row, 6, 1, 1)
			app.addImageButton("build_" + k, build_army, "add.gif", row, 6, 1, 1)
			app.setButtonTooltip("build_" + k, "Build " + k)
			if player.shipyard < 2 or player.AP < 1 or player.resources["iron"] < 1 or \
			player.goods["cannons"] < 1.5 or player.goods["parts"] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_" + k)
		if k == "battle_ship":
			app.addLabel("att_" + k, player.battle_ship["attack"], row, 2, 1, 1)
			app.addLabel("HP_" + k, player.battle_ship["HP"], row, 3, 1, 1)
			app.addLabel("ammo_use_" + k, player.battle_ship["ammo_use"], row, 4, 1, 1)
			app.addLabel("oil_use_" + k, player.battle_ship["oil_use"], row, 5, 1, 1)
			#app.addNamedButton("Build", "build_" + k, build_army, row, 6, 1, 1)
			app.addImageButton("build_" + k, build_army, "add.gif", row, 6, 1, 1)
			app.setButtonTooltip("build_" + k, "Build " + k)
			if player.shipyard < 3 or player.AP < 1 or player.goods["cannons"] < 4 \
			or player.resources["iron"] < 3 or player.goods["parts"] < 1 or player.goods["gear"] < 1:
				app.disableButton("build_" + k)
			else:
				enableButton("build_" + k)
		app.addNamedButton("Disband", "disband_" + k, disband_army, row, 7, 1, 1)
		if player.military[k] < 1:
			app.disableButton("disband_" + k)
		else:
			app.enableButton("disband_" + k)
		row += 1
	app.stopLabelFrame()
	app.stopScrollPane()
	app.stopTab()
	############################################################################################
	app.startTab("Diplomacy")
	app.setBg("RoyalBlue1")

	
	app.startScrollPane("diplomacy")
	app.startLabelFrame("Nations")
	count = 1
	for k, v in players.items():
		if k == player.name:
			continue
		app.addImage(k + " flag", k + ".gif", count, 1)
		app.setImageTooltip(k + " flag", k)
		relata = frozenset([player.name, v.name])
		app.addLabel("relations_with_" + k, "Relations: %.2f" % relations[relata].relationship, count, 2)
		app.setLabelFg("relations_with_" + k, "white")
		app.setLabelBg("relations_with_" + k, "black")
		
		app.addImageButton("imp_rel_w" + k, improve_relations, "diplomacy.gif", count, 3)
		app.setButtonTooltip("imp_rel_w" + k, "Improve Relations")
		app.addImageButton("dmg_rel_w" + k, damage_relations, "fire.gif", count, 4)
		app.setButtonTooltip("dmg_rel_w" + k, "Damage Relations")
		app.addImageButton("CB_" + k, gain_casus_belli, "casus_belli.gif", count, 5)
		app.setButtonTooltip("CB_" + k, "Gain Casus Belli")
		app.addImageButton("destab" + k, destabilize_nation, "unrest.gif", count, 6)
		app.setButtonTooltip("destab" + k, "Destabilize Nation")
		app.addImageButton("bribe" + k, bribe, "bribe.gif", count, 7)
		app.setButtonTooltip("bribe" + k, "Bribe Nation")
		app.addImageButton("sab_rel" + k, sabotage_relatons, "divide.gif", count, 8)
		app.setButtonTooltip("sab_rel" + k, "Sabotage Relations")
		app.addImageButton("embargo" + k, embargo_nation, "embargo.gif", count, 9)
		app.setButtonTooltip("embargo" + k, "Embargo!")
		app.addImageButton("war_on" + k, wage_war, "war.gif", count, 10)
		app.setButtonTooltip("war_on" + k, "Wage War!")
		app.addImageButton("info" + k, get_nation_info, "info.gif", count, 11)
		app.setButtonTooltip("info" + k, "Nation Details")

		relata = frozenset([player.name, k])
		if player.diplo_action < 1 or relations[relata].relationship >= 3.0:
			app.disableButton("imp_rel_w" + k)
		else:
			app.enableButton("imp_rel_w" + k)
		if player.diplo_action < 1 or relations[relata].relationship <= - 3.0:
			app.disableButton("dmg_rel_w" + k)
		else:
			app.enableButton("dmg_rel_w" + k)
		if player.diplo_action < 1 or relations[relata].relationship >= -2.5:
			app.disableButton("CB_" + k)
		else:
			app.enableButton("CB_" + k)

		if player.diplo_action < 1 or players[k].stability <= - 3.0:
			app.disableButton("destab" + k)
		else:
			app.enableButton("destab" + k)
		if player.resources["gold"] < 2.0 or relations[relata].relationship >= 3.0 or players[k].type == "major":
			app.disableButton("bribe" + k)
		else:
			app.enableButton("bribe" + k)
		if player.diplo_action < 1:
			app.disableButton("sab_rel" + k)
		else:
			app.enableButton("sab_rel" + k)
		if player.diplo_action < 1 or (player.name not in players[k].embargo and relations[relata].relationship > -1.5):
			app.disableButton("embargo" + k)
		else:
			app.enableButton("embargo" + k)
		count += 1

	app.stopLabelFrame()
	app.stopScrollPane()
	app.stopTab()

	app.stopTabbedFrame()
	app.hideSubWindow("loading new game")

def none(btn):
	return

def improve_relations(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations
	player = players[human_player]
	other = btn[9:]
	relata = frozenset([player.name, other])
	player.improve_Relations(other, relations, players)
	message = "Relationship with %s is now %.2f" % (other, relations[relata].relationship) 
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def damage_relations(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations
	player = players[human_player]
	other = btn[9:]
	relata = frozenset([player.name, other])
	player.damage_Relations(other, relations, players)
	message = "Relationship with %s is now %.2f" % (other, relations[relata].relationship) 
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def gain_casus_belli(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations, provinces
	player = players[human_player]
	other = btn[3:]
	opts = player.check_for_claims(other, provinces)
	if len(opts) == 0:
		message = "We have no claims to any of territory currently belonging to %s but can still wage war for loot" % other
		app.setLabel("general_message", message)
		app.showSubWindow("Message_")
		player.gain_CB(other, "", provinces)
		message = "You have gained a Casus Belli against " + other
		app.setLabel("general_message", message)
		update_diplomacy_tab()
		app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
		app.setLabel("l24", "%.2f" % round(player.reputation, 2))

	else:	 
		app.changeOptionBox("prov_to_annex", opts)
		app.showSubWindow("Province to Annex")


def cb_2(btn):
	print("1276")
	prov = app.getOptionBox("prov_to_annex")
	print("1278")
	app.hideSubWindow("Province to Annex")
	print("1280")
	app.hideSubWindow("Message_")
	global players, human_player, provinces
	player = players[human_player]
	prov = app.getOptionBox("prov_to_annex")
	prov = provinces[prov]
	#other = provinces[prov].owner
	player.gain_CB(prov.owner, prov.name, provinces)
	message = "You have gained a Casus Belli against " + prov.owner
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	update_military_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def destabilize_nation(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations
	player = players[human_player]
	other = btn[6:]
	player.destabilize_Nation(other, players, relations)
	message = "The stability of %s has been reduced to %.2f" % (other, players[other].stability)
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def bribe(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations
	player = players[human_player]
	other = btn[5:]
	player.bribeNation(other, relations, players)
	relata = frozenset([player.name, other])
	message = "Relationship with %s is now %.2f" % (other, relations[relata].relationship) 
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l4", "%.2f" % round(player.resources["gold"], 2))
	app.showSubWindow("Message_")


def sabotage_relatons(btn):
	app.hideSubWindow("Message_")
	global players, human_player, OTHER
	player = players[human_player]
	OTHER = btn[7:]
	print("OTHER: %s" % OTHER)
	firstOther = players[OTHER]
	all_others = firstOther.everyone_but_self(players)
	app.changeOptionBox("other_player", all_others)
	app.showSubWindow("Choose Other Player")

def sab_rel_2(btn):
	global players, human_player, relations, OTHER
	player = players[human_player]
	app.hideSubWindow("Choose Other Player")
	other2 = app.getOptionBox("other_player")
	print("Other2: %s" % other2)
	player.sabotage_Relatons(OTHER, other2, players, relations)
	relata = frozenset([OTHER, other2])
	message = "Relation between %s and %s have been reduced to %.2f!" % (OTHER, other2, relations[relata].relationship)
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def embargo_nation(btn):
	app.hideSubWindow("Message_")
	global players, human_player, relations
	player = players[human_player]
	other = btn[7:]
	#other = players[other]
	player.embargo_Nation(other, players, relations)
	if player.name in players[other].embargo:
		message = "%s will no longer be able to purchase any of our resources or goods!" % other
	else:
		message = "We have decided that %s has been a good boy are are willing to resume trade... for now" % other
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.setLabel("l11", "%.2f" % round(player.diplo_action, 2))
	app.setLabel("l24", "%.2f" % round(player.reputation, 2))
	app.showSubWindow("Message_")


def get_nation_info(btn):
	global players, human_player, relations
	other = btn[4:]
	other = players[other]
	update_Nation_Info(other)
	app.showSubWindow("Nation Info")

def update_Nation_Info(other):
	app.setLabel("Nation_Name", other.name)
	fact_level = other.get_fact_level()
	app.setLabel("PrimaryStats", "Gold: %.2f  DevLevel: %d  Number Tech: %d  ProvinceDevs: %d  Number Factory-Levels: %d" % \
		(other.resources["gold"], other.development_level, len(other.technologies), other.number_developments, fact_level))
	app.setLabel("NationMiddleCLass", "Scientists: %.2f,  Officers: %.2f,  Bureaucrats: %.2f,  Artists: %.2f,  Managers: %.2f " % \
		(other.developments["research"], other.developments["military"], other.developments["government"], \
		other.developments["culture"], other.developments["management"]))
	app.setLabel("factories_1", "Parts: %d,  Cannons: %d,  Clothing: %d,  Paper: %d,  Furniture: %d, Chemicals: %d" % \
		(other.factories["parts"]["number"], other.factories["cannons"]["number"], other.factories["clothing"]["number"], \
		other.factories["paper"]["number"], other.factories["furniture"]["number"], other.factories["chemicals"]["number"]))
	app.setLabel("factories_2", "Gear: %d,  Radio: %d,  Telephone: %d,  Auto: %d,  Fighter: %d,  Tank: %d" % \
		(other.factories["gear"]["number"], other.factories["radio"]["number"], other.factories["telephone"]["number"], \
		other.factories["auto"]["number"], other.factories["fighter"]["number"], other.factories["tank"]["number"]))
	invent = ""
	for (k1,v1), (k2,v2) in zip(other.resources.items(), other.goods.items()):
		add = 		 (" %-12s: %.2f        %-12s: %.2f \n" % (k1, v1, k2, v2))
		invent = invent + add
	app.setMessage("NationInventory", invent)

	military_info = ""
	total_att = other.calculate_base_attack_strength()
	total_defense = other.calculate_base_defense_strength()
	total_naval = other.calculate_naval_strength()
	military_info = military_info + " Total Land Attack Strength: %.2f \n" % total_att
	military_info = military_info + " Total Land Defense Strength: %.2f \n" % total_defense
	military_info = military_info + " Total Naval Strength: %.2f \n" % total_naval
	for k, v in other.military.items():
		military_info = military_info + "%s: %.2f,   \n" % (k, v)
	app.setMessage("NationMilitary", military_info)

def wage_war(btn):
	global players, human_player
	player = players[human_player]
	other = btn[:6]

def update_production_gui():
	global players, human_player
	player = players[human_player]
	fact_options = player.factory_optons()
	for f in player.goods.keys():	
		app.setLabel("level_" + f, player.factories[f]["number"])
		app.setLabel("used_" + f, player.factories[f]["used"])
		if f not in fact_options:
			app.disableButton("upgrade_" + f)
		else:
			app.enableButton("upgrade_" + f)
		app.setLabel("iamount_" + f, player.goods[f])
		app.setLabel("producing_" + f, player.goods_produced[f])
		app.setLabel("abprod_" + f, player.amount_can_manif(f))
		if player.amount_can_manif(f) < 1 or player.factories[f]["used"] == True or player.crafted == True:
			app.disableButton("produce_" + f)
		else:
			app.enableButton("produce_" + f)
	app.setLabel("upgrade_fortification", "Fortification Level: %.2f" % player.fortification)
	if player.goods["cannons"] < 1 or player.AP < 1 or (player.fortification >= 1.1 and "cement" \
		not in player.technologies) or player.fortification >= 1.2:
		app.disableButton("upgrade_fort")
	else:
		app.enableButton("upgrade_fort")

	app.setLabel("upgrade_shipyard", "shipyard Level: %d" % player.shipyard)
	if player.AP < 1 or player.new_development < 1 or player.resources["wood"] < 1 or player.goods["parts"] < 1:
		app.disableButton("upgrade_shipyard")
	elif player.shipyard == 1 and "ironclad" not in player.technologies:
		app.disableButton("upgrade_shipyard")
	elif player.shipyard == 2 and oil_powered_ships not in player.technologies:
		app.disableButton("upgrade_shipyard")
	else:
		app.enableButton("upgrade_shipyard")


	if "synthetic_dyes" not in player.technologies or player.goods["chemicals"] < 1:
		app.disableButton("Synthetic Dyes")
	else:
		app.enableButton("Synthetic Dyes")
	if "fertilizer" not in player.technologies or player.goods["chemicals"] < 1:
		app.disableButton("Fertilize Soil")
	else:
		app.enableButton("Fertilize Soil")
	if "synthetic_rubber" not in player.technologies or player.goods["chemicals"] < 1 or player.goods["oil"] < 1:
		app.disableButton("Synthetic Rubber")
	else:
		app.enableButton("Synthetic Rubber")
	if "synthetic_oil" not in player.technologies or player.goods["chemicals"] < 3:
		app.disableButton("Synthetic Oil")
	else:
		app.enableButton("Synthetic Oil")
	

def update_military_tab():
	global players, human_player, market
	player = players[human_player]
	attack = player.calculate_base_attack_strength()
	defense = player.calculate_base_defense_strength()
	naval = player.calculate_naval_strength()
	app.setLabel("total_attack_str", "Land Attack Strength: %.2f" % (attack))
	app.setLabel("total_defense_str", "Land Defense Strength: %.2f" % (defense))
	app.setLabel("total_naval_str", "Naval Strength: %.2f" % (naval))

	cb_list = []
	for cb in player.CB:
		addition = "%s: %s, %d" % (cb.opponent, cb.province, cb.time)
		cb_list.append(addition)
	app.changeOptionBox("CB List:", cb_list)

	for k in player.military.keys():
		if k == "irregulars":
			continue
		app.setLabel("num_" + k, player.military[k])

		if k == "infantry":
			app.setLabel("att_" + k, "%.2f" % player.infantry["attack"])
			app.setLabel("def_" + k, "%.2f" % player.infantry["defend"])
			app.setLabel("man_" + k, "%.2f" % player.infantry["manouver"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.infantry["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.infantry["oil_use"])
			if player.freePOP < 0.2 or player.goods["cannons"] < 1.5:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)

		if k == "cavalry":
			app.setLabel("att_" + k, "%.2f" % player.cavalry["attack"])
			app.setLabel("def_" + k, "%.2f" % player.cavalry["defend"])
			app.setLabel("man_" + k, "%.2f" % player.cavalry["manouver"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.cavalry["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.cavalry["oil_use"])
			if player.freePOP < 0.2 or player.goods["cannons"] < 1.5 or player.resources["food"] < 2:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)
		if k == "artillery":
			app.setLabel("att_" + k, "%.2f" % player.artillery["attack"])
			app.setLabel("def_" + k, "%.2f" % player.artillery["defend"])
			app.setLabel("man_" + k, "%.2f" % player.artillery["manouver"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.artillery["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.artillery["oil_use"])
			if player.freePOP < 0.2 or player.goods["cannons"] < 2.5:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)

		if k == "tank":
			app.setLabel("att_" + k, "%.2f" % player.tank["attack"])
			app.setLabel("def_" + k, "%.2f" % player.tank["defend"])
			app.setLabel("man_" + k, "%.2f" % player.tank["manouver"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.tank["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.tank["oil_use"],)
			if player.freePOP < 0.2 or player.goods[k] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)

		if k == "fighter":
			app.setLabel("att_" + k, "%.2f" % player.fighter["attack"])
			app.setLabel("def_" + k, "%.2f" % player.fighter["defend"])
			app.setLabel("man_" + k, "%.2f" % player.fighter["manouver"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.fighter["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.fighter["oil_use"])
			if player.freePOP < 0.2 or player.goods[k] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)
		if k == "frigates":
			app.setLabel("att_" + k, "%.2f" % player.frigates["attack"])
			app.setLabel("HP_" + k, "%.2f" % player.frigates["HP"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.frigates["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" %  player.frigates["oil_use"])
			if player.shipyard < 1 or player.AP < 1 or player.resources["wood"] < 1 or player.goods["cannons"] < 1.5 or player.resources["cotton"] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)
		if k == "iron_clad":
			app.setLabel("att_" + k, "%.2f" % player.iron_clad["attack"])
			app.setLabel("HP_" + k, "%.2f" % player.iron_clad["HP"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.iron_clad["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.iron_clad["oil_use"])
			if player.shipyard < 2 or player.AP < 1 or player.resources["iron"] < 1 or \
			player.goods["cannons"] < 1.5 or player.goods["parts"] < 1:				
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)
		if k == "battle_ship":
			app.setLabel("att_" + k, "%.2f" % player.battle_ship["attack"])
			app.setLabel("HP_" + k, "%.2f" % player.battle_ship["HP"])
			app.setLabel("ammo_use_" + k, "%.2f" % player.battle_ship["ammo_use"])
			app.setLabel("oil_use_" + k, "%.2f" % player.battle_ship["oil_use"])
			if player.shipyard < 3 or player.AP < 1 or player.goods["cannons"] < 4 \
			or player.resources["iron"] < 3 or player.goods["parts"] < 1 or player.goods["gear"] < 1:
				app.disableButton("build_" + k)
			else:
				app.enableButton("build_"+ k)
		if player.military[k] < 1:
			app.disableButton("disband_" + k)
		else:
			app.enableButton("disband_" + k)


def update_buy_button():
	global human_player, players, market
	player = players[human_player]
	for k in market.market_keys:
		price = market.buy_price(k, player.supply[k])
		if player.supply[k] < 1 or (player.resources["gold"] < price):
			app.disableButton(k + "_buy")
		else:
			app.enableButton(k + "_buy")
	

def update_sell_button():
	global human_player, players, market
	player = players[human_player]
	for k in player.resources.keys():
		if k in ["gold", "/", "//"]:
			continue
		if player.resources[k] < 1:
			app.disableButton(k + "_sell")
		else:
			app.enableButton(k + "_sell")
	for k in player.goods.keys():
		if player.goods[k] < 1:
			app.disableButton(k + "_sell")
		else:
			app.enableButton(k + "_sell")

def update_military_buttons():
	global human_player, players, market
	player = players[human_player]
	if player.freePOP < 0.2 or player.goods["cannons"] < 1.5:
		app.disableButton("build_infantry")
	else:
		app.enableButton("build_infantry")
	if player.freePOP < 0.2 or player.goods["cannons"] < 1.5 or player.resources["food"] < 2:
		app.disableButton("build_cavalry")
	else:
		app.enableButton("build_cavalry")
	if player.freePOP < 0.2 or player.goods["cannons"] < 2.5:
		app.disableButton("build_artillery")
	else:
		app.enableButton("build_artillery")
	if player.freePOP < 0.2 or player.goods[k] < 1:
		app.disableButton("build_tank")
	else:
		app.enableButton("build_tank")
	if player.freePOP < 0.2 or player.goods[k] < 1:
		app.disableButton("build_fighter")
	else:
		app.enableButton("build_fighter")

	if player.shipyard < 1 or player.AP < 1 or player.resources["wood"] < 1 or player.goods["cannons"] < 1.5 or player.resources["cotton"] < 1:
		app.disableButton("build_frigates")
	else:
		app.enableButton("build_frigates")
	if player.shipyard < 2 or player.AP < 1 or player.resources["iron"] < 1 or \
	player.goods["cannons"] < 1.5 or player.goods["parts"] < 1:
		app.disableButton("build_iron_clad")
	else:
		app.enableButton("build_iron_clad")
	if player.shipyard < 3 or player.AP < 1 or player.goods["cannons"] < 4 \
	or player.resources["iron"] < 3 or player.goods["parts"] < 1 or player.goods["gear"] < 1:
		app.disableButton("build_battle_ship")
	else:
		enableButton("build_battle_ship")

	for k in player.military.keys():
		if k == "irregulars":
			continue
		if player.military[k] < 1:
			app.disableButton("disband_" + k)
		else:
			app.enableButton("disband_" + k)


def AI_turnS(auto_save):
	global players, market, relations, provinces, human_player
	market.report = []
	market.market_report = " "
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
	app.setMessage("turn_market_report", market.market_report)

	player = players[human_player]
	print("____________________________________________________________________________________")
	player.calculate_access_to_goods(market)
	app.setLabel("t1", "Turn:" +  str(market.turn))
	update_gui()
	update_diplomacy_tab()


def increase_stability(btn):
	global players, human_player, market
	player = players[human_player]
	player.increase_Stability()
	app.setLabel("l10", "%.2f" % round(player.stability, 2))
	app.setLabel("l5", "%.2f" % round(player.culture_points, 2))
	update_culture_tab()

def improve_reputation(btn):
	global players, human_player, market
	player = players[human_player]
	player.improve_Reputation()
	update_main_tab()
	update_culture_tab()


def integrate_culture(btn):
	global players, human_player, market
	player = players[human_player]
	opts = player.check_for_non_accepted_cultures()
	app.changeOptionBox("prov_to_integrate", opts)
	app.showSubWindow("Province to Integrate")


def integrate_culture_2(btn):
	app.hideSubWindow("Message_")
	global players, human_player
	player = players[human_player]
	app.hideSubWindow("Provinces to Integrate")
	prov = app.getOptionBox("prov_to_int")
	if player.integrate_Culture(prov):
		message = "The people of %s have been 'integrated' into our superior culture!" % prov
		update_gui()
	else:
		message = "Despite our best efforts, the stubborn populace of %s do not self-identify with \
		themselves as people of %s" % (prov, player.name)
	app.setLabel("general_message", message)
	update_diplomacy_tab()
	app.showSubWindow("Message_")	


def export_culture(btn):
	global players, human_player, market
	player = players[human_player]
	player.export_Culture(players)
	update_main_tab()
	update_culture_tab()

def consume_spice(btn):
	global players, human_player, market
	player = players[human_player]
	player.use_Spice_Stability() 
	update_gui()

def upgrade_fort(btn):
	global players, human_player, market
	player = players[human_player]
	player.improve_fortifications()
	update_gui()

def upgrade_shipyard(btn):
	global players, human_player, market
	player = players[human_player]
	player.build_steam_ship_yard()
	update_gui()

def synthetic_dyes(btn):
	global players, human_player, market
	player = players[human_player]
	player.create_synthetic_dyes()
	update_market_tab()
	update_production_gui()

def fertilize_soil(btn):
	global players, human_player, market
	player = players[human_player]
	player.chem_to_food()
	update_market_tab()
	update_production_gui()

def synthetic_rubber(btn):
	global players, human_player, market
	player = players[human_player]
	player.create_synthetic_rubber()
	update_market_tab()
	update_production_gui()

def synthetic_oil(btn):
	global players, human_player, market
	player = players[human_player]
	player.create_synthetic_oil()
	update_market_tab()
	update_production_gui()


def select_technology(btn):
	global players, human_player, market
	player = players[human_player]
	tech = btn[4:]
	app.setMessage("tech_description", tech_descriptions[tech])
	app.setImage("tech_image", tech + ".gif")


def research_technology(btn):
	global players, human_player, market
	player = players[human_player]
	tech = btn[4:]
	player.research_tech(tech)
	update_gui()


def build_army(btn):
	global players, human_player, market
	player = players[human_player]
	_type = btn[6:]
	player.build_army_unit(_type)
	message = "The new %s unit will appear next turn" % _type
	update_gui()
	app.setLabel("general_message", message)
	app.showSubWindow("Message_")


def disband_army(btn):
	global players, human_player, market
	player = players[human_player]
	_type = btn[8:]
	player.disband_unit(_type)
	if player.military[_type] < 1:
		app.disableButton("disband_" + _type)
	else:
		app.enableButton("disband_" + _type)
	update_gui()


def add_pro_pop(btn):
	global players, human_player, market
	player = players[human_player]
	player.pro_POP_add()
	app.setLabel("l12", "%.2f" % round(player.freePOP, 2))

	if player.freePOP < 1:
		app.disableButton("add_pro_pop")
	else:
		app.enableButton("add_pro_pop")
	app.enableButton("remove_pro_pop")
	app.setLabel("num_urban_workers", "Number of Urban Workers %s" % (player.proPOP))


def remove_pro_pop(btn):
	global players, human_player, market
	player = players[human_player]
	player.pro_POP_subtract()
	app.enableButton("add_pro_pop")
	if player.proPOP < 1:
		app.disableButton("remove_pro_pop")
	else:
		app.enableButton("remove_pro_pop")
	app.setLabel("num_urban_workers", "Number of Urban Workers %s" % (player.proPOP))
	app.setLabel("l12", "%.2f" % round(player.freePOP, 2))


def manifacture_good_1(btn):
	global players, human_player, market, PRODUCE
	print(human_player)
	player = players[human_player]
	_type = btn[8:]
	print(_type)
	PRODUCE = _type
	max_amt = int(player.amount_can_manif(_type)) + 1
	opts = list(range(1, max_amt))
	app.changeOptionBox("amount_to_man", opts)
	app.showSubWindow("amount_to_man")
	update_gui()

def manifacture_good_2(btn):
	global players, human_player, market, PRODUCE
	player = players[human_player]
	app.hideSubWindow("amount_to_man")
	_type = PRODUCE
	amount = app.getOptionBox("amount_to_man")
	player.manifacture_good(_type, int(amount))
	print(player.goods_produced[_type])
	print(player.name)
	update_gui()


def good_material(_type):
	if _type in ["parts", "cannons"]:
		return ["iron", "coal"]
	if _type == "clothing":
		return ["cotton", "dyes"]
	if _type == "furniture":
		return ["wood", "cotton"]
	if _type == "paper":
		return []

def build_fact(btn):
	global players, human_player, market
	player = players[human_player]
	_type = btn[8:]
	print(_type)
	player.build_factory(_type, market)
	app.setLabel("level_" + _type, player.factories[_type]["number"])
	update_gui()

def increase_population(btn):
	global players, human_player
	player = players[human_player]
	if player.POP_increased == 1.0:
		#showSubWindow("chem_growth")
		#cont = if_spend_chem()
		player.goods["chemicals"] -= 1
		return
	else:
		player.increase_pop()
		app.setLabel("l6",  "%.2f" % round(player.POP, 2))
		app.setLabel("l12", "%.2f" % round(player.freePOP, 2))

		app.setLabel("i_food_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources["food"]), len(market.market["food"]), player.supply["food"], \
				market.buy_price("food", len(market.market["food"])), market.buy_price("food", player.supply["food"])))
		app.setLabel("i_clothing_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods["clothing"]), len(market.market["clothing"]), player.supply["clothing"], \
			market.buy_price("clothing", len(market.market["clothing"])), market.buy_price("clothing", player.supply["clothing"])))
		if(player.POP_increased > 1):
			app.disableButton("POP UP")
		if player.POP_increased == 1.0 and player.goods["chemicals"] < 1:
			app.disableButton("POP UP")
		if player.resources["food"] < 1 or player.goods["clothing"] < 1:
			app.disableButton("POP UP")
		else:
			app.enableButton("POP UP")
		app.enableButton("add_pro_pop")	


def if_spend_chem():
	cont = getYesNoBox("chem_for_growth")
	app.hideSubWindow("chem_growth")
	return cont

def	dev_type(btn):
	global players, human_player
	player = players[human_player]
	d_options = player.development_options()
	app.changeOptionBox("get_dev_type", d_options)
	#app.setOptionBox(title, position, value=True, callFunction=True, override=False)
	app.showSubWindow("chose_dev_type")
	

def increase_dev_level(btn):
	global players, human_player
	player = players[human_player]
	app.hideSubWindow("chose_dev_type")
	kind = app.getOptionBox("get_dev_type")
	requirements = player.determine_middle_class_need()
	player.increase_development(kind)
	for k in requirements:
		if k == "spice":
			app.setLabel("i_spice_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources["spice"]), len(market.market["spice"]), player.supply["spice"], \
				market.buy_price("spice", len(market.market["spice"])), market.buy_price("spice", player.supply["spice"])))
	
		else: 
			app.setLabel("i_" + k + "_value", "%.2f     %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods[k]), len(market.market[k]), player.supply[k], \
			market.buy_price(k, len(market.market[k])), market.buy_price(k, player.supply[k])))

	app.setLabel("l22", "%s" % (player.development_level))
	if player.check_development() == False:
		app.disableButton("Develop")
	else:
		app.enableButton("Develop")
	if kind == "military":
		doc_ops = player.doctrine_options()
		app.changeOptionBox("get_mil_doct", doc_ops)
		app.showSubWindow("choose doctrine")
	update_gui()


def acquire_doctrine(btn):
	global human_player, players, market
	player = players[human_player]
	app.hideSubWindow("choose doctrine")
	choice = app.getOptionBox("get_mil_doct")
	player.choose_doctrine(choice)


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
	if player.freePOP < 1:
		app.disableButton("add_pro_pop")
	else:
		app.enableButton("add_pro_pop")
	app.hideSubWindow("human" + p.position)



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
	if player.freePOP < 1:
		app.disableButton("add_pro_pop")
	else:
		app.enableButton("add_pro_pop")
	app.hideSubWindow("human" + p.position)


def dev_prov(btn):
	global players, human_player
	print("Button before: %s" % (btn))
	btn = btn[8:]
	print("Button after %s" % (btn))
	player = players[human_player]
	player.dev_p(btn)
	p = player.provinces[btn]
	app.setLabel("dev" + p.name, str(p.development_level))
	app.setLabel("l16", player.AP)
	app.setLabel("l23", player.new_development)
	if player.can_improve_prov(p) == False:
		app.disableButton("Develop " + p.name)
	else:
		app.enableButton("Develop " + p.name)
	app.hideSubWindow("human" + p.position)
	update_gui()


def press_prov(btn):
	print(btn)
	global players
	global provinces, human_player
	player = players[human_player]
	for p in provinces.values():
		if btn == p.position:
			if p in player.provinces.values():
				print('Human Province')
				show_human_province(p)
			else:
				print("AI province")
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
	
	if owner.check_if_prov_can_be_dev(p.name):
		print("Yes____________________________________________________________________")
		if owner.AP >= 1 and owner.goods["parts"] >= 1 and owner.resources["wood"] > 1 and owner.new_development >= 1:
			print("But no :(___________________________________________________")
			app.enableButton("Develop " + p.name)
		else:
			app.disableButton("Develop " + p.name)
	else:
		app.disableButton("Develop " + p.name)

def show_AI_province(p):
	global players 
	owner = p.owner
	owner = players[owner]
	print("Owner: %s", owner.name)
	print(owner.name)
	app.showSubWindow("ai"+ p.position)
	app.setLabel(p.name, "Owner: %s" % (owner.name))
	app.setImage(p.name, owner.name + ".gif")
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
	global market, human_player, players
	player = players[human_player]
	btn = btn[:-4]
	seller_list = market.getSellers(btn, player)
	app.changeOptionBox("Sellers", seller_list)
	app.setLabel("item_to_buy", btn)
	app.showSubWindow("chose_seller")


def _buy(btn):
	other = app.getOptionBox("Sellers")
	_type = app.getLabel("item_to_buy")
	global human_player, market, players, relations
	player = players[human_player]
	market.buy_item(other, _type, player, players, relations)
	if _type in player.resources.keys():
		app.setLabel("i_" + _type + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources[_type]), len(market.market[_type]), player.supply[_type], \
			market.buy_price(_type, len(market.market[_type])), market.buy_price(_type, player.supply[_type])))
	else:
		app.setLabel("i_" + _type + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods[_type]), len(market.market[_type]), player.supply[_type], \
			market.buy_price(_type, len(market.market[_type])), market.buy_price(_type, player.supply[_type])))
	app.setLabel("l4", "%.2f" % round(player.resources["gold"], 2))
	app.hideSubWindow("chose_seller")
	update_buy_button()

def sell(btn):
	global human_player, players, market
	_type = btn[:-5]
	player = players[human_player]
	market.sell_item(_type, player, players)
	if _type in player.resources.keys():
		app.setLabel("i_" + _type + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.resources[_type]), len(market.market[_type]), player.supply[_type], \
			market.buy_price(_type, len(market.market[_type])), market.buy_price(_type, player.supply[_type])))
	else:
		app.setLabel("i_" + _type + "_value", "%.2f    %-6.1f (%-6.1f)  %-6.1f (%-6.1f)" % \
			(round(player.goods[_type]), len(market.market[_type]), player.supply[_type], \
			market.buy_price(_type, len(market.market[_type])), market.buy_price(_type, player.supply[_type])))



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
	#start_game_tread()


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
	app.addLabel("saving label", "Saving Game ...")
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

	app.startSubWindow("Province to Annex", modal = True)
	app.addLabel("prov_to_annex", "Which Province would you like to annex?")
	app.addLabel("(If list is empty, you may still go to war for general spoils (33\%\ of opponent's gold")
	app.addOptionBox("prov_to_annex", [])
	app.addNamedButton("OK", "prov_to_annex_", cb_2)
	app.stopSubWindow()

	app.startSubWindow("Choose Other Player", modal = True)
	app.addLabel("choose_other", "Please chose another player")
	app.addOptionBox("other_player", [players.keys()])
	app.addNamedButton("OK", "other_player", sab_rel_2)
	app.stopSubWindow()

	app.startSubWindow("Nation Info", modal = False)
	app.startLabelFrame("Report")
	app.addLabel("Nation_Name", " ")
	app.getLabelWidget("Nation_Name").config(font="Times 13 bold underline")
	app.addLabel("PrimaryStats", " ")
	#Primary Stats: Gold, DevelopmentLevel, NumTechnologies, NumDevelopments, NumFactories
	app.addLabel("NationMiddleCLass", " ")
	app.addLabel("factories_1", " ")
	app.addLabel("factories_2", " ")
	app.stopLabelFrame()
	app.addMessage("NationInventory", """ """)
	app.addMessage("NationMilitary", """ """)
	app.stopSubWindow()

	app.startSubWindow("Message_")
	app.addLabel("general_message", " ")
	app.stopSubWindow()

	app.startSubWindow("Land Battle")
	app.addImage("attacking_nation", "England.gif", 1, 1)
	app.addImage("att_infantry", "infantry.gif", 2, 1)
	app.addImage("att_cavalry", "cavalry.gif", 3, 1)
	app.addImage("att_artillery", "artillery.gif", 4, 1)
	app.addImage("att_tank", "tank.gif", 5, 1)
	app.addImage("att_fighter", "fighter.gif", 6, 1)
	app.addLabel("total_att_str", "Total Str", 8, 1)
	app.addLabel("att_ammo_deficit", "Ammo Deficit: %.2f" % 0, 10, 1)
	app.addLabel("def_ammo_deficit", "Oil Deficit: %.2f" % 0, 11, 1)

	app.addLabel("num_att_infantry", 0, 2, 2)
	app.addLabel("num_att_cavalry", 0, 3, 2)
	app.addLabel("num_att_artillery", 0, 4, 2)
	app.addLabel("num_att_figthers", 0, 5, 2)
	app.addLabel("num_tanks", 0, 6, 2)
	


	#app.startSubWindow("chem_growth", modal = True)
	#app.yesNoBox("chem_for_growth", "Increasing Your Pop again this turn will require 1 chemical", parent= None)
	#app.stopSubWindow()

app = gui("Imperialist Bastards", "960x600")
app.setIcon("crown.gif")
app.setFont("11", "arial")
app.setLocation("CENTER")
app.setExpand("all")
app.setPadding([1, 1])
app.setInPadding([2, 2])

app.setBg("khaki", override=False, tint=False)
#app.setGeometry("fullscreen")
app.setImageLocation("Images")
app.setSoundLocation("Sounds")
app.setBgImage("IB.png")


fileMenus = ["New Game", "Load Game", "Save", "Save as...", "Exit Game", "Close"]
app.createMenu("Menu")
app.addMenuItem("Menu", "New Game", func = new_game, shortcut=None, underline=-1)
app.addMenuItem("Menu", "Load Game", func = gui_load_game, shortcut = None, underline = -1)
app.addMenuItem("Menu", "Save Game", func= gui_save_game, shortcut = "S", underline = -1)
app.addMenuItem("Menu", "Exit", func = exit_game, shortcut = None, underline = -1)

app.go()