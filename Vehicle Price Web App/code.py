import pickle
import streamlit as st
from streamlit_option_menu import option_menu

car_model = pickle.load(open('car_prediction.sav', 'rb'))
bike_model = pickle.load(open('bike_prediction.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Vehicle Price Prediction',
                           ['Car Price Prediction',
                            'Bike Price Prediction'],
                           icons=['car-front', 'bicycle'], default_index=0)

if selected == 'Car Price Prediction':
    st.title('Enter Details to Prediction Your Car Price')

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input('Model Year')

    with col2:
        price = st.number_input('Ex Showroom Price in Lakhs')
        price = float(price)

    with col1:
        driven = st.number_input('Driven in Kms')

    with col2:
        fuel_type = st.text_input('Fuel Type', value='Diesel/Petrol/CNG')
        if fuel_type.lower() == 'diesel':
            fuel_type = 0
        elif fuel_type.lower() == 'cng':
            fuel_type = 2
        else:
            fuel_type = 1

    with col1:
        seller = st.text_input('Seller Type', value='Individual/ Dealer')
        if seller.lower() == 'dealer':
            seller = 1
        else:
            seller = 0

    with col2:
        transmission = st.text_input('Transmission Type', value='Manual/Automatic')
        if transmission.lower() == 'automatic':
            transmission = 1
        else:
            transmission = 0

    with col1:
        owner = st.number_input('Number of Owners')

    car_price_prediction = ''

    if st.button('Price'):
        car_price_prediction = car_model.predict([[year, price, driven, fuel_type, seller, transmission, owner]])
    st.success(car_price_prediction)

if selected == 'Bike Price Prediction':
    st.title('Enter Details to Prediction Your Bike Price')

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input('Model Year')

    with col2:
        seller_type = st.text_input('Seller Type', value='Individual/ Dealer')
        if seller_type.lower() == 'dealer':
            seller_type = 1
        else:
            seller_type = 0

    with col1:
        owner = st.number_input('Number of Owners')

    with col2:
        driven = st.number_input('Driven in kms')

    with col1:
        price = st.number_input('Ex Showroom price')

    bike_price_prediction = ''

    if st.button('Price'):
        bike_price_prediction = bike_model.predict([[year, seller_type, owner, driven, price]])
    st.success(bike_price_prediction)
