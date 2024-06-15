s = input("Enter a string: ")

maxlen = 1
start = 0

for i in range(1, len(s)):
  odd = s[i-maxlen-1 : i+1]
  even = s[i-maxlen : i+1]
  if i-maxlen-1 >= 0 and odd == odd[::-1]:
    start = i-maxlen-1
    maxlen = maxlen + 2
    continue
  if even == even[::-1]:
    start = i-maxlen
    maxlen = maxlen + 1

print("Longest palindrome substring is: ", str(s[start: start+maxlen]))
print("Length is: ", len(s[start: start+maxlen]))