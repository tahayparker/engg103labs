import matplotlib.pyplot as plt
import numpy as np
import csv

fig, ax = plt.subplots()

def readfile():
    f = open("lab4.csv", "r", encoding="utf-8")
    data = csv.reader(f)
    data = list(data)
    f.close()

def metals():
    readfile()
    ax.plot(data[0], data[1], color='#e63946', linewidth=1)
    ax.plot(data[2], y1011, color='#2a9d8f', linewidth=1)
    ax.plot(x1020, y1020, color='#fb8500', linewidth=1)


ax.set_facecolor('#EBEBEB')
ax.set_axisbelow(True)
[ax.spines[side].set_visible(False) for side in ax.spines]
ax.grid()

ax.grid(which='major', color='white', linewidth=1.2)
ax.grid(which='minor', color='white', linewidth=0.6)

ax.minorticks_on()

ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
ax.set_ylabel('Stress ($\\sigma$)', fontweight ='bold')
ax.set_title("Shear Stresss vs Shear Strain", fontweight ='bold')
ax.legend([m1, m2, m3, m4, m5], bbox_to_anchor=(0.75, 0.35))
# plt.show()
plt.savefig("ENGG103 Lab 3 - Part 1.png", format='png', dpi=2500, bbox_inches='tight')