import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import shapely.geometry as sg
import math
from scipy.stats import linregress

def metals():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    # Import CSV for each metal
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True)
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True)
    s3 = np.genfromtxt("s3.csv", delimiter=",", autostrip=True)

    # Plot each metal
    ax.plot(s1[0], s1[1], color='#e63946', linewidth=1)
    ax.plot(s2[0], s2[1], color='#2a9d8f', linewidth=1)
    ax.plot(s3[0], s3[1], color='#fb8500', linewidth=1)
    
    # Name each metal
    m1 = "High Carbon Steel"
    m2 = "Galvanized Mild Steel"
    m3 = "Aluminum"

    stress_unit = "GPa"

    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Metallic Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')
    plt.savefig("ENGG103 Lab 4 Part 1.png", format='png', dpi=3000, bbox_inches='tight')

def pla():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    # Import CSV for each material
    s4 = np.genfromtxt("s4.csv", delimiter=",", autostrip=True)
    s5 = np.genfromtxt("s5.csv", delimiter=",", autostrip=True)
    s6 = np.genfromtxt("s6.csv", delimiter=",", autostrip=True)
    
    # Plot each material
    ax.plot(s4[0], s4[1], color='#593F62', linewidth=1)
    ax.plot(s5[0], s5[1], color='#005f73', linewidth=1)
    ax.plot(s6[0], s6[1], color='#8FC93A', linewidth=1)
    
    # Name each material
    m1 = "PLA - Vertical Longitudinal Lines"
    m2 = "PLA - Horizontal Longitudinal Lines"
    m3 = "PLA - Mixed Orientations"

    # Print total elongation
    print("Total elongation PLA 1 :", max(s4[0]))
    print("Total elongation PLA 2 :", max(s5[0]))
    print("Total elongation PLA 3 :", max(s6[0]))

    stress_unit = "GPa"

    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - PLA Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')
    plt.savefig("ENGG103 Lab 4 Part 2.png", format='png', dpi=3000, bbox_inches='tight')

def metal_elastic():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    # Import CSV for each metal, only using elastic region
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True, usecols=range(1,312))
    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True, usecols=range(1,378))
    s3 = np.genfromtxt("s3.csv", delimiter=",", autostrip=True, usecols=range(1,344))

    # Assign x and y values for each metal
    x1, y1 = s1[0], s1[1]
    x2, y2 = s2[0], s2[1]
    x3, y3 = s3[0], s3[1]
    
    # Plot each metal
    ax.plot(x1, y1, color='#e63946', linewidth=1)
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1)
    ax.plot(x3, y3, color='#fb8500', linewidth=1)

    # Print slope of each line for use in table
    print("Metal 1 slope:", linregress(x1, y1).slope)
    print("Metal 2 slope:", linregress(x2, y2).slope)
    print("Metal 3 slope:", linregress(x3, y3).slope)

    # Get slope of each line using linregress for use in graph
    z1 = (linregress(x1, y1).slope) / 1000
    z2 = (linregress(x2, y2).slope) / 1000
    z3 = (linregress(x3, y3).slope) / 1000

    # Name each metal with integrated slope
    m1 = "High Carbon Steel - Slope = {} GPa".format(z1.round(2))
    m2 = "Galvanized Mild Steel - Slope = {} GPa".format(z2.round(2))
    m3 = "Aluminum - Slope = {} GPa".format(z3.round(2))

    stress_unit = "GPa"

    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Linear Region of Metallic Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='lower right', fontsize=9)
    plt.savefig("ENGG103 Lab 4 Part 3.png", format='png', dpi=3000, bbox_inches='tight')

### MILD STEEL NOT DONE ###
def mild_steel():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    fig.set_size_inches(22, 11)

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
    ax.annotate('0.2% Proof Yield Strength - {} GPa'.format(intersection.y.round(2)), xy=(intersection.x, intersection.y), xytext=(intersection.x + 0.005, intersection.y - 50), arrowprops=dict(arrowstyle='->', facecolor='black'),)

    # Find Ultimate Tensile Strength
    max_stress = max(s2[1])
    print("Max Stress =", max_stress)

    # Mark Ultimate Tensile Strength
    plt.plot(0.00497636363636364, max_stress, 'x', color='red', markersize=6)

    max_strain = max(s2[0])
    print("Max Strain =", max_strain)

    ax.annotate('Ultimate Tensile Strength - {} GPa'.format(max_stress.round(2)), xy=(0.00497636363636364, max_stress), xytext=(0.00497636363636364 + 0.005, max_stress + 10), arrowprops=dict(arrowstyle='->', facecolor='black'),)

    # Plot the Elastic Strain line
    arrow = patches.FancyArrowPatch((0,-0.1), (0.0055,-0.1), color='red', arrowstyle='<->', mutation_scale=15)
    plt.gca().add_patch(arrow)
    plt.text(0.0025, -0.5, "$\\epsilon_E$")

    # Plot the Plastic Strain Line
    arrow = patches.FancyArrowPatch((0.0055, -0.1), (max_strain,-0.1), color='orange', arrowstyle='<->', mutation_scale=15)
    plt.gca().add_patch(arrow)
    plt.text(0.1626, -0.5, "$\\epsilon_P$")
    stress_unit = "GPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Galvanized Mild Steel", fontweight ='bold')

    plt.show()
    plt.savefig("ENGG103 Lab 4 Part 4.png", format='png', dpi=3000, bbox_inches='tight')

def high_carbon():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    # Import CSV for metal
    s1 = np.genfromtxt("s1.csv", delimiter=",", autostrip=True)
    xeng, yeng = s1[0], s1[1]

    # Plot Engineering Stress Strain
    ax.plot(xeng, yeng, color='red', linewidth=1)

    # Calculate True Stress Strain

    # Strain = ln(1 + Eng Strain)
    xtrue = [math.log(1 + i) for i in xeng]

    # Stress = Eng Stress(1 + Eng Strain)
    ytrue = [math.prod([yeng[i], (1 + xeng[i])]) for i in range(len(yeng))] 

    # Plot True Stress Strain
    ax.plot(xtrue, ytrue, color='#2a9d8f', linewidth=1)
    
    stress_unit = "GPa"
    
    # Name each curve
    m1 = "Engineering Stress Strain"
    m2 = "True Stres Strain"
    
    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Engineering vs True Stress Strain - High Carbon Steel", fontweight ='bold')
    ax.legend([m1, m2], loc='best')
    plt.savefig("ENGG103 Lab 4 Part 5.png", format='png', dpi=3000, bbox_inches='tight')

ch = int(input("Enter option: "))
metals() if ch == 1 else print()
pla() if ch == 2 else print()
metal_elastic() if ch == 3 else print()
mild_steel() if ch == 4 else print()
high_carbon() if ch == 5 else print()