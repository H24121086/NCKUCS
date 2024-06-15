# show message to input richter scale value

r = input("Please input a Richter scale value:")

# Calcualtions. e = energy(joule), t = tons of TNT, n = number of nutritious lunches

e = 10**(1.5*float(r)+4.8)

t = (10**((1.5)*float(r)+4.8))/(4.184*(10**9))

n = (10**(1.5*float(r)+4.8))/2930200


# output the calculated values

print("Richter scale value:", r)
print("Equivalence in Joules:", round(e, 5))
print("Equivalence in tons of TNT:", round(t, 5))
print("Equivalence in the number of nutritious lunches:", round(n, 5))

