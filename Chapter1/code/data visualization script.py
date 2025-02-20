##Data visualization
#creating a box plot that shows the effect of smoking history on the left ventricular fraction %
ax= sns.stripplot(data=newdf1, y='Left ventricular ejection fraction (%)', x='Group', hue='Smoking history', alpha=.5, jitter=.2, size=5, zorder=0, legend=True, dodge=True)
#creating a strip plot that shows the effect of smoking history in different drug groups on the left ventricular fraction %
sns.boxplot(data=newdf1, x='Group', y='Left ventricular ejection fraction (%)', fliersize=0, boxprops={'edgecolor':'black', 'facecolor':(1,1,1,0)}, zorder=5)
#setting the aesthetics of the plot
sns.despine()
sns.set_style('white')
sns.set_context('notebook')
ax.set(ylabel= 'Left ventricular ejection fraction %', xlabel='Smoking History')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#saving the plot
plt.savefig("/content/combineplot.pdf", bbox_inches= 'tight')

#Exploring the efficacy of sacubitril/valsartan and enalapril at 4 weeks and 8 weeks
#making new dataframes based on the columns of interest
columnsofinterest= ['Pre-treatment NT-proBNP (pg/mL)', 'Group']
Pretreateddf= newdf1[columnsofinterest]
Pretreateddf
columnsofinterest2=['Week 4 NT-proBNP (pg/mL)', 'Group']
week4df= newdf1[columnsofinterest2]
week4df
columnsofinterest3=['Week 8 NT-proBNP (pg/mL)', 'Group']
week8df= newdf1[columnsofinterest3]
week8df
#adding a timepoint column in each of the new dataframes
week4dfnew= week4df.copy()
week4dfnew['Timepoint']= 'week 4'
week4dfnew
week8dfnew= week8df.copy()
week8dfnew['Timepoint']= 'week 8'
week8dfnew
Pretreateddf1= Pretreateddf.copy()
Pretreateddf1['Timepoint']= 'Pre-treatment'
Pretreateddf1
#concatenating the three dataframes together
dataframemerged= pd.concat([Pretreateddf1, week4dfnew, week8dfnew], ignore_index=True)
dataframemerged
#Replacing all the NaN values with 0
dfReplaced=dataframemerged.fillna(0)
dfReplaced
#creating a new column for NT-proBNP concentration for all timepoints
dfReplaced['NT-proBNP concentration'] = dfReplaced['Pre-treatment NT-proBNP (pg/mL)'] + dfReplaced['Week 4 NT-proBNP (pg/mL)'] + dfReplaced['Week 8 NT-proBNP (pg/mL)']
dfReplaced
#using errorbar='sd' to replace the error message when ci='sd' was used for making a lineplot.
#This was because Seaborn has moved towards a more consistent interface with Matplotlib for error bar.
#This functionality has been standardized and integrated with Matplotlib's errorbar function.
sns.lineplot(data=dfReplaced, y='NT-proBNP concentration', x='Timepoint', errorbar='sd', err_style='bars', marker="o", hue='Group')
plt.savefig("/content/drugsefficacy4weeks8weeks.pdf", bbox_inches= 'tight')

#Explore the efficacy of sacubitril/valsartan and enalapril for a demographic
#converting categorical data into matrix data
#Collapsing duplicate entries by .groupby
newdf2= newdf1.copy()
# Only calculate the mean for numeric columns
dfGrouped=newdf2.groupby(['Week 8 NT-proBNP (pg/mL)', 'Group']).mean(numeric_only=True).reset_index()
#dfGrouped = dfGrouped.reset_index()
dfGrouped
#converting the categorical data frame into matrix data frame
#matrixDF = dfGrouped.pivot('Week 8 NT-proBNP (pg/mL)', 'Group', 'Age')
#matrixDF.head()
#converting the categorical data frame into matrix data frame
matrixDF = dfGrouped.pivot(index='Week 8 NT-proBNP (pg/mL)', columns='Group', values='Age')
matrixDF.head()
#Plotting the heatmap with age as one of the demographic factor
ax = sns.heatmap(data=matrixDF, cbar_kws={'label': 'Age'}, cmap='coolwarm')
ax.set(xlabel='Intervention Groups', ylabel='NT-proBNP concentration (pg/ml)')
plt.savefig("/content/heatmap.pdf", bbox_inches= 'tight')
