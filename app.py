
import streamlit as st
import pandas as pd
import joblib

# --- 1. Load Model ---
# Load the model file
@st.cache_data  # Cache the model load
def load_model():
    try:
        model = joblib.load('model.pkl')
        return model
    except FileNotFoundError:
        return None

model = load_model()

# --- 2. Set Up Page ---
st.set_page_config(page_title="Wine Quality Predictor", layout="wide")
st.title('🍷 Wine Quality Prediction App')

# Check if model is loaded
if model is None:
    st.error("Model file 'model.pkl' not found. Please upload it to the Colab environment.")
else:
    st.success("Model loaded successfully. You can now make predictions!")

    # --- 3. Create UI (Sliders in Sidebar) ---
    st.sidebar.header('Input Wine Features:')
    
    # Get feature names from the model (assuming it's a scikit-learn pipeline/model)
    # HACK: For this specific app, we know the wine features. 
    # Let's manually define them.
    
    # Example features (replace with your actual features from your notebook)
    fixed_acidity = st.sidebar.slider('Fixed Acidity', min_value=4.0, max_value=16.0, value=7.4, step=0.1)
    volatile_acidity = st.sidebar.slider('Volatile Acidity', min_value=0.1, max_value=2.0, value=0.7, step=0.01)
    citric_acid = st.sidebar.slider('Citric Acid', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    residual_sugar = st.sidebar.slider('Residual Sugar', min_value=0.9, max_value=16.0, value=1.9, step=0.1)
    chlorides = st.sidebar.slider('Chlorides', min_value=0.01, max_value=0.7, value=0.076, step=0.001)
    free_sulfur_dioxide = st.sidebar.slider('Free Sulfur Dioxide', min_value=1.0, max_value=72.0, value=11.0, step=1.0)
    total_sulfur_dioxide = st.sidebar.slider('Total Sulfur Dioxide', min_value=6.0, max_value=289.0, value=34.0, step=1.0)
    density = st.sidebar.slider('Density', min_value=0.99, max_value=1.01, value=0.9978, step=0.0001, format="%.4f")
    pH = st.sidebar.slider('pH', min_value=2.7, max_value=4.1, value=3.51, step=0.01)
    sulphates = st.sidebar.slider('Sulphates', min_value=0.3, max_value=2.1, value=0.56, step=0.01)
    alcohol = st.sidebar.slider('Alcohol', min_value=8.4, max_value=15.0, value=9.4, step=0.1)

    # --- 4. Prediction Logic ---
    if st.sidebar.button('Predict Quality'):
        # Create a DataFrame from the inputs
        # IMPORTANT: The column order MUST match the order your model was trained on
        input_data = pd.DataFrame(
            [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
              chlorides, free_sulfur_dioxide, total_sulfur_dioxide, 
              density, pH, sulphates, alcohol]],
            columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 
                     'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 
                     'density', 'pH', 'sulphates', 'alcohol']
           
        )
        
        # Make prediction
        prediction = model.predict(input_data)
        predicted_quality = prediction[0]
        
        st.subheader(f'Predicted Wine Quality: {predicted_quality}')
        if predicted_quality >= 7:
            st.success("This is a high-quality wine! 🌟")
        elif predicted_quality >= 5:
            st.warning("This is an average-quality wine. 😐")
        else:
            st.error("This is a low-quality wine. 👎")
