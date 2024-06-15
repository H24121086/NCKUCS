sa = float(input("Enter the shopping amount:"))
ml = input("Enter the memebership level (Regular or Gold):")

if ml == "Regular":
	print(ml)	
	else if sa >= 1000:
	print("$",sa*(0.9))
	else if sa >= 2000:
	print("$",sa*(0.85))
	else if sa >= 3000:
	print("$",sa*(0.8))
else:
	print("$", sa)

if ml == "Gold":
	print(ml)
if sa >= 1000:
	print("$",sa*(0.85))
if sa >= 2000:
	print("$",sa*(0.8))
if sa >= 3000:
	print("$",sa*(0.75))
else:
	print("$",sa)

if ml != "Regular" or "Gold":
	print("Invalid membership level. Please enter \'Regular\' or \'Gold\'.")



	