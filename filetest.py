from appJar import gui
from save import*
from player_class import*

app = gui()


file = app.openBox(title= "Open something", dirName=None, fileTypes= None, asFile= True, parent=None)
print(file)
print(file.name)

state = load_game(file.name)

for j, k in state.items():
	print(j, k)
app.go()