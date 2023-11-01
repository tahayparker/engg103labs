import matplotlib.pyplot as plt
import numpy as np
import vals3minor

x1010 = vals3minor.x1010
y1010 = vals3minor.y1010
m1 = "TR1010"

x1011 = vals3minor.x1011
y1011 = vals3minor.y1011
m2 = "TR1011"

x1020 = vals3minor.x1020
y1020 = vals3minor.y1020
m3 = "TR1020"

x1021 = vals3minor.x1021
y1021 = vals3minor.y1021
m4 = "TR1021"

x1040 = vals3minor.x1040
y1040 = vals3minor.y1040
m5 = "TR1040"

fig, ax = plt.subplots()
ax.plot(x1010, y1010, color='#e63946', linewidth=1)
ax.plot(x1011, y1011, color='#2a9d8f', linewidth=1)
# ax.plot(x1020, y1020, color='#fb8500', linewidth=1)
# ax.plot(x1021, y1021, color='#457b9d', linewidth=1)
# ax.plot(x1040, y1040, color='#005f73', linewidth=1)

ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()

ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)

ax.minorticks_on()

ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
ax.set_ylabel('Stress ($\\sigma$)', fontweight ='bold')
ax.set_title("Shear Stress vs Strain", fontweight ='bold')
ax.legend([m1, m2, m3, m4, m5], loc='best')
plt.show()
# plt.savefig("ENGG103 Lab 2.png", format='png', dpi=2500, bbox_inches='tight')