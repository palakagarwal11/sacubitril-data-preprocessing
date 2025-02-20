For the CXPT501 final project, I explored a large dataset that was simulated and modified based on a clinical trial (PIONEER-HF, ClinicalTrials.gov Identifier: NCT02554890).
In this study, researchers compared the effects of sacubitril/valsartan versus enalapril in stabilized acute heart failure patients with reduced ejection fraction.
Information included in the dataset:
Demographics:
Age;
Sex;
Race;
Ethnicity.
Baseline characteristics:
Height (cm);
Weight (kg);
Smoking history;
Pre-treatment NT-proBNP (pg/mL);
Pre-treatment BNP (pg/mL).
Disease characteristics:
Prior use of ACEi/ARB;
Left ventricular ejection fraction (%);
Chronic renal insufficiency.
Intervention:
Sacubitril/valsartan;
Enalapril.
Efficacy outcome:
Week 4 NT-proBNP (pg/mL);
Week 8 NT-proBNP (pg/mL).
Safety outcome:
Symptomatic hypotension;
Hyperkalemia;
Angioedema;
Death.

The dataset has data for 1 million patients, 1 per row.

For data cleaning,
Based on the study's inclusion criteria, I filter out patients who don't meet the following criteria and store the remaining patient data in a new DataFrame.
Inclusion criteria
age >= 18
pre-treatment NT-proBNP >= 1600 pg/mL
pre-treatment BNP >= 400 pg/mL
left ventricular ejection fraction <= 40%

For data visualisation,
Categorical Data
I use one or more of the most appropriate plot types to visualize some aspect of the categorical data. Intervention type must be distinguished by hue by
・Using one of Seaborn's Plot-Styles
・Using one of Seaborn's Plot-Contexts
・Despine my plot
I save the plot in a vector form (.pdf).
I follow the steps below to visualize NT-proBNP concentrations over time with a relational-type plot. The plot is then saved in a vector form (.pdf).
I subset the cleaned and filtered DataFrame into three smaller DataFrames containing the following columns:
Pre-treatment NT-proBNP & Intervention Group
Week 4 NT-proBNP & Intervention Group
Week 8 NT-proBNP & Intervention Group
These smaller dataframes are then merged.
The same steps are followed for exploring the efficacy of the drugs against a demographic.

For statistical analysis,
I explore the safety of sacubitril/valsartan and enalapril in this stabilized acute heart failure patient population. First, I evaluate the following statistical measures for various characteristics, including BMI, and group the results by the intervention type (sacubitril/valsartan and enalapril):
For Sacubitril/Valsartan Intervention:
Mean and standard deviation (std) for each characteristic, including BMI. Median for each characteristic, including BMI.
For Enalapril Intervention:
Mean and standard deviation (std) for each characteristic, including BMI. Median for each characteristic, including BMI.

What statistical test should be employed to analyze the effectiveness of the new heart failure medication formulations developed by two pharmaceutical companies, sacubitril and enalapril, with respect to their claims of reducing NT-proBNP levels? The claims state that sacubitril reduces NT-proBNP levels by an average of 3000 within 4 weeks and 2000 within 8 weeks, while enalapril reduces NT-proBNP levels by an average of 2500 within 4 weeks and 1500 within 8 weeks. A clinical trial was conducted using samples from both companies, and the objective is to determine which formulation is more effective.

For the sacubitril group, is there a significant difference between pre-treatment and Week 4 NT-proBNP levels? 
For the sacubitril group, is there a significant difference between pre-treatment and Week 8 NT-proBNP levels?
For the enalapril group, is there a significant difference between pre-treatment and Week 4 NT-proBNP levels? 
For the enalapril group, is there a significant difference between pre-treatment and Week 8 NT-proBNP levels?
Is there a significant difference in NT-proBNP levels at Week 4 between the two groups (sacubitril and enalapril)? 
Is there a significant difference in NT-proBNP levels at Week 8 between the two groups (sacubitril and enalapril)? 
Among participants aged 60 or older, is there a significant difference in NT-proBNP levels at Week 4 between the two groups (sacubitril and enalapril)?
Among participants aged 60 or older, is there a significant difference in NT-proBNP levels at Week 8 between the two groups (sacubitril and enalapril)? 
For evaluation of conclusions from 1-4, paired t-test was used because the observations were recorded in pairs of different parameters for two different groups. For evaluation of conclusions from 5-8, independent t-test was used as the groups were different but the observations belonged to the same parameter
Is there a statistically significant difference between the pre-treatment NT-proBNP and week 4 NT-proBNP, and between baseline and week 8 NT-proBNP in sacubitril/valsartan and enalapril groups?
