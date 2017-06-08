
#Market Place
from player_class import Player

from empire_class import Empire
from Old_Minor_Class import Old_minor


goods_produced = {
	"parts": 0.0,
	"clothing": 0.0,
	"paper": 0.0,
	"cannons": 0.0,
	"furniture": 0.0,
	"chemicals": 0.0
}


count = 1

for k in goods_produced.keys():
	goods_produced[k] = count
	count += 1

for k, v in goods_produced.items():
	print (k, v)

for k in goods_produced.keys():
	goods_produced[k] = 0

for k, v in goods_produced.items():
	print (k, v)
