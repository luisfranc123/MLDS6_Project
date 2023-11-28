#Load MLFlow environment:
!cat /etc/os-release
!apt install tree

#import libraries
import os
import mlflow
import matplotlib.pyplot as plt
from IPython import get_ipython
from IPython.display import display

#Create folder where all the mlfiles will be stored
!mkdir mlruns

#MLFlow server
command = """
mlflow server \
        --backend-store-uri sqlite:///tracking.db \
        --default-artifact-root file:mlruns \
        -p 5000 &
"""
get_ipython().system_raw(command)

!pip install pyngrok

#NGROK token:
token = "2Y2MVSZcRpdpIRJ4MzHZL9fR4B9_4H3EtkJPKnYedsmv7YbrR"
os.environ["NGROK_TOKEN"] = token
#NGROK authentication:
!ngrok authtoken $NGROK_TOKEN
#ngrok connection:
from pyngrok import ngrok
ngrok.connect(5000, "http")
#set tracking uri in mlflow:
mlflow.set_tracking_uri("http://localhost:5000")
#create an experiment ID with the name 'Agri_food':
exp_id = mlflow.create_experiment(name="Agri_food", artifact_location="mlruns/")

#Training and Hyperparameter optimization:
!pip install optuna
import optuna
#Import libraries:
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#Train XGBoost Regressor model function:
def train_model_XGBR(X_train, y_train, n_estimators, max_depth, booster, gamma,
                learning_rate, random_state):
  model_XGBR = XGBRegressor(n_estimators = n_estimators, max_depth = max_depth,
                       booster = booster, gamma = gamma,
                       learning_rate = learning_rate,
                       random_state = random_state).fit(X_train, y_train)

  return model_XGBR

#Evaluate XGBoost Regressor model function:
def eval_model_XGBR(model_XGBR, X_test, y_test):

    y_pred = model_XGBR.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mae, mse, r2

#XGBoost Regressor MLFlow run:
def mlflow_run_XGBR(X_train, y_train, X_test, y_test, n_estimators, max_depth,
                booster, gamma, learning_rate, random_state, exp_id, run_name):

  params = {'n_estimators': n_estimators, 'max_depth': max_depth, 'booster': booster, 'gamma': gamma,
            'learning_rate': learning_rate}

  run = mlflow.start_run(run_name = run_name, experiment_id = exp_id)



  model_XGBR = train_model_XGBR(X_train = X_train, y_train = y_train,
                      n_estimators = n_estimators,
                      max_depth = max_depth, booster = booster,
                      gamma = gamma, learning_rate = learning_rate,
                      random_state = random_state)

  mae, mse, r2 = eval_model_XGBR(model_XGBR, X_test, y_test)

  mlflow.log_params(params)
  mlflow.xgboost.log_model(model_XGBR, 'xgboost_model')
  mlflow.log_metrics({'mae': mae, 'mse': mse, 'r2_score': r2})
  mlflow.end_run()
  return run, mae, mse, r2

#XGBoost Rgressor Hyperparameter Optimization:
def objective_XGBR(trial):
  #hyperparameters to be optimized:
  n_estimators = trial.suggest_int('n_estimators', 25, 200)
  max_depth = trial.suggest_int('max_depth', 2, 10)
  booster = trial.suggest_categorical('booster', ['gbtree', 'gblinear', 'dart'])
  gamma = trial.suggest_float('gamma', 0.01, 10, log=True)
  l_r = trial.suggest_float('learning_rate', 1e-6, 1, log = True)

  _, _, _, r2 = mlflow_run_XGBR(X_train = X_train, y_train = y_train,
                           X_test = X_test, y_test = y_test,
                           n_estimators = n_estimators,
                           max_depth = max_depth, booster = booster,
                           gamma = gamma, learning_rate = l_r,
                           random_state = 0, exp_id = exp_id,
                           run_name = 'optuna_xgboost')
  return r2

#Run XGBoost study:
study_XGBR = optuna.create_study(
    direction="maximize",
    storage="sqlite:///hp.db",
    study_name="Agri_food",
    )
study_XGBR.optimize(func = objective_XGBR, n_trials=30, n_jobs=1)

#Extract XGBoost best Parameters:
params_XGBR = study_XGBR.best_params
#Train XGboost model with the best hyperparemeters:
trained_model_XGBR = XGBRegressor(**params_XGBR).fit(X_train, y_train)
#XGBoost model evaluation with the test dataset.
mae, mse, r2 = eval_model_XGBR(trained_model_XGBR, X_test, y_test)


#create an experiment ID with the name 'Agri_food_2':
exp_id_2 = mlflow.create_experiment(name="Agri_food_2", artifact_location="mlruns/")

#Train Random-Forest Regressor model function:
def train_model_RFR(X_train, y_train, n_estimators, max_depth, max_features,
                    max_samples, random_state):
  model_RFR = RandomForestRegressor(n_estimators = n_estimators,
                                    max_depth = max_depth,
                                    max_samples = max_samples,
                                    random_state = random_state).fit(X_train, y_train)

  return model_RFR

#Random_Forest-Regressor evaluate model:
def eval_model_RFR(model_RFR, X_test, y_test):

    y_pred = model_RFR.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mae, mse, r2

#Random_Forest-Regressor MLFlow run:
def mlflow_run_RFR(X_train, y_train, X_test, y_test, n_estimators, max_depth,
                   max_features, max_samples, random_state, exp_id, run_name):

  params = {'n_estimators': n_estimators, 'max_depth': max_depth,
            'max_features': max_features, 'max_samples': max_samples,
            'random_state': random_state}

  run = mlflow.start_run(run_name = run_name, experiment_id = exp_id_2)



  model_RFR = train_model_RFR(X_train = X_train, y_train = y_train,
                              n_estimators = n_estimators,
                              max_depth = max_depth,
                              max_features = max_features,
                              max_samples = max_samples,
                              random_state = random_state)

  mae, mse, r2 = eval_model_RFR(model_RFR, X_test, y_test)

  mlflow.log_params(params)
  mlflow.sklearn.log_model(model_RFR, 'RandomForest_model')
  mlflow.log_metrics({'mae': mae, 'mse': mse, 'r2_score': r2})
  mlflow.end_run()
  return run, mae, mse, r2

##Random_Forest-Regressor Hyperparameters Optimization: 
def objective_RFR(trial):

  #hyperparameters to be optimized:
  n_estimators = trial.suggest_int('n_estimators', 25, 200)
  max_depth = trial.suggest_int('max_depth', 2, 10)
  max_features = trial.suggest_float('max_features', 0.01, 1, log = True)
  max_samples = trial.suggest_float('max_samples', 0.001, 1, log = True)

  _, _, _, r2 = mlflow_run_RFR(X_train = X_train, y_train = y_train,
                           X_test = X_test, y_test = y_test,
                           n_estimators = n_estimators,
                           max_depth = max_depth,
                           max_features = max_features,
                           max_samples = max_samples,
                           random_state = 0, exp_id = exp_id_2,
                           run_name = 'optuna_randomforest')
  return r2

#Random_Forest-Regressor run study:
study_RFR = optuna.create_study(
    direction="maximize",
    storage="sqlite:///hp.db",
    study_name="Agri_food_2",
    )
study_RFR.optimize(func = objective_RFR, n_trials=30, n_jobs=1)

#Extract the RFR model best Parameters:
params_RFR = study_RFR.best_params
#Train best RFR model
trained_model_RFR = RandomForestRegressor(**params_RFR).fit(X_train, y_train)
#Random_Forest-Regressor model evaluation with the test dataset.
mae, mse, r2 = eval_model_RFR(trained_model_RFR, X_test, y_test)


