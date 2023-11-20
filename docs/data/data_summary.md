# Data Report


## General Summary of the data

This dataset contains 7k rows and 31 columns. The dataset used for the study on CO2 emissions and temperature change for each country from 1990 to 2020 was compiled using data from the FAO (Food and Agriculture Organization of the United Nations) and IPCC (Intergovernmental Panel on Climate Change). All the emission were recorde in kilotones (kt): 1kt = 1000 kg.


## Data quality summary

Based on the exploratory analysis, we have the following summary which gives us an idea of how many missing values are in each numerical variable: 

| **Variable** | **Total number of missing values** |
| --- | --- |
| Area | 0 |                                  
| Year | 0 |                                  
| Savanna fires | 31 |                        
| Forest fires | 93 |                         
| Crop Residues | 1389 |                      
| Rice Cultivation | 0 |                      
| Drained organic soils (CO2) | 0 |           
| Pesticides Manufacturing | 0 |              
| Food Transport | 0 |                        
| Forestland | 493 |                          
| Net Forest conversion | 493 |               
| Food Household Consumption | 0 |          
| Food Retail | 0 |                           
| On-farm Electricity Use | 0 |               
| Food Packaging | 0 |                        
| Agrifood Systems Waste Disposal | 0 |       
| Food Processing | 0 |                       
| Fertilizers Manufacturing | 0 |             
| IPPU | 743 |                                
| Manure applied to Soils | 928 |             
| Manure left on Pasture | 0 |                
| Manure Management | 928 |                  
| Fires in organic soils | 0 |                
| Fires in humid tropical forests | 155 |     
| On-farm energy use | 956 |                  
| Rural population | 0 |                      
| Urban population | 0 |                      
| Total Population - Male | 0 |               
| Total Population - Female | 0 |             
| total_emission | 0 |                        
| Average Temperature °C | 0 |                

## Target Variable

The purpose of the present study is to explore distinct ML algorithms to predict the increase of **average temperature**, due to distinct agri-food activities around the globe from 1990 until 2020. 


## Individual Variables

1. The following visualization enables us to observe the change in average temperature since 1990: 

**File:** `Average_Temperature_Change.png`

2. Next, we applied a `MaxMin()` transformation employing the scikitlearn `MinMaxScaler` utility to visualize the relationship between population, CO2 emissions, and Temperature change since 1990.

   **File:** `Population_Change_Vs_CO2_Emissions_&_Temperature.png`

3. In order to visualize the evolution of total emissions of CO2 (in millions of tones) related to the change of temperature from 1990 to 2020, we created a plot that relates these two variables by employing a basic transformation of the data (each total emission value was divided by 1.0e+06) to obtain the following graph:

   **File:** `Global_Average_Temperature_Vs_Tital_Annual_Emissions_per_year.png` 

4. The last visualization is related to each activity and its contribution to CO2 emissions globally:

**File:** `Mean_CO2_emmissions_by_activity.png` 

## Variables Ranking

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
