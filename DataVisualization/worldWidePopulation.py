import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 
         1985, 1990, 1995, 2000, 2005, 2010, 2015]

# Billions people
pops = [ 2.525, 2.758, 3.018, 3.322, 3.682, 4.061, 4.440,
         4.853, 5.310, 5.735, 6.127, 6.535, 6.830, 7.349]

deaths = [1.2, 1.7, 1.9, 2.4, 2.7, 3.0, 3.1, 3.3, 3.4, 3.5, 3.9, 3.7, 3.6, 3.7]

plt.plot(years, pops,'--',  color=[1, .6, .6])
plt.plot(years, deaths, color=[.6, .6, 1])

plt.xlabel("Population growth by years")
plt.ylabel("Population in billions")
plt.title("Population growth")

#plt.show()

# Lets store it into a variable.

lines = plt.plot(years, pops, years, deaths)
plt.grid(True)

plt.setp(lines, color=[1, .4, .4], marker="o")
plt.show()
