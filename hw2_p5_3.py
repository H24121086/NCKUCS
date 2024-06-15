### Fibonacci Section ###

n = int(input("The number of the requested element in Fibonacci (n) = "))
a = 0
b = 1
sum = 0
count = 1

while count<=n:
	count += 1
	a = b
	b = sum
	sum = a + b

### String Section ###

s1 = input("The first string for Palindromic detection (s1) = ")

maxlen1 = 1
start1 = 0

for i in range(1, len(s1)):
	odd1 = s1[i-maxlen1-1 : i+1]
	even1 = s1[i-maxlen1 : i+1]
	if i-maxlen1-1 >= 0 and odd1 == odd1[::-1]:
		start1 = i-maxlen1-1
		maxlen1 = maxlen1 + 2
		continue
	if even1 == even1[::-1]:
		start1 = i-maxlen1
		maxlen1 = maxlen1 + 1

s2 = input("The second string for Palindromic detection (s2) = ")

maxlen2 = 1
start2 = 0

for j in range(1, len(s2)):
	odd2 = s2[j-maxlen2-1 : j+1]
	even2 = s2[j-maxlen2 : j+1]
	if j-maxlen2-1 >= 0 and odd2 == odd2[::-1]:
		start2 = j-maxlen2 - 1
		maxlen2 = maxlen2 + 2
		continue
	if even2 == even2[::-1]:
		start2 = j-maxlen2
		maxlen2 = maxlen2 + 1

p = str(input("The plaintext to be encrypted: "))


print("----- extract key for encrypt method -----")

print("The "+str(n)+"-th Fibonacci sequence number is:", sum)
print("Longest Palindromic substring within fist string is:", str(s1[start1: start1+maxlen1]))
print("Length is:", len(s1[start1: start1+maxlen1]))
print("Longest Palindromic substring within second string is:", str(s2[start2: start2+maxlen2]))
print("Length is:", len(s2[start2: start2+maxlen2]))

### Encryption Section ###


print("----- encryption completed -----")

print("The encrypted text is: ", end = "")

for i in range(len(p)):

	print(chr(((((ord(p[i])+sum)*(len(s1[start1: start1+maxlen1]))+len(s2[start2: start2+maxlen2]))-65)%26)+65), end = "")