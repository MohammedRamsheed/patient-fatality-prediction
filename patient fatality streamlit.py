import joblib
import streamlit as st

# Define the app layout and interaction here

if __name__ == '__main__':
    st.title("Patient Fatality Prediction")
    # ... Define your Streamlit app content here

import sklearn

# Load the saved machine learning model
model = joblib.load(r"C:\Users\HP\Desktop\PROJECT LUMINAR\PATIENT FATALITY\patient fatality project11 (1).sav")


# Define the list of input parameters
parameters = ['age', 'gcs_eyes_apache', 'gcs_motor_apache', 'gcs_verbal_apache',
              'heart_rate_apache', 'intubated_apache', 'temp_apache',
              'ventilated_apache', 'd1_diasbp_min', 'd1_diasbp_noninvasive_min',
              'd1_heartrate_max', 'd1_mbp_min', 'd1_mbp_noninvasive_min',
              'd1_resprate_max', 'd1_spo2_min', 'd1_sysbp_min',
              'd1_sysbp_noninvasive_min', 'd1_temp_min', 'h1_diasbp_min',
              'h1_diasbp_noninvasive_min', 'h1_heartrate_max', 'h1_mbp_min',
              'h1_mbp_noninvasive_min', 'h1_resprate_max', 'h1_resprate_min',
              'h1_spo2_min', 'h1_sysbp_min', 'h1_sysbp_noninvasive_min',
              'd1_potassium_max', 'apache_4a_hospital_death_prob',
              'apache_4a_icu_death_prob']


# Create input fields for user to enter parameters
parameter_values = []
for parameter in parameters:
    user_input = st.number_input(f"Enter the {parameter}:", value=0.0)
    parameter_values.append(user_input)

# Create a button to trigger the prediction
if st.button("Predict"):
    # Predict using the loaded model
    y_pred_rf = model.predict([parameter_values])

    # Display the prediction result
    if y_pred_rf == 0:
        st.write("There is no need to worry, recovery is imminent")
    else:
        st.write("The chance of death is high")
