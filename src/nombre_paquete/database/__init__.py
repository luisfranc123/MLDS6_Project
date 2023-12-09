file_id = 1h6Ot3n82VKWKtlu7U5FnRi7ixaUZ-GEC
import gdown
import pandas as pd

def load_data(file_id):
  #Download gdown to load the dataset
  !pip install gdown
  #Import all the needed libraries
  #Download dataset using its Google Drive ID  
  !gdown file_id
  #Define data frame (df) that will be used through the applied project
  df = pd.read_csv("Agrofood_co2_emission.csv", sep = ',')
  #The dataset contains 6965 records containing 31 variables each.  
  return df
