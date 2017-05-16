from player_class import Player
import market
import random
from province import Province


commands = {
	"1": "Get Information on...",
	"2": "Assign POPS",
	"3": "Manifacture Goods",
	"4": "Build"
	"5": "Military Actions",
	"6": "Diplomatic Action",
	"7": "Research Technology",
	"8": "Trade",
	"9": "End Turn"
}

information = {
	"1": "Overview of my empire"
	"2": "View Provinces",
	"3": "View POPs",
	"4": "View Military",
	"5": "View Inventory",
	"6": "View National Comparison"
}

produce_goods = {
	"1": "Manifacture with Artisans",
	"2": "Manifacture with Factories"
}

build = {
	"1": "Develop Province",
	"2": "Build Factory",
	"3": "Build/Develop Fortifications"
	"4": "Build Unit"
}

build_factory = {
	"1": "Machine Parts",
	"2": "Clothing",
	"3": "Paper",
	"4": "Furniture",
	"5": "Cannons",
	"6": "Chemicals"
	#"7": "Electric Gear",
	#"8": "Telephone"
	#"9": "Automobile"
}

build_unit = {
	"1": "Infantry",
	"2": "Artilary",
	"3": "Cavalry",
	"4": "Frigate".
	"5": "Iron Clad",
	#"6": "Fighher",
	#"7": "Tank"
}

great_power_relations = {
	"1": "Improve Relations",
	"2": "Damage Relations",
	"3": "Fabricate casus belli",
	"4": "Declare War",
	"5": "Offer Peace",
	"6": "Propose Non-Agression Treaty",
	"7": "Propose Defensice Alliance",
	"8": "Propose Full Alliance",
	"9": "Destablize Nation",
	"10": "Offer Loan",
	"11": "Offer to Sell Arms",
	"12": "Ask to Buy Arms"

}

minor_power_relations = {
	"1": "Gain Infulence",
	"2": "Remove Infulence",
	"3": "Guarentee Independence",
	"4": "Supply Arms",
	"5": "Foreign Investment",
	"4": "Sphere Nation"
}




num_prov = 5

print("____________________________________________________________________________________________ \n")
print ("Welcome to Imperialist Bastards! \n")
print ("___________________________________________________________________________________________ \n \n")

#num_players = input("Please enter the number of nations you would like to have in the game \n")
num_players = 6
i = 1
players = list()
while( i <= num_players):
	name = input("Please enter the name of player %s : \n" % (i))
	players.append(Player(name))
	i += 1

#Initialize the resources each player has in each province
for player in players:
	#print("player %s has %s armies \n" % (player, player.army))
	#player.provinces[1]["resource"] = "food"
	player.provinces[1] = Province("1", "food", 1.0)
	#player.provinces.append(Province("1", "food", 1.0))
	player.resources["food"] += 1
	prov = 2
	while(prov <= 5):
	#for prov in player.provinces:
		res = random.choice(['food', 'cotton', 'wood', 'coal', 'iron'])
		qual = random.triangular(0.5, 2.0, 1.0)
		#player.provinces[prov]["resource"] = res
		#player.provinces(prov)resource = res
		player.provinces.append(Province(prov, res, qual))
		print("Player %s is assigned %s at %s with %s quality\n" % (player.name, res, prov, qual))
		player.resources[res] += 1
		prov += 1

for player in players:
	player.view_inventory()

_continue = True

while(_continue == True):
	for player in players:
		print("%s, it is your turn to exploit the globe for the greatness of your nation \n" % (player.name)
		print("%s, what is your imperial decree? \n" % (player.name))
		for key, value in commands.items():
			print (" %s : %s \n" % (key, value))
		command = input()
		if command == "1":
			print("What would you like to know? \n")
			for key, value in information.items():
				print("%s : %s" % (key, values))
			info_command = input()
			if info_command == 1:
				print("Currently, your glorious empire has: \n")
				print("Gold: %s 				Action Points: %s \n" % (player.gold, player.AP))
				print("Stability: %s 			Total Population\n" % (player.stability, player.POP))
				print("Lower Class Pops: %s 	Middle Class Pops %s \n") % (player.numLowClass, player.numMidPOP)
			if info_command == 2:
				print("Province Overview: \n")
				for province in player.provinces:
					print("Name: %s 	Resource: %s 	Development Level: %s 	Worked?: %s 	Quality: %s \n" % \
						(province.name, province.resource, province.development_level, province.worked, province.quality))
			if info_command == "3":
				print("Population Overview: \n")
				print("Total Population: %s 	Unassigned Pops: %s 	Lower Class Pops: %s 	Middle Class Pops: %s \n" % \
					(player.POP, player.freePOP, player.numLowClass, player.numMidPOP))
				print("Urban Worker Pops: %s 	Military Pops: %s \n" % (player.proPOP, player.milPOP))
			if info_command == "4":
				print("Military Overview: \n")
				for k, v in player.military.items():
					print(" %s: %s " % (k, v) )
			if info_command == "5":
				print("Inventory:"):
				for k, v in player.resources.items():
					print(" %s: %s " % (k, v) )
				for k, v in player.goods.items():
					print(" %s: %s " % (k, v) )
			if info_command == "6":
				print("This feature is not yet implemented \n")
		if command == "2":
			player.assign_POP()
		if command == "3":
			print("What will be the means of production? \n")
			for k, v in produce_goods.items():
				print(k, v)
			means = input
			if means = "1":
				player.craftman_production()
			if means = "2"
				player.factory_production()
		if command == "4":
			print("What sort of item would you like to build? \n")
			for k, v in build.item()
				print(k, v)
			sort = input()
			if sort == "1":
				player.development_province()
			if sort == "2":
				print("What sort of factory would you like to build? \n")
				for k, v in build_factory.items():
					print(k, v)
				kind = input()
				player.build_factory(kind)
			if sort == "3":
				player.build_fortification()
			if sort == "4":
				player.build_unit()
		if command == "5":
            print("Please choose a Major Nation: \n" )
            for p in players:
                print(p.name)
            other = input()
            print("What action would you like to take? \n")
            for k, v in great_power_relations:
                print(k, v)
            #
            # To be implemented
        if command == "6":
            print("Please choose a minor nation")

commands = {
	"1": "Get Information on...",
	"2": "Assign POPS",
	"3": "Manifacture Goods",
	"4": "Build"
	"5": "Great Power Relations",
	"6": "Minor Power Relations",
	"7": "Research Technology",
	"8": "Trade",
	"9": "End Turn"
}
