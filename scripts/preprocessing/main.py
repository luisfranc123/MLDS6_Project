#Fill-in missing values using RandomForestRegressor from sklearn librery
#Import libraries
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

#Missing values
df.isna().sum()
Area                                  0
Year                                  0
Savanna fires                        31
Forest fires                         93
Crop Residues                      1389
Rice Cultivation                      0
Drained organic soils (CO2)           0
Pesticides Manufacturing              0
Food Transport                        0
Forestland                          493
Net Forest conversion               493
Food Household Consumption          473
Food Retail                           0
On-farm Electricity Use               0
Food Packaging                        0
Agrifood Systems Waste Disposal       0
Food Processing                       0
Fertilizers Manufacturing             0
IPPU                                743
Manure applied to Soils             928
Manure left on Pasture                0
Manure Management                   928
Fires in organic soils                0
Fires in humid tropical forests     155
On-farm energy use                  956
Rural population                      0
Urban population                      0
Total Population - Male               0
Total Population - Female             0
total_emission                        0
Average Temperature °C                0
total_population                      0
continent                          1743
emission_per_capita                   0

#Function to replace missing values using RandomForestRegressor forecasting
def regressor_imputer(df, feature, max_depth = 6):
  df_filled = df.copy()

  if df_filled[feature].isna().any():
    
    missing_data = df_filled[df_filled[feature].isna()]
    non_missing_data = df_filled.dropna(subset=[feature])
    X_train = non_missing_data.drop(columns = [feature])
    y_train = non_missing_data[feature]
    imputer = SimpleImputer()
    X_train_imputed = imputer.fit_transform(X_train)
    X_missing = missing_data.drop(columns = [feature])
    X_missing_imputed = imputer.transform(X_missing)
    rf = RandomForestRegressor(max_depth = max_depth)
    rf.fit(X_train_imputed, y_train)
    y_missing_pred = rf.predict(X_missing_imputed)
    df_filled.loc[df_filled[feature].isna(), feature] = y_missing_pred

  return df_filled


#Identify both numeric and categorical columns
num_features = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]
cat_features = [col for col in df.columns if df[col].dtypes in ['object']]

#Numerical features with missing values:
missing_values = df[num_features].isna().sum()
missing_list = missing_values[missing_values > 0].keys().tolist()

#get apart only the numerical variables and missing values imputation:
numerical = df[num_features]
def replace_missing(df, missing_list):
  numeric_df = df.copy()
  for feature in tqdm(missing_list):
    numeric_df = regressor_imputer(numeric_df, feature)
  return numeric_df

#Apply the function replace_missing to the numerical subset:
num_df = replace_missing(numerical, missing_list)

#Just checking
num_df.isna().sum()
Year                               0
Savanna fires                      0
Forest fires                       0
Crop Residues                      0
Rice Cultivation                   0
Drained organic soils (CO2)        0
Pesticides Manufacturing           0
Food Transport                     0
Forestland                         0
Net Forest conversion              0
Food Household Consumption         0
Food Retail                        0
On-farm Electricity Use            0
Food Packaging                     0
Agrifood Systems Waste Disposal    0
Food Processing                    0
Fertilizers Manufacturing          0
IPPU                               0
Manure applied to Soils            0
Manure left on Pasture             0
Manure Management                  0
Fires in organic soils             0
Fires in humid tropical forests    0
On-farm energy use                 0
Rural population                   0
Urban population                   0
Total Population - Male            0
Total Population - Female          0
total_emission                     0
Average Temperature °C             0
total_population                   0
emission_per_capita                0

#Preprocess categorical variables using LabelEncoder():
from sklearn.preprocessing import LabelEncoder
cat_df = df[cat_features].copy()
label_encoder = LabelEncoder()
for column in cat_df.columns:
  cat_df.loc[:, column] =  label_encoder.fit_transform(cat_df[column])

#Preprocessed Data Frame:
model_df = pd.concat([cat_df, num_df], axis = 1)
#Save model_df for mdeling purposes:
model_df.to_csv('model_df.csv', index = False)
#Features and labels sets
X = model_df.drop(columns = ["Average Temperature °C", "emission_per_capita", 
                             'Total Population - Female', 'Total Population - Male', 
                             'Rural population', 'Urban population', 'emission_per_capita'])
y = model_df["Average Temperature °C"]

#Training and Test Datasets:
X_train, X_test, y_train, y_test = train_test_split(X.to_numpy(), 
                                                    y.to_numpy(),
                                                    test_size = 0.2,
                                                    random_state = 46)
