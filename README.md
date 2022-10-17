# Water Potability Prediction 💦💧
Click to <a href="https://jadanpl-water-potability-prediction-app-mvo09g.streamlitapp.com/" target="_blank"><img src="https://camo.githubusercontent.com/767be70c92254555bd347ab07908fec67854c2264b77702581bd230fd7eac54f/68747470733a2f2f7374617469632e73747265616d6c69742e696f2f6261646765732f73747265616d6c69745f62616467655f626c61636b5f77686974652e737667" width="180"></a> and interact with the application. 🥂

## Problem Statement
Water is used to carry out activities such as dehydration, cleaning and food production. Well-mainteained water resources can boost countries’ economic growth (to be used in production or agriculture activities) and can reduce poverty rate. In contrast, contaminated water are often associated with the transmission of diseases such as cholera, diarrhoea, and hepatitis A. Lack of clean water resources could put both the patients and health care workers at additional risk of being infected by viruses.

## Main Objective 
To predict if each water sample is potable or not potable. (Binary Classification)

## Dataset Descriptions 
🌟The dataset is provided by <a href="https://www.kaggle.com/datasets/adityakadiwal/water-potability">Aditya Kadiwal on Kaggle</a>.
* ph:  Water pH level (0 to 14).
* Hardness: Capacity of water to precipitate soap in mg/L.
* Solids: Total dissolved solids in ppm.
* Chloramines: Amount of Chloramines in ppm.
* Sulfate: Amount of Sulfates dissolved in mg/L.
* Conductivity: Electrical conductivity of water in μS/cm.
* Organic_carbon: Amount of organic carbon in ppm.
* Trihalomethanes: Amount of Trihalomethanes in μg/L.
* Turbidity: Measure of light emiting property of water in NTU.
* Potability: Indicates if water is safe for human consumption. Potable = 1 and Not potable = 0

## Result
* 5 classifiers were sorted out based on their accuracy on the testing data. They are then further tuned. After that, 3 of these tuned classifiers (random forest, extra trees and SVC) were used to build a voting classifier that can achieve an accuracy of 69.11% on the testing data. This accuracy is higher than the accuracy of any other models built.
* The final model is deployed and is accessible on Streamlit. 

## Recommendations
* There are many other algorithms that could be tried out with this dataset, such as CatBoost Classifier and Light Gradient Boosting Machine.
* Tune the selected individual models with different hyperparameters.

