import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import shapely.geometry as sg
import math
from scipy.stats import linregress
from decimal import Decimal

# Transpose the CSVs
def transpose():
    for i in range(1,7):
        pd.read_csv('{}.csv'.format(i), header=None).T.to_csv('s{}.csv'.format(i), header=False, index=False)

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

    s1m = np.genfromtxt("s1.csv", delimiter=",", autostrip=True, usecols=range(1,312))
    s2m = np.genfromtxt("s2.csv", delimiter=",", autostrip=True, usecols=range(1,378))
    s3m = np.genfromtxt("s3.csv", delimiter=",", autostrip=True, usecols=range(1,360))


    # Set x and y values for each metal
    x1 = [Decimal(str(i)) / Decimal('55') for i in s1[0]]
    x2 = [Decimal(str(i)) / Decimal('55') for i in s2[0]]
    x3 = [Decimal(str(i)) / Decimal('55') for i in s3[0]]
    y1 = [Decimal(str(i)) / Decimal('5.4') for i in s1[1]]
    y2 = [Decimal(str(i)) / Decimal('5.4') for i in s2[1]]
    y3 = [Decimal(str(i)) / Decimal('5.4') for i in s3[1]]

    x1m = [Decimal(str(i)) / Decimal('55') for i in s1m[0]]
    x2m = [Decimal(str(i)) / Decimal('55') for i in s2m[0]]
    x3m = [Decimal(str(i)) / Decimal('55') for i in s3m[0]]
    y1m = [Decimal(str(i)) / Decimal('5.4') for i in s1m[1]]
    y2m = [Decimal(str(i)) / Decimal('5.4') for i in s2m[1]]
    y3m = [Decimal(str(i)) / Decimal('5.4') for i in s3m[1]]

    # Plot each metal
    ax.plot(x1, y1, color='#e63946', linewidth=1)
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1)
    ax.plot(x3, y3, color='#fb8500', linewidth=1)

    # Print max stress for each metal
    print("Max Stress Metal 1:", max(y1))    
    print("Max Stress Metal 2:", max(y2))
    print("Max Stress Metal 3:", max(y3))

    # Print max strain for each metal
    print("Max Strain Metal 1:", max(x1))
    print("Max Strain Metal 2:", max(x2))
    print("Max Strain Metal 3:", max(x3))
    
    # Name each metal
    m1 = "High Carbon Steel"
    m2 = "Galvanized Mild Steel"
    m3 = "Aluminum"

    stress_unit = "GPa"

    # 0.2% Proof Stress
    z1 = np.polyfit([float(i) for i in x1m], [float(i) for i in y1m], 1)
    z2 = np.polyfit([float(i) for i in x2m], [float(i) for i in y2m], 1)
    z3 = np.polyfit([float(i) for i in x3m], [float(i) for i in y3m], 1)
    
    # Plot the proof stress line with x += 0.002
    p1 = np.poly1d(z1)
    p2 = np.poly1d(z2)
    p3 = np.poly1d(z3)
    
    x1_int = [(Decimal(i) + Decimal('0.002')) for i in x1m]
    x2_int = [(Decimal(i) + Decimal('0.002')) for i in x2m]
    x3_int = [(Decimal(i) + Decimal('0.002')) for i in x3m]

    y1_int = p1([float(i) for i in x1m])
    y2_int = p2([float(i) for i in x2m])
    y3_int = p3([float(i) for i in x3m])

    # Find intersection of the two lines
    l11 = sg.LineString(np.column_stack((x1, y1)))
    l12 = sg.LineString(np.column_stack((x1_int, y1_int)))
    intersection1 = l11.intersection(l12)

    l21 = sg.LineString(np.column_stack((x2, y2)))
    l22 = sg.LineString(np.column_stack((x2_int, y2_int)))
    intersection2 = l21.intersection(l22)

    l31 = sg.LineString(np.column_stack((x3, y3)))
    l32 = sg.LineString(np.column_stack((x3_int, y3_int)))
    intersection3 = l31.intersection(l32)
 
    # Print Intersection values of all lines
    print("Intersection 1:", intersection1)
    print("Intersection 2:", intersection2)
    print("Intersection 3:", intersection3)

    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Metallic Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')
    # plt.show()
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

    # Set x and y values for each material
    x4 = [Decimal(str(i)) / Decimal('30') for i in s4[0]]
    x5 = [Decimal(str(i)) / Decimal('30') for i in s5[0]]
    x6 = [Decimal(str(i)) / Decimal('30') for i in s6[0]]
    y4 = [Decimal(str(i)) / Decimal('20') for i in s4[1]]
    y5 = [Decimal(str(i)) / Decimal('20') for i in s5[1]]
    y6 = [Decimal(str(i)) / Decimal('20') for i in s6[1]]
        
    # Plot each material
    ax.plot(s4[0], s4[1], color='#593F62', linewidth=1)
    ax.plot(s5[0], s5[1], color='#005f73', linewidth=1)
    ax.plot(s6[0], s6[1], color='#8FC93A', linewidth=1)
    
    # Name each material
    m1 = "PLA - Vertical Longitudinal Lines"
    m2 = "PLA - Horizontal Longitudinal Lines"
    m3 = "PLA - Mixed Orientations"

    # Print total elongation
    print("Total elongation PLA 1 :", max(x4))
    print("Total elongation PLA 2 :", max(x5))
    print("Total elongation PLA 3 :", max(x6))

    stress_unit = "GPa"

    # Get slope of line using linregress for use in table
    z1 = (linregress([float(i) for i in x4], [float(i) for i in y4]).slope)
    z2 = (linregress([float(i) for i in x5], [float(i) for i in y5]).slope)
    z3 = (linregress([float(i) for i in x6], [float(i) for i in y6]).slope)

    print("PLA 1 slope:", z1)
    print("PLA 2 slope:", z2)
    print("PLA 3 slope:", z3)

    # Print max stress
    print("Max Stress PLA 1:", max(y4))
    print("Max Stress PLA 2:", max(y5))
    print("Max Stress PLA 3:", max(y6))  

    # Set axis titles, graph title, and legend
    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - PLA Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')
    # plt.show()
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

    # Set x and y values for each metal
    x1 = [Decimal(str(i)) / Decimal('55') for i in s1[0]]
    x2 = [Decimal(str(i)) / Decimal('55') for i in s2[0]]
    x3 = [Decimal(str(i)) / Decimal('55') for i in s3[0]]
    y1 = [Decimal(str(i)) / Decimal('5.4') for i in s1[1]]
    y2 = [Decimal(str(i)) / Decimal('5.4') for i in s2[1]]
    y3 = [Decimal(str(i)) / Decimal('5.4') for i in s3[1]]

    # Plot each metal
    ax.plot(x1, y1, color='#e63946', linewidth=1)
    ax.plot(x2, y2, color='#2a9d8f', linewidth=1)
    ax.plot(x3, y3, color='#fb8500', linewidth=1)

    # Get slope of line using linregress for use in table
    z1 = (linregress([float(i) for i in x1], [float(i) for i in y1]).slope)
    z2 = (linregress([float(i) for i in x2], [float(i) for i in y2]).slope)
    z3 = (linregress([float(i) for i in x3], [float(i) for i in y3]).slope)

    # Print slope of each line for use in table
    print("Metal 1 slope:", z1)
    print("Metal 2 slope:", z2)
    print("Metal 3 slope:", z3)

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
    # plt.show()
    plt.savefig("ENGG103 Lab 4 Part 3.png", format='png', dpi=3000, bbox_inches='tight')

def mild_steel():
    fig, ax = plt.subplots()
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

    s2 = np.genfromtxt("s2.csv", delimiter=",", autostrip=True)
    s2m = np.genfromtxt("s2.csv", delimiter=",", autostrip=True, usecols=range(1,378))

    x1 = [Decimal(str(i)) / Decimal('55') for i in s2[0]]
    y1 = [math.prod([(Decimal(str(i)) / Decimal('5.4')), 1000]) for i in s2[1]]
    x2 = [Decimal(str(i)) / Decimal('55') for i in s2m[0]]
    y2 = [math.prod([(Decimal(str(i)) / Decimal('5.4')), 1000]) for i in s2m[1]]
    
    # Plot original line
    ax.plot(x1, y1, color='#8D5A97', linewidth=1)

    # 0.2% Proof Stress
    z = np.polyfit([float(i) for i in x2], [float(i) for i in y2], 1)
    
    # Plot the proof stress line with x += 0.002
    p = np.poly1d(z)
    x21 = [(Decimal(i) + Decimal('0.002')) for i in x2]
    y21 = p([float(i) for i in x2])
    ax.plot(x21, y21, color='#2a9d8f', linewidth=1, linestyle='--')

    # Find intersection of the two lines
    l1 = sg.LineString(np.column_stack((x1, y1)))
    l2 = sg.LineString(np.column_stack((x21, y21)))
    intersection = l1.intersection(l2)

    plt.plot(intersection.x, intersection.y, 'x', color='orange', markersize=6)

    # Point the intersection of the two lines with an arrow and label it away from the intersection below the graph so that it is readable
    ax.annotate('0.2% Proof Yield Strength - {} MPa'.format(intersection.y.round(2)), xy=(intersection.x, intersection.y), xytext=(intersection.x + 0.005, intersection.y - 50), arrowprops=dict(arrowstyle='->', facecolor='black'),)

    # Find Ultimate Tensile Strength
    max_stress = max([float(i) for i in y1])
    print("Max Stress =", max_stress)

    # Mark Ultimate Tensile Strength
    plt.plot(0.00497636363636364, max_stress, 'x', color='red', markersize=6)

    max_strain = max(x1)
    print("Max Strain =", max_strain)

    ax.annotate('Ultimate Tensile Strength - {} MPa'.format(round(max_stress, 2)), xy=(0.00497636363636364, max_stress), xytext=(0.00497636363636364 + 0.005, max_stress + 10), arrowprops=dict(arrowstyle='->', facecolor='black'),)
  
    # Plot the Elastic Strain line
    arrow = patches.FancyArrowPatch((0,-0.1), (0.0055,-0.1), color='red', arrowstyle='<->', mutation_scale=15)
    plt.gca().add_patch(arrow)
    plt.text(0.0025, -0.7, "$\\epsilon_E$")

    # Plot the Plastic Strain Line
    arrow = patches.FancyArrowPatch((0.0055, -0.1), (max_strain,-0.1), color='orange', arrowstyle='<->', mutation_scale=15)
    plt.gca().add_patch(arrow)
    plt.text(0.1626, -0.5, "$\\epsilon_P$")
    

    stress_unit = "MPa"

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Galvanized Mild Steel", fontweight ='bold')

    # plt.show()
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

    # Set x and y values for each metal
    x1 = [Decimal(str(i)) / Decimal('55') for i in s1[0]]
    y1 = [Decimal(str(i)) / Decimal('5.4') for i in s1[1]]

    xeng, yeng = x1, y1

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
    # plt.show()
    plt.savefig("ENGG103 Lab 4 Part 5.png", format='png', dpi=3000, bbox_inches='tight')




while True:
    ch = int(input("Enter option: "))
    if ch == 1:
        metals()
    elif ch == 2:
        pla()
    elif ch == 3:
        metal_elastic()
    elif ch == 4:
        mild_steel()
    elif ch == 5:
        high_carbon()
    elif ch == 0:
        transpose()
    elif ch == 9:
        exit()
    else:
        print("Invalid input")
