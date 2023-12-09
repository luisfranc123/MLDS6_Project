#Import load_data function from agro_ind package
import from agro_ind.database load_data
#Fill-in missing values using RandomForestRegressor from sklearn librery
#Import libraries
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

file_id = 1h6Ot3n82VKWKtlu7U5FnRi7ixaUZ-GEC
#Call load_data function to load the csv file:
df = load_data(file_id)

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
#get apart only the numerical variables and missing values imputation:
numerical = df[num_features]
#Numerical features with missing values:
missing_values = df[num_features].isna().sum()
missing_list = missing_values[missing_values > 0].keys().tolist()

def replace_missing(df, missing_list):
  numeric_df = df.copy()
  for feature in tqdm(missing_list):
    numeric_df = regressor_imputer(numeric_df, feature)
  return numeric_df

#Apply the function replace_missing to the numerical subset:
num_df = replace_missing(numerical, missing_list)

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

#Function to split data into train and test set:
def split_data(X, y, test_size, random_state):
  #Training and Test Datasets:
  X_train, X_test, y_train, y_test = train_test_split(X.to_numpy(), 
                                                      y.to_numpy(),
                                                      test_size = 0.2,
                                                      random_state = 46)
  return X_train, X_test, y_train, y_test
