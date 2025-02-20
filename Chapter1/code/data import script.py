##Data import
#importing the python libraries to be used in the sheet
import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
#loading the csv file from the github repository by copying a raw csv link
df= pd.read_csv('https://raw.githubusercontent.com/Mangul-Lab-USC/CXPT-501-Fall_23/main/Palak_Agarwal.csv')
#display the dataset
df

##Data cleaning
#examining the NaN values present in each column
df.isnull().sum()
#display of the datatypes present in the dataframe
df.dtypes
#dropping all the rows containing NaN values from the dataframe
df_clean= df.dropna(how='any')
df_clean.isnull().sum()
#making a new dataframe based on the study's inclusion criteria
newdf= df_clean.loc[(df_clean['Pre-treatment NT-proBNP (pg/mL)'] >= 1600) & (df_clean['Age'] >= 18) & (df_clean['Pre-treatment BNP (pg/mL)'] >= 400) & (df_clean['Left ventricular ejection fraction (%)'] <= 40) ]
newdf
#number of filtered patients in the new dataframe
len(newdf)
#making a copy of the previous dataframe to skip the referencial copying error message
newdf1=newdf.copy()
newdf1
#Creating a new column of BMI (kg/m^2) based on the formula as the condition
newdf1['BMI (kg/m^2)'] = newdf1['Weight (kg)'] / (newdf1['Height (cm)']/100 ** 2)
newdf1
