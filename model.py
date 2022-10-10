# import libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.ensemble import ExtraTreesClassifier as ET
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
import pickle

# read dataset
wq_df = pd.read_csv("https://raw.githubusercontent.com/jadanpl/Water-Potability-Prediction/main/water_potability.csv")

# data preprocessing
wq_df.columns = wq_df.columns.str.lower()
wq_df['ph'] = wq_df['ph'].fillna(wq_df['ph'].median())
wq_df['sulfate'] = wq_df['sulfate'].fillna(wq_df['sulfate'].median())
wq_df['trihalomethanes'] = wq_df['trihalomethanes'].fillna(wq_df['trihalomethanes'].median())

# Create training and testing sets
X = wq_df[['ph', 'hardness', 'solids', 'chloramines', 'sulfate']]
Y = wq_df['potability']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# model building
final_rf = RF(class_weight='balanced', max_depth=25, max_features=1,
              min_samples_leaf=3, n_estimators=500, random_state=42)
final_etree = ET(class_weight='balanced', max_depth=30, max_features=3,
                 min_samples_leaf=3, random_state=42)
final_svc = SVC(C=1000, class_weight='balanced', gamma=1, probability=True, random_state=42)
final_model = VotingClassifier(estimators = [('RF',final_rf), ('ET',final_etree), ('SVC',final_svc)],
                         voting = 'soft')
final_model.fit(X,Y)
# final_model.predict()

# Saving the model
pickle.dump(final_model, open('voting_clf.pkl', 'wb'))
