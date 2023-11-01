import matplotlib.pyplot as plt
import numpy as np
import vals3

x

fig, ax = plt.subplots()
ax.plot(x, y1, color="#FF0000")
ax.plot(x, y2, color="#00FF00")
ax.plot(x, y3, color="#0000FF")
ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()
ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)
ax.minorticks_on()
ax.set_xlabel('Temperature ($^\\degree C$)', fontweight ='bold')
ax.set_ylabel('Fracture Energy ($J/mm^2$)', fontweight ='bold')
ax.set_title("Fracture Energy - Temperature Graph", fontweight ='bold')
ax.legend([m1, m2, m3, m4, m5], loc='best')
plt.show()
# plt.savefig("ENGG103 Lab 2.png", format='png', dpi=2500, bbox_inches='tight')