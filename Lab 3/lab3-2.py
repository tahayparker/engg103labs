import matplotlib.pyplot as plt
import numpy as np
import vals3minor

x1010 = vals3minor.x1010
y1010 = vals3minor.y1010

x1011 = vals3minor.x1011
y1011 = vals3minor.y1011

x1020 = vals3minor.x1020
y1020 = vals3minor.y1020

x1021 = vals3minor.x1021
y1021 = vals3minor.y1021

x1040 = vals3minor.x1040
y1040 = vals3minor.y1040

fig, ax = plt.subplots()
ax.plot(x1010, y1010, color='#e63946', linewidth=1)
ax.plot(x1011, y1011, color='#2a9d8f', linewidth=1)
ax.plot(x1020, y1020, color='#fb8500', linewidth=1)
ax.plot(x1021, y1021, color='#593F62', linewidth=1)
ax.plot(x1040, y1040, color='#005f73', linewidth=1)

ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()

ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)

ax.minorticks_on()

# Get slope of each line using numpy polyfit
z1010 = np.polyfit(x1010, y1010, 1)
z1011 = np.polyfit(x1011, y1011, 1)
z1020 = np.polyfit(x1020, y1020, 1)
z1021 = np.polyfit(x1021, y1021, 1)
z1040 = np.polyfit(x1040, y1040, 1)

m1 = "TR1010 - Slope = {} Pa".format(z1010[0].round(2))
m2 = "TR1011 - Slope = {} Pa".format(z1011[0].round(2))
m3 = "TR1020 - Slope = {} Pa".format(z1020[0].round(2))
m4 = "TR1021 - Slope = {} Pa".format(z1021[0].round(2))
m5 = "TR1040 - Slope = {} Pa".format(z1040[0].round(2))


ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
ax.set_ylabel('Stress ($\\sigma$)', fontweight ='bold')
ax.set_title("Shear Stresss vs Shear Strain (Linear Region)", fontweight ='bold')
ax.legend([m1, m2, m3, m4, m5], loc='best', fontsize='small')


# Print slopes of each line
print("Slope of TR1010: ", z1010[0])
print("Slope of TR1011: ", z1011[0])
print("Slope of TR1020: ", z1020[0])
print("Slope of TR1021: ", z1021[0])
print("Slope of TR1040: ", z1040[0])

# plt.show()
plt.savefig("ENGG103 Lab 3 - Part 2.png", format='png', dpi=2500, bbox_inches='tight')