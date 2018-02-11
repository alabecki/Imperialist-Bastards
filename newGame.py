


def new_game(btn):
	app.addLabel("Scenario_Choice", "Which Scenario Would You Like to Play?")
	app.addRadioButton("Scen", "None")
	app.addRadioButton("Scen", "Semi-Historical")
	app.addRadioButton("Scen", "Fictional")
	app.addButton("Cont", scen_press)
	app.addRadioButton("nation_type", "Major Power")
	app.addRadioButton("nation_type", "Minor Power")
	app.addRadioButton("nation_type", "Old Empire")
	app.addButton("Cont.", nation_type_press)
	app.addLabelOptionBox("nation", nation_type)
	app.addNamedButton("OK", "select_nation", nation_press)



def game_option_screen(btn):
	app.setBg("khaki", override=False, tint=False)
	app.setFont("13")
	app.addLabel("Scenario_options", Scenarios:)
	app.addLabelRadioButton("Scenario:", "Semi-Historical")
	app.addLabelRadioButton("Scenario:", "Fictional")
	app.setRadioButtonChangeFunction("Scenario:", pick_scenario)

	app.addLabelRadioButton("Auto Save:", "On")
	app.addLabelRadioButton("Auto Save:", "Off")

	app.addLabelOptionBox("Nation:", [])
	app.addLabelRadioButton("Sound:", "On")
	app.addLabelRadioButton("Sound:", "Off")

	app.addImageButton("Start Game", start_game, "Start Game.gif", )


def pick_scenario(btn):
	scenario = getRadioButtin("Scenario:")
	nation_choices = []
	if scenario == "Semi-Historical":
		nation_choices = ["England", "France", "Russia", "Germany", "Austria", "Italy", "Ottoman", "Spain", \
		"Netherlands", "Sweden", "Portugal", "Two Sicilies", "Switzerland", "Saxony", "China", "India", "Japan", "Persia"]

	if scenario == "Fictional":
		nation_choices = ["Bambaki", "Hyle", "Trope", "Sidero", "Isorropia", "Karbouno"]
	app.changeOptionBox("Nation:", nation_choices, callFunction=False)


def start_game(btn):
	player = app.getOptionBox("Nation:")
	scenario = app.getRadioButton("Scenario:")
	global initial, human_player
	human_player = player

	print("Human Nation %s" % (player))
	if scenario == "Semi-Historical":
		initial = historical(player)
	if scenario == "Fictional":
		initial = balance(player)
	global players
	global provinces
	global relations
	global market
	players = initial["players"]
	provinces = initial["provinces"]
	relations = initial["relations"]
	isAutoSaving = app.getRadioButton("Auto Save:")
	if isAutoSaving == "On":
		market.auto_save = app.getEntry("auto_save")
	start_main_screen()