import streamlit as st

# Title
st.title("💰 Tip Calculator")

st.write("Welcome to Tip Calculator! Please enter the details below:")

# Inputs
a1 = st.number_input("What was the net amount?", min_value=0.0, format="%.2f")
a2 = st.number_input("How much tip would you like to give? (%)", min_value=0.0, format="%.1f")
a3 = st.number_input("How many people to split the bill?", min_value=1, step=1)

# Calculate only if inputs are given
if a1 > 0:
    # Tip calculation
    a2_1 = a2 / 100
    a2_3 = a2_1 * 100
    a2_4 = int(a2_3) + int(a1)

    # Split among people
    a4 = a2_4 / a3
    a5 = f"{a4:.3f}"

    st.success(f"Each person has to pay: **{a5} $** 💵")

st.write("---")
st.write("THANK YOU 🙂")
