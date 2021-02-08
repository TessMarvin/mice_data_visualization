#Author: Tess Marvin (tmarvin@nd.edu)
#Usage: python mice_weights.py
#Purpose: Creates a plot of the organ mice weights over time for Vaughan Lab
import pandas as pd
import matplotlib.pyplot as plt
import math

def o_weights(wdata, organ):
    for wtype in ["HW", "DW"]:
        W_dict = {"A":[], "B":[], "C":[]}
        for mouse in wdata.index:
            if(wtype == "HW"):
                col_string = organ + " % of HW"
            else:
                col_string = organ+ " % of DW"
            treat = wdata.loc[mouse, 'Treatment']
            W = float(wdata.loc[mouse,col_string])
            if(math.isnan(W) or treat == "UNTREATED"):
                continue
            else:
                W_dict[treat].append(W)

        labels, data = [*zip(*W_dict.items())]  # 'transpose' items to parallel key, value lists
        plt.boxplot(data)
        plt.xticks(range(1, len(labels) + 1), labels)
        if(wtype == "HW"):
            plt.ylabel( "% of Highest Weight")
        else:
            plt.ylabel( "% of Death Weight")
        plt.xlabel("Drug Treatment")
        if(wtype == "HW"):
            t= organ + " % of Highest Weight"
        else:
            t= organ + " % of Death Weight"
        plt.title(t)
        i = 1
        for group in W_dict.keys():
            y = list(sorted(W_dict[group]))
            x = []
            for j in range(len(y)):
                x.append(i)
            i = i + 1
            plt.scatter(x,y,alpha=0.5, color="black")
        plt.show()

def main():
    wdata= pd.read_csv("oweight.csv", header=0, index_col=0)
    organs = ["Liver", "Brain", "Spleen"]
    for o in organs:
        o_weights(wdata,o)

if __name__ == '__main__':
    main()
