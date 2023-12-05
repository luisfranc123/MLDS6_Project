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
#As observed here, we obtained an overall 0.63 in the r2_score when using the xgboost regressor, which enable us to
#predict with a decend amount of certeinity what would be the increse of average temperature in °C due to the 
#emission of different agro-industrial activities globally. More experiementation is needed to find better models that 
#fit the data and make better predictions, as identifying the main activities thah mostly contribute to the Global Warming 
#trend is essential to create technical-based policies to reduce such effects and contribute to a more sustainable 
#agro-industrial development
