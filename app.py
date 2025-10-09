import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("trained_model.sav", "rb"))

st.title("Student Math Score Prediction App")

st.write("Predict a student's Math Score based on their attributes.")

reading = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
writing = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["completed", "none"])
parent_edu = st.selectbox(
    "Parental Level of Education",
    ["some high school", "high school", "associate's degree", "bachelor's degree", "master's degree"]
)

lunch_num = 1 if lunch == "standard" else 0
test_prep_num = 1 if test_prep == "completed" else 0

parent_edu_map = {
    "some high school": 1,
    "high school": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}
parent_edu_num = parent_edu_map[parent_edu]

input_data = pd.DataFrame({
    "reading score": [reading],
    "writing score": [writing],
    "lunch_num": [lunch_num],
    "test_prep_num": [test_prep_num],
    "parent_edu_num": [parent_edu_num]
})

if st.button("Predict Math Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Math Score: {prediction:.2f}")
