# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from matplotlib.pyplot import subplots
import pandas as pd
from ISLP import load_data

#
#
#
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
college = pd.read_csv('ISLP_data/College.csv')
college
#
#
#
#
#
#
#
#

college2 = pd.read_csv('ISLP_data/College.csv', index_col=0)
#college2

college3 = college.rename({'Unnamed: 0': 'college'},
  axis=1)
#college3

college3 = college3.set_index('college')
#college3
#
#
#
#
#
#
college = college3
college
#
#
#
#
#

college.describe()

#
#
#
#
#
#
#
#
#fig, ax = subplots(figsize=(8, 8))
pd.plotting.scatter_matrix(college[['Top10perc','Apps','Enroll']])
#plt.show()
#
#
#
#
#
#
#

#
#
#
#
#
#
college['Elite'] = pd.cut(college['Top10perc'],
  [0,0.5,1],
  labels=['No', 'Yes'])
#
#
#
#
#
#
#
#
college['Elite'].value_counts()
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#

#
#
#
#
#
#
#

Auto = pd.read_csv('ISLP_data/Auto.csv',
                    na_values=['?'])
Auto

#
#
#
#
#
#
#
#
Auto.info()
#
#
#
Auto['cylinders'] = Auto['cylinders'].astype('object') 
Auto['cylinders']
#
#
#
#
#
#
mpg_min = Auto['mpg'].min( )
mpg_max = Auto['mpg'].max( )

print('The min and max miles per gallon are', (mpg_min, mpg_max))
#
#
#
#
dsp_min = Auto['displacement'].min( )
dsp_max = Auto['displacement'].max( )

print('The min and max displacement are', (dsp_min, dsp_max))
#
#
#
#
hpwr_min = Auto['horsepower'].min( )
hpwr_max = Auto['horsepower'].max( )

print('The min and max horsepower are', (hpwr_min, hpwr_max))
#
#
#
wt_min = Auto['weight'].min( )
wt_max = Auto['weight'].max( )

print('The min and max weights are', (wt_min, wt_max))
#
#
#
acc_min = Auto['acceleration'].min( )
acc_max = Auto['acceleration'].max( )

print('The min and max accelerations are', (acc_min, acc_max))
#
#
#
#
#
#

mpg_mean = Auto['mpg'].mean( )
mpg_sd = Auto['mpg'].std( )

print('The mean and standard deviation of miles per gallon are', mpg_mean,'and', mpg_sd)
#
#
#
#
dsp_mean = Auto['displacement'].mean( )
dsp_sd = Auto['displacement'].std( )

print('The mean and standard deviation of weight are', dsp_mean,'and', dsp_sd)
#
#
#
#
hpwr_mean = Auto['horsepower'].mean( )
hpwr_sd = Auto['horsepower'].std( )

print('The mean and standard deviation of horsepower are', hpwr_mean,'and', hpwr_sd)
#
#
#
wt_mean = Auto['weight'].mean( )
wt_sd = Auto['weight'].std( )

print('The mean and standard deviation of weight are', wt_mean,'and', wt_sd)
#
#
#
acc_mean = Auto['acceleration'].mean( )
acc_sd = Auto['acceleration'].std( )

print('The mean and standard deviation of acceleration are', acc_mean,'and', acc_sd)
#
#
#
#
#
#
Auto_new = Auto.drop(Auto.index[10:85])
Auto_new
#
#
#
#
mpg_min = Auto_new['mpg'].min( )
mpg_max = Auto_new['mpg'].max( )

print('The min and max miles per gallon of the subsetted data are', (mpg_min, mpg_max))

mpg_mean = Auto_new['mpg'].mean( )
mpg_sd = Auto_new['mpg'].std( )

print('The mean and standard deviation of miles per gallon of the subsetted data are', mpg_mean,'and', mpg_sd)
#
#
#
#
dsp_min = Auto_new['displacement'].min( )
dsp_max = Auto_new['displacement'].max( )

print('The min and max displacement of the subsetted data are', (dsp_min, dsp_max))

dsp_mean = Auto_new['displacement'].mean( )
dsp_sd = Auto_new['displacement'].std( )

print('The mean and standard deviation of weight of the subsetted data are', dsp_mean,'and', dsp_sd)
#
#
#
#
hpwr_min = Auto['horsepower'].min( )
hpwr_max = Auto['horsepower'].max( )

print('The min and max horsepower of the subsetted data are', (hpwr_min, hpwr_max))

hpwr_mean = Auto['horsepower'].mean( )
hpwr_sd = Auto['horsepower'].std( )

print('The mean and standard deviation of horsepower of the subsetted data are', hpwr_mean,'and', hpwr_sd)
#
#
#
wt_min = Auto['weight'].min( )
wt_max = Auto['weight'].max( )

print('The min and max weights of the subsetted data are', (wt_min, wt_max))

wt_mean = Auto['weight'].mean( )
wt_sd = Auto['weight'].std( )

print('The mean and standard deviation of weight of the subsetted data are', wt_mean,'and', wt_sd)
#
#
#
acc_min = Auto['acceleration'].min( )
acc_max = Auto['acceleration'].max( )

print('The min and max accelerations of the subsetted data are', (acc_min, acc_max))

acc_mean = Auto['acceleration'].mean( )
acc_sd = Auto['acceleration'].std( )

print('The mean and standard deviation of acceleration of the subsetted data are', acc_mean,'and', acc_sd)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
Boston = load_data("Boston")
Boston
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
