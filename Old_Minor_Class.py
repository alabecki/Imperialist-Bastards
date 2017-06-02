# Old Minors class Empire(Player):
from player_class import Player


class Old_minor(Player):
	def __init__ (self, _name, _human, number):
		Player.__init__(self, _name, _human, number)
		#super(Player, self).__init__(self, _name, _human)
		#super().__init__(_name, _human)
        # Basic Attributes
		self.stability = 0.0
		self.stability_mod = 0.0
        #General POP Attributes
		self.production_modifier = 1.0

		self.POP = 2.425
		self.freePOP = 2.0
		self.milPOP = 0.3

		self.midPOP = {
		"researchers": {"number": 0.025, "priority": 0.2},
		"officers": {"number": 0.025, "priority": 0.2},
		"bureaucrats": {"number": 0.025, "priority": 0.2},
		"artists": {"number": 0.025, "priority": 0.2},
		"managers": {"number": 0.025, "priority": 0.2}
		}

		self.numMidPOP = 0.125

        #Good and Resources
		self.resources = {
		"gold": 4.0,
		"food": 0.0,
		"iron": 0.0,
		"wood": 0.0,
		"coal": 0.0,
		"cotton": 0.0,
		"spice": 0.25,
		"dyes": 0.0
		}

		self.goods = {
		"parts": 0.0,
		"clothing": 0.2,
		"paper": 0.2,
		"cannon": 0.2,
		"furniture": 0.15,
		"chemicals": 0.0
		}


        #Technology
		self.technologies = set()
		self.techModifier = 0.75

        #diplomacy
		self.reputation = 0.5
		self.diplo_action = -1.0

        #Military

		self.military = {
			"irregulars": 2.0,
			"infantry": 0.0,
			"cavalry": 0.0,
			"artillery": 0.0,
			"frigates": 0.0,
			"iron_clad": 0.0
		}

		self.colonization = -10.0
