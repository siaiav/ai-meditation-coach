import streamlit as st
from transformers import pipeline
import pandas as pd
from datetime import datetime
import os

# Load model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", 
                   model="google/flan-t5-base")

model = load_model()

# Mood check-in
mood = st.slider("Mood (1-5)", 1, 5)
stress = st.slider("Stress (1-5)", 1, 5)

if st.button("Start Meditation"):
    prompt = f"Create a 3-minute guided meditation for someone feeling mood:{mood}, stress:{stress}. Short sentences, calming."
    script = model(prompt, max_length=200)[0]['generated_text']
    
    st.markdown("###  Your Session")
    st.write(script)
    
    # Log session
    log_data = {
        'timestamp': datetime.now(),
        'mood': mood,
        'stress': stress,
        'script': script[:100]
    }
    df = pd.read_csv('data/session_logs.csv') if os.path.exists('data/session_logs.csv') else pd.DataFrame()
    df = pd.concat([df, pd.DataFrame([log_data])], ignore_index=True)
    df.to_csv('data/session_logs.csv', index=False)
