import numpy as np
import matplotlib.pyplot as plt

# bar(col1, col2, label, xlabel, ylabel, title, color)

# multi_bar(x, y, x1, y1, label1, label2, xlabel, ylabel, title, color1, color2)

#histogram(data_list, bins, color, xlabel, ylabel, title, label=None, histtype='bar', edgecolor='black', axvline_value=None, axvline_label=None, axvline_color=None, axvline_width=None)

#pie(slices_list, labels_list, colors_list, title, start_angle = 0, explode=None, shadow=True)

#line(x, y, xlabel, ylabel, label=None, title=None, color='black')

#scatter(x, y, xlabel, ylabel, title, label=None, s=10, linewidth=0, edgecolor=None, c=None, cmap=None, cbar_label=None, log=None)

#Function for bar graph.
def bar(col1, col2, label, xlabel, ylabel, title, color, width=0.7):
    plt.bar(col1, col2, label=label, color=color, width=width)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

#Function for bar graps with more than one data sets.
def multi_bar(x, y, y1, label1, label2, xlabel, ylabel, title, color1, color2, width=0.2):
    # Convert the x (categories) to numerical values
    x_indexes = np.arange(len(x))
    
    # Shift the positions for the second set of bars
    x1_indexes = x_indexes + width
    
    plt.bar(x_indexes, y, width=width, label=label1, color=color1)  # First set of bars
    plt.bar(x1_indexes, y1, width=width, label=label2, color=color2)  # Second set of bars
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(ticks=x_indexes + width/2, labels=x)  # Set the x-ticks to the center of the bars
    plt.legend()
    plt.show()

#Function for Histogram.
def histogram(data_list, bins, color, xlabel, ylabel, title, label=None, r_width=None, histtype='bar', edgecolor='black', axvline_value=None, axvline_label=None, axvline_color=None):
    plt.hist(data_list, bins, color=color, label=label, histtype=histtype, edgecolor=edgecolor, rwidth=r_width)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    if axvline_value != None:
        plt.axvline(axvline_value, color=axvline_color, label=axvline_label)
    
    if label != None:
        plt.legend()
    
    plt.show()

#Function to create pie chart
def pie(slices_list, labels_list, colors_list, title, start_angle = 0, explode=None, shadow=True):
    plt.pie(slices_list, labels=labels_list, colors=colors_list, startangle=start_angle, explode=explode, shadow=shadow, autopct='%1.2f%%')
    plt.title(title)
    plt.legend()
    plt.show()

#Function to create line graph
def line(x, y, xlabel, ylabel, label=None, title=None, color='black'):
    plt.plot(x, y, color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if label != None:
        plt.legend()
    
    plt.show()

#Function to create scatter plot
def scatter(x, y, xlabel, ylabel, title, label=None, s=10, linewidth=0, edgecolor=None, c=None, cmap=None, cbar_label=None, log=None):
    plt.scatter(x, y, s, linewidths=linewidth, edgecolors=edgecolor,c=c, cmap=cmap)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if label!=None:
        plt.legend()
    
    if c is list:
        cbar = plt.colorbar()
        cbar.set_label(cbar_label)
    
    if log!=None:
        plt.xscale('log')
        plt.yscale('log')
    
    plt.show()
