!pip install gdown
#Install Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gdown
#Drive path ID
!gdown 1h6Ot3n82VKWKtlu7U5FnRi7ixaUZ-GEC
#df object as the dataframe for the data
df = pd.read_csv("Agrofood_co2_emission.csv", sep = ',')
#Shape and how the data looks like
df.shape
df.head()
df.columns
df.info()
#Identify the total number of countries included in the analysis
len(df['Area'].unique())

#Basic descriptive statistics, excluding the column Year, which does not provide
#any valuable information in this summary:
df.iloc[:,2:].describe().applymap('{:.2f}'.format)
#Let's now take a look of the mean values from each variable:
(df.iloc[:,2:].describe().applymap('{:.2f}'.format)).loc['mean']
#Missing values from the dataset
df.isna().sum()
#Average Temperature change since 1990
sns.set_theme(style = "darkgrid")
fig, ax =plt.subplots(figsize = (16,8))
sns.lineplot(data = df, x = 'Year', y = 'Average Temperature °C', ax = ax);
fig.suptitle('Average Temperature Change Since 1990');
plt.savefig("Average_Temperature_Change.png")
#Note: From this time-series, it can be observed a clear upward trend on
#the average temperature since 1990.
#We now want to visualize the change in Urban Population, Rural Population,
#total emission and the average temperature across time.
#First, we need to standarize the values.
from sklearn.preprocessing import MinMaxScaler
# Define the instance scaler
scaler = MinMaxScaler()
temp_emission = df.groupby('Year').agg({'Average Temperature °C': 'mean',
                                        'total_emission': 'mean',
                                        'Urban population': 'mean',
                                        'Rural population': 'mean'})
#Standarization
norm_emission = scaler.fit_transform(temp_emission)
#Data frame with the new standarized mean values
temp_emission_df = pd.DataFrame(norm_emission, columns = ['S_Average_Temperature',
                                                          'S_Mean_CO2_Emission',
                                                          'S_Urban_population',
                                                          'S_Rural_population'])
#Define the indexes, as the data frame was grouped by year
temp_emission_df.index = [i for i in range(1990, 2021)]
temp_emission_df.head()
#change in Urban Population, Rural Population, total emission and the average
#temperature across time.
fig, ax =plt.subplots(figsize = (16,8))
g = sns.lineplot(temp_emission_df, ax = ax);
fig.suptitle('Standarized CO2 Emission, Average Temperature, and change in Urban and Rural Population')
plt.plot()
plt.savefig("Population_Change_Vs_CO2_Emissions_&_Temperature.png")

# Now, we generate a plot of mean CO2 emissions vs Avg. Temperature
from matplotlib.ticker import FuncFormatter
# group by year
temp_total_emission = df.groupby('Year').agg({'Average Temperature °C': 'mean',
                                        'total_emission': 'sum'})
# Assign a new column Emissions_MT
temp_total_emission = temp_total_emission.assign(Emissions_MT =
                                 temp_total_emission['total_emission']/1000000)

fig, ax =plt.subplots(figsize = (16,8))
g = sns.scatterplot(temp_total_emission, x = 'Emissions_MT',
                    y = 'Average Temperature °C', ax = ax,
                    hue = 'Year', size = 'Year', sizes = (20, 200),
                    palette = 'mako');
fig.suptitle('Average Temperature Vs Total CO2 emissions per year')
ax.set_xlabel('Total annual emissions of CO2 in millions of tons')
plt.plot();
plt.savefig("Global_Average_Temperature_Vs_Tital_Annual_Emissions_per_year.png");

# Contribution of each agri-food related activity to the total CO2 emissions anually
activity_emissions = df.iloc[:, 2: -7].copy()
list_deletion = ['Forestland', 'Net Forest conversion', 'On-farm Electricity Use']
activity_emissions = activity_emissions.drop(list_deletion, axis = 1)
mean_emisions = activity_emissions.mean()
mean_emisions.sort_values(ascending = False, inplace = True)
cols = mean_emisions.index

fig, ax = plt.subplots(figsize=(16, 12))
sns.barplot(x = mean_emisions, y = cols, ax = ax) #wrap x and y parameters
ax.set_ylabel("Activity")  # Set the y-axis label
ax.set_xlabel("Mean CO2 emmissions (in tons)")     # Set the x-axis label
fig.suptitle('Mean CO2 emmissions (in tons) by Agri-food activity')
plt.xticks(rotation = 90)      # Rotate x-axis labels for better visibility
plt.tight_layout()           # Adjust layout to prevent labels from getting cut off
plt.plot();
plt.savefig("Mean_CO2_emmissions_by_activity.png");

#To analyze distinct correlations between the response and the target
#variables, we grouped the data following common categories as follows:
#Fire-related emissions:
fire_emissions = ['Savanna fires', 'Forest fires', 'Fires in organic soils',
                  'Fires in humid tropical forests']
#Industrial-related emissions:
industrial_emissions = ['Pesticides Manufacturing', 'Food Transport', 'Food Retail',
                        'Food Packaging', 'Food Processing', 'Fertilizers Manufacturing',
                        'IPPU']
#Cultivation-related emissions:
cultivation_emissions = ['Crop Residues', 'Rice Cultivation', 'Drained organic soils (CO2)',
                         'Manure applied to Soils', 'Manure left on Pasture', 'Manure Management']

#'Agrifood Systems Waste Disposal' 'Food Household Consumption'

df_fire = df[fire_emissions].assign(total_fire_emissions = df[fire_emissions].sum(axis = 1))
df_industrial = df[industrial_emissions].assign(total_industrial_emissions =
                                               df[industrial_emissions].sum(axis = 1))
df_cultivation = df[cultivation_emissions].assign(total_cultivation_emissions =
                                                  df[cultivation_emissions].sum(axis = 1))

#Create a new dataframe with the target values:
data_emission_sources = {'total_fire_emissions': df_fire['total_fire_emissions'],
                          'total_industrial_emissions': df_industrial['total_industrial_emissions'],
                          'total_cultivation_emissions': df_cultivation['total_cultivation_emissions'],
                          'Agrifood Systems Waste Disposal': df['Agrifood Systems Waste Disposal'],
                          'Food Household Consumption': df['Food Household Consumption'],
                          'Average Temperature °C': df['Average Temperature °C'],
                          'Year': df['Year'], 'total_emission': df['total_emission']}

total_emission_sources = pd.DataFrame(data = data_emission_sources)

#Heat map of correlations
sns.heatmap(data = total_emission_sources.corr(), annot = True, cmap = 'twilight',
            fmt=".2f");
plt.savefig("Correlation_HeatMap.png");
#Correlation Table:
total_emission_sources.corr()

