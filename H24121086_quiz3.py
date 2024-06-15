print("Welcome to the simple calculator program!")



fn = float(input("Enter the first number: "))
sn = float(input("Enter the second number: "))
operation = input("Select an arithmetic operatoin (+, -, *, /): ")
if float(sn) == 0 and operation == "/":
	print("Error: Division by zero!")
elif operation == "+":
	print("Result: ", float(fn) + float(sn))
elif operation == "-":
	print("Result: ", float(fn) - float(sn))
elif operation == "*":
	print("Result: ", float(fn) * float(sn))
elif operation == "/":
	print("Result: ", float(fn) / float(sn))
else:
	print("Unable to calculate!")

decision = input("Do you want to perform another calcluation? (yes or no): ")

if decision == "no":
	print("Goodbye!")
else:
	while decision == "yes":
		fn = float(input("Enter the first number: "))
		sn = float(input("Enter the second number: "))
		operation = input("Select an arithmetic operatoin (+, -, *, /): ")
		if operation == "/" and sn == "0":
			print("Error: Division by zero!")
		elif operation == "+":
			print("Result: ", float(fn) + float(sn))
		elif operation == "-":
			print("Result: ", float(fn) - float(sn))
		elif operation == "*":
			print("Result: ", float(fn) * float(sn))
		elif operation == "/" and sn != "0":
			print("Result: ", float(fn) / float(sn))
		else:
			print("unable to calculate!")
		decision = input("Do you want to perform another calcluation? (yes or no): ")