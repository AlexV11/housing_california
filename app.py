import streamlit as st
import pandas as pd
import numpy as np
import prediction
import joblib
from combined_attributes_adder import CombinedAttributesAdder



colh1, colh2 = st.columns(2)
colh1.header('Housing predictions')
colh2.image('California.jpg', width = 200)

col1, col2 = st.columns(2)

longitude = col1.number_input('Longitude', value = -119.56, min_value = -124.0, max_value = -110.0, format = "%.2f")
total_rooms = col1.number_input('Total rooms', value = 2635.0, min_value = 1.0, max_value = 50000.0, format = "%.0f")
median_income = col1.number_input('Median income', value = 3.8706, min_value = 0.0, max_value = 17.0, format = "%.4f")
households = col1.number_input('Households', value = 499.0, min_value = 1.0, max_value = 10000.0, format = "%.0f")
housing_median_age = col1.slider('Housing median age', value = 28.0, step=1.0, min_value=1.0, max_value=100.0, format = "%.0f")

latitude = col2.number_input('Latitude', value = 35.63, min_value = 30.0, max_value = 50.0, format = "%.2f")
total_bedrooms = col2.number_input('Total bedrooms', value = 537.0, min_value = 1.0, max_value = 7000.0, format = "%.0f")
population = col2.number_input('Population', value = 1425.0, min_value = 1.0, max_value = 50000.0, format = "%.0f")
ocean_proximity = col2.selectbox('Ocean proximity', ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])
model = col2.radio(
    'Select the model to use:',
    (
        'Linear regression', 
        'Decision tree regression', 
        'Random forest regression', 
        'Support vector regression'
    )
)

colr1, colr2 = st.columns(2)
if colr1.button('Predict'):
    data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]}
    )

    result = prediction.predict(data, model)
    
    colr1.write('The predicted price is: ${:.2f}'.format(result[0]))

# do a dataframe with lat and long
latlong = pd.DataFrame({
    'longitude': [longitude],
    'latitude': [latitude]
})
colr2.map(latlong, zoom = 7)