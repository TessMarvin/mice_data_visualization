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
    #find where the metadata ends and the weight log begins
    first_col = 0
    for i in range(0, wdata.shape[1]):
        if str.isdigit(columns[i]):
            first_col = i
            break
    #parse the weight data for each mouse and store it in a dictionary
    for mouse in wdata.index:
        y = []
        x = []
        for i in range(first_col,wdata.shape[1]):
            if math.isnan(wdata.loc[mouse,columns[i]]):
                continue
            else:
                y.append(wdata.loc[mouse,columns[i]].tolist())
                x.append(int(columns[i]))
        data[mouse] = y, x
        #print(mouse, data[mouse])
    #Create two plots, vertically arranged (one for each gender)
    fig, axs = plt.subplots(1,1)
    #Give the plots a little space between them so we can have x-axis titles and tick marks
    fig.subplots_adjust(hspace=0.5)
    #Name the plot EDIT NEEDED TO MAKE FLEXIBLE
    fig.suptitle("Body Weight")
    #So this for loop goes and builds each subplot
    for mouse in data.keys():
            axs.scatter(data[mouse][1], data[mouse][0])
            #ax.set(xlabel= , ylabel=)
            #Because there are so many progeny, rotate the tick labels and decrease the font size
            #plt.setp(ax.get_xticklabels(), rotation=45, ha='right', fontsize = 6)
    plt.show()

def main():
        wdata = pd.read_csv("treated_w.csv", sep = ',')
        weightplot_hero(wdata)

if __name__ == '__main__':
    main()
