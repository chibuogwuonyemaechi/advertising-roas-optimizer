import streamlit as st
import pandas as pd
import joblib

st.title("📊 Advertising ROAS Optimizer")
st.write("Upload campaign data to predict ROAS.")

# Load the trained model
model = joblib.load("models/best_model.pkl")

# Expected columns from training
expected_columns = model.feature_names_in_

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", data.head())

    # --- Preprocessing ---
    # 1. One-hot encode categorical features
    data_processed = pd.get_dummies(data, columns=["audience_segment"])

    # 2. Add any missing columns that were in training
    for col in expected_columns:
        if col not in data_processed.columns:
            data_processed[col] = 0

    # 3. Ensure same column order as training
    data_processed = data_processed[expected_columns]

    # --- Predict ---
    preds = model.predict(data_processed)
    data["Predicted_ROAS"] = preds

    st.write("### Predictions", data)

    # Download button
    st.download_button(
        label="Download Predictions",
        data=data.to_csv(index=False),
        file_name="predictions.csv",
        mime="text/csv"
    )
