#show message to input force, mass of m1, distance

F = input("Input the force:")

m1 = input("Input the mass of m1:")        

r = input("Input the distance:")     

#Newton's Law, m2=(F*r^2)/(G*m1), G=6.67x10^(-11)

mass_m2 = (float(F)*float(r)*float(r))/(6.67*10**(-11)*float(m1))        

#Mass-energy equivalence, E=(m2)*c^2, c=299,792,458 m/s

energy_m2 = float(mass_m2)*(299792458**2)        

#output the result of the mass of m2 and the energy of m2

print("The mass of m2 =", mass_m2)   
print("The energy of m2 =", energy_m2)     
