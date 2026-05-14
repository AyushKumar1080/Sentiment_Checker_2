import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)

# Title
st.title("Twitter Sentiment Analysis")

# Subtitle
st.write("Enter a tweet or sentence to predict sentiment")

# User input
text = st.text_area(
    "Enter Text",
    height=150
)

# Predict button
if st.button("Predict Sentiment"):

    # Check empty input
    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        try:

            # Send request to FastAPI
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                params={"text": text}
            )

            # Convert response to JSON
            result = response.json()

            # Display result
            sentiment = result["sentiment"]

            if "positive" in sentiment.lower():
                st.success(sentiment)

            else:
                st.error(sentiment)

        except Exception as e:

            st.error("FastAPI server is not running.")
            st.write(e)