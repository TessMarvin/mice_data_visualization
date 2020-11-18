#Author: Tess Marvin (tmarvin@nd.edu)
#Usage: python mice_weights.py
#Purpose: Creates a plot of the mice weights over time for Vaughan Lab
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from argparse import ArgumentParser
import numpy as np
from scipy import stats
from gooey import Gooey
from gooey import GooeyParser
from argparse import ArgumentParser
from collections import Counter
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import math

def weightplot_hero(wdata):
    columns = list(wdata)
    wdata.index = wdata['Mouse']
    #print(wdata.loc['O573', '30'])
    #print(columns)
    data = {}
    for mouse in wdata.index:
        y = []
        x = []
        for i in range(5,wdata.shape[1]):
            if math.isnan(wdata.loc[mouse,columns[i]]):
                continue
            else:
                y.append(wdata.loc[mouse,columns[i]].tolist())
                x.append(int(columns[i]))
        data[mouse] = y, x
    for mouse in data.keys():
        

def main():
        wdata = pd.read_csv("treated_w.csv", sep = ',')
        weightplot_hero(wdata)

if __name__ == '__main__':
    main()
