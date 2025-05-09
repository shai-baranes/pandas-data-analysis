import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.max_rows', None) #


sales = pd.read_csv(r"./data/sales_data.csv")
# data = pd.read_csv("./data/sales_data.csv", usecols = ["final_price", "image_url", "url", "title", "categories"], chunksize = 10) # chunksize for preformance

print(sales.head())


print(sales.shape[0]) # 113036 lines
# sales.shape --> (113036, 18)

print(sales.info())  # prefered over > sales.columns
# Data columns (total 18 columns):
#  #   Column            Non-Null Count   Dtype
# ---  ------            --------------   -----
#  0   Date              113036 non-null  object
#  1   Day               113036 non-null  int64
#  2   Month             113036 non-null  object
#  3   Year              113036 non-null  int64
#  4   Customer_Age      113036 non-null  int64
#  5   Age_Group         113036 non-null  object
#  6   Customer_Gender   113036 non-null  object
#  7   Country           113036 non-null  object
#  8   State             113036 non-null  object
#  9   Product_Category  113036 non-null  object
#  10  Sub_Category      113036 non-null  object
#  11  Product           113036 non-null  object
#  12  Order_Quantity    113036 non-null  int64
#  13  Unit_Cost         113036 non-null  int64
#  14  Unit_Price        113036 non-null  int64
#  15  Profit            113036 non-null  int64
#  16  Cost              113036 non-null  int64
#  17  Revenue           113036 non-null  int64
# dtypes: int64(9), object(9)
# memory usage: 15.5+ MB

print(sales.describe())
#                  Day           Year   Customer_Age  Order_Quantity      Unit_Cost     Unit_Price         Profit           Cost        Revenue
# count  113036.000000  113036.000000  113036.000000   113036.000000  113036.000000  113036.000000  113036.000000  113036.000000  113036.000000
# mean       15.665753    2014.401739      35.919212       11.901660     267.296366     452.938427     285.051665     469.318695     754.370360
# std         8.781567       1.272510      11.021936        9.561857     549.835483     922.071219     453.887443     884.866118    1309.094674
# min         1.000000    2011.000000      17.000000        1.000000       1.000000       2.000000     -30.000000       1.000000       2.000000
# 25%         8.000000    2013.000000      28.000000        2.000000       2.000000       5.000000      29.000000      28.000000      63.000000
# 50%        16.000000    2014.000000      35.000000       10.000000       9.000000      24.000000     101.000000     108.000000     223.000000
# 75%        23.000000    2016.000000      43.000000       20.000000      42.000000      70.000000     358.000000     432.000000     800.000000
# max        31.000000    2016.000000      87.000000       32.000000    2171.000000    3578.000000   15096.000000   42978.000000   58074.000000


print(sales['Unit_Cost'].describe())  # more focused
# count    113036.000000
# mean        267.296366
# std         549.835483
# min           1.000000
# 25%           2.000000
# 50%           9.000000
# 75%          42.000000
# max        2171.000000

sales['Unit_Cost'].mean()
# 267.296365759581

sales['Unit_Cost'].median()
# 9.0

## basic ( 2 seperate plots)
# sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,2))
# sales['Unit_Cost'].plot(kind='density', figsize=(14,4))


# # advanced (combining both plots into a single frame)
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(14, 6))
# sales['Unit_Cost'].plot(kind='box', vert=False, ax=axes[0])
# sales['Unit_Cost'].plot(kind='density', ax=axes[1])
# plt.tight_layout()
# plt.show()  # reminder that we also have session where we plug the plots directly into the excel


# # advanced + (aligning the x axes for both)
# # Calculate the min and max for the x-axis (with some padding)
# xmin = -200  # start at 0 or the actual min, whichever is smaller
# # xmin = min(sales['Unit_Cost'].min(), 0)  # start at 0 or the actual min, whichever is smaller
# xmax = sales['Unit_Cost'].max() * 1.05   # a little padding on the right

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(14, 6), sharex=True)

# # Boxplot
# sales['Unit_Cost'].plot(kind='box', vert=False, ax=axes[0])
# axes[0].set_xlim(xmin, xmax)
# axes[0].set_xlabel('')  # Hide x-label on top plot

# # Density plot
# sales['Unit_Cost'].plot(kind='density', ax=axes[1])
# axes[1].set_xlim(xmin, xmax)

# plt.tight_layout()
# plt.show()


# # --------------Start------------

## Now adding vertical lines for both 'mean' (red) & 'median' (green)
mean_val = sales['Unit_Cost'].mean()
median_val = sales['Unit_Cost'].median()

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 6), sharex=True)

# Boxplot
sales['Unit_Cost'].plot(kind='box', vert=False, ax=axes[0])
axes[0].axvline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
axes[0].axvline(median_val, color='green', linestyle='-', linewidth=2, label='Median')
axes[0].legend(loc='upper right')

# Density plot
sales['Unit_Cost'].plot(kind='density', ax=axes[1])
axes[1].axvline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
axes[1].axvline(median_val, color='green', linestyle='-', linewidth=2, label='Median')
axes[1].legend(loc='upper right')

xmin = -200  # start at 0 or the actual min, whichever is smaller
xmax = sales['Unit_Cost'].max() * 1.05   # a little padding on the right

axes[0].set_xlim(xmin, xmax)
axes[1].set_xlim(xmin, xmax)

# eventually also changing the y-axis from 'Density' into 'Number of Sales' and the x-axis from 'tbd' into 'dollars'
# sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2]).set_ylabel('Number of Sales')
# note that 'ax' can also be any other variable name
ax = sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2], bins=100)
# ax = sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2]) # 10 bin by default
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')


plt.tight_layout()
plt.show()

# # ----------------End---------------

print(sales['Age_Group'].info)
# 1            Youth (<25)
# 2         Adults (35-64)
# 3         Adults (35-64)
# 4         Adults (35-64)
#                ...
# 113031    Adults (35-64)
# 113032       Youth (<25)
# 113033       Youth (<25)
# 113034    Adults (35-64)
# 113035    Adults (35-64)


print(sales['Age_Group'].value_counts())
# Age_Group
# Adults (35-64)          55824
# Young Adults (25-34)    38654
# Youth (<25)             17828
# Seniors (64+)             730


# as if we're group by 'Age_Group' and getting the count statistics

# # --------------Start------------

# # again having 2 charts together, now side by side
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 14))
# sales['Age_Group'].value_counts().plot(kind='pie', figsize=(8,6), ax=axes[0])
# sales['Age_Group'].value_counts().plot(kind='bar', figsize=(12,6), ax=axes[1]).set_ylabel('Number of Sales')
# plt.tight_layout()
# plt.show()


# # --------------End--------------



# now let's have some visual correlation Analysis between each per of applicable columns
# Dark red is for negative (opposite) correlation while dark blue is for positive correlation. (range: -1.0 <-> 1.0)

# the following 2 lines are to avoid: "ValueError: could not convert string to float: '2013-11-26'" as happend upon: > corr = sales.corr()
numeric_sales = sales.select_dtypes(include='number')
corr = numeric_sales.corr()

print(corr)
#                      Day      Year  Customer_Age  Order_Quantity  Unit_Cost  Unit_Price    Profit      Cost   Revenue
# Day             1.000000 -0.007635     -0.014296       -0.002412   0.003133    0.003207  0.004623  0.003329  0.003853
# Year           -0.007635  1.000000      0.040994        0.123169  -0.217575   -0.213673 -0.181525 -0.215604 -0.208673
# Customer_Age   -0.014296  0.040994      1.000000        0.026887  -0.021374   -0.020262  0.004319 -0.016013 -0.009326
# Order_Quantity -0.002412  0.123169      0.026887        1.000000  -0.515835   -0.515925 -0.238863 -0.340382 -0.312895
# Unit_Cost       0.003133 -0.217575     -0.021374       -0.515835   1.000000    0.997894  0.741020  0.829869  0.817865
# Unit_Price      0.003207 -0.213673     -0.020262       -0.515925   0.997894    1.000000  0.749870  0.826301  0.818522
# Profit          0.004623 -0.181525      0.004319       -0.238863   0.741020    0.749870  1.000000  0.902233  0.956572
# Cost            0.003329 -0.215604     -0.016013       -0.340382   0.829869    0.826301  0.902233  1.000000  0.988758
# Revenue         0.003853 -0.208673     -0.009326       -0.312895   0.817865    0.818522  0.956572  0.988758  1.000000


# # --------------Start------------

# # Ploting the correlation matrix

# fig = plt.figure(figsize=(9,9))
# plt.matshow(corr, cmap='RdBu', fignum=fig.number)
# plt.xticks(range(len(corr.columns)), corr.columns, rotation=60)
# plt.yticks(range(len(corr.columns)), corr.columns)
# # plt.yticks(range(len(corr.columns)), corr.columns, rotation=90)

# plt.show()

# # --------------End--------------




# # # --------------Start------------

# # depicting specific pairs correlations

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(30, 14))
# # # Scatter plot to show there's no correlation between Customer_Age and Profit
# sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(15,6), ax=axes[0])

# # Scatter plot to show that there is some correlation between Revenue and Profit
# sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(15,6), ax=axes[1])
# plt.show()
# # # --------------End--------------





# # # --------------Start------------

# # lovely BOX Plots:

# # to show if there's correlation between Profit and any of the Age Groups.
# # it appears that there's no much correlation, apart to some outliers for (35-64) that may impact the initial assessment
# ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
# ax.set_ylabel('Profit')
# plt.show()

# # displaying multiple box plots in a nicely arranged matrix
# boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
# sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
# plt.show()

# # # --------------End--------------




# adding new column: 'Calculated_Cost' (equivalent to 'Cost')
sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']



# to evidence that 'Calculated_Cost' is equivalent to the existing 'Cost' column
(sales['Calculated_Cost'] != sales['Cost']).sum()  # summing up all the rows 'True' for deviation seek,  and we see that we have no deviations and the sum() is "0" -> Zero
# 0


## not interesting
# sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))
# plt.show()


sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
(sales['Calculated_Revenue'] != sales['Revenue']).sum() # again zero
# 0