import streamlit as st

st.title("💰 Tip Calculator")

# Inputs
amount = st.number_input("What was the net amount?", min_value=0.0, step=0.01)
tip = st.number_input("How much tip would you like to give? (just a number, not %)", min_value=0.0, step=0.01)
people = st.number_input("How many people to split the bill?", min_value=1, step=1, value=1)

# Calculation (same logic as your original script)
if amount > 0 and people > 0:
    total = amount + tip
    per_person = total / people
    st.success(f"Each person has to pay: **${per_person:.2f}**")

st.write("🙏 THANK YOU :)")
