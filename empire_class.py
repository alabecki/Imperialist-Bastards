
from player_class import Player

class Empire(Player):
	def __init__(self, _name, _human, *args, **kwargs):
		super(Empire, self).__init__(_name, _type, *args, **kwargs)

		self.name = _name
		self.type = "Empire"
		#Player.__init__(self, _name, _human)
		#super(Player, self).__init__()
		#super(Player, self).__init__(_name, _human)
		# Basic Attributes
		self.stability = -1.0
		self.stability_mod = 1.0

		#General POP Attributes
		self.production_modifier = 1.0
		self.milPOP = 0.9

		self.midPOP = {
		"researchers": {"number": 0.05, "priority": 0.2},
		"officers": {"number": 0.05, "priority": 0.2},
		"bureaucrats": {"number": 0.05, "priority": 0.2},
		"artists": {"number": 0.05, "priority": 0.2},
		"managers": {"number": 0.05, "priority": 0.2}
		}

		self.numMidPOP = 0.25

        #Good and Resources
		self.resources = {
		"gold": 12.0,
		"food": 0.0,
		"iron": 0.0,
		"wood": 0.0,
		"coal": 0.0,
		"cotton": 0.0,
		"spice": 0.5,
		"dyes": 0.1
		}

		self.goods = {
		"parts": 0.0,
		"clothing": 0.5,
		"paper": 0.5,
		"cannons": 0.25,
		"furniture": 0.25,
		"chemicals": 0.0
		}


        #Technology
		self.technologies = set()
		self.techModifier = 0.75

        #diplomacy
		self.reputation = 0.5
		self.diplo_action = 0.0

        #Military

		self.military = {
			"irregulars": 4.0,
			"infantry": 0.0,
			"cavalry": 1.0,
			"artillery": 0.0,
			"frigates": 1.0,
			"iron_clad": 0.0
		}

		self.colonization = -5.0
