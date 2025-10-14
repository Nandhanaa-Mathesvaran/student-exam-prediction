import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("trained_model.sav", "rb"))

st.title("Student Math Score Prediction App")
st.write("Predict a student's Math Score based on their attributes.")

race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
gender = st.selectbox("Gender", ["male", "female"])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["completed", "none"])
parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "associate's degree",
        "some college",
        "bachelor's degree",
        "master's degree"
    ]
)

gender_num = 1 if gender == "male" else 0
lunch_num = 1 if lunch == "standard" else 0
test_prep_num = 1 if test_prep == "completed" else 0

parent_edu_map = {
    "some high school": 1,
    "high school": 2,
    "associate's degree": 3,
    "some college": 4,
    "bachelor's degree": 5,
    "master's degree": 6
}
parent_edu_num = parent_edu_map[parent_edu]

race_columns = ["race_group B", "race_group C", "race_group D", "race_group E"]
race_dummies = pd.DataFrame(0, index=[0], columns=race_columns)
if race != "group A":
    race_column = f"race_{race}"
    race_dummies[race_column] = 1

input_data = pd.concat([race_dummies, pd.DataFrame({
    "gender_num": [gender_num],
    "lunch_num": [lunch_num],
    "test_prep_num": [test_prep_num],
    "parent_edu_num": [parent_edu_num]
})], axis=1)

if st.button("Predict Math Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Math Score: {prediction:.2f}")
