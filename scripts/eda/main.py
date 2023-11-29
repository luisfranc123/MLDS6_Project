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

pip install --upgrade "kaleido==0.1.*"
import kaleido
#Average Temperature distribution by years
fig = px.box(df, x = 'Year', y = 'Average Temperature °C', color = 'Year',
             color_discrete_sequence = px.colors.sequential.Electric,
             title = '<b> Average Temperature distribution by years')
fig.show()
fig.write_image("AverageTemp_dist_by_years.png");

#Correlation between Emissions and Average Temperature:
#Total Population:
#Total population seems to play a key role in total emissions
df['total_population'] = df['Total Population - Female'] + df['Total Population - Male']
# Assign Continent:
#Note: This task was assigned to ChatGPT to speed up the continent classification process
continent_mapping = {
    'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Côte d\'Ivoire', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'],
    'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
    'Europe': ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City'],
    'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States'],
    'Oceania': ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'],
    'South America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
}

#Function to assign to each country its correspondent continent
def assign_continent(country):
  for continent, countries in continent_mapping.items():
    if country in countries:
      return continent
  return None
#Apply the function assign_continent to df:
df['continent'] = df['Area'].apply(assign_continent)

#Plot: CO2 Emissions & Temperature - Population
fig_2 = px.scatter(df, df['Average Temperature °C'], df['total_emission'],
           size = 'total_population',
           title = '<b>CO2 Emissions and Temperature - Population',
           template = 'plotly_dark', color = 'continent')
fig_2.write_image("CO2_Emissions_Temp_Pop.png");
#Correlation
correlation = df.groupby(['Year']).agg({'total_emission': 'sum',
                                        'Average Temperature °C': 'mean',
                                        'total_population': 'sum'})
correlation.corr()
###Conclusion: Here, we can observe a significant correlation between Average Temperature, total population, and total emission. 
"""
                   total_emission 	Average Temperature °C 	total_population
total_emission 	         1.000000                  0.90552          0.981828
Average Temperature °C 	 0.905520 	               1.00000 	        0.912050
total_population 	       0.981828 	               0.91205 	        1.000000
"""
#Scatter plot - Temperature & CO2 Emissions - Global Relation:

fig_3 = px.scatter(correlation.reset_index(),
           x = 'total_emission',
           y = 'Average Temperature °C',
           size = 'total_population',
           color = 'Year',
           title = '<b>Temperature & CO2 Emissions - Global Relation',
           template = 'plotly_dark')
fig_3.write_image("Temperature_CO2_GlobalRelation.png")

#Emissions per year per country:
def country_emission(df, year, length):
  df = df.copy()
  #Establish the year in which we want to make the comparisson
  plot = df.loc[df['Year'] == year]
  #Descending order by total_emission
  plot = plot.sort_values(by = 'total_emission', ascending = True).tail(length)
  colors = plt.cm.get_cmap('viridis', len(plot))
  plt.figure(figsize = (12, 16))
  plt.barh(plot['Area'], plot['total_emission'],
           color = colors(range(len(plot))))
  plt.title(f'CO2 Emission by top {length} country in {year}')
  plt.xlabel('CO2 Emission in kilotones')
  plt.savefig(f"CO2_Emissions_Top{length}_{year}.png")
  plt.show();

#Plot: Top 30 countries with the highest total emissions in 2020
country_emission(df, 2020, 30)

#Emissions per year per country per capita:
df['emission_per_capita'] = df['total_emission']/df['total_population']

def country_emission_per_capita(df, year, length):
  df = df.copy()
  #Establish the year in which we want to make the comparisson and
  #filter small islands by population
  plot = df.loc[(df['Year'] == year) & (df['total_population'] > 800000)]
  #Descending order by total_emission
  plot = plot.sort_values(by = 'emission_per_capita', ascending = True).tail(length)
  colors = plt.cm.get_cmap('viridis', len(plot))
  plt.figure(figsize = (12, 16))
  plt.barh(plot['Area'], plot['emission_per_capita'],
           color = colors(range(len(plot))))
  plt.title(f'CO2 Emission by top {length} country in {year} per Capita')
  plt.xlabel('CO2 Emission in kilotones/inhabitant')
  plt.savefig(f"CO2_Emissions_Top{length}_{year}_per_capita.png")
  plt.show();

#Plot: Top 30 countries with the highest total emissions per capita in 2020
country_emission_per_capita(df, 2020, 30)

total_emission_sources['continent'] = df['continent']
#Sns plot: Correlation between Explanatory Variables and the Target Variable (Avg. Temperature)
sns_plot = sns.pairplot(total_emission_sources, vars = ['total_fire_emissions', 'total_industrial_emissions',
       'total_cultivation_emissions', 'Agrifood Systems Waste Disposal',
       'Food Household Consumption', 'Average Temperature °C'],
             y_vars = 'Average Temperature °C', hue = 'continent')
plt.show()
sns_plot.figure.savefig("Correlation_ExplanatoryVar_Target_Variable.png")


