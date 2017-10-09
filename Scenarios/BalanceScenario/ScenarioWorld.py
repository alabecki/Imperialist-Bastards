
# Creates a list containing 5 lists, each of 8 items, all set to 0
cols, rows = 33, 22;

world = [Province() for y in range(cols) for x in range(rows)]

provinces = create_provinces()

for p in province: 
	x = p.x
	y = p.y
	world[x][y] = p


