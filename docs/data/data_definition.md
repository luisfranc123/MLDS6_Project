# Data Definition

## Data Origin

- [ ] The Agri-food CO2 emission dataset was obtained in the repository [Kaggle](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml/data). 

## Specification of the scripts for data loading

-  [ ] df = pd.read_csv("Agrofood_co2_emission.csv", sep = ',')

## References to source and destination routes or databases

- [ ] The dataset was downloaded directly to my personal Drive for convenience:
- [ ] /content/Agrofood_co2_emission.csv

### Data path origin 

- [ ] [kaggle datasets download -d alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml](url)
- [ ] 7k rows and 31 columns. The dataset used for the study on CO2 emissions and temperature change for each country from 1990 to 2020 was compiled using data from the FAO (Food and Agriculture Organization of the United Nations) and IPCC (Intergovernmental Panel on Climate Change). All the emissions were recorded in kilotonnes (kt): 1kt = 1000 kg. The data is in `cvc` format.  
- [ ] The only preprocessing done so far is the standardization of some columns to better visualize their changes across time. 


