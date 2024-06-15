# show message to input the height of the 1st ball, mass of the 1st ball, mass of the 2nd ball, orderly

h = input("Input the height of the 1st ball:")
m1 = input("Input the mass of the 1st ball:")
m2 = input("Input the mass of the 2nd ball:")

# (v1)^2=(g*h)/2, g=9.8 m/s

v1 = (2*9.8*float(h))**(0.5)

# since it's elastic collision, (v2)^2=(m1*(u1)^2)/m2

v2 = float(v1)*((float(m1)/float(m2))**0.5)

# output the results

print("The velocity of the 1st ball after slide:", v1, "m/s")
print("The velocity of the 2nd ball after collision:", v2, "m/s")



