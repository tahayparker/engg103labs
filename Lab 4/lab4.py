import matplotlib.pyplot as plt
import numpy as np
import dask.array as da
import csv

fig, ax = plt.subplots()

def readfile():
    f = open("vals.csv", "r", encoding="utf-8")
    data = csv.reader(f)
    data = list(data)
    f.close()
    return remove_whitespace_recursive(data)

def remove_whitespace_recursive(data):
    if isinstance(data, str):
        # If the element is a string, remove leading and trailing whitespaces
        return data.strip()
    elif isinstance(data, list):
        # If the element is a list, apply the function to each element in the list
        return [remove_whitespace_recursive(item) for item in data]
    else:
        # If the element is neither a string nor a list, return it as is
        return data

def graph_common():
    ax.set_facecolor('#EBEBEB')
    ax.set_axisbelow(True)
    [ax.spines[side].set_visible(False) for side in ax.spines]
    ax.grid()
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.minorticks_on()

def metals():
    data = readfile()

    assert data[0][0] == "\ufeffx1"
    assert data[1][0] == "y1"
    """
    assert data[2][0] == "x2"
    assert data[3][0] == "y2"
    assert data[4][0] == "x3"
    assert data[5][0] == "y3"
    """

    ax.plot(data[0][1:], data[1][1:], color='#e63946', linewidth=1)
    ax.plot(data[2][1:], data[3][1:], color='#2a9d8f', linewidth=1)
    ax.plot(data[4][1:], data[5][1:], color='#fb8500', linewidth=1)
    
    m1 = "High Carbon Steel"
    m2 = "Galvanized Mild Steel"
    m3 = "Aluminum"

    stress_unit = None

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Metals", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def pla():
    data = readfile()

    assert data[6][0] == "x4"
    assert data[7][0] == "y4"
    assert data[8][0] == "x5"
    assert data[9][0] == "y5"
    assert data[10][0] == "x6"
    assert data[11][0] == "y6"

    ax.plot(data[6][1:], data[7][1:], color='#593F62', linewidth=1)
    ax.plot(data[8][1:], data[9][1:], color='#005f73', linewidth=1)
    ax.plot(data[10][1:], data[11][1:], color='#8FC93A', linewidth=1)
    
    m1 = "PLA - Vertical Longitudinal Lines"
    m2 = "PLA - Horizontal Longitudinal Lines"
    m3 = "PLA - Mixed Orientations"

    stress_unit = None

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$, {})'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - PLA Samples", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def metal_elastic():
    data = readfile()

    assert data[12][0] == "x1.minor"
    assert data[13][0] == "y1.minor"
    assert data[14][0] == "x2.minor"
    assert data[15][0] == "y2.minor"
    assert data[16][0] == "x3.minor"
    assert data[17][0] == "y3.minor"

    ax.plot(data[12][1:], data[13][1:], color='#e63946', linewidth=1)
    ax.plot(data[14][1:], data[15][1:], color='#2a9d8f', linewidth=1)
    ax.plot(data[16][1:], data[17][1:], color='#fb8500', linewidth=1)

    # Get slope of each line using numpy.polyfit
    
    z1 = np.polyfit(data[12][1:], data[13][1:], 1)
    z2 = np.polyfit(data[14][1:], data[15][1:], 1)
    z3 = np.polyfit(data[16][1:], data[17][1:], 1)

    m1 = "High Carbon Steel - Slope = {} Pa".format(z1[0].round(2))
    m2 = "Galvanized Mild Steel - Slope = {} Pa".format(z2[0].round(2))
    m3 = "Aluminum - Slope = {} Pa".format(z3[0].round(2))

    stress_unit = None

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$), {}'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain", fontweight ='bold')
    ax.legend([m1, m2, m3], loc='best')

def mild_steel():
    data = readfile()

    assert data[2][0] == "x2"
    assert data[3][0] == "y2"
    assert data[14][0] == "x2.minor"
    assert data[15][0] == "y2.minor"

    ax.plot(data[2][1:], data[3][1:], color='#2a9d8f', linewidth=1)

    # 0.2% Proof Stress
    z = np.polyfit(data[14][1:], data[15][1:], 1)
    
    # Plot the line with x += 0.002
    p = np.poly1d(z)
    x = data[14][1:]
    ax.plot(x, (p(x) + 0.002), color='#2a9d8f', linewidth=1)

    # Find Ultimate Tensile Strength
    max_stress = max(data[3][1:])

    # Mark Ultimate Tensile Strength with an arrow and value
    ax.annotate('Ultimate Tensile Strength', xy=(0.002, max_stress), xytext=(0.002, max_stress + 100000), arrowprops=dict(facecolor='black', shrink=0.05),)
    
    # Mark the x-axis with an arrow indicating the Elastic Strain
    ax.annotate('Elastic Strain', xy=(0.002, 0), xytext=(0.002, -100000), arrowprops=dict(facecolor='black', shrink=0.05),)

    # Mark the x-axis with an arrow indicating the Plastic Strain
    ax.annotate('Plastic Strain', xy=(0.002, 0), xytext=(0.002, -200000), arrowprops=dict(facecolor='black', shrink=0.05),)

    stress_unit = None

    ax.set_xlabel('Strain ($\\epsilon$)', fontweight ='bold')
    ax.set_ylabel('Stress ($\\sigma$), {}'.format(stress_unit), fontweight ='bold')
    ax.set_title("Stresss vs Strain - Galvanized Mild Steel", fontweight ='bold')

metals()
graph_common()
# plt.show()
plt.savefig("ENGG103 Lab 4 Part 1", format='png', dpi=2500, bbox_inches='tight')