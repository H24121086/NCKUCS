# show message to input velocity

v = input("Input velocity:")

# calculate the percentage of light speed, light speed = 299,792,458 m/s

pv = float(v)/(299792458)

# take the time of light to the destinatoins into calculation
# AC = Alpha Centauri, BS = Barnard's Star, Bg = Betelgeuse, AG = Andromeda Galaxy

AC = 4.3*(1-(float(pv))**2)**(0.5)
BS = 6.0*(1-(float(pv))**2)**(0.5)
Bg = 309*(1-(float(pv))**2)**(0.5)
AG = 2000000*(1-(float(pv))**2)**(0.5)

# output the results

print("Percentage of light speed =", round(pv, 6))
print("Travel time to Alpha Centauri =", round(AC, 6))
print("Travel time to Barnard's Star =", round(BS, 6))
print("Travel time to Betelgeuse (in the Milky Way) =", round(Bg, 6))
print("Travel time to Andromeda Galaxy (closest galaxy) =", round(AG, 6))