# print the initial grid
grid = int(input("Enter the size of the grid: "))
i = 0
while i < grid:
	print(grid*"_ ")
	i = i + 1

cord = str(input("Enter the coordinate to edit: "))
val = input("Enter the new value for the cell: ")

cord.split()
row = cord[0]
col = cord[2]

# 座標化
while i < grid:
	if row == "0" and col == "0":
		print(val, (i-1)*"_ ")
	elif row == "":
		while j < grid:
			print(i*"_ ")
