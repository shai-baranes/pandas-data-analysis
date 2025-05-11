# TBD - put some plots into a repository folder!

# def header_creator(text):
#   print(f" {'#'*100}")    
#   print(" #", " "*96, "#")
#   print(" #", " "*int((95-len(text))/2), text, " "*int((94-len(text))/2), "#")
#   print(" #", " "*96, "#")
#   print("", "#"*100)

# ###     Example:
# header_creator("Data Cleaning:")


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re # ?? TBD

# pd.set_option('display.max_rows', None) #




 ####################################################################################################
 #                                                                                                  #
 #                                          sales_data.csv                                          #
 #                                                                                                  #
 ####################################################################################################

 

sales = pd.read_csv(r"./data/sales_data.csv")
# data = pd.read_csv("./data/sales_data.csv", usecols = ["final_price", "image_url", "url", "title", "categories"], chunksize = 10) # chunksize for preformance

print(sales.head())


sales.shape[0] # 113036 lines
# sales.shape --> (113036, 18)

sales.info()  # prefered over > sales.columns
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


# Slicing options using '.loc' / 'iloc' (equivalent options for the same below result)
sales.loc[1:5, 'Country': 'Order_Quantity'] # we can also have here a single column or a single row
sales.iloc[1:5, 7:13] # see that the column indices match the above info
#      Country             State Product_Category Sub_Category              Product  Order_Quantity
# 1     Canada  British Columbia      Accessories   Bike Racks  Hitch Rack - 4-Bike               8
# 2  Australia   New South Wales      Accessories   Bike Racks  Hitch Rack - 4-Bike              23
# 3  Australia   New South Wales      Accessories   Bike Racks  Hitch Rack - 4-Bike              20
# 4  Australia   New South Wales      Accessories   Bike Racks  Hitch Rack - 4-Bike               4
# 5  Australia   New South Wales      Accessories   Bike Racks  Hitch Rack - 4-Bike               5


sales.describe()
#                  Day           Year   Customer_Age  Order_Quantity      Unit_Cost     Unit_Price         Profit           Cost        Revenue
# count  113036.000000  113036.000000  113036.000000   113036.000000  113036.000000  113036.000000  113036.000000  113036.000000  113036.000000
# mean       15.665753    2014.401739      35.919212       11.901660     267.296366     452.938427     285.051665     469.318695     754.370360
# std         8.781567       1.272510      11.021936        9.561857     549.835483     922.071219     453.887443     884.866118    1309.094674
# min         1.000000    2011.000000      17.000000        1.000000       1.000000       2.000000     -30.000000       1.000000       2.000000
# 25%         8.000000    2013.000000      28.000000        2.000000       2.000000       5.000000      29.000000      28.000000      63.000000
# 50%        16.000000    2014.000000      35.000000       10.000000       9.000000      24.000000     101.000000     108.000000     223.000000
# 75%        23.000000    2016.000000      43.000000       20.000000      42.000000      70.000000     358.000000     432.000000     800.000000
# max        31.000000    2016.000000      87.000000       32.000000    2171.000000    3578.000000   15096.000000   42978.000000   58074.000000


sales['Unit_Cost'].describe()  # more focused
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

# ## Now adding vertical lines for both 'mean' (red) & 'median' (green)
# mean_val = sales['Unit_Cost'].mean()
# median_val = sales['Unit_Cost'].median()

# fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 6), sharex=True)

# # Boxplot
# sales['Unit_Cost'].plot(kind='box', vert=False, ax=axes[0])
# axes[0].axvline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
# axes[0].axvline(median_val, color='green', linestyle='-', linewidth=2, label='Median')
# axes[0].legend(loc='upper right')

# # Density plot
# sales['Unit_Cost'].plot(kind='density', ax=axes[1])
# axes[1].axvline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
# axes[1].axvline(median_val, color='green', linestyle='-', linewidth=2, label='Median')
# axes[1].legend(loc='upper right')

# xmin = -200  # start at 0 or the actual min, whichever is smaller
# xmax = sales['Unit_Cost'].max() * 1.05   # a little padding on the right

# axes[0].set_xlim(xmin, xmax)
# axes[1].set_xlim(xmin, xmax)

# # eventually also changing the y-axis from 'Density' into 'Number of Sales' and the x-axis from 'tbd' into 'dollars'
# # sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2]).set_ylabel('Number of Sales')
# # note that 'ax' can also be any other variable name
# ax = sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2], bins=100)
# # ax = sales['Unit_Cost'].plot(kind = 'hist', ax=axes[2]) # 10 bin by default
# ax.set_ylabel('Number of Sales')
# ax.set_xlabel('dollars')


# plt.tight_layout()
# plt.show()

# # ----------------End---------------

sales['Age_Group'].info
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


sales['Age_Group'].value_counts()
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




sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
(sales['Calculated_Revenue'] != sales['Revenue']).sum() # again zero
# 0

# can also prove it by:
(sales['Calculated_Revenue'] != sales['Cost'] + sales['Profit']).sum()


# we can easily increasing the prices
sales['Unit_Cost'] *= 1.03


# equivalent queries:
sales[sales['State'] == 'Kentucky']
sales.loc[sales['State'] == 'Kentucky']


# mean revenue of the Adults (35-64) sales group
sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean() # numpy float value
sales[sales['Age_Group'] == 'Adults (35-64)'][['Revenue']].mean() # pandas class (Series) w/ a single value
# 762.828765


# how many records belong to Age Group Youth (<25) or Adults (35-64)?

sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]
sales[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]
# 73652

sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean().round(2) # and also rounding to 2 decimal points
sales[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States')][['Revenue']].mean()
# 726.73

# before revenue increase:
sales.loc[sales['Country'] == 'France', 'Revenue'].head() # first ('a')value in loc[a,b] is the row index (as we grouped here into rows)
# 50     787
# 51     787
# 52    2957
# 53    2851
# 60     626


sales.loc[sales['Country'] == 'France', 'Revenue'] *= 1.1 # in-place change! increasing the revenue only for 'France' sales

# after revenue increase
sales.loc[sales['Country'] == 'France', 'Revenue'].head() #to demonstrate the change (revenue increase)
# 50     865.7
# 51     865.7
# 52    3252.7
# 53    3136.1
# 60     688.6


# non-equivalent and wrong:
sales[sales['Country'] == 'France'][['Revenue']].Revenue *= 1.1 # wrong! - we cannot update the DF in-place fashion


sales.info()
#  #   Column            Non-Null Count   Dtype
# ---  ------            --------------   -----
# 0   Date                113036 non-null  object
# 1   Day                 113036 non-null  int64
# 2   Month               113036 non-null  object
# 3   Year                113036 non-null  int64
# 3   Customer_Age        113036 non-null  int64
# 4   Age_Group           113036 non-null  object
# 5   Customer_Gender     113036 non-null  object
# 6   Country             113036 non-null  object
# 7   State               113036 non-null  object
# 8   Product_Category    113036 non-null  object
# 9   Sub_Category        113036 non-null  object
# 10  Product             113036 non-null  object
# 11  Order_Quantity      113036 non-null  int64
# 12  Unit_Cost           113036 non-null  float64
# 13  Unit_Price          113036 non-null  int64
# 14  Profit              113036 non-null  int64
# 15  Cost                113036 non-null  int64
# 16  Revenue             113036 non-null  float64
# 17  Calculated_Cost     113036 non-null  int64
# 18  Calculated_Revenue  113036 non-null  int64


sales.drop(columns='Year', inplace = True)
# sales.drop(columns=['Day', 'Month', 'Year'], inplace = True) # can also get a list of columns
sales.info()
# Data columns (total 18 columns):
#  #   Column            Non-Null Count   Dtype
# ---  ------            --------------   -----
#  0   Date              113036 non-null  object
#  1   Day               113036 non-null  int64
#  2   Month             113036 non-null  object
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


sales.drop([0, 1, 2, 3, 4], inplace = True) # can also drop rows by indices or numbered if not indexed uniquely




 ####################################################################################################
 #                                                                                                  #
 #                                           G7_States.csv                                          #
 #                                                                                                  #
 ####################################################################################################






df = pd.read_csv(r"./data/G7_States.csv", index_col=0) # the left most column becomes the index for our df

#                 Population  GDP  Surface  HDI Continent
# Canada                  38  625     4563    2   America
# France                  67  749      632    3    Europe
# Germany                 83  294      633    4    Europe
# Italy                   59   37      192    2    Europe
# Japan                   97   56      765    4      Asia
# United Kingdom          67   26      292    3    Europe
# United States          318   25       17    6   America

crisis = pd.Series([-20, -1], index=['GDP', 'HDI'])

df[['GDP', 'HDI']] += crisis  # df is now updated for the indexed columns

#                 Population  GDP  Surface  HDI Continent
# Canada                  38  605     4563    1   America
# France                  67  729      632    2    Europe
# Germany                 83  274      633    3    Europe
# Italy                   59   17      192    1    Europe
# Japan                   97   36      765    3      Asia
# United Kingdom          67    6      292    2    Europe
# United States          318    5       17    5   America


langs = pd.Series(['French', 'German', 'Italian'],
            index = ['France', 'Germany', 'Italy'],
            name = 'Language', # this line is not mandatory!
)

df['Language'] = langs # adding a column

print(df)
#                 Population  GDP  Surface  HDI Continent Language
# Canada                  38  605     4563    1   America      NaN
# France                  67  729      632    2    Europe   French
# Germany                 83  274      633    3    Europe   German
# Italy                   59   17      192    1    Europe  Italian
# Japan                   97   36      765    3      Asia      NaN
# United Kingdom          67    6      292    2    Europe      NaN
# United States          318    5       17    5   America      NaN


df.loc['Japan', 'Language'] = 'Japanese'

#                 Population  GDP  Surface  HDI Continent  Language
# Canada                  38  605     4563    1   America       NaN
# France                  67  729      632    2    Europe    French
# Germany                 83  274      633    3    Europe    German
# Italy                   59   17      192    1    Europe   Italian
# Japan                   97   36      765    3      Asia  Japanese
# United Kingdom          67    6      292    2    Europe       NaN
# United States          318    5       17    5   America       NaN


df.rename(columns={'HDI': 'Human Dev Index', 'APC': 'Anual Popcorn Consumption'}, # we change only the applicable fields ('APC' & 'Argentina' not exist)
            index= {'United States': 'USA', 'United Kingdom': 'UK', 'Argentina': 'AR'},
          inplace= True)

#          Population  GDP  Surface  Human Dev Index Continent  Language
# Canada           38  605     4563                1   America       NaN
# France           67  729      632                2    Europe    French
# Germany          83  274      633                3    Europe    German
# Italy            59   17      192                1    Europe   Italian
# Japan            97   36      765                3      Asia  Japanese
# UK               67    6      292                2    Europe       NaN
# USA             318    5       17                5   America       NaN

df.rename(index=str.upper, inplace=True) # upper on all index
df.rename(index=lambda x: x.lower(), inplace=True) # lower on all index


# adding values

# df = df._append(pd.Series({'Population': 3, 'GDP': 5}, name='China')) # appending a row by Series
# koko = pd.DataFrame({'Population': 3, 'GDP': 5}, index=['China']) # appending a row by DataFrame
koko = pd.DataFrame({'Population': [3, 7], 'GDP': [5, 9]}, index=['China', 'Romania']) # appending a row by DataFrame (can leverage it for multiple rows)
df = df._append(koko) # there's no in-place option

#          Population  GDP  Surface  Human Dev Index Continent  Language
# canada           38  605   4563.0              1.0   America       NaN
# france           67  729    632.0              2.0    Europe    French
# germany          83  274    633.0              3.0    Europe    German
# italy            59   17    192.0              1.0    Europe   Italian
# japan            97   36    765.0              3.0      Asia  Japanese
# uk               67    6    292.0              2.0    Europe       NaN
# usa             318    5     17.0              5.0   America       NaN
# China             3    5      NaN              NaN       NaN       NaN
# Romania           7    9      NaN              NaN       NaN       NaN


df.reset_index(inplace=True)
#      index  Population  GDP  Surface  Human Dev Index Continent  Language
# 0   canada          38  605   4563.0              1.0   America       NaN
# 1   france          67  729    632.0              2.0    Europe    French
# 2  germany          83  274    633.0              3.0    Europe    German
# 3    italy          59   17    192.0              1.0    Europe   Italian
# 4    japan          97   36    765.0              3.0      Asia  Japanese
# 5       uk          67    6    292.0              2.0    Europe       NaN
# 6      usa         318    5     17.0              5.0   America       NaN
# 7    China           3    5      NaN              NaN       NaN       NaN
# 8  Romania           7    9      NaN              NaN       NaN       NaN

df.set_index('index', inplace=True) # back to normal

# extracting specific cell based on another cell value - as if was unique/index/key (equivalents)
float(df[df['GDP'] == 729].Surface.iloc[0]) # without the [0] we get Series type, and after the [0] we get 'numpy.float' type (the first value of a single value)
float(df.loc[df['GDP'] == 729].Surface.iloc[0]) # without the [0] we get Series type, and after the [0] we get 'numpy.float' type (the first value of a single value)
# 632.0



# Equivalent ways to extract the Surface value of germany
df.loc['germany', 'Surface'] # location by row, column
df[df.index == 'germany'][['Surface']].iloc[0].iloc[0] # the tedious way (multiple piping for the isolated value)
# 633.0



# adding a column(by broadcasting operation) :
df['GDP Per Capita'] = df['GDP'] / df['Population']

#          Population  GDP  Surface  Human Dev Index Continent  Language  GDP Per Capita
# index
# canada           38  605   4563.0              1.0   America       NaN       15.921053
# france           67  729    632.0              2.0    Europe    French       10.880597
# germany          83  274    633.0              3.0    Europe    German        3.301205
# italy            59   17    192.0              1.0    Europe   Italian        0.288136
# japan            97   36    765.0              3.0      Asia  Japanese        0.371134
# uk               67    6    292.0              2.0    Europe       NaN        0.089552
# usa             318    5     17.0              5.0   America       NaN        0.015723
# China             3    5      NaN              NaN       NaN       NaN        1.666667
# Romania           7    9      NaN              NaN       NaN       NaN        1.285714




 ####################################################################################################
 #                                                                                                  #
 #                                       btc-market-price.csv                                       #
 #                                                                                                  #
 ####################################################################################################



df = pd.read_csv(r"./data/btc-market-price.csv", names=["Timestamp", "Price"]) # + adding column names to data with no names (alternative to the following 2 lines)
# df = pd.read_csv(r"./data/btc-market-price.csv", header = None) # to ignore the first row as header, since it's a regular data (these 2 grayed-out lines live together)
# df.columns = ["Timestamp", "Price"]  # adding the columns' names after retrieving the data without the columns


# note that we could spared more actions by adding prior arguments to the read_csv command:
df_2 = pd.read_csv(r"./data/btc-market-price.csv", names=["Timestamp", "Price"], index_col=0, parse_dates=True) # adding the first column (TS) to be the index column!
# # replacing both:
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# df.set_index('Timestamp', inplace=True)

df.head() # or df.tail()

#              Timestamp        Price                                                                                                                                                                                                
# 0  2017-04-02 00:00:00  1099.169125                                                                                                                                                                                                
# 1  2017-04-03 00:00:00  1141.813000                                                                                                                                                                                                
# 2  2017-04-04 00:00:00  1141.600363                                                                                                                                                                                                
# 3  2017-04-05 00:00:00  1133.079314                                                                                                                                                                                                
# 4  2017-04-06 00:00:00  1196.307937



df.shape
# (365, 2)


df.info()
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Timestamp  365 non-null    object
#  1   Price      365 non-null    float64


df.dtypes
# Timestamp     object
# Price        float64


pd.to_datetime(df['Timestamp']).head() # convert data into actual dates
# 0   2017-04-02
# 1   2017-04-03
# 2   2017-04-04
# 3   2017-04-05
# 4   2017-04-06


df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df.set_index('Timestamp', inplace=True)

df.head()
#                   Price
# Timestamp
# 2017-04-02  1099.169125
# 2017-04-03  1141.813000
# 2017-04-04  1141.600363
# 2017-04-05  1133.079314
# 2017-04-06  1196.307937


df.loc['2017-09-29'].iloc[0] # extracting value from index
# 4193.574667


# ----------------------------------Plot Begin

# df.plot() # pandas quick integration w/ Mathplotlib
# plt.show() # btc-market-price_Figure_1.png
# ----------------------------------Plot End

eth = pd.read_csv(r'./data/eth-price.csv', parse_dates=True, index_col=0)
eth.info()
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   UnixTimeStamp  362 non-null    int64
#  1   Value          362 non-null    float64


# creating a new DataFrame with the index from the Bitcoin DF (btc-market-price.csv)
prices = pd.DataFrame(index=df.index)
prices.head()
# Columns: []
# Index: [2017-04-02 00:00:00, 2017-04-03 00:00:00, 2017-04-04 00:00:00, 2017-04-05 00:00:00, 2017-04-06 00:00:00]


prices['Bitcoin'] = df['Price'] # importing the Bitcoin prices
# prices.plot() # the familiar plot from above
# plt.show()

prices['Eth'] = eth['Value'] # importing the Eth prices


prices.info() # you can see the gap/hole below (362 vs. 365 values)
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Bitcoin  365 non-null    float64
#  1   Eth      362 non-null    float64

# ----------------------------------Plot Begin
# prices.plot(figsize=(12,6))
# plt.show() # Bitcoin_Eth_combined_Figure_2.png 
# ----------------------------------Plot End



 ####################################################################################################
 #                                                                                                  #
 #                                          Data Cleaning:                                          #
 #                                                                                                  #
 ####################################################################################################


prices.loc['2017-12-01':'2018-01-01'] # range taken from the plot w/ hole. from below we find that there are missing Eth values for 3 days (2017-12-08, 2017-12-09, 2017-12-10)
#                  Bitcoin     Eth
# Timestamp
# 2017-12-01  10883.912000  461.58
# 2017-12-02  11071.368333  457.96
# 2017-12-03  11332.622000  462.81
# 2017-12-04  11584.830000  466.93
# 2017-12-05  11878.433333  453.96
# 2017-12-06  13540.980000  422.48
# 2017-12-07  16501.971667  421.15
# 2017-12-08  16007.436667     NaN
# 2017-12-09  15142.834152     NaN
# 2017-12-10  14869.805000     NaN
# 2017-12-11  16762.116667  513.29
# 2017-12-12  17276.393333  656.52
# 2017-12-13  16808.366667  699.09
# ...
# 2017-12-31  14165.575000  741.13
# 2018-01-01  13812.186667  756.20


pd.isnull(prices).loc['2017-12-07':'2017-12-11']
pd.isna(prices).loc['2017-12-07':'2017-12-11'] # equivalents (TBD how to we utilize that?)
#             Bitcoin    Eth
# Timestamp
# 2017-12-07    False  False
# 2017-12-08    False   True
# 2017-12-09    False   True
# 2017-12-10    False   True
# 2017-12-11    False  False


# now knowing that the null are for the Eth., we can run this: (filtering only the null for the entire DF - where we have 'True')
prices[pd.isna(prices)['Eth']]
prices[prices.isna()['Eth']]
#                  Bitcoin  Eth
# Timestamp
# 2017-12-08  16007.436667  NaN
# 2017-12-09  15142.834152  NaN
# 2017-12-10  14869.805000  NaN


# ----------------------------------Plot Begin
# prices.loc['2017-12-01':'2018-01-01'].plot() # to zoom in on the hole
# plt.show() # 'eth_hole_Figure_3.png'
# ----------------------------------Plot End



# Equivalents (counting the rows with nulls)
pd.isnull(prices).sum()  # count how many missing values are there in prices DF (sums up the bool vals is equivalent to count)
prices.isnull().sum() # it is also a class method, so we can simplify the call
pd.isna(prices).sum()  # equivalent to above
prices.isna().sum() # equivalent to above
# Bitcoin    0
# Eth        3


prices.dropna(axis=1) # losing any column that has a null value

# and we can drop rows (instead) where we have some nulls (no more hols - dangerous cmd)
prices.dropna() # thus losing also the equivalent BTC prices 
# prices.dropna(inplace=True) # if we want a permanent change on 'prices'

# ----------------------------------Plot Begin
# prices.plot(figsize=(12,6))
# plt.show() # 'Bitcoin_Eth_combined_Figure_2.png'
# ----------------------------------Plot End


# optional dropna usage:
df.dropna(how='all') # only if all values in the relevant axis have Nulls
df.dropna(how='any') # default
df.dropna(thresh=3) # minimum 3 valid values to keep the row/column without dropping it (again it is axis dependent)



temp_prices = prices.fillna(0)
temp_prices.loc['2017-12-07':'2017-12-11']         
#                  Bitcoin     Eth
# Timestamp
# 2017-12-07  16501.971667  421.15
# 2017-12-08  16007.436667    0.00
# 2017-12-09  15142.834152    0.00
# 2017-12-10  14869.805000    0.00
# 2017-12-11  16762.116667  513.29


temp_prices = prices.fillna(prices.mean())
temp_prices.loc['2017-12-07':'2017-12-11'] 
#                  Bitcoin         Eth
# Timestamp
# 2017-12-07  16501.971667   421.150000
# 2017-12-08  16007.436667  [429.927514]
# 2017-12-09  15142.834152  [429.927514]
# 2017-12-10  14869.805000  [429.927514]
# 2017-12-11  16762.116667   513.290000

# ----------------------------------Plot Begin
## now we see that we filled the gaps with the '429.93' mean value
# prices.plot(figsize=(12,6)) # before filling the holes
# temp_prices.plot(figsize=(12,6)) # after filling the holes: 'dropping_hole_Figure_4.png'
# plt.show()
# ----------------------------------Plot End





temp_prices = prices.fillna(prices.ffill()) # forward fill (as if it moves forward and keeping the previous values as it goes)
# temp_prices = prices.fillna(method='ffill') # deprecated
temp_prices.loc['2017-12-07':'2017-12-11'] 
#                  Bitcoin     Eth
# Timestamp
# 2017-12-07  16501.971667   421.15
# 2017-12-08  16007.436667  [421.15]
# 2017-12-09  15142.834152  [421.15]
# 2017-12-10  14869.805000  [421.15]
# 2017-12-11  16762.116667   513.29



temp_prices = prices.fillna(prices.bfill()) # backward fill (as if it moves forward and keeping the previous values as it goes)
temp_prices.loc['2017-12-07':'2017-12-11'] 
#                  Bitcoin     Eth
# Timestamp
# 2017-12-07  16501.971667   421.15
# 2017-12-08  16007.436667  [513.29]
# 2017-12-09  15142.834152  [513.29]
# 2017-12-10  14869.805000  [513.29]
# 2017-12-11  16762.116667   513.29




# -------------------------------
# TBD  TBD  TBD  TBD  TBD  TBD  TBD  
# -------------------------------

# continue from here:
# BLUhttps://www.youtube.com/watch?v=r-uOLxNrNk8&t=11070s

df = pd.DataFrame({
                    'Sex': ['N', 'F', 'F', 'D', '?'],  # '?' as outlier or the exception here
                    'Age': [29, 30, 24, 290, 25],      # '290' as outlier or the exception here

})


#   Sex  Age
# 0   N   29
# 1   F   30
# 2   F   24
# 3   D  290
# 4   ?   25


df['Sex'].unique()
# array(['N', 'F', 'D', '?'], dtype=object)


df['Sex'].value_counts()
# Sex
# F    2
# N    1
# D    1
# ?    1

df['Sex'].replace('D', 'F') # without inplace (immutable cmd)
# 0    N
# 1    F
# 2    F
# 3    F
# 4    ?


df['Sex'].replace({'D': 'F', 'N': 'M'}) # multiple replace using dict - without inplace (immutable cmd)
# 0    M
# 1    F
# 2    F
# 3    F
# 4    ?


# pinpoint replace, per column
df.replace({ 
            'Sex': {'D': 'F', 'N': 'M'},
            'Age': {290: 29},
})
# 0   M   29
# 1   F   30
# 2   F   24
# 3   F   29
# 4   ?   25


df[df['Age'] > 100]
#   Sex  Age
# 3   D  290  # say we want to divide all such errors by 10



df2=df.copy() # to avoid having a pointer instead of independent DF


df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
# equivalent to this:
df2['Age'] = df2['Age'].apply(lambda x: x if x<=25 else x/10)






ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gerard Araud',
    'Kim Darrorch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Petter Witting',
    'Peter Ammon',
    'Klaus Scharioth',
])

# Gerard Araud                  France
# Kim Darrorch          United Kingdom
# Peter Westmacott      United Kingdom
# Armando Varricchio             Italy
# Petter Witting               Germany
# Peter Ammon                  Germany
# Klaus Scharioth              Germany


ambassadors.duplicated() # first instance is considered as valid
# Gerard Araud          False
# Kim Darrorch          False
# Peter Westmacott       [True]
# Armando Varricchio    False
# Petter Witting        False
# Peter Ammon            [True]
# Klaus Scharioth        [True]




ambassadors.duplicated(keep='last') # last instance is considered as valid (as if the last update is the correct one)
# Gerard Araud          False
# Kim Darrorch           [True]
# Peter Westmacott      False
# Armando Varricchio    False
# Petter Witting         [True]
# Peter Ammon            [True]
# Klaus Scharioth       False



ambassadors.duplicated(keep=False) # not keeping any of the duplicates (only 2 rows are valid now)
# Gerard Araud          False
# Kim Darrorch           [True]
# Peter Westmacott       [True]
# Armando Varricchio    False
# Petter Witting         [True]
# Peter Ammon            [True]
# Klaus Scharioth        [True]


ambassadors.drop_duplicates(keep='last') # non-mutable cmd (no 'inplace') - all keep rules apply here!
# Gerard Araud                  France
# Peter Westmacott      United Kingdom
# Armando Varricchio             Italy
# Klaus Scharioth              Germany




players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})


#               Name Pos
# 0      Kobe Bryant  SG
# 1     LeBron James  SF
# 2      Kobe Bryant  SG
# 3  Carmelo Anthony  SF
# 4      Kobe Bryant  SF


players.duplicated() # here also you can decide on the 'keep' and drop as needed...

# 0     False
# 1     False
# 2     [True]
# 3     False
# 4     False

players.duplicated(subset=['Name'])
# 0     False
# 1     False
# 2     [True]
# 3     False
# 4     [True]


players.duplicated(subset=['Pos'])
# 0     False
# 1     False
# 2     [True]
# 3     [True]
# 4     [True]


df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

#               Data
# 0     1987_M_US _1
# 1     1990?_M_UK_1
# 2      1992_F_US_2
# 3  1970?_M_   IT_1
# 4    1985_F_I  T_2


df['Data'].str.split('_')
# 0       [1987, M, US , 1]
# 1       [1990?, M, UK, 1]
# 2        [1992, F, US, 2]
# 3    [1970?, M,    IT, 1]
# 4      [1985, F, I  T, 2]


df['Data'].str.split('_', expand = True)
#        0  1      2  3
# 0   1987  M    US   1
# 1  1990?  M     UK  1
# 2   1992  F     US  2
# 3  1970?  M     IT  1
# 4   1985  F   I  T  2


df = df['Data'].str.split('_', expand = True)
df.columns = ['Year', 'Sex', 'Country', 'No Children']

#     Year Sex Country No Children
# 0   1987   M     US            1
# 1  1990?   M      UK           1
# 2   1992   F      US           2
# 3  1970?   M      IT           1
# 4   1985   F    I  T           2

df['Year'].str.contains(r'\?') # we get a Series of True & False accordingly - supports regex patterns
df['Country'].str.contains(r'U') # we get a Series of True & False accordingly

df['Country'].str.strip() # removing blank spaces - before and after the text (immutable method)

df['Country'].str.replace(' ', '') # removing blank spaces (immutable method) - supports regex patterns
# 0    US
# 1    UK
# 2    US
# 3    IT
# 4    IT


# df['Year'].str.replace(r'(\d{4})?', lambda m: m.group(1), regex=True)



# using regex to ditch the '?' suffix from the 'Year' column
df['Year'].str.replace(r'(\d{4})\?', lambda m: m.group(1), regex=True)

# same as above, only now we name the group: 'year' using the param prefix: ?P<year>
df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'), regex=True)

# 0    1987
# 1    1990
# 2    1992
# 3    1970
# 4    1985


