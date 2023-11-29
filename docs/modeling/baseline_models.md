# Baseline Model Report


## Model Description 

We implemented XGBoost Regressor and Random Forest Regressor approaches as our baseline models due to their well-known efficiency and performance when dealing with nonlinear multiple regression problems. 

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
 
**Table 1:** XGBoost MLFlow runs metrics and hyperparameters summary

| **Model (MLFlow run)** | **max_depth** | **max_features** | **max_samples** | **n_estimators** | **mae** | **mse** | **r2_score** |
 | ---- | ---- | ----| ---- | ---- | ---- | ---- | ---- | 
 | 1 | 10 | 0.029473 | 0.902412 | 67 | 0.254459 | 0.124865  | 0.590938 |
 | 2 | 10 | 0.023797 | 0.792905 | 98 | 0.257386 | 0.126889  | 0.584307 | 
 | 3 | 10 | 0.030506 | 0.874975 | 67 | 0.257671 | 0.127655  | 0.580172 | 
 | 4 | 10 | 0.021106 | 0.793425 | 28 | 0.259247 | 0.128151  | 0.116976 | 
 | 5 | 9 | 0.033379 | 0.992276 | 74 | 0.259405 | 0.128517  | 0.578973 | 
 
**Table 2:** Random-Forest-Regressor MLFlow runs metrics and hyperparameters summary

Then, we evaluated both models using the test dataset and obtained the results summarized in the following table:

| **Model** | **MAE** | **MSE** | **R2_Score** |
| ---- | ---- | ---- | ---- |
| XGBoost R. | 0.2473 | 0.1144 | 0.6252 |
| Random Forest R. | 0.3076 | 0.1751 | 0.4262 |

**Table 3:** XGBoost and Random-Forest-Regressors Test Evaluation metrics

As observed in table 3, XGBoost regressor performed significantly better when evaluating with the test dataset. This comparison enables us to pick up the model to be used during the deployment stage.  

## Results Analysis 

We can observe that the best r2_score obtained when implementing the XRGBoost Regressor model is 0.625213, which is significantly better than the ones reported in previous models used to predict the change in the average temperature due to the aforementioned Agro-food related activities. Additionally, the hyperparameter optimization process enables us to find a better model that fits the given data. One of the advantages of this baseline model is that it progressively learns through each iteration, which represents a leap forward in terms of efficiency. However, there is still much unknown variation that cannot be explained by the model itself, therefore, further analysis needs to be done. 


## Conclusions

This study is an attempt to understand the main Agri-food activities related to the increased trend in average temperature globally and possibly, disentangle potential insights that enable us to better formulate policies and technical-based insights that ultimately contribute to reducing the impacts of human activities on global warming. By the implementation of ML-based algorithms, such as XGBoost and Random Forest regressors, we might forecast and identify the activities that mainly contribute to the increased average temperature with a variance explanation of around 63% and 43%, respectively. However, further research is needed regarding socio-environmental factors that contribute to Global Warming, as there is still some unknown variation when implementing this type of approach. 



## References

- https://xgboost.readthedocs.io/en/stable/parameter.html
- https://www.kaggle.com/code/alessandrolobello/deep-eda-analysis-and-ml-model-evaluation



