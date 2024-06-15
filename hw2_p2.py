n = int(input("Input the range number:"))
print("Perfect numbers:")
for num in range(1, n+1):
	sum = 0
	for i in range(1, num):
		if(num % i == 0):
			sum += i
	if (sum == num):
		print(num)