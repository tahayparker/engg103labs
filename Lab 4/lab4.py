import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as sg
import math
from scipy.stats import linregress

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
    x2, y2 = s2[0], s2[1]
    x3, y3 = s3[0], s3[1]
    
    ax.plot(x1, y1, color='#e63946', linewidth=1)
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1)
    ax.plot(x3, y3, color='#fb8500', linewidth=1)

    print(linregress(x1, y1).slope)
    print(linregress(x2, y2).slope)
    print(linregress(x3, y3).slope)

    # Get slope of each line using linregress
    
    z1 = (linregress(x1, y1).slope) / 1000
    z2 = (linregress(x2, y2).slope) / 1000
    z3 = (linregress(x3, y3).slope) / 1000

    m1 = "High Carbon Steel - Slope = {} GPa".format(z1.round(2))
    m2 = "Galvanized Mild Steel - Slope = {} GPa".format(z2.round(2))
    m3 = "Aluminum - Slope = {} GPa".format(z3.round(2))

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='lower right', fontsize=9)

def mild_steel():
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True)
    s2m = np.genfromtxt("s2.csv", delimiter=",", autostrip=True, usecols=range(1,378))

    x1, y1 = s2[0], s2[1]
    
    # Plot original line
    ax.plot(x1, y1, color='#8D5A97', linewidth=1)

    # 0.2% Proof Stress
    z = np.polyfit(s2m[0], s2m[1], 1)
    
    # Plot the proof stress line with x += 0.002
    p = np.poly1d(z)
    x2 = [(i + 0.002) for i in s2m[0]]
    y2 = p(s2m[0])
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1, linestyle='--')

    # Find intersection of the two lines
    l1 = sg.LineString(np.column_stack((x1, y1)))
    l2 = sg.LineString(np.column_stack((x2, y2)))
    intersection = l1.intersection(l2)

    plt.plot(intersection.x, intersection.y, 'x', color='orange', markersize=6)

    # Point the intersection of the two lines with an arrow and label it away from the intersection below the graph so that it is readable
    ax.annotate('Intersection', xy=(intersection.x, intersection.y), xytext=(intersection.x + 0.005, intersection.y - 50), arrowprops=dict(arrowstyle='->', facecolor='black'),)

    # Find Ultimate Tensile Strength

    max_stress = max(s2[1])
    print("Max Stress =", max_stress)

    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Galvanized Mild Steel", fontweight ='bold')

def high_carbon():
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True)
    xeng, yeng = s1[0], s1[1]
    ax.plot(xeng, yeng, color='red', linewidth=1)

    xtrue = [math.log(1 + i) for i in xeng] # Strain = ln(1 + eng strain)
    ytrue = [math.prod([yeng[i], (1 + xeng[i])]) for i in range(len(yeng))] # Stress = Eng Stress(1 + eng strain)

    ax.plot(xtrue, ytrue, color='#2a9d8f', linewidth=1)
    
    stress_unit = "GPa"
    
    m1 = "Engineering Stress Strain"
    m2 = "True Stres Strain"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Engineering vs True Stress Strain - High Carbon Steel", fontweight ='bold')
    ax.legend([m1, m2], loc='best')


high_carbon()
graph_common()
plt.show()


# plt.savefig("ENGG103 Lab 4 Part 1.png", format='png', dpi=2500, bbox_inches='tight')