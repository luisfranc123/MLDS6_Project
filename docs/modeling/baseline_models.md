# Baseline Model Report


## Model Description 

We chose the XGBoost Regressor model as our baseline model due to its well-known efficiency and performance. 

## Input Variables

- [] Features (Explanatory Variables):
*Area, continent, Year, Savanna fires, Forest fires, Crop Residues, Rice Cultivation, Drained organic soils (CO2), Pesticides Manufacturing, Food Transport, Forestland, Net Forest conversion, Food Household  Consumption, Food Retail, On-farm Electricity Use, Food Packaging, Agrifood Systems Waste Disposal, Food Processing, Fertilizers Manufacturing, IPPU, Manure applied to Soils, Manure left on Pasture, Manure Management, Fires in organic soils, Fires in humid  tropical forests, On-farm energy use, total_emission, total_population.*



## Target Variable

- [] Target (Response Variable):
  *Average Temperature °C.*

## Model Evaluation: 

### Evaluation Metrics

As our study implements a regression model, we implemented the following metrics: 
Mean Absolute Error (MAE), Mean Squared Error (MSE), and r_squared score.   


### Evaluation Results
 After 30 iterations using `optuna` library, we present the results of the five best models, jointly with their optimized hyper-parameters and performance metrics. 


 | **Model (MLFlow run)** | **Booster** | **Gamma** | **Learning Rate** | **max_depth** | **n_estimators** | **mae** | **mse** | **r2_score** |
 | ---- | ---- | ----| ---- | ---- | ---- | ---- | ---- | ---- |
 | 1 | gbtree | 0.276061 | 0.13378 | 8 | 56 | 0.247258  | 0.114403 | 0.625213 |
 | 2 | dart | 0.326981 | 0.147188 | 8 | 90 | 0.247697  | 0.115368 | 0.622049 |
 | 3 | gbtree | 0.347706 | 0.223800 | 9 | 25 | 0.247682  | 0.115756 | 0.620779 |
 | 4 | dart | 0.390285 | 0.065763 | 8 | 52 | 0.248799  | 0.116976 | 0.616783 |
 | 5 | dart | 0.308206 | 0.203255 | 9 | 93 | 0.248230  | 0.117930 | 0.613659 |
 

## Results Analysis 

We can observe that the best r2_score obtained when implementing the XRGBoost Regressor model is 0.625213, which is significantly better than the ones reported in previous models used to predict the change in the average temperature due to the aforementioned Agro-food related activities. Additionally, the hyperparameter optimization process enables us to find a better model that fits the given data. One of the advantages of this baseline model is that it progressively learns through each iteration, which represents a leap forward in terms of efficiency. However, there is still much unknown variation that cannot be explained by the model itself, therefore, further analysis needs to be done. 


## Conclusions

This study is an attempt to understand the main Agri-food activities related to the increased trend in average temperature globally and possibly, disentangle potential insights that enable us to better formulate policies and technical-based insights that ultimately contribute to reducing the impacts of human activities on global warming. By the implementation of ML-based algorithms, such as XGBoost regressor, we might forecast and identify the activities that mainly contribute to the increased average temperature with a variance explanation of around 63%. However, further research is needed regarding socio-environmental factors that contribute to Global Warming, as there is still some unknown variation when implementing this type of approach. 



## References

- https://xgboost.readthedocs.io/en/stable/parameter.html
- https://www.kaggle.com/code/alessandrolobello/deep-eda-analysis-and-ml-model-evaluation



