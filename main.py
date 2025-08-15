import streamlit as st

st.title("Brand Name Generator")

# Get user inputs
city_name = st.text_input("Please enter your city name")
pet_name = st.text_input('Please enter your "pet" name')

# Show result when both inputs are given
if city_name and pet_name:
    st.subheader("Your brand name is:")
    st.success(f"{city_name} {pet_name}!")
