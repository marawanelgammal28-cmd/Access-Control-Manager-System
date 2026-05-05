import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Path Traversal Attack Detection")

st.write("Enter a URL or file path to check for vulnerability.")

url = st.text_input("Enter path:")

def extract_features(text):
    return pd.DataFrame([{
        "has_dotdot": int("../" in text),
        "num_slashes": text.count("/"),
        "length": len(text),
        "has_sensitive": int("etc" in text or "passwd" in text or "shadow" in text)
    }])

if st.button("Check"):
    features = extract_features(url)
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Path Traversal Attack Detected")
    else:
        st.success("✅ Safe Input")