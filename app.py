# import libraries
import streamlit as st
import pandas as pd
import bz2
import _pickle as cPickle

st.header("Water Potability Prediction App")
st.write("This app predicts whether the water sample is potable or not!")
st.write("Data was provided [by Aditya Kadiwal on Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability).",unsafe_allow_html=True)

st.image("https://images.pexels.com/photos/372882/pexels-photo-372882.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

def user_input():
    ph = st.number_input(label="pH Value", min_value=0.0, max_value=14.0, value=7.04, step=1e-12, format="%.6f")
    hardness = st.number_input(label="Hardness", min_value=47.0, max_value=325.0, value=196.97, step=1e-12, format="%.6f")
    solids = st.number_input(label="Solids", min_value=320.0, max_value=61230.0, value=20927.83, step=1e-12, format="%.6f")
    chloramines = st.number_input(label="Chloramines", min_value=0.0, max_value=14.00, value=7.13, step=1e-12, format="%.6f")
    sulfate = st.number_input(label="Sulfate", min_value=120.0, max_value=482.0, value=333.07, step=1e-12, format="%.6f")

    inputs = pd.DataFrame({'ph': [ph],
                           'hardness': [hardness],
                           'solids': [solids],
                           'chloramines': [chloramines],
                           'sulfate': [sulfate]}, index=[0])
    return inputs

input_df = user_input()

# Load saved classification model
# model = pickle.load(open('voting_clf.pkl', 'rb'))
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data
model = decompress_pickle('voting_clf')

# Apply model to make predictions
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
if prediction == 1:
    st.success('The Water Sample Is Potable')
elif prediction == 0:
    st.success('The Water Sample Is Not Potable')

st.subheader('Prediction Probability')
st.write(prediction_proba)
