import numpy as np
import joblib
import streamlit as st

# Loading the saved model
loaded_model = joblib.load("C:/salman/ML/Parkinson's Disease Detection/model.joblib")  # Replace 'your_model_filename.joblib' with your actual model file

# Creating a function for prediction
def parkinsons_prediction(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person may not have Parkinson\'s disease'
    else:
        return 'The person may have Parkinson\'s disease'

def main():
    # Giving a title
    st.title('Parkinson\'s Disease Prediction Web App')

    # Getting the input data from the user
    fo_hz = st.text_input('MDVP:Fo(Hz)')
    fhi_hz = st.text_input('MDVP:Fhi(Hz)')
    flo_hz = st.text_input('MDVP:Flo(Hz)')
    jitter_percent = st.text_input('MDVP:Jitter(%)')
    jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    rap = st.text_input('MDVP:RAP')
    ppq = st.text_input('MDVP:PPQ')
    jitter_ddp = st.text_input('Jitter:DDP')
    shimmer = st.text_input('MDVP:Shimmer')
    shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    shimmer_apq3 = st.text_input('Shimmer:APQ3')
    shimmer_apq5 = st.text_input('Shimmer:APQ5')
    apq = st.text_input('MDVP:APQ')
    shimmer_dda = st.text_input('Shimmer:DDA')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button('Parkinson\'s Test Result'):
        input_params = [
            fo_hz, fhi_hz, flo_hz, jitter_percent, jitter_abs, rap, ppq, jitter_ddp,
            shimmer, shimmer_db, shimmer_apq3, shimmer_apq5, apq, shimmer_dda,
            nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe
        ]
        diagnosis = parkinsons_prediction(input_params)

    st.success(diagnosis)

if __name__ == '__main__':
    main()
