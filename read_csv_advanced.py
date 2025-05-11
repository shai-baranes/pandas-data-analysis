# lecture URL: https://github.com/rmotr-curriculum/RDP-Reading-Data-with-Python-and-Pandas/blob/master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/Lecture.ipynb
# YT: https://www.youtube.com/watch?v=r-uOLxNrNk8&t=11070s


import pandas as pd



filepath = r'data/btc-market-price_broken.csv'

with open(filepath, 'r') as reader:
    for index, line in enumerate(reader.readlines()):
    # read just the first 10 lines
        if (index < 10):
            print(index, line, end="")

# 0 2/4/17 0:00,1099.169125
# 1 3/4/17 0:00,1141.813
# 2 4/4/17 0:00,?
# 3 5/4/17 0:00,1133.079314
# 4 6/4/17 0:00,-
# 5 7/4/17 0:00,-
# 6 8/4/17 0:00,1181.149838
# 7 9/4/17 0:00,1208.8005
# 8 10/4/17 0:00,1207.744875
# 9 11/4/17 0:00,1226.617038



csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv" # can read either locally or remote csv file
pd.read_csv(csv_url).head()
#   Country Name Country Code  Year         Value
# 0  Afghanistan          AFG  2000  3.521418e+09
# 1  Afghanistan          AFG  2001  2.813572e+09
# 2  Afghanistan          AFG  2002  3.825701e+09
# 3  Afghanistan          AFG  2003  4.520947e+09
# 4  Afghanistan          AFG  2004  5.224897e+09



# NA values definition:
# (We can define a na_values parameter with the values we want to be recognized as NA/NaN. In this case empty strings '', ? and - will be recognized as null values.)

df = pd.read_csv(filepath, header=None, na_values=['', '?', '-'], names=['Timestamp', 'Price'])

df.head()
     # Timestamp        Price
# 0  2/4/17 0:00  1099.169125
# 1  3/4/17 0:00  1141.813000
# 2  4/4/17 0:00          NaN
# 3  5/4/17 0:00  1133.079314
# 4  6/4/17 0:00          NaN


# We can use dtype parameter to force pandas to use certain dtype.
# In this case we'll force the Price column to be float:

df = pd.read_csv(filepath,
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'})


pd.to_datetime(df['Timestamp']).head() # immutable action
# 0   2017-02-04
# 1   2017-03-04
# 2   2017-04-04
# 3   2017-05-04
# 4   2017-06-04


# a better way to deal with the dates format is to parse upon retrieval:
# I'm also adding the first date column to be the index here
df = pd.read_csv(filepath,
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'},
                 parse_dates=[0],
                 index_col=[0])

df.head()
#                   Price
# Timestamp
# 2017-02-04  1099.169125
# 2017-03-04  1141.813000
# 2017-04-04          NaN
# 2017-05-04  1133.079314
# 2017-06-04          NaN




 ####################################################################################################
 #                                                                                                  #
 #                                       Challenging Parsing:                                       #
 #                                                                                                  #
 ####################################################################################################

exam_file = r'data/exam_review.csv'

exam_df = pd.read_csv(exam_file, sep='>')

exam_df.head()
#   first_name last_name  age math_score french_score
# 0        Ray    Morley   18     68,000       75,000
# 1     Melvin     Scott   24         77           83
# 2     Amirah     Haley   22         92           67
# 3     Gerard     Mills   19     78,000           72
# 4        Amy    Grimes   23         91           81


# -----------------------------
# files are stored using different "encodings". You've probably heard about ASCII, UTF-8, latin1, etc.

# While reading data custom encoding can be defined with the encoding parameter.

# encoding='UTF-8': will be used if data is UTF-8 encoded.
# encoding='iso-8859-1': will be used if data is ISO/IEC 8859-1 ("extended ASCII") encoded.
# In our case we don't need a custom enconding as data is properly loaded.
# -----------------------------

exam_df = pd.read_csv(exam_file,
                      sep='>',
                      decimal=',') # in europ, the comma is the decimal place

exam_df.head()
#   first_name last_name  age  math_score  french_score
# 0        Ray    Morley   18        68.0          75.0
# 1     Melvin     Scott   24        77.0          83.0
# 2     Amirah     Haley   22        92.0          67.0
# 3     Gerard     Mills   19        78.0          72.0
# 4        Amy    Grimes   23        91.0          81.0


exam_df = pd.read_csv(exam_file,
            sep='>',
            thousands=',') # alternatively we can consider the , to be for thousands

exam_df.head()
#   first_name last_name  age  math_score  french_score
# 0        Ray    Morley   18       68000         75000
# 1     Melvin     Scott   24          77            83
# 2     Amirah     Haley   22          92            67
# 3     Gerard     Mills   19       78000            72
# 4        Amy    Grimes   23          91            81



# we can also skip rows and start from the 3rd row in following example.
# note that twe also loose our headers!


exam_df = pd.read_csv(exam_file,
            sep='>',
            skiprows=2, # skipping the first 2 rows
            names = ['first_name', 'last_name', 'age', 'math_score', 'french_score'],
            )


exam_df.head()
#   first_name last_name  age math_score  french_score
# 0     Melvin     Scott   24         77            83
# 1     Amirah     Haley   22         92            67
# 2     Gerard     Mills   19     78,000            72
# 3        Amy    Grimes   23         91            81



# to avoid losing the header, we can define the skip slot/slice:

exam_df = pd.read_csv(exam_file,
                      sep='>',
                      decimal=',',
                      skiprows=[1,3]) # skipping explicitly defined rows 


exam_df.head()
#   first_name last_name  age  math_score  french_score
# 0     Melvin     Scott   24        77.0            83
# 1     Gerard     Mills   19        78.0            72
# 2        Amy    Grimes   23        91.0            81






# we can also see the get the blank lines from the csv file if desired,
# and loading only specific columns:

exam_df = pd.read_csv(exam_file,
            sep='>',
            usecols=['first_name', 'last_name', 'age'],
            # usecols=[0, 1, 2], # equivalent to above
            skip_blank_lines=False)

exam_df.head()
#   first_name last_name   age
# 0        Ray    Morley  18.0
# 1     Melvin     Scott  24.0
# 2     Amirah     Haley  22.0
# 3        NaN       NaN   NaN
# 4     Gerard     Mills  19.0


# saving to csv file
exam_df.to_csv('out.csv')

exam_df.to_csv('out.csv', index=None) # in case we don't want the enumerate index at the left