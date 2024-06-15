n = int(input("Input an integer number: "))
a = 0
b = 1
sum = 0
count = 1

while count<=n:
	count += 1
	a = b
	b = sum
	sum = a + b
print("The "+str(n)+"-th Fibonacci sequence number is:", sum)