#Technologies
#Each has a:
#name
#
 #technologies = {
#    name: {requirements: {A, B, C}, cost: int}
#
#}

technologies = {
	"high_pressure_steam_engine": {"requiremnt": "any", "cost": 1},
	"square_timbering": {"requirement": "high_pressure_steam_engine", "cost": 1},
	"cotton_gin": {"requirement": "any", "cost": 1},
	"steel_plows": {"requirement": "any", "cost": 1},
	"saw_mill": {"requirement": "high_pressure_steam_engine", "cost": 1}
	"cement": {"requirement": "square_timbering", "cost": 1.5}
	"bessemer_process": {"requirement": "high_pressure_steam_engine", "cost": 1.5}
	"muzzle_loaded_arms": {"requirement": "any", "cost": 1.0}
	"breach_loaded_arms": {"requirement": "bessemer_process", "cost": 2.0}
	"machine_guns": {"requirement": "mechanical_reaper", "cost": 2.5}
	"indirect_fire": {"requirement": "iron_clad", "cost": 3.0}
	"power_loom": {"requirement": "high_pressure_steam_engine", "cost": 1.5}
	"chemistry": {"requirement": "power_loom", "cost": 2.0}
	"pulping": {"requirement": "chemistry", "cost": 2.0}
	"iron_clad": {"requirement": "dynamite": "cost": 2.5}
	"electricity": {"requirement": "chemistry", "cost": 2.5}
	"medicine": {"requirement": "chemistry", "cost": 2.5}
	"synthetic_dyes": {"requirement": "chemistry", "cost": 2.5}
	"fertlizer": {"requirement": "chemistry", "cost": 2.5}
	"dynamite": {"requirement": "chemistry", "cost": 2.5}
	"compound_steam_engine": {"requirement": "bessemer_process", "cost": 2.5}
	"telegraph": {"requirement:" "electricity", "cost": 3}
	"radio": {"requirement": "electricity", "cost": 3}
	"mechanical_reaper": {"requirement": "power_loom": 2}



}
