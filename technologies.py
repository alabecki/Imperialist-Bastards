#Technologies
#Each has a:
#name
#
 #technologies = {
#    name: {requirements: {A, B, C}, cost: int}
#
#}

technology_dict = {
	"basic_civ": {"requirement": {}, "cost": 1, "min_mid": 0},
	"pre_modern": {"requirement": {"basic_civ"}, "cost": 2, "min_mid": 0},
	"professional_armies": {"requirement": {"pre_modern"}, "cost": 1, "min_mid": 0},
	"flint_lock": {"requirement": {"pre_industry"}, "cost": 1, "min_mid": 0},
	"pre_industry": {"requirement": {"pre_modern"}, "cost": 2, "min_mid": 0},
	"high_pressure_steam_engine": {"requirement": {"pre_industry"}, "cost": 1, "min_mid": 1},
	"square_timbering": {"requirement": {"high_pressure_steam_engine"}, "cost": 2, "min_mid": 1},
	"cotton_gin": {"requirement": {"high_pressure_steam_engine"}, "cost": 2, "min_mid": 1},
	"steel_plows": {"requirement": {"pre_industry"}, "cost": 2, "min_mid": 1},
	"saw_mill": {"requirement": {"high_pressure_steam_engine"}, "cost": 2, "min_mid": 1},
	"cement": {"requirement": {"square_timbering"}, "cost": 2, "min_mid": 2},
	"bessemer_process": {"requirement": {"square_timbering"}, "cost": 3, "min_mid": 2},
	"muzzle_loaded_arms": {"requirement": {"flint_lock", "high_pressure_steam_engine"}, "cost": 3, "min_mid": 3},
	"breach_loaded_arms": {"requirement": {"muzzle_loaded_arms", "bessemer_process"}, "cost": 3, "min_mid": 4},
	"machine_guns": {"requirement": {"mechanical_reaper", "breach_loaded_arms"}, "cost": 5, "min_mid": 6},
	"indirect_fire": {"requirement": {"dynamite"}, "cost": 5, "min_mid": 9},
	"power_loom": {"requirement": {"cotton_gin"}, "cost": 3, "min_mid": 2},
	"chemistry": {"requirement": {"power_loom"}, "cost": 4, "min_mid": 3},
	"pulping": {"requirement": {"chemistry"}, "cost": 4, "min_mid": 3},
	"mechanical_reaper": {"requirement": {"power_loom", "steel_plows"}, "cost": 4, "min_mid": 4},
	"ironclad": {"requirement": {"breach_loaded_arms", "compound_steam_engine"}, "cost": 5, "min_mid": 8},
	"electricity": {"requirement": {"chemistry"}, "cost": 5, "min_mid": 6},									#electrical gear factory, rubber
	"medicine": {"requirement": {"chemistry"}, "cost": 5, "min_mid": 7},
	"synthetic_dyes": {"requirement": {"fertilizer"}, "cost": 5, "min_mid": 8},					
	"fertilizer": {"requirement": {"chemistry"}, "cost": 5, "min_mid": 8},
	"dynamite": {"requirement": {"fertilizer"}, "cost": 5, "min_mid": 8},
	"compound_steam_engine": {"requirement": {"bessemer_process", "chemistry"}, "cost": 5, "min_mid": 8},
	"telegraph": {"requirement": {"electricity"}, "cost": 5, "min_mid": 7},
	"radio": {"requirement": {"telephone"}, "cost": 7, "min_mid": 10},									#radio factory
	"oil_drilling": {"requirement": {"dynamite"}, "cost": 6, "min_mid": 10},				#oil resource
	#"photography": {"requirement": {"electricity"}, "cost": 3, "min_mid": 1.0},			
	"combustion": {"requirement": {"oil_drilling", "compound_steam_engine"}, "cost": 6, "min_mid": 11},		
	"flight": {"requirement": {"combustion", "machine_guns"}, "cost": 8, "min_mid": 12},		# plane factory
	"automobile": {"requirement": {"combustion", "radio"}, "cost": 8, "min_mid": 13},					# auto factory
	"telephone": {"requirement": {"telegraph"}, "cost": 5, "min_mid": 8},									# phone factory
	"rotary_drilling": {"requirement": {"automobile"}, "cost": 9, "min_mid": 16},
	"mobile_warfare": {"requirement": {"automobile", "flight"}, "cost": 8, "min_mid": 14},			# tanks
	"bombers": {"requirement": {"flight", "automobile"}, "cost": 8, "min_mid": 16}, 
	"oil_powered_ships": {"requirement": {"combustion", "indirect_fire"}, "cost": 7, "min_mid": 11},				# Battleship - level 3 port
	"synthetic_oil": { "requirement":{"oil_powered_ships", "mobile_warfare"}, "cost": 10, "min_mid": 16},		# Use chemicals for oil (3 for 1)
	"synthetic_rubber": {"requirement": {"oil_powered_ships", "mobile_warfare"}, "cost": 10, "min_mid": 16},  # Use chemicals for rubber (3 for 1)
	"radar": {"requirement": {"radio", "flight"}, "cost": 10, "min_mid": 16},
	"rockets": {"requirement": {"synthetic_oil"}, "cost": 10, "min_mid": 18},
	"early_computers": {"requirement": {"radar"}, "cost": 12, "min_mid": 18},
	"atomic_bomb": {"requirement": {"rockets", "early_computers"}, "cost": 20, "min_mid": 20}
}


tech_descriptions = {
	"basic_civ": """The minimal technology level of any nation.""",
	"pre_modern": """Your 'civilization' is not entirely savage - but still pretty backward. No immediate effect.
	(Requires: basic_civ) """,
	"professional_armies": """our armies are now composed of well trained professionals rather than ragtag
	 bands of ruffians. Effects: increases attack and defense of all units by 0.15, except 0.2 for frigates.(Requires: pre_modern)""",
	"flint_lock": """You have moved beyond primitive muskets and have really come into the age of gunpowder! 
	Effects: Infantry att +0.1 def +0.2,  Cavalry att +0.2 def +0.1  Artillery att +0.3, def +0.1, Frigates att + 0.25. 
	(Requires: pre_industry)""",
	"pre_industry": """One small step in the direction of being a real nation. No immediate effect.
	(Requires: pre_modern)""",
	"high_pressure_steam_engine": """Your nation may finally embark upon the road of modern industrialization!
	Effect: You may now construct Level 1 Factories of the following kinds: Parts, Arms, Clothing, Paper, and Furniture. 
	(Requires: pre_industry)""",
	"square_timbering": """Effect: You may now develop your Iron provinces to Level 1. 
	(Requires: high_pressure_steam_engine)""",
	"cotton_gin": """Effect: May develop Cotton provinces to Level 1. (Requires: high_pressure_steam_engine)""",
	"steel_plows": """Effect: May develop Food provinces to Level 1 (Requires: pre_industry)""",
	"saw_mill": """Effect: May develop Wood provinces to Level 1 (Requires: high_pressure_steam_engine)""",
	"cement": """Increases Max Fortification Level by 0.1 (Requires: square_timbering) """,
	"bessemer_process": """May upgrade Parts and Arms factories to Level 2 (Requires: square_timbering)""",
	"muzzle_loaded_arms": """Effects: Infantry att +0.3 def +0.1,  Cavalry att +0.2 def +0.05  Artillery att +0.3 def +0.1. Frigates +0.25  
	(Requires: high_pressure_steam_engine and flint_lock)""",
	"breach_loaded_arms": """Effects: Infantry att +0.35 def +0.2,  Cavalry att +0.25 def +0.1  Artillery att +0.35 def +0.2, Frigates att +0.35 
	(Requires: muzzle_loaded_arms and bessemer_process)""",
	"machine_guns": """Effects: Infantry def +1  Cavalry def +0.1 (Requires: breach_loaded_arms and mechanical_reaper""",
	"indirect_fire": """Artillery att + 0.15 def +0.5, Iron Clad att + 0.25 (Requires: dynamite""",
	"power_loom": """May upgrade Clothing factory to Level 2 (Requires: cotton_gin)""",
	"chemistry": """"May Construct Level 1 Chemical factory and Rubber Provinces may produce Rubber if improved to Level 1.
	(Requires: power_loom)""",
	"pulping": """May upgrade Paper factory to Level 2. (Requires: chemistry)""",
	"mechanical_reaper": """May develop Food provinces to Level 2 (Requires: power_loom and steel_plows)""",
	"ironclad": """May upgrade Shipyard to Level 2, which permits the construction of Iron Clad ships. 
	(Requires: breach_loaded_arms and compound_steam_engine)""",
	"electricity": """May produce Level 1 Electric Gear Factory, Factory throughput +1, production_modifier + 0.15. 
	(Requires: chemistry)""",	
	"medicine": """May use Chemicals if you wish to increase your Pop twice in a single turn. (Requires: chemistry) """,
	"synthetic_dyes": """Chemicals may be converted into dyes and Chemical factory may be upgraded to Level 2. 
	Also, Rubber provinces may be developed to Level 2. (Requires: fertilizer)""",					
	"fertilizer": """May convert a Chemical unit to a Food unit once for each Food producing province. (Requires: chemistry)""",
	"dynamite": """May develop Iron provices may be upgraded to Level 2, Gold provinces may be upgraded to Level 1. 
	 (Requires: fertilizer)""",
	"compound_steam_engine": """Cotton and Wood provinces may be upgraded to Level 2, Dyes provinces may be upgraded to Level 1 
	(Requires: chemistry and bessemer_process)""",
	"telegraph": """Factory throughput +1, Production Modifier +0.15, Organization  factor +0.15. 
	(Requires: electricity)""",
	"radio": "May construct Level 1 Radio factory. (Requires: telephone)",									#radio factory
	"oil_drilling": "Oil provinces may be upgraded to Level 1 and produce oil. (Requires: dynamite)",				#oil resource
	#"photography": {"requirement": {"electricity"}, "cost": 3, "min_mid": 1.0},			
	"combustion": "No immediate effect. (Requires: compound_steam_engine and oil_drilling)",		
	"flight": "May construct Level 1 Plane factory. (Requires: machine_guns and combustion)",		# plane factory
	"automobile": "May produce Level 1 Auto Factory. (Requires: combustion and radio)",					# auto factory
	"telephone": "May produce Level 1 Telephone factory. (Requires: telegraph)",									# phone factory
	"rotary_drilling": "May improve Oil provinces to Level 2. (Requires: automobile)",
	"mobile_warfare": "May produce Tank factory.(Requires: automobile and flight)",			# tanks
	"bombers": "Fighter att +1.2 (Requires: automobile and flight)", 
	"oil_powered_ships": """May upgrade Shipyard to Level 3, which enables construction of Battleships! 
	(Requires: combustion and indirect_fire)""",
	"synthetic_oil": "May convert Chemicals to Oil (3 for 1). (Requires: mobile_warfare and oil_powered_ships)",		# Use chemicals for oil (3 for 1)
	"synthetic_rubber": "May convert oil to rubber (2 for 1). (Requires: mobile_warfare and oil_powered_ships",
	"radar": "Fighter att + 1.2, Battleship att +1.(Requires: Radio and flight)",
	"rockets": "Has no immediate effect. (Requires: synthetic_oil)",
	"early_computers": "Battleship att +1, Production Modifier +0.15 (Requires: radar)",
	"atomic_bomb": "Technological victory (if enabled). (Requires: early_computers and rockets)",
}


