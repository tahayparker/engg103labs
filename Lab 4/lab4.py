import matplotlib.pyplot as plt
import numpy as np
import csv

fig, ax = plt.subplots()

def graph_common():
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

def metals():
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True)
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True)
    s3 = np.genfromtxt("s3.csv", delimiter=",", autostrip=True)

    ax.plot(s1[0], s1[1], color='#e63946', linewidth=1)
    ax.plot(s2[0], s2[1], color='#2a9d8f', linewidth=1)
    ax.plot(s3[0], s3[1], color='#fb8500', linewidth=1)
    
    m1 = "High Carbon Steel"
    m2 = "Galvanized Mild Steel"
    m3 = "Aluminum"

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Metals", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def pla():
    s4 = np.genfromtxt("s4.csv", delimiter=",", autostrip=True)
    s5 = np.genfromtxt("s5.csv", delimiter=",", autostrip=True)
    s6 = np.genfromtxt("s6.csv", delimiter=",", autostrip=True)
    
    ax.plot(s4[0], s4[1], color='#593F62', linewidth=1)
    ax.plot(s5[0], s5[1], color='#005f73', linewidth=1)
    ax.plot(s6[0], s6[1], color='#8FC93A', linewidth=1)
    
    m1 = "PLA - Vertical Longitudinal Lines"
    m2 = "PLA - Horizontal Longitudinal Lines"
    m3 = "PLA - Mixed Orientations"

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - PLA Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def metal_elastic():
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True, usecols=range(1,312))
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True, usecols=range(1,378))
    s3 = np.genfromtxt("s3.csv", delimiter=",", autostrip=True, usecols=range(1,344))

    x1, y1 = s1[0], s1[1]
    print(x1)
    x2, y2 = s2[0], s2[1]
    x3, y3 = s3[0], s3[1]
    
    ax.plot(x1, y1, color='#e63946', linewidth=1)
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1)
    ax.plot(x3, y3, color='#fb8500', linewidth=1)

    # Get slope of each line using numpy.polyfit
    
    z1 = np.polyfit(x1, y1, 1)
    z2 = np.polyfit(x2, y2, 1)
    z3 = np.polyfit(x3, y3, 1)

    m1 = "High Carbon Steel - Slope = {} GPa".format(z1[0].round(2))
    m2 = "Galvanized Mild Steel - Slope = {} GPa".format(z2[0].round(2))
    m3 = "Aluminum - Slope = {} GPa".format(z3[0].round(2))

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$), {}'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def mild_steel():
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True)
    s8 = np.genfromtxt("s8.csv", delimiter=",", autostrip=True)

    ax.plot(s2[0], s2[1], color='#2a9d8f', linewidth=1)

    # 0.2% Proof Stress
    z = np.polyfit(s8[0], s8[1], 1)
    
    # Plot the line with x += 0.002
    p = np.poly1d(z)
    x = s2[0]
    ax.plot(x, (p(x) + 0.002), color='#2a9d8f', linewidth=1)

    # Find Ultimate Tensile Strength
    max_stress = max(s2[1])

    # Mark Ultimate Tensile Strength with an arrow and value
    ax.annotate('Ultimate Tensile Strength', xy=(0.002, max_stress), xytext=(0.002, max_stress + 100000), arrowprops=dict(facecolor='black', shrink=0.05),)
    
    # Mark the x-axis with an arrow indicating the Elastic Strain
    ax.annotate('Elastic Strain', xy=(0.002, 0), xytext=(0.002, -100000), arrowprops=dict(facecolor='black', shrink=0.05),)

    # Mark the x-axis with an arrow indicating the Plastic Strain
    ax.annotate('Plastic Strain', xy=(0.002, 0), xytext=(0.002, -200000), arrowprops=dict(facecolor='black', shrink=0.05),)

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$), {}'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Galvanized Mild Steel", fontweight ='bold')

"""
metals()
graph_common()
plt.show()

pla()
graph_common()
plt.show()
"""

metal_elastic()
graph_common()
plt.show()

# plt.savefig("ENGG103 Lab 4 Part 1.png", format='png', dpi=2500, bbox_inches='tight')