import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl']
sizes = [33, 52, 12, 37, 20, 5]
separated = (.1, 0, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct= '%1.1f%%', explode=separated) # autopct shows the percentage of each piece
plt.axis("equal") # Makes the circle stable to changes on the window size.

plt.show()

