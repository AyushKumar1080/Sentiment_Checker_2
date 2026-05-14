import numpy as np
import joblib
import pandas as pd
from utils import clean_text,stop_words

model=joblib.load('models/sentiment_model.pkl')
vectorizer=joblib.load('models/tfidf_vectorizer.pkl')

times=int(input("How many times you want to test the sentiment analysis: "))

for _ in range(times):
    text_input=input("Enter your sentence: ")

    cleaned_text=clean_text(text_input)

    text_vectorized=vectorizer.transform([cleaned_text])

    prediction=model.predict(text_vectorized)

    print("This is a positive sentence." if prediction[0] == 1 else "This is a negative sentence.")
    
