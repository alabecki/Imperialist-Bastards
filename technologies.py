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
	"pre_modern": {"requirement": {"basic_civ"}, "cost": 1, "min_mid": 0},
	#"professional_armies": {"requirement": {"pre_industry_1"}, "cost": 1, "min_mid": 0},
	"flint_lock": {"requirement": {"pre_industry_2", "professional_armies"}, "cost": 1, "min_mid": 0},
	"pre_industry_1": { "requirement": {"pre_modern"}, "cost": 1, "min_mid": 0},
	"pre_industry_2": {"requirement": {"pre_industry_1"}, "cost": 1, "min_mid": 0},
	"pre_industry_3": {"requirement": {"pre_industry_2"}, "cost": 1.25, "min_mid": 0},
	"high_pressure_steam_engine": {"requirement": {"pre_industry_3"}, "cost": 1.75, "min_mid": 1},
	"square_timbering": {"requirement": {"high_pressure_steam_engine"}, "cost": 1.5, "min_mid": 1},
	"cotton_gin": {"requirement": {"high_pressure_steam_engine"}, "cost": 1.5, "min_mid": 1},
	"steel_plows": {"requirement": {"pre_industry_3"}, "cost": 1.5, "min_mid": 1},
	"saw_mill": {"requirement": {"high_pressure_steam_engine"}, "cost": 1.5, "min_mid": 1},
	"cement": {"requirement": {"square_timbering"}, "cost": 1.5, "min_mid": 2},
	"bessemer_process": {"requirement": {"high_pressure_steam_engine", "square_timbering"}, "cost": 2, "min_mid": 2},
	"muzzle_loaded_arms": {"requirement": {"flint_lock", "high_pressure_steam_engine"}, "cost": 2, "min_mid": 3},
	"breach_loaded_arms": {"requirement": {"muzzle_loaded_arms", "bessemer_process"}, "cost": 3, "min_mid": 4},
	"machine_guns": {"requirement": {"mechanical_reaper", "breach_loaded_arms"}, "cost": 4.5, "min_mid": 6},
	"indirect_fire": {"requirement": {"dynamite"}, "cost": 5, "min_mid": 9},
	"power_loom": {"requirement": {"high_pressure_steam_engine", "cotton_gin"}, "cost": 2, "min_mid": 2},
	"chemistry": {"requirement": {"power_loom"}, "cost": 3.5, "min_mid": 3},
	"pulping": {"requirement": {"chemistry"}, "cost": 3, "min_mid": 3},
	"mechanical_reaper": {"requirement": {"power_loom", "steel_plows"}, "cost": 3.5, "min_mid": 4},
	"iron_clad": {"requirement": {"breach_loaded_arms", "compound_steam_engine"}, "cost": 4, "min_mid": 8},
	"electricity": {"requirement": {"chemistry"}, "cost": 4, "min_mid": 6},									#electrical gear factory, rubber
	"medicine": {"requirement": {"chemistry"}, "cost": 4, "min_mid": 7},
	"synthetic_dyes": {"requirement": {"chemistry", "fertlizer"}, "cost": 4, "min_mid": 8},					
	"fertlizer": {"requirement": {"chemistry"}, "cost": 4, "min_mid": 8},
	"dynamite": {"requirement": {"chemistry", "fertlizer"}, "cost": 4, "min_mid": 8},
	"compound_steam_engine": {"requirement": {"bessemer_process", "chemistry"}, "cost": 4, "min_mid": 8},
	"telegraph": {"requirement": {"electricity"}, "cost": 4, "min_mid": 9},
	"radio": {"requirement": {"telephone"}, "cost": 6, "min_mid": 10},									#radio factory
	"oil_drilling": {"requirement": {"chemistry", "dynamite"}, "cost": 5, "min_mid": 10},				#oil resource
	#"photography": {"requirement": {"electricity"}, "cost": 3, "min_mid": 1.0},			
	"combustion": {"requirement": {"oil_drilling", "compound_steam_engine"}, "cost": 5, "min_mid": 11},		
	"flight": {"requirement": {"combustion", "machine_guns"}, "cost": 7, "min_mid": 12},		# plane factory
	"automobile": {"requirement": {"combustion", "radio"}, "cost": 7, "min_mid": 13},					# auto factory
	"telephone": {"requirement": {"telegraph"}, "cost": 4, "min_mid": 8},									# phone factory
	"rotary_drilling": {"requirement": {"automobile"}, "cost": 8, "min_mid": 16},
	"mobile_warfare": {"requirement": {"automobile", "flight"}, "cost": 7, "min_mid": 14},			# tanks
	"bombers": {"requirement": {"flight", "automoblie"}, "cost": 7, "min_mid": 16}, 
	"oil_powered_ships": {"requirement": {"combustion", "machine_guns"}, "cost": 6, "min_mid": 11},				# Battleship - level 3 port
	"synthetic_oil": { "requirement":{"oil_powered_ships", "mobile_warfare"}, "cost": 10, "min_mid": 16},		# Use chemicals for oil (3 for 1)
	"synthetic_rubber": {"requirement": {"oil_powered_ships", "mobile_warfare"}, "cost": 10, "min_mid": 16},  # Use chemicals for rubber (3 for 1)
	"radar": {"requirement": {"radio", "flight"}, "cost": 10, "min_mid": 16},
	"rockets": {"requirement": {"synthetic_oil"}, "cost": 10, "min_mid": 18},
	"early_computers": {"requirement": {"radar"}, "cost": 12, "min_mid": 18},
	"atomic_bomb": {"requirement": {"synthetic_oil", "synthetic_rubber", "early_computers"}, "cost": 20, "min_mid": 20}
}
