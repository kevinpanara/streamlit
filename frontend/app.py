import streamlit as st
import requests

st.title("Streamlit Frontend")

if st.button('Get Data from Flask'):
    response = requests.get('http://localhost:5000/api/data')
    if response.status_code == 200:
        data = response.json()
        st.write(data['message'])
    else:
        st.write("Failed to get data from Flask")
