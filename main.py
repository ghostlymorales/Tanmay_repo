import streamlit as st

st.title("💰 Tip Calculator")

# Inputs
amount = st.number_input("What was the net amount?", min_value=0.0, step=0.01)
tip_percent = st.slider("How much tip would you like to give? (%)", 0, 100, 10)
people = st.number_input("How many people to split the bill?", min_value=1, step=1, value=1)

# Calculation
if amount > 0 and people > 0:
    tip_amount = (tip_percent / 100) * amount
    total = amount + tip_amount
    per_person = total / people

    st.success(f"Each person has to pay: **${per_person:.2f}**")

st.write("🙏 THANK YOU :)")
