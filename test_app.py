"""
Minimal test app to verify Streamlit Cloud deployment
"""
import streamlit as st

st.set_page_config(page_title="Test App", page_icon="📊")

st.title("✅ Streamlit App Test")
st.success("If you see this, Streamlit is working!")

# Test imports
try:
    import pandas as pd
    import numpy as np
    import plotly.express as px
    st.success("All imports successful!")
except Exception as e:
    st.error(f"Import error: {str(e)}")

# Test data loading
try:
    import os
    if os.path.exists('data/processed/dashboard_metrics.csv'):
        df = pd.read_csv('data/processed/dashboard_metrics.csv')
        st.success(f"Data loaded successfully! Shape: {df.shape}")
        st.dataframe(df.head())
    else:
        st.warning("Data file not found at: data/processed/dashboard_metrics.csv")
except Exception as e:
    st.error(f"Data loading error: {str(e)}")

