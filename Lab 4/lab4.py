import matplotlib.pyplot as plt
import numpy as np

def readfile():
    f = open("lab4.csv", "r", encoding="utf-8")
    data = f.readlines()
    f.close()
    