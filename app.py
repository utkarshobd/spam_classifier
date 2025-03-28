import streamlit as st
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))  # Load the vectorizer used during training

# Streamlit app
st.title("Spam Mail Checker")

# Input text box for the user to enter an email
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
            if prediction[0] ==0:  # Assuming 1 = Spam, 0 = Not Spam
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
            st.error(f"An error occurred: {e}")