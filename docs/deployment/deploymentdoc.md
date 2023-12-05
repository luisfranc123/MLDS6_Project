# Model Deployment

## Infrastructure

- **Model Name:** Agri_food_xgboost
- **Deployment Platform:** MLFlow
- **Technical requirements:**

  python: 3.10.12

  **build dependencies:**

  pip = 23.1.2

  setuptools = 67.7.2

  wheel = 0.42.0

  mlflow >= 2.1

  joblib = 1.3.2

  pandas = 1.5.3

  scikit-learn = 1.3.2

  xgboost = 2.0.2

- **Architecture Diagram:**
<img src="https://drive.google.com/uc?export=view&id=1bxZY2WvENueRXwbXbaZbhcOMiMFxWV7f" width="80%">

## Deployment Code: 

- **Main file:** MLDS6_model_deployment.ipynb
- **Access path to the files:**
  
  `os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"`

  `command = """ mlflow models serve -m 'models:/Argi_food_xgboost/Production' -p 8001 --env-manager 'local' & """`

  `get_ipython().system_raw(command)`

- **Environment Variables:**

   First, we create the folder where all the mlfiles will be stored:

  `!mkdir mlruns`

  Then, we get in contact with the MLFlow server:

  `command = """mlflow server \--backend-store-uri sqlite:///tracking.db \ --default-artifact-root file:mlruns \-p 5000 &"""`

  Install Pyngrok:

  `!pip install pyngrok`

  NGrok token:

  `token = "###_4H3EtkJPKnYedsmv7YbrR"`
  
  `os.environ["NGROK_TOKEN"] = token`
  
  NGrok authentication:

  `!ngrok authtoken $NGROK_TOKEN`

  Set up Ngrok connection:
  
  `from pyngrok import ngrok`

  `ngrok.connect(5000, "http")`

   **Set tracking `uri` in mlflow:**
  
   `mlflow.set_tracking_uri("http://localhost:5000")`

  Finally, create the experiment id in mlflow:

   `exp_id = mlflow.create_experiment(name="Agri_food", artifact_location="mlruns/")`

## Deployment Documentation

- **Installation Instructions:** First of all, the Python environment dependencies need to be installed:

  `!cat /etc/os-release`

  `!apt install tree`

  Import all the needed libraries and packages: 

  `import os`

  `import mlflow`

  `import matplotlib.pyplot as plt`

  `from IPython import get_ipython`

  `from IPython.display import display`

  As observed in the **Deployment code** section, we first need to contact a remote server, in this case, we used the `p 5000`server. We then set up the ngrok platform, which delivers instant ingress to our apps in any cloud, private network, or devices with authentication, load balancing, API gateway, and other critical controls. Following, we create a folder to store the temporal files and finally, we contact the MLFlow server using the `command` displayed in the previous section. To set up the ngrok environment, we need to create an authentication token in the ngrok web site https://ngrok.com/ and finally launch it through the mlflow tracking `URI`.

  **Note: For more details, please refer to the code displayed in the previous section.**      
  
- **Model setup Instructions:** Once we have run the experiments to identify the best parameters that optimize the target metric, which in our case was r^2_score, we select the best model by filtering the runs by score as follows (in the MLFlow platform):


  
<img src = "https://drive.google.com/uc?export=view&id=1IjgPpAAZHONV23W9ZtJUD0QWkUm5LhWy" width="80%">


  To have a better visualization of the models' comparison, we can click on the comparison button to obtain the following visualization: 
  

<img src = "https://drive.google.com/uc?export=view&id=1jOOhcW1o569XIobnhBr4m5J7e2nbF_HN" width="80%">


  Finally, we then select the best model and put it in **`production`**:
  

<img src = "https://drive.google.com/uc?export=view&id=167vHDZbeeKhIIb8zPNVRFWKCb7BY9gZ5" width="80%">

  
- **Instructions for use:** Once the model is deployed in MLFlow, as final users, we can implement the model to print predictions based on test data or new coming data regarding Agri-food industrial activities. The following commands will enable any user from Python to use the model to make any desirable predictions:

Import requests library: 

`import requests`

Create, for instance, a list of 10 records from the test dataset to make predictions using the implemented XGBoost model:


`data_request = X_test[:10].tolist()`

Finally, by launching a request to the server, and returning a text file, we can observe the predictions givn the `data_request` set: 

`r = requests.post("http://localhost:8001/invocations", json = {"inputs": data_request})`
`print(r.text)`

In this example, we obtained the following **predictions**: 


`{"predictions": [1.7788593769073486, 0.7580377459526062, 1.07029128074646, 1.3890321254730225, 0.3866143226623535, 0.9527288675308228, 0.7149747610092163, 0.4785969853401184, 0.18529534339904785, 1.102358341217041]}`

