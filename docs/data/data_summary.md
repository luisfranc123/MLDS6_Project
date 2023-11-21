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

According to this plot, we can observe an upward trend in the global average temperature over time (from 1990 to 2020).

2. Next, we applied a `MaxMin()` transformation employing the scikitlearn `MinMaxScaler` utility to visualize the relationship between population, CO2 emissions, and Temperature change since 1990.

   **File:** `Population_Change_Vs_CO2_Emissions_&_Temperature.png`

Here, it seems that there is a linear positive relationship between the increase in urban population, total CO2 emissions, and the increase in  temperature. On the contrary, there has been a dramatic drop in the rural population since 1990, which suggests a massive migration of people from rural areas to the big urban centers. 

3. To visualize the evolution of total emissions of CO2 (in millions of tones) related to the change in temperature from 1990 to 2020, we created a plot that displays the relationship between these two variables by employing a transformation of the data (each total emission value was divided by 1.0e+06) to obtain the following graph:


   **File:** `Global_Average_Temperature_Vs_Tital_Annual_Emissions_per_year.png` 

Here, the plot displays a constant increase in average temperature versus total emissions of CO2 (in millions of tons) across time. 

4. The last visualization is related to each activity and its contribution to CO2 emissions globally:

   **File:** `Mean_CO2_emmissions_by_activity.png` 

Finally, we can observe here that the activity, by far, that emits the greatest amount of CO2 into the atmosphere is IPPU, which corresponds to *emissions from industrial processes and product use.*

## Variables Ranking and their Relationship

To explore the correlation between each explanatory variable with the target variable (**Average Temperature °C**) we grouped the data as follows: 

- **Total Fire-related Emissions:** *Savanna fires, Forest fires, Fires in organic soils, Fires in humid tropical forests.*
- **Total Industrial Emissions:** *Pesticides Manufacturing, Food Transport, Food Retail, Food Packaging, Food Processing, Fertilizers Manufacturing, IPPU.*
- **Total Cultivation Emissions:** *Crop Residues, Rice Cultivation, Drained organic soils (CO2), Manure applied to Soils, Manure left on Pasture, Manure Management.*

We then analyzed the correlation matrix to observe the most significant relationships among the variables; we found that our target variable is poorly correlated to each type of emission, with the exception of the Year.
Please refer to the plot `Correlation_HeatMap.png` to visualize the results. 




