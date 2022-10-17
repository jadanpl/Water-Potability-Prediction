# import libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.ensemble import ExtraTreesClassifier as ET
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
import pickle
import bz2

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
trans = ColumnTransformer(transformers=[("num", MinMaxScaler(), ['ph', 'hardness', 'solids', 'chloramines', 'sulfate'])],
                          remainder='passthrough')

# model building
final_rf = RF(class_weight='balanced', max_depth=25, max_features=1,
              min_samples_leaf=3, n_estimators=500, random_state=42)
final_etree = ET(class_weight='balanced', max_depth=30, max_features=3,
                 min_samples_leaf=3, random_state=42)
final_svc = SVC(C=1000, class_weight='balanced', gamma=1, probability=True, random_state=42)
voting_clf = VotingClassifier(estimators=[('RF', final_rf), ('ET', final_etree), ('SVC', final_svc)],
                              voting='soft')
final_model = Pipeline(steps=[("trans", trans), ("voting_clf", voting_clf)])
final_model.fit(X, Y)

# Saving the model
# pickle.dump(final_model, open('voting_clf.pkl', 'wb')) # file size too large

# Saving zipped model
pickle.dump(final_model, bz2.BZ2File("voting_clf",'wb'))
