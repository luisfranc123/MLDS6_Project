#Run MLFlow study (Experimentsto identify the parameters that optimize the R2_score value)
study_XGBR = optuna.create_study(
    direction="maximize",
    storage="sqlite:///hp.db",
    study_name="Agri_food",
    )
study_XGBR.optimize(func = objective_XGBR, n_trials=30, n_jobs=1)

#Extract best Parameters from the experiemntal runs:
params_XGBR = study_XGBR.best_params

#We train the model 
trained_model_XGBR = XGBRegressor(**params_XGBR).fit(X_train, y_train)

# Calculate the metrics mean absolute error (mae), mean squared error (mse), and r2_score (r2) using the test datset:
mae, mse, r2 = eval_model_XGBR(trained_model_XGBR, X_test, y_test)
print(f"Mean Absolute Error: {mae}, Mean Squared Error: {mse}, R-Squared: {r2}")

>> Mean Absolute Error: 0.2420003765115058, Mean Squared Error: 0.11161802804848274, R-Squared: 0.6343357834675165

#Conclusion:
#As observed here, we obtained an overall r2_score of 0.63 when implementing the xgboost regressor, compared to the 
#Random Forest regressor, which obtained an optimized r2_score of 0.42. After careful experimentation, we can conclude
#that the XGBoost regresors, thanks to its iterable learning process, had a significant better performance when predicting 
#changes in average temperature due to agri-industrial activities. 
#However, there is still some unknown variation that contribute to the average change in temperature that may be related 
#to other industrial activities and should be added to the present study. All in all, this study is a step ahead in 
#understanding the complex relationship between anthropogenic activities and the current global warming trend that has 
#affected a wide range of ecological processes and needs urgent attention from both the science community and decision 
#makers around the world. 


