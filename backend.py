import pandas as pd
import numpy as np
from fastapi import FastAPI
from utils import clean_text,stop_words
import joblib

app = FastAPI()

model=joblib.load('models/sentiment_model.pkl')
vectorizer=joblib.load('models/tfidf_vectorizer.pkl')

@app.get('/')
def home():
    return {"message": "Sentiment Analysis API is running!"}

@app.post('/predict')
def sentiment_predict(text: str):
    cleaned_text=clean_text(text)
    
    text_vector=vectorizer.transform([cleaned_text])
    
    prediction=model.predict(text_vector)
    
    sentiment = "This is a positive sentence" if prediction[0]==1 else "This is a negative sentence"
    return {"sentiment" : sentiment}
    
    
    