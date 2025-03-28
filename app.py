import streamlit as st
import pickle
import os

# Check if the required files exist
if not os.path.exists('model.pkl') or not os.path.exists('vectorizer.pkl'):
    st.error("Model or Vectorizer files are missing. Please upload them.")
else:
    # Load the trained model and vectorizer
    try:
        model = pickle.load(open('model.pkl', 'rb'))
        vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))  # Load the vectorizer used during training
    except Exception as e:
        st.error(f"Error loading the model or vectorizer: {e}")
    
    # Add custom CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit app
    st.title("Spam Sms Checker")

    # Input text box for the user to enter an SMS
    input_email = st.text_area("Enter the SMS content:")

    if st.button("Check for Spam"):
        if input_email.strip() == "":
            st.warning("Please enter some text to check.")
        else:
            try:
                # Preprocess the input using the vectorizer
                input_feature = vectorizer.transform([input_email])  # Transform the input text to numeric format

                # Predict using the model
                prediction = model.predict(input_feature)

                # Display the result with custom colors
                if prediction[0] == 0:  # Assuming 0 = Not Spam, 1 = Spam
                    st.markdown(
                        "<h3 style='color: darkred;'>This SMS is classified as SPAM.</h3>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<h3 style='color: green;'>This SMS is classified as NOT SPAM.</h3>",
                        unsafe_allow_html=True,
                    )
            except Exception as e:
                st.error(f"An error occurred while predicting: {e}")
