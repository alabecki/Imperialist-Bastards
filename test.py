
#Market Place
from player_class import Player
from AI import*
from empire_class import Empire
from Old_Minor_Class import Old_minor
from start import*
from random import*
from market import*



new = AI("dummy", "major", 1)
dummy = new

res = "iron"
qual = 1
name = doname()
new = Province(name, res, qual, "core", dummy.name)
dummy.provinces[name] = new
dummy.new_development = 2

res = "food"
qual = 1
name = doname()
new = Province(name, res, qual, "core", dummy.name)
dummy.provinces[name] = new
dummy.new_development = 2


market = Market()
#players[name].borders.add(b1)
#players[name].borders.add(b2)
dummy.stability = 1
dummy.technologies.add("high_pressure_steam_engine")
dummy.technologies.add("square_timbering")
dummy.resources["iron"] = 5
dummy.resources["coal"] = 3
dummy.resources["gold"] = 10
dummy.proPOP = 3
dummy.AP = 3
dummy.factories.add("parts")
dummy.ai_factory_production("parts")
dummy.steam_ship_yard = True

flag = True
if dummy.goods["parts"] < 1:
	print("Wants parts")
	decision = dummy.ai_decide_on_good("parts", market)
	get = dummy.ai_obtain_good("parts", decision, market)
	if get == "false":
		flag = False
if dummy.resources["iron"] < 0.5:
	print("Wants iron")
	get = dummy.ai_buy("iron", 1, market)
	if get == "fail":
		flag = False
if dummy.resources["wood"] < 1:
	print("Wants wood")
	get = dummy.ai_buy("wood", 1, market)
	if get == "fail":
		flag = False
if flag == False:
	print("failure")
else:
	print("Past Improve Province Flags")
	#priorities = (sorted(dummy.improve_province_priority.items(), key=lambda x:x[1], reverse=True ))
	priorities = sorted(dummy.improve_province_priority, key=dummy.improve_province_priority.get, reverse = True)
	print("priorities")
	for p in priorities:
		print(p)
	print ("options")
	options = dummy.ai_improve_province_options()
	for o in options:
		print (o)
	for p in priorities:
		if p in options:
			if p == "improve_fortifications" and dummy.goods["cannons"]["amount"] >= 1.5:
				dummy.ai_improve_fortifications()
			elif p == "improve_food_provice":
				dummy.ai_develop_province("food")
			elif p == "improve_iron_province":
				dummy.ai_develop_province("iron")
			elif p == "improve_coal_province":
				dummy.ai_develop_province("coal")
			elif p == "improve_wood_province":
				dummy.ai.develop_province("wood")
			elif p == "improve_cotton_province":
				dummy.ai_develop_province("cotton")
			elif p == "improve_gold_province":
				dummy.ai.develop_province("gold")
			elif p == "improve_spice_province":
				dummy.ai_develop_province("spice")
			elif p == "improve_dyes_province":
				dummy.ai_develop_province("dyes")
				break
			elif p == "build_steam_ship_yard":
				dummy.ai_build_steam_ship_yard()
