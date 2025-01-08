# Parkinson's Disease Prediction Web App

This Python script is a web application designed to predict whether an individual may have Parkinson's disease or not based on certain voice-related features. It utilizes a pre-trained machine learning model to make predictions.


## Dataset

- **Dataset Name**: Parkinson's Disease Prediction
- **Data Source**: data upload on git

## Project Structure

- **README.md**: Documentation of the project.
- **main.py**: Python script for the Parkinson's Disease Prediction Web App.
- **model.joblib**: Pre-trained machine learning model for Parkinson's disease prediction.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd parkinsons-prediction


2. Create a virtual environment (recommended) and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use: venv\Scripts\activate


## Usage
-Clone this repository to your local machine.

-Ensure you have the pre-trained machine learning model ('model.joblib') in the same directory as the script ('main.py').

-Open a command prompt or terminal and navigate to the directory where the script is located.

-Run the script using Streamlit:
    `streamlit run main.py`

-Access the web application in your browser and enter the voice-related features to get the prediction result.

## Model Information
The project uses a machine learning model trained to classify individuals into two classes: potential Parkinson's disease or no Parkinson's disease. The pre-trained model is saved as 'model.joblib'.

## Input Features
The input features required for prediction include:

-MDVP:Fo(Hz)

-MDVP:Fhi(Hz)

-MDVP:Flo(Hz)

-MDVP:Jitter(%)

-MDVP:Jitter(Abs)
...

-Results
The web application provides a prediction for Parkinson's disease based on the input voice-related features.

## Future Improvements
There are several ways to enhance the project:

-Explore more advanced machine learning techniques.

-Collect more data to improve model accuracy.

-Enhance the user interface for a better user experience.


## References

- Author: Muhammad Mubashir Ali
- Contact: muhammadmubashirali63@gmail.com

Feel free to customize this README to include any additional information you want to provide about the project.

