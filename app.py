# the dashboard

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# setup the page look
st.set_page_config(page_title="Car Price Predictor", layout="wide")
st.title("Car Price Prediction Dashboard")

# load data but cache it so it dont lag every time we click something
@st.cache_data
def load_data():
    return pd.read_csv('car_price_prediction_.csv')

df = load_data()

# let user see the table if they want
if st.checkbox('Show Raw Data'):
    st.write(df.head(10))

# eda part starts here
st.header("Exploratory Data Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Price'], kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Mileage vs Price")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['Mileage'], y=df['Price'], ax=ax)
    st.pyplot(fig)

# this part handles the modeling logic inside the app
st.header("Linear Regression Modeling")

# basic cleaning so the model works
df_ml = pd.get_dummies(df.drop(['Car ID', 'Model'], axis=1), drop_first=True)
X = df_ml.drop('Price', axis=1)
y = df_ml['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# show the accuracy to the user
r2 = r2_score(y_test, y_pred)
st.success(f"Model Accuracy (R² Score): {r2:.4f}")

# a tool for user to play with and predict prices
st.subheader("Predict a Car Price")
user_mileage = st.slider("Select Mileage", int(df.Mileage.min()), int(df.Mileage.max()), 50000)

# simple math to show a prediction based on mileage
# i used the mileage coefficient for this part
base_price = model.intercept_
mileage_coef = model.coef_[0] 
predicted_price = base_price + (mileage_coef * user_mileage)
st.metric("Estimated Price", f"${predicted_price:,.2f}")