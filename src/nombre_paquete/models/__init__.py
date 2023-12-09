import os
import mlflow
import matplotlib.pyplot as plt
from IPython import get_ipython
from IPython.display import display
from agri-ind.training import model_XGBR

model = model_XGBR
#Access path to the files:
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"

command = """ mlflow models serve -m 'models:/Argi_food_xgboost/Production' -p 8001 --env-manager 'local' & """

get_ipython().system_raw(command)

#First, we create the folder where all the mlfiles will be stored:
!mkdir mlruns

#Then, we get in contact with the MLFlow server:

command = """mlflow server \--backend-store-uri sqlite:///tracking.db \ 
            --default-artifact-root file:mlruns \-p 5000 &"""

#Install Pyngrok:

!pip install pyngrok

#NGrok token:

token = "###_###"

os.environ["NGROK_TOKEN"] = token

#NGrok authentication:

!ngrok authtoken $NGROK_TOKEN

#Set up Ngrok connection:

from pyngrok import ngrok

ngrok.connect(5000, "http")

#Set tracking uri in mlflow:

mlflow.set_tracking_uri("http://localhost:5000")

#Finally, create the experiment id in mlflow:

exp_id = mlflow.create_experiment(name="Agri_food", artifact_location="mlruns/")
