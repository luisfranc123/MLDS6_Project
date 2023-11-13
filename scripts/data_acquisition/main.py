# Download gdown to load the dataset
!pip install gdown
# Import all the needed libraries
import gdown
import pandas as pd
 # Download dataset using its Google Drive ID  
!gdown 1h6Ot3n82VKWKtlu7U5FnRi7ixaUZ-GEC

# Define data frame (df) that will be used through the applied project
df = pd.read_csv("Agrofood_co2_emission.csv", sep = ',')
# The dataset contains 6965 records containing 31 variables each.  
display(df.shape)
# Basic descriptive statistics 
display(df.describe())
