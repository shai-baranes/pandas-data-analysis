# C:\Python_Rust_Removal\data_analysis_harvard\output
# def header_creator(text):
#   print(f" {'#'*100}")    
#   print(" #", " "*96, "#")
#   print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
#   print(" #", " "*96, "#")
#   print("", "#"*100)

# header_creator("Now with Sub-Plots:")



import numpy as np
import matplotlib.pyplot as plt

# data: https://github.com/rmotr-curriculum/data-cleaning-rmotr-freecodecamp/blob/master/4%20-%20More%20Visualizations.ipynb
# YT: https://www.youtube.com/watch?v=r-uOLxNrNk8&t=11070s

x = np.arange(-10, 11)
# array([-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1,   0,   1,   2, 3,   4,   5,   6,   7,   8,   9,  10])



# ---------------------------------------------------------------------------------------------------------------------
#   "Global API" # "Global API" # "Global API" # "Global API" (no recommended - non object oriented, line-order dependent)
# ---------------------------------------------------------------------------------------------------------------------


# -------------Plot Start-------------------

# plt.figure(figsize=(12, 6))

# plt.title('My Nice Plot #1')


# plt.plot(x, x ** 2)
# plt.plot(x, -1 * (x ** 2)) # added to the same plot panel

# plt.show() # 'My Nice Plot #1.png'
# -------------Plot Ends---------------------




# -------------Plot Start-------------------
# plt.figure(figsize=(12, 6))
# plt.title('My Nice Plot #2')


# plt.subplot(1, 2, 1)  # rows, columns, panel selected (starting with the 1st pannel)
# plt.plot(x, x ** 2)
# plt.plot([0, 0, 0], [-10, 0, 100]) # printing the vertical line
# plt.legend(['X^2', 'Vertical Line'])
# plt.xlabel('X')
# plt.ylabel('X Squared')


# plt.subplot(1, 2, 2) # rows, columns, panel selected (starting with the 2nd pannel)
# plt.plot(x, -1 * (x ** 2))
# plt.plot([-10, 0, 10], [-50, -50, -50]) # printing the horizontal line
# plt.legend(['-X^2', 'Horizontal Line'])
# plt.xlabel('X')
# plt.ylabel('X Squared')


# plt.show() # 'My Nice Plot #2.png'
# -------------Plot Ends---------------------




# -----------------------------------------------------------------------------------------------------------------------------
#   "OOP Interface" # "OOP Interface" # "OOP Interface" # "OOP Interface" # "OOP Interface" # "OOP Interface" # "OOP Interface"
# -----------------------------------------------------------------------------------------------------------------------------


# -------------Plot Start-------------------

# fig, axes = plt.subplots(figsize=(12, 6))


# axes.plot(x, (x ** 2), color='red', linewidth=3, marker='o', markersize=8, label='X^2') # 1st plot

# axes.plot(x, -1 * (x ** 2), 'b--', label='-X^2') # 2nd plot (same panel)

# axes.set_xlabel('X')
# axes.set_ylabel('X Squared')
# axes.set_title("My Nice Plot #3")
# axes.legend()

# fig.show() # 'My Nice Plot #3.png'
## plt.show() # that will also work (but the above is more OOP-wise)
# -------------Plot Ends---------------------




## nice example for line types
# -------------Plot Start-------------------

# fig, axes = plt.subplots(figsize=(12, 6))

# axes.plot(x, x + 0, linestyle='solid')
# axes.plot(x, x + 1, linestyle='dashed')
# axes.plot(x, x + 2, linestyle='dashdot')
# axes.plot(x, x + 3, linestyle='dotted');

# axes.set_title("My Nice Plot #4")

# fig.show() # My Nice Plot #4.png
# -------------Plot Ends---------------------



## another example with line types and color control
# -------------Plot Start-------------------

# fig, axes = plt.subplots(figsize=(12, 6))

# axes.plot(x, x + 0, '-og', label="solid green")
# axes.plot(x, x + 1, '--c', label="dashed cyan")
# axes.plot(x, x + 2, '-.b', label="dashdot blue")
# axes.plot(x, x + 3, ':r', label="dotted red")
# axes.plot(x, x + 4, '-.y', marker = "+", label="yellow w/ +")
# axes.plot(x, x + 5, 'p', marker = "|", label="ligh blue piped")

# axes.set_title("My Nice Plot # 5") # My Nice Plot #5.png

# axes.legend()
# fig.show()
# -------------Plot Ends---------------------


# linestyle options
linestyles = ['_', '-', '--', ':']
print(f"{linestyles=}")
# linestyles=['_', '-', '--', ':']

# many options for the markers:
markers = [m for m in plt.Line2D.markers]
print(f"{markers=}")
# markers=['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', 'P', 'X', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'None', 'none', ' ', '']



 ####################################################################################################
 #                                                                                                  #
 #                                        Now with Sub-Plots:                                       #
 #                                                                                                  #
 ####################################################################################################



# When we call the subplots() function we get a tuple containing a Figure and a axes element.

# most basic usage:
plot_objects = plt.subplots()

fig, ax = plot_objects

ax.plot([1,2,3], [1,2,3])

# fig.show() # uncomment to view




# 4 panes with OOP access for each:
# -------------Plot Start-------------------

# plot_objects = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))

# fig, ((ax1, ax2), (ax3, ax4)) = plot_objects # each element in a tuple shares 'Y' axis, plots w/ similar index shares 'X' axis

# # now the order doesn't matter
# ax4.plot(np.random.randn(50), c='yellow')
# ax1.plot(np.random.randn(50), c='red', linestyle='--')
# ax2.plot(np.random.randn(50), c='green', linestyle=':')
# ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3.0)

# ax1.set_title("My Nice sub-plot #1")
# ax2.set_title("My Nice sub-plot #2")
# ax3.set_title("My Nice sub-plot #3")
# ax4.set_title("My Nice sub-plot #4")

# fig.suptitle("This is the Main Figure Title", fontsize=18, fontweight='bold')

# fig.show() # 'Quadrants Combined.png'

# -------------Plot Ends---------------------




# There is another way to make subplots using a grid-like format:
# -------------Plot Start-------------------

# plt.figure(figsize=(14, 6))

# ax1 = plt.subplot2grid((3,3), (0,0), colspan=3) # starts from 1st row (0) and first col (0)
# ax2 = plt.subplot2grid((3,3), (1,0), colspan=2) # starts from 2nd row (1) and first col (0)
# ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2) # starts from 2nd row (1) and 3rd col (2)
# ax4 = plt.subplot2grid((3,3), (2,0))            # starts from 3rd row (2) and 1st col (0)
# ax5 = plt.subplot2grid((3,3), (2,1))            # starts from 3rd row (2) and 2nd col (1)
# ax1.plot(np.random.randn(50), c='red', linestyle='--')
# ax2.plot(x, x**2, linestyle='solid')
# plt.show() # 'Grid Plot.png'
# -------------Plot Ends---------------------