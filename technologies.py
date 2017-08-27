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
	"professional_armies": {"requirement": {"pre_industry_1"}, "cost": 1, "min_mid": 0},
	"flint_lock": {"requirement": {"pre_industry_2", "professional_armies"}, "cost": 1, "min_mid": 0},
	"pre_industry_1": { "requirement": {"pre_modern"}, "cost": 1, "min_mid": 0},
	"pre_industry_2": {"requirement": {"pre_industry_1"}, "cost": 1, "min_mid": 0},
	"pre_industry_3": {"requirement": {"pre_industry_2"}, "cost": 1, "min_mid": 0},
	"high_pressure_steam_engine": {"requirement": {"pre_industry_3"}, "cost": 1, "min_mid": 0},
	"square_timbering": {"requirement": {"high_pressure_steam_engine"}, "cost": 1, "min_mid": 0},
	"cotton_gin": {"requirement": {"high_pressure_steam_engine"}, "cost": 1, "min_mid": 0.5},
	"steel_plows": {"requirement": {"pre_industry_3"}, "cost": 1, "min_mid": 0.5},
	"saw_mill": {"requirement": {"high_pressure_steam_engine"}, "cost": 1, "min_mid": 0.5},
	"cement": {"requirement": {"square_timbering"}, "cost": 1, "min_mid": 0},
	"bessemer_process": {"requirement": {"high_pressure_steam_engine", "square_timbering"}, "cost": 1.5, "min_mid": 0.0},
	"muzzle_loaded_arms": {"requirement": {"flint_lock", "high_pressure_steam_engine"}, "cost": 1.5, "min_mid": 0},
	"breach_loaded_arms": {"requirement": {"muzzle_loaded_arms", "bessemer_process"}, "cost": 2.0, "min_mid": 0},
	"machine_guns": {"requirement": {"mechanical_reaper", "breach_loaded_arms"}, "cost": 2.5, "min_mid": 0},
	"indirect_fire": {"requirement": {"dynamite"}, "cost": 3.0, "min_mid": 0},
	"power_loom": {"requirement": {"high_pressure_steam_engine", "cotton_gin"}, "cost": 1.5, "min_mid": 0},
	"chemistry": {"requirement": {"power_loom"}, "cost": 2.0, "min_mid": 0},
	"pulping": {"requirement": {"chemistry"}, "cost": 2.0, "min_mid": 0},
	"mechanical_reaper": {"requirement": {"power_loom", "steel_plows"}, "cost": 2, "min_mid": 0},
	"iron_clad": {"requirement": {"breach_loaded_arms", "compound_steam_engine"}, "cost": 2.5, "min_mid": 0},
	"electricity": {"requirement": {"chemistry"}, "cost": 2.5, "min_mid": 0},									#electrical gear factory, rubber
	"medicine": {"requirement": {"chemistry"}, "cost": 2.5, "min_mid": 0},
	"synthetic_dyes": {"requirement": {"chemistry", "fertlizer"}, "cost": 2.5, "min_mid": 0},					
	"fertlizer": {"requirement": {"chemistry"}, "cost": 2.5, "min_mid": 0},
	"dynamite": {"requirement": {"chemistry", "fertlizer"}, "cost": 2.5, "min_mid": 0},
	"compound_steam_engine": {"requirement": {"bessemer_process", "chemistry"}, "cost": 2.5, "min_mid": 0},
	"telegraph": {"requirement": {"electricity"}, "cost": 2.5, "min_mid": 0},
	"radio": {"requirement": {"electricity"}, "cost": 3, "min_mid": 0},									#radio factory
	"oil_drilling": {"requirement": {"chemistry", "dynamite"}, "cost": 3, "min_mid": 1.0},				#oil resource
	#"photography": {"requirement": {"electricity"}, "cost": 3, "min_mid": 1.0},			
	"combustion": {"requirement": {"oil_drilling", "compound_steam_engine"}, "cost": 3.5, "min_mid": 0},		
	"flight": {"requirement": {"combustion", "machine_guns"}, "cost": 4, "min_mid": 0},		# plane factory
	"automobile": {"requirement": {"combustion", "radio"}, "cost": 3, "min_mid": 0},					# auto factory
	"telephone": {"requirement": {"telegraph"}, "cost": 3.5, "min_mid": 0},									# phone factory
	"mobile_warfare": {"requirement": {"automobile", "flight"}, "cost": 4.0, "min_mid": 0},			# tanks
	"bombers": {"requirement": {"flight", "automoblie"}, "cost": 5, "min_mid": 0}, 
	"oil_powered_ships": {"requirement": {"combustion", "machine_guns"}, "cost": 4.0, "min_mid": 0},				# Battleship - level 3 port
	"synthetic_oil": { "requirement":{"oil_powered_ships", "mobile_warfare"}, "cost": 6, "min_mid": 0},		# Use chemicals for oil (3 for 1)
	"synthetic_rubber": {"requirement": {"oil_powered_ships", "mobile_warfare"}, "cost": 6, "min_mid": 0},  # Use chemicals for rubber (3 for 1)
	"radar": {"requirement": {"radio", "flight"}, "cost": 6, "min_mid": 0},
	"rockets": {"requirement": {"synthetic_oil"}, "cost": 6, "min_mid": 0},
}
