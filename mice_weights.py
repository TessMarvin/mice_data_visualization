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
import math

def weightplot_hero(wdata, fig_title = "Body Weight", yaxis = "Age (days)", xaxis = "Weight (grams)"):
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
    #Create two plots, vertically arranged (one for each gender)
    fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, sharey=True)
    #Give the plots a little space between them so we can have x-axis titles and tick marks
    fig.subplots_adjust(hspace=0.5)
    #Name the plot EDIT NEEDED TO MAKE FLEXIBLE
    fig.suptitle(fig_title)
    #So this for loop goes and builds each subplot
    color_dict = {'A':'r', 'B':'b', 'C':'k'}
    grps = []
    grps2 = []
    for mouse in data.keys():
            if(wdata.loc[mouse, 'Gender'] == 'F'):
                drug_group = wdata.loc[mouse, 'Drug Treatment']
                if(drug_group in grps):
                    ax1.scatter(data[mouse][1], data[mouse][0], color = color_dict[drug_group])
                    ax1.set(title= "Female Mice", xlabel= xaxis, ylabel=yaxis)
                else:
                    grps.append(drug_group)
                    ax1.scatter(data[mouse][1], data[mouse][0], color = color_dict[drug_group], label = drug_group)
                    ax1.legend()
                    ax1.set(title= "Female Mice", xlabel= xaxis, ylabel=yaxis)
            else:
                drug_group = wdata.loc[mouse, 'Drug Treatment']
                if(drug_group in grps2):
                    ax2.scatter(data[mouse][1], data[mouse][0], color = color_dict[drug_group])
                    ax2.set(title= "Male Mice", xlabel= xaxis, ylabel=yaxis)
                else:
                    grps2.append(drug_group)
                    ax2.scatter(data[mouse][1], data[mouse][0], color = color_dict[drug_group], label = drug_group)
                    ax2.legend()
                    ax2.set(title= "Male Mice", xlabel= xaxis, ylabel=yaxis)
    plt.show()
def untreated_hero(tdata, fig_title = "Body Weight", yaxis = "Age (days)", xaxis = "Weight (grams)"):
        columns = list(tdata)
        tdata.index = tdata['Mouse']
        #print(wdata.loc['O573', '30'])
        #print(columns)
        data = {}
        #find where the metadata ends and the weight log begins
        first_col = 0
        for i in range(0, tdata.shape[1]):
            if str.isdigit(columns[i]):
                first_col = i
                break
        #parse the weight data for each mouse and store it in a dictionary
        for mouse in tdata.index:
            y = []
            x = []
            for i in range(first_col,tdata.shape[1]):
                if math.isnan(tdata.loc[mouse,columns[i]]):
                    continue
                else:
                    y.append(tdata.loc[mouse,columns[i]].tolist())
                    x.append(int(columns[i]))
            data[mouse] = y, x
        #Create two plots, vertically arranged (one for each gender)
        fig, (ax1, ax2) = plt.subplots(2,1, sharex=True, sharey=True)
        #Give the plots a little space between them so we can have x-axis titles and tick marks
        fig.subplots_adjust(hspace=0.5)
        #Name the plot EDIT NEEDED TO MAKE FLEXIBLE
        fig.suptitle(fig_title)
        color_dict = {'+/+-/-':'r', '-/-+/+':'b', '-/+-/+':'k', '-/+-/-':'c', '-/++/+':'m', \
        '+/++/+':'g', '+/+-/+':'y', '-/--/-':'orange', '-/--/+':'burlywood' }
        #So this for loop goes and builds each subplot
        grps = []
        grps2 = []
        for mouse in data.keys():
                if(tdata.loc[mouse, 'Gender'] == 'F'):
                    geno_group = tdata.loc[mouse, 'StARD9 GENOTYPE'] + tdata.loc[mouse, 'I1061T GENOTYPE']
                    if(geno_group in grps):
                        ax1.scatter(data[mouse][1], data[mouse][0], color = color_dict[geno_group])
                        ax1.set(title= "Female Mice", xlabel= xaxis, ylabel=yaxis)
                    else:
                        grps.append(geno_group)
                        ax1.scatter(data[mouse][1], data[mouse][0], color = color_dict[geno_group], label = geno_group)
                        ax1.set(title= "Female Mice", xlabel= xaxis, ylabel=yaxis)
                        ax1.legend()
                else:
                    geno_group = tdata.loc[mouse, 'StARD9 GENOTYPE'] + tdata.loc[mouse, 'I1061T GENOTYPE']
                    if(geno_group in grps2):
                        ax2.scatter(data[mouse][1], data[mouse][0], color = color_dict[geno_group])
                        ax2.set(title= "Male Mice", xlabel= xaxis, ylabel=yaxis)
                    else:
                        grps2.append(geno_group)
                        ax2.scatter(data[mouse][1], data[mouse][0], color = color_dict[geno_group], label = geno_group)
                        ax2.set(title= "Male Mice", xlabel= xaxis, ylabel=yaxis)
                        ax2.legend()
        plt.show()
#So this turns the command line arguments into a beautiful GUI
#Here I built out a File Menu with an About Menu
@Gooey(
    program_name='Mice Treatment Analysis',
    menu=[{
    'name':'File',
    'items': [{
            'type': 'AboutDialog',
            'menuTitle': 'About',
            'name': 'Mice Weight Figure Generation',
            'description': 'A tool to create visuals of data concerning the weight of mice treated with drug',
            'version': '1.0',
            'copyright': '2020',
            'website': 'https://github.com/TessMarvin',
            'developer': 'Tess Marvin (tmarvin@nd.edu)',
            'license': 'University of Notre Dame'
    }]
    }]
)
def main():
        #wdata = pd.read_csv("treated_w.csv", sep = ',')
        #weightplot_hero(wdata)
        #tdata = pd.read_csv("JJmice.csv", sep = ',')
        #untreated_hero(tdata)
        #So first we will handle the arguments that are "required"
        #Here we give our GUI a title
        parser = GooeyParser(description="Dashboard for Mice Analysis")
        #Here we allow for the selection of the data files to analyze
        #Because there is no - infront of file_chooser it is required!
        parser.add_argument("file_chooser", help = 'Choose the csv file to analyze.', widget='FileChooser')
        parser.add_argument("-Graph_title", help="Choose the label for the Figure.")
        parser.add_argument("-y_axis_title", help="Choose the label for the y-axis.")
        parser.add_argument("-x_axis_title", help="Choose the label for the x-axis.")
        parser.add_argument(
            '-mouse_type',
            metavar='Choose Data Type to Analyze',
            help='Select the type of mouse being analyzed',
            dest='m_type',
            widget='Dropdown',
            choices= ['JJ Mice', 'Treated Mice'],
            gooey_options={
                'validator': {
                    'test': 'user_input != "Select Option"',
                    'message': 'Choose a save file from the list'
                }
            }
        )
        #Now we parse all these arguments
        args = parser.parse_args()
        raw_data= args.file_chooser
        yaxis=args.y_axis_title
        fig_title=args.Graph_title
        xaxis=args.x_axis_title
        analysis_type = args.m_type
        #if no CSV file is found and we want to visualize, fail gracefully and request the CSV file be provided
        if(len(raw_data) == 0):
            print("Please ensure that you select files to analyze")
            return(None)
        #if the user would like to provide y-axis and figure title, use it, otherwise use the default
        else:
            wdata = pd.read_csv(raw_data, sep = ',')
            if(yaxis is not None):
                if(fig_title is not None):
                    if(xaxis is not None):
                        if(analysis_type == 'JJ Mice'):
                            untreated_hero(wdata, fig_title, yaxis, xaxis)
                        else:
                            weightplot_hero(wdata, fig_title, yaxis, xaxis)
            elif(fig_title is not None):
                if(xaxis is not None):
                    if(analysis_type == 'JJ Mice'):
                        untreated_hero(wdata, fig_title=fig_title, xaxis=xaxis)
                    else:
                        weightplot_hero(wdata, fig_title=fig_title, xaxis=xaxis)
                else:
                    if(analysis_type == 'JJ Mice'):
                        untreated_hero(wdata, fig_title=fig_title)
                    else:
                        weightplot_hero(wdata, fig_title=fig_title)
            elif(xaxis is not None):
                if(analysis_type == 'JJ Mice'):
                    untreated_hero(wdata, xaxis=xaxis)
                else:
                    weightplot_hero(wdata, xaxis=xaxis)
            else:
                if(analysis_type == 'JJ Mice'):
                    untreated_hero(wdata)
                else:
                    weightplot_hero(wdata)
if __name__ == '__main__':
    main()
