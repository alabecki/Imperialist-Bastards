# AI

from player_class import*
from market import*
from technologies import*
from random import*


import math

craft = {
	"parts" : "iron",
	"cannons" : "iron",
	"paper" : "wood",
	"clothing" : "cotton",
	"furniture" : "wood",
	"chemicals" : "coal"
	}

manufacture = {
	"parts": {"iron": 0.6, "coal": 0.3},
	"cannons": {"iron": 0.6, "coal": 0.3},
	"paper": {"wood": 0.9},
	"clothing": {"cotton": 0.8, "dyes": 0.1},
	"furniture": {"wood": 0.6, "cotton": 0.3},
	"chemicals": {"coal": 0.6}
			}




class AI(Player):
	def __init__(self, _name, _type, number, *args, **kwargs):
		super(AI, self).__init__(_name, _type, number, *args, **kwargs)

		self.resources = {
			"gold": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"food": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"iron": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"wood": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"coal": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"cotton": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"spice": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"dyes": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0}
		}

		self.goods = {
			"parts": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"clothing": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"paper": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"cannons": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"furniture": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0},
			"chemicals": {"amount": 0, "produces": 0, "needs": 0, "forecast": 0}
		}

		self.build_priority = {
			"frigates": 1,
			"iron_clad": 1,
			"parts_factory": 1,
			"clothing_factory": 0,
			"furniture_factory": 0,
			"paper_factory": 0,
			"cannon_factory": 0.5,
			"chemical_factory": 0,
			"improve_food_provice": 0.5,
			"improve_iron_province": 1,
			"improve_coal_province": 0,
			"improve_wood_province": 0,
			"improve_cotton_province": 0,
			"improve_gold_province": 1,
			"improve_spice_province": 1,
			"improve_dyes_province": 0,
			"improve_fortifications": 1,
			"build_steam_ship_yard": 1,
			"build_infantry": 1,
			"build_cavalry": 1,
			"build_artillery": 1,
			"build_irregulars": 1
		}


		self.objective = 0

		self.build_factory_priority = {
			"parts_factory": 1,
			"clothing_factory": 0,
			"furniture_factory": 0,
			"paper_factory": 0,
			"cannon_factory": 0.5,
			"chemical_factory": 0
		}

		self.improve_province_priority = {
			"improve_food_provice": 0.5,
			"improve_iron_province": 1,
			"improve_coal_province": 0,
			"improve_wood_province": 0,
			"improve_cotton_province": 0,
			"improve_gold_province": 1,
			"improve_spice_province": 1,
			"improve_dyes_province": 0,
			"improve_fortifications": 1,
			"build_steam_ship_yard": 1,
		}

		self.military_priority = {
			"infantry": 1,
			"cavalry": 1,
			"artillery": 1,
			"irregulars": 1,
			"iron_clad": 1,
			"frigates": 1
		}

		self.technology_priority = {
			"pre_industry_1": 6,
			"pre_industry_2": 6,
			"high_pressure_steam_engine": 10,
			"square_timbering": 4,
			"cotton_gin": 4,
			"steel_plows": 4,
			"saw_mill": 4,
			"cement": 2,
			"bessemer_process": 3,
			"muzzle_loaded_arms": 3,
			"breach_loaded_arms": 3,
			"machine_guns": 3,
			"indirect_fire": 3,
			"power_loom": 3,
			"chemistry": 4,
			"pulping": 2,
			"iron_clad": 4,
			"electricity": 3,
			"medicine": 3,
			"synthetic_dyes": 3,
			"fertlizer": 3,
			"dynamite": 3,
			"compound_steam_engine": 4,
			"telegraph": 2,
			"radio": 2,
			"mechanical_reaper": 2,
		}

		self.resource_priority = {
			"food":	1,
			"iron": 1,
			"coal": 0.2,
			"cotton": 0.75,
			"wood": 0.5,
			"spice": 1,
			"dyes": 0.75,
			"gold": 2
		}

		self.resourse_to_keep = {
			"food":	3,
			"iron": 3,
			"coal": 2,
			"cotton": 2,
			"wood": 2,
			"spice": 2,
			"dyes": 1.0,
			"gold": 1.0
		}


	def AI_set_objective(self, turn):
		if turn <= 10:
			print("WTF!!!")
			if self.military["frigates"] < 2:
				print("Navy????")
				self.objective = 1
				print(self.objective)
				return
			elif "high_pressure_steam_engine" in self.technologies and self.new_development >= 1 and len(self.ai_factory_options()) != 0:
				self.objective = 2
				return
			else:
				self.objective = 3
				return
		elif turn > 10:
			print("STILL WTF!!!!")
			opt = self.ai_improve_province_options()
			if len(opt) > 1 and self.new_development >= 1:
				self.objective = 4
				return
			elif "high_pressure_steam_engine" in self.technologies and self.new_development >= 1 and len(self.ai_factory_options()) != 0:
				print("Factory?????")
				self.objective = 2
				return
			elif self.military["frigates"] < 3:
				self.objecive = "navy"
				return
			else:
				self.objective = 3
				return



	def attempt_objective(self, market):
		print("Attempting objective: - %s" % (self.objective))
		print("Has %s New Development Points \n" % (self.new_development))
		if self.AP >= 1:
			if self.objective == 1:
				print("Wants to build frigate")
				if self.goods["cannons"]["amount"] > 1:
					print("Wants cannons")
					decision = self.ai_decide_on_good("cannons", market)
					self.ai_obtain_good("cannons", decision)
				if self.resources["wood"]["amount"] < 1:
					get = self.ai_buy("wood", 1, market)

				if self.resources["cotton"]["amount"] < 1:
					get = self.ai_buy("cotton", 1, market)
					if get == "fail":
						return
				self.ai_build_frigates()
			if self.objective == 2:
				print("Wants to build factory")
				if self.goods["parts"]["amount"] < 1:
					print("Wants machine parts")
					decision = self.ai_decide_on_good("parts", market)
					self.ai_obtain_good("parts", decision, market)
				if self.resources["iron"]["amount"] < 1:
					get = self.ai_buy("iron", 1, market)
					if get == "fail":
						return
				priorities = (sorted(self.build_factory_priority.items(), key=lambda x:x[1], reverse=True ))
				options = self.ai_factory_options()
				for p in priorities:
					if p in options:
						self.ai_build_build_factory(p)
			if self.objective == 4:
				print("Wants to improve province")
				if self.goods["parts"]["amount"] < 1:
					print("Wants parts")
					decision = self.ai_decide_on_good("parts", market)
					self.ai_obtain_good("parts", decision, market)
				if self.resources["iron"]["amount"] < 0.5:
					get = self.ai_buy("iron", 1, market)
					if get == "fail":
						return
				if self.resources["wood"]["amount"] < 1:
					get = self.ai_buy("wood", 1, market)
					if get == "fail":
						return
				priorities = (sorted(self.improve_province_priority.items(), key=lambda x:x[1], reverse=True ))
				options = self.ai_improve_province_options()
				for p in priorities:
					if p in options:
						if p == "improve_fortifications" and self.goods["cannons"]["amount"] >= 1:
							self.ai_improve_fortifications()
							return
						elif p == "improve_food_provice":
							self.ai_develop_province("food")
							return
						if p == "improve_iron_province":
							self.ai_develop_province("iron")
							return
						if p == "improve_coal_province":
							self.ai_develop_province("coal")
							return
						if p == "improve_wood_province":
							self.ai.develop_province("wood")
							return
						if p == "improve_cotton_province":
							self.ai_develop_province("cotton")
							return
						if p == "improve_gold_province":
							self.ai.develop_province("gold")
							return
						if p == "improve_spice_province":
							self.ai_develop_province("spice")
							return
						if p == "improve_dyes_province":
							self.ai_develop_province("dyes")
							return
						if p == "build_steam_ship_yard":
							self.ai_build_steam_ship_yard()
							return
			if self.objective == 3:
				print("Wants to build army")
				if self.goods["cannons"]["amount"] < 1.0:
					print("Wants to get cannons")
					decision = self.ai_decide_on_good("cannons", market)
					self.ai_obtain_good("cannons", decision, market)
				#priorities = (sorted(self.military_priority(), key=lambda x:x[1], reverse=True ))
				priorities = sorted(self.military_priority, key=self.military_priority.get, reverse = True)
				for p in priorities:
					if p == "infantry":
						if self.goods["clothing"]["amount"] >= 0.15 and self.freePOP >= 0.15:
							self.ai_build_infantry()
					if p == "cavalry":
						if self.goods["clothing"]["amount"] >= 0.1 and self.resources["food"]["amount"] >= 0.1 and self.freePOP >= 0.15:
							self.ai_build_cavalry()
					if p == "artillery":
						if self.goods["clothing"]["amount"] >= 0.1 and self.freePOP >= 0.15 and self.goods["cannons"]["amount"] >= 2:
							self.ai_build_artillery()
					if p == "irregulars":
						if self.goods["clothing"]["amount"] >= 0.5 and self.freePOP >= 0.15:
							self.ai_build_irregulars()
					if p == "iron_clad":
						if "iron_clad" in self.technologies and self.goods["parts"]["amount"] >= 1 and self.resources["iron"]["amount"] >= 1 and self.steam_ship_yard == True:
							self.ai_build_ironclad()
					if p == "frigates":
						if(self.resources["wood"]["amount"] >= 1 and self.resources["cotton"]["amount"] >= 1 and self.goods["cannons"]["amount"] >= 1 and "iron_clad" not in self.technologies and self.freePOP >= 0.15):
							self.ai_build_frigates()


	def ai_obtain_good(self, _type, decision, market):
		if decision == "manufacture_prepare":
			for i in manufacture[_type]:
				material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2 + 0.2)
				material_max = 1000
				for i in manufacture[_type]:
					temp = int((manufacture[_type][i] * material_mod)/self.resources[i] + 0.2)
					if temp < material_max:
						material_max = temp
				need = int(5 - material_max)
				for i in manufacture[_type]:
					get = self.ai_buy(i, need, market)
					if get == "fail":
						break
				self.ai_factory_production(_type)
		elif decision == "buy":
			self.ai_buy(_type, 1, market)
		elif decision == "craft_ready":
			self.ai_craftman_production(_type)
		else:
			get = self.ai_buy(craft[_type], 1, market)
			if get == "sucess":
				self.ai_craftman_production(_type)


	def assign_priorities_to_provs(self):
		for p, prov in self.provinces.items():
			kind = prov.resource
			prov.AI_priority = self.resource_priority[kind] * prov.quality
		sorted_provinces = sorted(self.provinces.values(), key = lambda x: (x.AI_priority), reverse = True)
		for k, v in self.resource_priority.items():
			print(k, v)
		return sorted_provinces

	def AI_reset_POP(self):
		for p, prov in self.provinces.items():
			if prov.worked == True:
				prov.worked = False
				self.freePOP += 1
		while self.proPOP >= 1:
			self.proPOP -= 1
			self.freePOP += 1


	def AI_assign_POP(self):
		#priorities = (sorted(self.resource_priority.items(), key=lambda x:x[1], reverse=True )
		priorities = self.assign_priorities_to_provs()
		desired_producers = len(self.factories) + 2
		#min_producers = int(self.freePOP/3.25)
		#min_producers = 2
		for i in range(desired_producers):
			self.proPOP += 1
			self.freePOP -=1
		count = 0
		while self.freePOP >= 1 and count < len(self.provinces):
			for p in priorities:
				temp = p.name
				if temp in self.provinces.keys():
					self.provinces[temp].worked = True
					print(self.provinces[temp].worked)
					self.freePOP -= 1
					if self.freePOP < 1:
						break
					count += 1
		while self.freePOP >= 1.5:
			self.proPOP += 1
			self.freePOP -=1


	def AI_sell_surplus(self, market):
		for r, resource in self.resources.items():
			if r == "gold":
				continue
			if resource["amount"] > self.resourse_to_keep[r]:
				amount = int(resource["amount"] - self.resourse_to_keep[r])
				if amount >= 1:
					self.ai_sell(r, amount, market)
		if self.goods["clothing"]["amount"] > self.goods["clothing"]["needs"] * 2.3:
			amount = int(self.goods["clothing"]["amount"] - self.goods["clothing"]["needs"] * 2.3)
			if amount >= 1:
				self.ai_sell("clothing", amount, market)
		if self.goods["furniture"]["amount"] > self.goods["furniture"]["needs"] * 2.1:
			amount = int(self.goods["furniture"]["amount"] - self.goods["furniture"]["needs"] * 2.1)
			if amount >= 1:
				self.ai_sell("furniture", amount, market)
		if self.goods["paper"]["amount"] > self.goods["paper"]["needs"] * 2.1:
			amount = int(self.goods["paper"]["amount"] - self.goods["paper"]["needs"] * 2.1)
			if amount >= 1:
				self.ai_sell("paper", amount, market)
		if self.goods["cannons"]["amount"] > 5:
			amount = int(self.goods["cannons"]["amount"] - 5)
			if amount >= 1:
				self.ai_sell("cannons", amount, market)
		if self.goods["chemicals"]["amount"] > 4:
			amount = int(self.goods["chemicals"] - 4)
			if amount >= 1:
				self.ai_sell("chemicals", amount, market)


	def view_AI_inventory(self):
		print("%s Inventory \n" % (self.name))
		for r, resource in self.resources.items():
			for i, item in resource.items():
				print (r, i, item)
		for g, good in self.goods.items():
			for i, item in good.items():
				print(g, i, item)

	def calculate_resource_production(self):
		for k, v in self.resources.items():
			v["produces"] = 0
		stab_rounds = round(self.stability * 2) / 2
		for k, p in self.provinces.items():
			if p.worked == True:
				self.resources[p.resource]["produces"] += development_map[p.development_level] * stability_map[stab_rounds] * p.quality

	def calculate_resource_need(self):
		self.resources["food"]["needs"] = (self.numLowerPOP * 0.2) + (self.numMidPOP * 0.3) + self.military["cavalry"] * 0.1
		self.resourse_to_keep["food"] = self.resources["food"]["needs"] * 1.25
		self.resources["spice"]["needs"] = self.numMidPOP * 0.3
		self.resources["coal"]["needs"] =  0.3 * self.number_developments

	def calculate_goods_need(self):
		self.goods["clothing"]["needs"] = (self.numLowerPOP * 0.1) + (self.numMidPOP * 0.2)
		self.goods["furniture"]["needs"] = (self.numLowerPOP * 0.05) + (self.numMidPOP * 0.2)
		self.goods["paper"]["needs"] = self.numMidPOP * 0.4
		self.goods["cannons"]["needs"] =  self.midPOP["officers"]["number"] * 0.3
		print ("Mid POPs: %s " % (self.numMidPOP))

	def calculate_resource_forecast(self):
		for k, v in self.resources.items():
			v["forecast"] = (v["amount"] + v["produces"]) - v["needs"]
			if v["produces"] < v["needs"]:
				self.resource_priority[k] + 0.25
			if v["amount"] > self.numLowerPOP * 1.25:
				self.resource_priority[k] - 0.25


	def calculate_goods_forecast(self):
		for k, v in self.goods.items():
			v["forecast"] = (v["amount"] + v["produces"]) - v["needs"]


	def ai_decide_on_good(self, _type, market):
		print("Wants to  get %s \n" % (_type))
		price_to_buy = market.buy_price(_type)
		print("Price to buy %s" % (price_to_buy))
		price_to_craft = market.buy_price(craft[_type]) * 1.2
		print("price to craft %s " % (price_to_craft))
		material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		price_to_man = 0
		for i in manufacture[_type]:
			price_to_man += market.buy_price(i) * int(manufacture[_type][i] * material_mod)
		if _type in self.factories:
			material_max = 1000
			for i in manufacture[_type]:
				temp = int((manufacture[_type][i] * material_mod)/self.resources[i])
				if temp < material_max:
					material_max = temp
			if material_max >= 3:
				print("Make w factory")
				return "manufacture_ready"
			else:
				if (price_to_man * 1.3) < price_to_buy and market.market[manufacture][type][1] >= 3:
					return "manufacture_prepare"
		elif (price_to_buy < price_to_craft * 1.7 and market.market[_type] >= 1):
			print("Decide to buy good")
			return "buy"
		elif self.resources[craft[_type]]["amount"] > 1.2:
			print("Decide to craft good")
			return "craft_ready"
		elif market.market[craft[_type]] >= 2:
			print("Buy materail then craft")
			return "craft_prepare"
		else:
			print("Decide to buy good")
			return "buy"



	def fulfill_needs(self, market):
		for k, v in self.resources.items():
			if v["forecast"] < 0.0 and k != "gold":
				amount = math.ceil(abs(v["forecast"]))
				print("Amount need" + str(amount))
				self.ai_buy(k, amount, market)
		for k, v in self.goods.items():
			if v["forecast"] < 0.0:
				amount = math.ceil(abs(v["forecast"]))
				if self.AP < 1:
					self.ai_buy(k, amount, market)
					continue
				decision = self.ai_decide_on_good(k, market)
				self.ai_obtain_good( k, decision, market)


	def ai_buy(self, _type, _amount, market):
		stock = market.market[_type]
		if (stock < _amount):
			_amount = stock
			if _amount == 0:
				return "fail"
		price = market.total_buy_price(_type, _amount)
		while self.resources["gold"]["amount"] < price:
			#print("Go to raise money")
			#self.ai_raise_money(market)
			print("Not enough money")
			return "fail"
		else:
			print("Actually buying something?: %s" % (_type))
			self.resources["gold"]["amount"] -= price
			market.gold += price
			if _type in market.resources:
				self.resources[_type]["amount"]  += _amount
				return "sucess"
			else:
				if(_type == "chemicals"):
					self.goods["chemicals"]["amount"] += 2* _amount
					return "sucess"
				else:
					self.goods[_type]["amount"] += _amount
					return "sucess"

	def ai_raise_money(self, market):
		_type = self.ai_choose_sell()
		self.ai_sell(_type, 1, market)


	def ai_choose_sell(self):
		max_good_prod =  " "
		max_amount = 0
		for k, v in self.goods.items():
			if v["produces"] >= max_amount:
				max_good_prod = k
				if self.goods[max_good_prod]["forecast"] > 1:
					return max_good_prod
		max_res_prod = " "
		max_amount = 0
		for k, v in self.resources.items():
			if v["produces"] > max_amount:
				max_res_prod = k
		if self.resources[max_res_prod]["forecast"] > 1:
			return max_res_prod
		good_most = " "
		max_amount = 0
		for k, v in self.goods.items():
			if v["forecast"] > max_amount:
				good_most = v
		if self.goods[good_most] > 2:
			return good_most
		resource_most = " "
		max_amount = 0
		for k, v in self.resources.items():
			if v["forecast"] > max_amount:
				resource_most = v
		if self.resources[resource_most] > 2:
			return resource_most

	def ai_sell(self, _type, amount, market):
		print("Try to see type %s, amount %s" % (_type, amount))
		price = market.total_sell_price(_type, amount)
		if(market.gold < price):
			print(" %s was unable to sell %s because the market was broke \n" % (self.name, _type))
			return
		market.gold -= price
		self.resources["gold"]["amount"] += price
		if _type in market.resources:
			self.resources[_type]["amount"] -= amount
		elif _type in market.goods:
			if _type == "chemicals":
				self.goods["chemicals"] -= 2 * amount
			else:
				self.goods[_type]["amount"] -= amount
			self.new_development +=  amount * 0.1


	def ai_factory_production(self, _type):
		print('Factory Production++++++++++++++++++++++++++++++++++++++++++++++++++')
		stab_rounds = round(self.stability * 2) / 2
		material_mod = 1 - (self.midPOP["managers"]["number"])/(self.proPOP*2)
		material_max = 1000
		for i in manufacture[_type]:
			temp = int((manufacture[_type][i] * material_mod)/self.resources[i])
			if temp < material_max:
				material_max = temp
		max_amount = self.factory_throughput * stability_map[stab_rounds]
		if(_type == "parts"):
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		elif(_type == "cannons"):
			if("bessemer_process" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		elif(_type == "paper"):
			if("pulping" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		elif(_type == "furniture"):
			if("electricity" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		elif(_type == "clothing"):
			if("power_loom" in self.technologies):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		elif(_type == "chemicals"):
				max_amount = (self.factory_throughput + 4) * stability_map[stab_rounds]
		amount = min[material_max, max_amount]
		#if amount < 2.5:
	#		return False
		for i in manufacture[_type]:
			self.resources[i] -= manufacture[_type][i] * amount * material_mod
		self.goods_produced[_type] += amount
		print("Produced %s %s " % (amount, _type))
		self.AP -= 1
		return True

	def ai_craftman_production(self, _type):
		self.resources[craft[_type]]["amount"] -= 1.2
		self.goods_produced[_type] += 1.0
		self.AP -= 1
		print("Crafted %s" % (_type))
		print("AP points remaining__: %s \n" % (self.AP))
		self.new_development -= 0.001
		return

	def ai_modify_priorities_from_province(self, resource):
		if resource == "food":
			self.technology_priority["steel_plows"] += 1
			self.technology_priority["mechanical_reaper"] += 1
			self.technology_priority["fertlizer"] += 1
			self.improve_province_priority["improve_food_provice"] + 0.5
		if resource == "iron":
			self.technology_priority["square_timbering"] += 1
			self.technology_priority["dynamite"] += 1
			self.technology_priority["bessemer_process"] += 1
			self.technology_priority["iron_clad"] += 0.5
			self.technology_priority["muzzle_loaded_arms"] += 1
			self.technology_priority["breach_loaded_arms"] += 1
			self.technology_priority["machine_guns"] += 1
			self.technology_priority["indirect_fire"] += 1
			self.improve_province_priority["improve_iron_province"] += 0.75
			self.build_factory_priority["parts_factory"] += 1
			self.improve_province_priority["improve_coal_province"] += 0.5
			self.build_factory_priority["cannon_factory"] + 0.5
			self.improve_province_priority["build_steam_ship_yard"] += 0.75
			self.military_priority["iron_clad"] += 1
			self.military_priority["frigates"] + 0.4
		if resource == "coal":
			self.technology_priority["square_timbering"] += 1
			self.technology_priority["dynamite"] += 0.5
			self.technology_priority["bessemer_process"] += 0.5
			self.technology_priority["chemistry"] += 1
			self.technology_priority["synthetic_dyes"] + 0.5
			self.technology_priority["fertlizer"] + 1
			self.technology_priority["medicine"] + 1
			self.improve_province_priority["improve_coal_province"] += 0.5
			self.build_factory_priority["parts_factory"] += 0.5
			self.build_factory_priority["cannon_factory"] += 0.5
			self.build_factory_priority["chemical_factory"] += 0.75
		if resource == "wood":
			self.technology_priority["saw_mill"] += 1
			self.technology_priority["pulping"] += 1
			self.technology_priority["compound_steam_engine"] += 1
			self.build_factory_priority["paper_factory"] += 1
			self.build_factory_priority["furniture_factory"] += 0.65
			self.improve_province_priority["improve_wood_province"] += 0.75
			self.military_priority["frigates"] + 0.4
		if resource == "cotton":
			self.technology_priority["cotton_gin"] += 1
			self.technology_priority["power_loom"] += 1
			self.technology_priority["compound_steam_engine"] += 1
			self.technology_priority["synthetic_dyes"] + 2
			self.technology_priority["chemistry"] += 1
			self.build_factory_priority["clothing_factory"] += 1
			self.build_factory_priority["furniture_factory"] += 0.35
			self.build_factory_priority["chemical_factory"] += 0.3
			self.improve_province_priority["improve_cotton_province"] += 0.8
			self.military_priority["frigates"] + 0.4
		if resource == "dyes":
			self.technology_priority["synthetic_dyes"] -= 1
			self.technology_priority["compound_steam_engine"] += 1
			self.improve_province_priority["improve_dyes_province"] += 1
		if resource == "spice":
			self.technology_priority["steel_plows"] += 1
			self.improve_province_priority["improve_spice_province"] += 2.5
		if resource == "gold":
			self.technology_priority["dynamite"] += 1
			self.improve_province_priority["improve_gold_province"] += 2.5


	def choose_technology(self):
		available = []
		for k, t in technology_dict.items():
			if(k not in self.technologies and t["requirement"] in self.technologies):
				print(k, t)
				available.append(k)
		options = []
		for t in available:
			if(technology_dict[k]["cost"] <= self.research):
				options.append(t)
		print("Options: %s \n" % (options))
		if len(options) == 0:
			return None
		#priorities = sorted([self.technology_priority(v,k) for (k,v) in self.technology_priority], reverse=True)
		#priorities = (sorted(self.technology_priority.keys(), key=lambda x:x[1]))
		priorities = sorted(self.technology_priority, key=self.technology_priority.get, reverse = True)
		for p in priorities:
			if p in options:
		#priorities = sorted(self.technology_priority, key=my_dict.get)
				self.ai_research_tech(p)
				return



	def ai_research_tech(self, choice):
		print("Researched  %s ______________________________________________________ \n" % (choice))
		self.research -= technology_dict[choice]["cost"]
		self.technologies.add(choice)
		if(choice == "muzzle_loaded_arms"):
			self.irregulars["attack"] += 0.1
			self.irregulars["defend"] += 0.06
			self.infantry["attack"] += 0.25
			self.infantry["defend"] += 0.10
			self.cavalry ["attack"] += 0.20
			self.cavalry["defend"] += 0.10
			self.artillery["attack"] += 0.25
			self.artillery["defend"] += 0.10
			self.frigates["attack"] += 0.25
			self.frigates["attack"] += 0.25
		if(choice == "cement"):
			self.max_fortification += 0.1
			self.improve_province_priority["improve_fortifications"] += 0.25
		if(choice == "breach_loaded_arms"):
			self.irregulars["attack"] += 0.15
			self.irregulars["defend"] += 0.08
			self.infantry["attack"] += 0.30
			self.infantry["defend"] += 0.15
			self.cavalry["attack"] += 0.25
			self.cavalry["defend"] += 0.12
			self.artillery["attack"] += 0.30
			self.artillery["defend"] += 0.15
			self.frigates["attack"] += 0.30
			self.frigates["attack"] += 0.30
		if(choice == "machine_guns" ):
			self.irregulars["defend"] += 0.2
			self.infantry["defend"] += 1.0
			self.cavalry["defend"] + 0.15
		if(choice == "indirect_fire"):
			self.artillery["attack"] += 0.1
			self.artillery["defend"] += 0.5
			self.iron_clad["attack"] += 0.25
			self.iron_clad["defend"] += 0.25
		if(choice == "electricity"):
			self.production_modifier += 0.1
		if(choice == "medicine"):
			self.POP_growth_mod += 0.10
			self.chemicals.add("medicine")
		if(choice == "synthetic_dyes"):
			self.chemicals.add("dyes")
		if(choice == "fertlizer"):
			self.chemicals.add("fertlizer")
		if(choice == "telegraph"):
			self.production_modifier += 0.1
			self.stability_mod += 0.1
		if(choice == "radio"):
			self.stability_mod += 0.15

	def ai_improve_province_options(self):
		options = []
		if self.new_development > 1.0:
			for p, prov in self.provinces.items():
				if prov.resource == "food":
					max_dev = 0
					if("steel_plows" in self.technologies):
						max_dev = 1
					if("mechanical_reaper" in self.technologies):
						max_dev = 2
					if prov.development_level > max_dev:
						options.append("improve_food_provice")
				elif prov.resource == "iron":
					max_dev = 0
					if("square_timbering" in self.technologies):
						max_dev = 1
					if("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level > max_dev:
						options.append("improve_iron_provice")
				elif prov.resource == "coal":
					max_dev = 0
					if("square_timbering" in self.technologies):
						max_dev = 1
					if("dynamite" in self.technologies):
						max_dev = 2
					if prov.development_level > max_dev:
						options.append("improve_coal_provice")
				elif prov.resource == "cotton":
					max_dev = 0
					if("cotton_gin" in self.technologies):
						max_dev = 1
					if("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level > max_dev:
						options.append("improve_cotton_province_provice")
				elif prov.resource == "wood":
					max_dev = 0
					if("saw_mill" in self.technologies):
						max_dev = 1
					if("compound_steam_engine" in self.technologies):
						max_dev = 2
					if prov.development_level > max_dev:
						options.append("improve_wood_province")
				elif prov.resource == "spice":
					max_dev = 0
					if("steel_plows" in self.technologies):
						max_dev = 1
					if prov.development_level > max_dev:
						options.append("improve_spice_province")
				elif prov.resource == "gold":
					max_dev = 0
					if("dynamite" in self.technologies):
						max_dev = 1
					if prov.development_level > max_dev:
						options.append("improve_gold_province")
				elif prov.resource == "dyes":
					max_dev = 0
					if("compound_steam_engine" in self.technologies):
						max_dev = 1
					if prov.development_level > max_dev:
						options.append("improve_dyes_province")
		if self.resources["iron"]["amount"] >= 1 and self.steam_ship_yard == False and self.new_development > 1.0:
			options.append("build_steam_ship_yard")
		if (self.fortification == 1.0 or (self.fortification == 1.1 and "cement" in self.technologies)) and self.goods["cannons"]["amount"] >= 1:
			options.append("improve_fortifications")
		return options


	def ai_factory_options(self):
		options = []
		if "high_pressure_steam_engine" in self.technologies and self.new_development > 1.0:
			if "parts" not in self.factories:
				options.append("parts_factory")
			if "clothing" not in self.factories:
				options.append("clothing_factory")
			if "furniture" not in self.factories:
				options.append("furniture_factory")
			if "paper" not in self.factories:
				options.append("paper_factory")
			if "cannons" not in self.factories:
				options.append("cannon_factory")
			if "chemicals" not in self.factories and "chemistry" in self.technologies:
				options.append("chemical_factory")
		return options


	def ai_build_options(self):
		options = []
		if self.AP < 1:
			return options
		for k, v in self.build_priority.items():
			if(self.resources["wood"]["amount"] >= 1 and self.resources["cotton"]["amount"] >= 1 and self.goods["cannons"]["amount"] >= 1 and "iron_clad" not in self.technologies and self.freePOP >= 0.15):
				options.append("frigates")
			if(self.resources["iron"]["amount"] >= 1 and self.goods["parts"]["amount"] >=1 and self.goods["cannons"]["amount"] > 1 and "ironclads" in self.technologies and self.freePOP >= 0.15):
				options.append("iron_clad")
			if(self.goods["parts"]["amount"] >= 1 and self.resources["iron"]["amount"] > 1 and "high_pressure_steam_engine" in self.technologies and self.new_development > 1.0):
				if "parts" not in self.factories:
					options.append("parts_factory")
				if "clothing" not in self.factories:
					options.append("clothing_factory")
				if "furniture" not in self.factories:
					options.append("furniture_factory")
				if "paper" not in self.factories:
					options.append("paper_factory")
				if "cannons" not in self.factories:
					options.append("cannon_factory")
				if "chemicals" not in self.factories and "chemistry" in self.technologies:
					options.append("chemical_factory")
			if self.new_development > 1.0:
				for p, prov in self.provinces.items():
					if prov.resource == "food":
						max_dev = 0
						if("steel_plows" in self.technologies):
							max_dev = 1
						if("mechanical_reaper" in self.technologies):
							max_dev = 2
						if prov.development_level > max_dev:
							options.append("improve_food_provice")
					elif prov.resource == "iron":
						max_dev = 0
						if("square_timbering" in self.technologies):
							max_dev = 1
						if("dynamite" in self.technologies):
							max_dev = 2
						if prov.development_level > max_dev:
							options.append("improve_iron_provice")
					elif prov.resource == "coal":
						max_dev = 0
						if("square_timbering" in self.technologies):
							max_dev = 1
						if("dynamite" in self.technologies):
							max_dev = 2
						if prov.development_level > max_dev:
							options.append("improve_coal_provice")
					elif prov.resource == "cotton":
						max_dev = 0
						if("cotton_gin" in self.technologies):
							max_dev = 1
						if("compound_steam_engine" in self.technologies):
							max_dev = 2
						if prov.development_level > max_dev:
							options.append("improve_cotton_province_provice")
					elif prov.resource == "wood":
						max_dev = 0
						if("saw_mill" in self.technologies):
							max_dev = 1
						if("compound_steam_engine" in self.technologies):
							max_dev = 2
						if prov.development_level > max_dev:
							options.append("improve_wood_province")
					elif prov.resource == "spice":
						max_dev = 0
						if("steel_plows" in self.technologies):
							max_dev = 1
						if prov.development_level > max_dev:
							options.append("improve_spice_province")
					elif prov.resource == "gold":
						max_dev = 0
						if("dynamite" in self.technologies):
							max_dev = 1
						if prov.development_level > max_dev:
							options.append("improve_gold_province")
					elif prov.resource == "dyes":
						max_dev = 0
						if("compound_steam_engine" in self.technologies):
							max_dev = 1
						if prov.development_level > max_dev:
							options.append("improve_dyes_province")
			if "iron_clad" in self.technologies and self.goods["parts"]["amount"] >= 1 and self.resources["wood"]["amount"] >= 1 and self.resources["iron"]["amount"] >= 1 and self.steam_ship_yard == False and self.new_development > 1.0:
				options.append("build_steam_ship_yard")
			if (self.fortification == 1.0 or (self.fortification == 1.1 and "cement" in self.technologies)) and self.goods["cannons"]["amount"] >= 1:
				options.append("improve_fortifications")
			if self.goods["clothing"]["amount"] >= 0.15 and self.freePOP >= 0.15 and self.goods["cannons"]["amount"] >= 1:
				options.append("build_infantry")
			if self.goods["clothing"]["amount"] >= 0.1 and self.resources["food"]["amount"] >= 0.1 and self.freePOP >= 0.15 and self.goods["cannons"]["amount"] >= 1:
				options.append("build_cavalry")
			if self.goods["clothing"]["amount"] >= 0.1 and self.freePOP >= 0.15 and self.goods["cannons"]["amount"] >= 2:
				options.append("build_artillery")
			if self.goods["clothing"]["amount"] >= 0.5 and self.freePOP >= 0.15 and self.goods["cannons"]["amount"] >= 0.5:
				options.append("build_irregulars")
		return options


	def ai_choose_build(self):
		#priorities = sorted(self.build_priority, key=self.build_priority)
		#priorities = sorted(self.technology_priority, key=self.build_priority)
		#priorities = sorted([self.build_priority(v,k) for (k,v) in self.build_priority.items()], reverse=True)
		#priorities = sorted(self.build_priority)
		priorities = (sorted(self.build_priority.items(), key=lambda x:x[1], reverse=True ))
		options = self.ai_build_options()
		for p in priorities:
			if p in options:
				if p == "frigates":
					self.ai_build_frigates()
				if p == "iron_clad":
					self.ai_build_ironclad()
				if p == "parts_factory":
					self.ai_build_build_factory("parts")
				if p == "clothing_factory":
					self.ai_build_build_factory("clothing")
				if p == "paper_factory":
					self.ai_build_build_factory("paper")
				if p == "furniture_factory":
					self.ai_build_build_factory("furniture")
				if p == "cannon_factory":
					self.ai_build_build_factory("cannons")
				if p == "chemical_factory":
					self.ai_build_build_factory("chemicals")
				if p == "improve_food_provice":
					self.ai_develop_province("food")
				if p == "improve_iron_province":
					self.ai_develop_province("iron")
				if p == "improve_coal_province":
					self.ai_develop_province("coal")
				if p == "improve_wood_province":
					self.ai.develop_province("wood")
				if p == "improve_cotton_province":
					self.ai_develop_province("cotton")
				if p == "improve_gold_province":
					self.ai.develop_province("gold")
				if p == "improve_spice_province":
					self.ai_develop_province("spice")
				if p == "improve_dyes_province":
					self.ai_develop_province("dyes")
				if p == "improve_fortifications":
					self.ai_improve_fortifications()
				if p == "build_steam_ship_yard":
					self.ai_build_steam_ship_yard()
				if p == "build_infantry":
					self.ai_build_infantry()
				if item == "build_cavalry":
					self.ai_build_cavalry()
				if p == "build_artillery":
					self.ai_build_artillery()
				if p == "build_irregulars":
					self.ai_build_irregulars()

	def ai_build_frigates(self):
		self.AP -= 1
		self.goods["cannons"]["amount"] -= 1.0
		self.resources["cotton"]["amount"] -= 1.0
		self.resources["wood"]["amount"] -= 1.0
		self.military["frigates"] += 1.0
		self.freePOP -= 0.15
		self.milPOP += 0.15
		print("Frigate completed___________________________________________________________________")


	def ai_build_ironclad(self):
		self.AP -= 1
		self.goods["cannons"]["amount"] -= 1.0
		self.resources["iron"]["amount"] -= 1.0
		self.goods["parts"]["amount"] -= 1.0
		self.military["iron_clad"] += 1
		self.freePOP -= 0.15
		self.milPOP += 0.15
		print("Ironclad completed___________________________________________________________________________")

	def ai_build_build_factory(self, _type):
		if _type == "parts" or _type == "cannons":
			self.resource_priority["coal"] += 0.3
			self.resouece_priority["iron"] += 0.3
			self.resourse_to_keep["coal"] += 1
			self.resourse_to_keep["iron"] += 2
		if _type == "clothing":
			self.resource_priority["cotton"] += 0.5
			self.resource_priority["dyes"] += 0.5
			self.resourse_to_keep["cotton"] += 2.5
			self.resourse_to_keep["dyes"] += 0.5
		if _type == "paper":
			self.resource_priority["wood"] += 0.5
			self.resourse_to_keep["wood"] += 3
		if _type == "furniture":
			self.resource_priority["wood"] += 0.3
			self.resource_priority["cotton"] += 0.2
			self.resourse_to_keep["wood"] += 2
			self.resourse_to_keep["cotton"] += 1
		if _type == "chemicals":
			self.resource_priority["coal"] += 0.5
			self.resourse_to_keep["coal"] += 3
		self.AP -= 1
		self.resources["iron"]["amount"] -= 1.0
		self.goods["parts"]["amount"] -= 1.0
		self.factories.add(_type)
		self.stability_mod -= 0.05
		self.new_development -= 1
		print("%s Factory Completed ________________________________________________________" % (_type))

	def ai_develop_province(self, _type):
		options = []
		for p, province in self.provinces.items():
			if province.resource == _type:
				if check_if_prov_can_be_dev(p) == True:
					self.resources["iron"]["amount"] -= 0.5
					self.goods["parts"]["amount"] -= 1.0
					self.resources["wood"]["amount"] -= 1.0
					self.AP -= 1
					self.new_development -= 1
					self.provinces[prov].development_level += 1
					self.resource_priority["coal"] += 0.25
					self.number_developments += 1
					print("Developed %s province ____________________________" % (_type))

	def ai_improve_fortifications(self):
		self.AP -= 1
		self.goods["cannons"]["amount"] -= 1
		self.fortification += 0.1
		print("Fortification improved____________________________________________")

	def ai_build_steam_ship_yard(self):
		self.goods["parts"]["amount"] -= 1
		self.resources["iron"]["amount"] -= 1
		self.resources["wood"]["amount"] -= 1
		self.AP -1
		self.new_development -1
		self.steam_ship_yard = True
		print("steam_ship_yard completed!____________________________________________________")

	def ai_build_infantry(self):
			self.goods["clothing"]["amount"] -= 0.15
			self.freePOP -= 0.15
			self.milPOP += 0.15
			self.goods["cannons"]["amount"] -= 1.0
			self.military["infantry"] += 1.0
			print("Infantry build_____________________________________________________________")

	def ai_build_cavalry(self):
		self.resources["food"]["amount"] -= 0.15
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.goods["cannons"]["amount"] -= 1.0
		self.goods["clothing"]["amount"] -= 0.1
		self.military["cavalry"]["amount"] += 1.0
		print("Cavalry build_________________________________________________________________")

	def ai_build_artillery(self):
		self.goods["cannons"] -= 2.0
		self.goods["clothing"] -= 0.1
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.military["artillery"] += 1.0
		print("Artillary built_______________________________________________________________")

	def ai_build_irregulars(self):
		self.goods["cannons"] -= 0.5
		self.goods["clothing"] -= 0.1
		self.freePOP -= 0.15
		self.milPOP += 0.15
		self.military["artillery"] += 0.5

	def check_if_prov_can_be_dev(self, prov):
		if(self.provinces[prov].resource == "food"):
			max_dev = 0
			if("steel_plows" in self.technologies):
				max_dev = 1
			if("mechanical_reaper" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "iron" or self.provinces[prov].resource == "coal"):
			max_dev = 0
			if("square_timbering" in self.technologies):
				max_dev = 1
			if("dynamite" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "cotton"):
			max_dev = 0
			if("cotton_gin" in self.technologies):
				max_dev = 1
			if("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "wood"):
			max_dev = 0
			if("saw_mill" in self.technologies):
				max_dev = 1
			if("compound_steam_engine" in self.technologies):
				max_dev = 2
		elif(self.provinces[prov].resource == "spice"):
			max_dev = 0
			if("steel_plows" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "gold"):
			max_dev = 0
			if("dynamite" in self.technologies):
				max_dev = 1
		elif(self.provinces[prov].resource == "dyes"):
			max_dev = 0
			if("compound_steam_engine" in self.technologies):
				max_dev = 1
		if self.provinces[prov].development_level == max_dev:
			return False
		else:
			return True

	def collect_resources(self):
		print("%s collects resources: \n" % (self.name))
		stab_rounds = round(self.stability * 2) / 2
		for k, p in self.provinces.items():
			#if(self.provinces[i]["worked"] == True):
			if(p.worked == True):
				quality = p.quality
				dev = p.development_level
				if p.resource == "gold":
					if p.powered == True:
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality * 5
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource]["amount"] += gain
					else:
						gain = stability_map[stab_rounds] * p.quality * 5
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource]["amount"] += gain
				else:
					if p.powered == True:
						gain = development_map[dev] * stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource]["amount"] += gain
					else:
						gain = stability_map[stab_rounds] * p.quality
						print("%s gains %s %s" % (self.name, gain, p.resource))
						self.resources[p.resource]["amount"] += gain

	def collect_goods(self):
		print("%s collects: " % (self.name))
		for k, p in self.goods_produced.items():
			print("%s: %s " % (k, p))
			self.goods[k]["amount"] += p

	def payMaintenance(self):
		print("Do you really pay maintenance? __####################################################################")
		temp = self.calMaintenance()
		print("Temp:")
		for i in temp:
			print(i)
		stab_change = 0
		if(self.resources["food"]["amount"] < temp[0]):
			self.freePOP -= (self.resources["food"]["amount"]  - temp[0])
			self.stability -= 0.1
			stab_change -= 0.1
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["food"]["amount"]  = 0.0
			self.midGrowth = False
		else:
			self.resources["food"]["amount"]  -= temp[0]
		if(self.goods["clothing"]["amount"]  < temp[1]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.goods["clothing"]["amount"]  = 0.0
			self.midGrowth = False
		else:
			self.goods["clothing"]["amount"]  -= temp[1]
			self.new_development += temp[1] * 0.1
		if(self.goods["furniture"]["amount"]  < temp[2]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.midGrowth = False
			self.goods["furniture"]["amount"]  = 0.0
		else:
			self.goods["furniture"]["amount"]  -= temp[2]
			self.new_development += temp[2] * 0.1
		if(self.goods["paper"]["amount"]  < temp[3]):
			self.stability -= 0.05
			stab_change -= 0.05
			if self.stability < -3.0:
				self.stability = -3.0
			self.goods["paper"]["amount"]  = 0.0
			self.midGrowth = False
		else:
			self.goods["paper"]["amount"]  -= temp[3]
			self.new_development += temp[3] * 0.1
		if(self.resources["spice"]["amount"]  < temp[4]):
			self.stability -= 0.075
			stab_change -= 0.075
			if self.stability < -3.0:
				self.stability = -3.0
			self.resources["spice"]["amount"]  = 0.0
			self.midGrowth = False
		else:
			self.resources["spice"]["amount"]  -= temp[4]
			self.new_development += temp[4] * 0.1
		if(self.goods["cannons"]["amount"]  < temp[5]):
			temp2 = self.midPOP["officers"]["number"] * 0.9
			self.midPOP["officers"]["number"] -= temp2
			self.numMidPOP -= temp2
			self.freePOP += temp2
		else:
			self.goods["cannons"]["amount"]  -= temp[5]
			self.new_development += temp[5] * 0.1
		if(self.resources["coal"]["amount"] < 0.25 * self.number_developments):
			print("You do not have enough coal to run all your railroads this turn, only some will be powered \n")
			while(self.resources["coal"]["amount"]  >= 0.3 ):
				for k, prov in self.provinces.items():
					if(prov.development_level == 1):
						self.resources["coal"]["amount"]  -= 0.25
						self.provinces[prov].powered = True
					elif(prov.development_level == 2):
						self.resources["coal"]["amount"]  -= 0.5
						self.provinces(prov).powered = True
		else:
			self.resources["coal"]["amount"]  -= self.number_developments * 0.25
			for k, prov in self.provinces.items():
				prov.powered = True




	def popChange(self):
		if(self.resources["food"]["amount"] > 0.5):
			change =  self.POP * 0.02
			if(self.stability > 0):
				stab_rounds = round(self.stability * 2) / 2
				change += (self.POP * 0.02) * (stability_map[stab_rounds] * self.POP_growth_mod)
			mChemicals = (self.numMidPOP * 0.15)
			if(self.goods["chemicals"]["amount"] >= mChemicals):
				self.goods["chemicals"]["amount"] -= mChemicals
				change += 0.05 * self.numMidPOP
			self.freePOP += change
			self.numLowerPOP += change
			self.POP += change
			print("Population changed by %s " % (change))
