
# importing required libraries
import pickle
import streamlit as st
# import joblib
from io import BytesIO

import requests # or https

# e.g. a file call stopwords saved by joblib
# https://github.com/Proteusiq/hisia/v1.0.1/hisia/models/data/stops.pkl

# change github.com to raw.githubusercontent.com

# URI = "https://raw.githubusercontent.com/Proteusiq/hisia/v1.0.1/hisia/models/data/stops.pkl"
# STOPWORDS = joblib.load(BytesIO(requests.get(URI).content))
# loading the trained model
URI = 'https://raw.githubusercontent.com/Ninad2603/ML_Projects/raw/main/rf_1.pkl'
pickle_in = open(BytesIO(requests.get(URI).content), 'rb') 
classifier = pickle.load(pickle_in)


# this is the main function in which we define our app
def main():
    # header of the page
    st.markdown("Company Bankrupcy Prediction")

    # 2. Loading the data

    X9  = st.number_input("After-tax net Interest Rate")
    X11 = st.number_input("Continuous interest rate_(after tax)")
    X14 = st.number_input("Cash flow rate")
    X19 = st.number_input("Net Value Per Share (C)")
    X34 = st.number_input("Current Ratio")
    X36 = st.number_input("Interest Expense Ratio")
    X47 = st.number_input("Accounts Receivable Turnover")
    X49 = st.number_input("Inventory Turnover Rate (times)")
    X59 = st.number_input("Quick Assets/Current Liability")
    X95 = st.selectbox('Net Income Flag',("0","1"))

    result =""

    # when 'Check' is clicked, make the prediction and store it
    if st.button("Check"):
        result = prediction([X9, X11, X14, X19, X34, X36, X47, X49, X59, X95])
        st.success('Your loan is {}'.format(result))

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount): 
    # header of the page
    st.markdown("Company Bankruptcy Prediction")

    prediction = classifier.predict([['X9', 'X11', 'X14', 'X19', 'X34', 'X36', 'X47', 'X49', 'X59', 'X95']])
     
    # Get the probability of the positive class (Approved)
    probability_approved = prediction_proba[0, 1]

    # Convert probability to percentage
    confidence_percentage = round(probability_approved * 100, 2)

    return f" Company to get bankrupted is {confidence_percentage} percentage"

if __name__=='__main__':
    main()
