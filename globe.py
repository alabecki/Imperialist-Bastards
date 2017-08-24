#GLOBAL

#from player_class import*
#from combat import*

class Globe(object):

	def __init__ (self):

		defeated = []


		self.factories = {
			"parts":   0,
			"clothing":  0,
			"cannons":  0,
			"paper": 0,
			"furniture": 0,
			"chemicals": 0
		}

		self.culture = list([["a", 0]])
		self.research = list([["a", 0]])
		self.diplomacy = list([["a", 0]])
		self.colonization = list([["a", 0]])

		self.wealth = list()

		self.resources = {

			"gold": list(),
			"food": list(),
			"iron": list(),
			"wood": list(),
			"cotton": list(),
			"coal": list(),
			"dyes": list(),
			"spice": list(),
			"rubber": list(),
			"oil": list(),
		}

		self.goods = {

			"parts": [],
			"cannons": [],
			"clothing": [],
			"paper": [],
			"furniture": [],
			"chemicals": [],
			"gear": [],
			"radio": [],
			"telephone": [],
			"fighter": [],
			"auto": [],
			"tank": [],
			"frigates": [],
			"iron_clad": [],
			"battle_ship": [],
		}

		self.army_strength = []

		self.naval_strength = []

	def world_update(self, players):
		
		for p, player in players.items():
			self.wealth.append([p, player.resources["gold"]])

			self.goods['parts'].append([p, player.goods_produced["parts"]])
			self.goods['cannons'].append([p, player.goods_produced["cannons"]])
			self.goods['clothing'].append([p, player.goods_produced["clothing"]])
			self.goods['paper'].append([p, player.goods_produced["paper"]])
			self.goods['furniture'].append([p, player.goods_produced["furniture"]])
			self.goods['chemicals'].append([p, player.goods_produced["chemicals"]])
			self.goods['gear'].append([p, player.goods_produced["gear"]])
			self.goods['radio'].append([p, player.goods_produced["radio"]])
			self.goods['telephone'].append([p, player.goods_produced["telephone"]])
			self.goods['fighter'].append([p, player.goods_produced["fighter"]])
			self.goods['auto'].append([p, player.goods_produced["auto"]])
			self.goods['tank'].append([p, player.goods_produced["tank"]])
			self.goods['frigates'].append([p, player.goods_produced["frigates"]])
			self.goods['iron_clad'].append([p, player.goods_produced["iron_clad"]])
			self.goods['battle_ship'].append([p, player.goods_produced["battle_ship"]])

		self.wealth = self.wealth.sort(key = lambda x: x[1])


		self.culture = self.culture.sort(key = lambda x: x[1])
		self.research = self.research.sort(key = lambda x: x[1])
		self.diplomacy = self.diplomacy.sort(key = lambda x: x[1])
		self.colonize = self.colonization.sort(key = lambda x: x[1])


		for f in self.resources["food"]:
			print(f)

		self.resources['food']= self.resources['food'].sort(key = lambda x: x[1])
		self.resources['iron'] = self.resources['iron'].sort(key = lambda x: x[1])
		self.resources['cotton'] = self.resources['cotton'].sort(key = lambda x: x[1])
		self.resources['wood'] = self.resources['wood'].sort(key = lambda x: x[1])
		self.resources['coal'] = self.resources['coal'].sort(key = lambda x: x[1])
		self.resources['dyes'] = self.resources['dyes'].sort(key = lambda x: x[1])
		self.resources['spice'] = self.resources['spice'].sort(key = lambda x: x[1])
		self.resources['oil'] = self.resources['oil'].sort(key = lambda x: x[1])
		self.resources['rubber'] = self.resources['rubber'].sort(key = lambda x: x[1])
		self.resources['gold'] = self.resources['gold'].sort(key = lambda x: x[1])



		self.goods['parts'] = self.goods['parts'].sort(key = lambda x: x[1])
		self.goods['cannon'] = self.goods['cannons'].sort(key = lambda x: x[1])
		self.goods['clothing']= self.goods['clothing'].sort(key = lambda x: x[1])
		self.goods['furniture'] = self.goods['furniture'].sort(key = lambda x: x[1])
		self.goods['paper'] = self.goods['paper'].sort(key = lambda x: x[1])
		self.goods['chemicals'] = self.goods['chemicals'].sort(key = lambda x: x[1])
		self.goods['gear'] = self.goods['gear'].sort(key = lambda x: x[1])
		self.goods['radio'] = self.goods['radio'].sort(key = lambda x: x[1])
		self.goods['telephone'] = self.goods['telephone'].sort(key = lambda x: x[1])
		self.goods['auto'] = self.goods['auto'].sort(key = lambda x: x[1])
		self.goods['fighter'] = self.goods['fighter'].sort(key = lambda x: x[1])
		self.goods['tank'] = self.goods['tank'].sort(key = lambda x: x[1])
		self.goods['frigates'] = self.goods['frigates'].sort(key = lambda x: x[1])
		self.goods['iron_clad'] = self.goods['iron_clad'].sort(key = lambda x: x[1])
		self.goods['battle_ship'] = self.goods['battle_ship'].sort(key = lambda x: x[1])

		for k, v in players.items():
			att_str = v.calculate_base_attack_strength()
			def_str = v.calculate_base_defense_strength()
			a_str = (att_str + def_str)/2
			self.army_strength.append([k, a_str])

			nav_str = v.calculate_naval_strength()
			self.naval_strength.append([k, nav_str])

		self.army_strength = self.army_strength.sort(key = lambda x: x[1])
		self.naval_strength = self.naval_strength.sort(key = lambda x: x[1])
		


















		