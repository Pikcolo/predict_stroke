import os
import numpy
import joblib

def load_scaler_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(
        base_dir, "../utils/scaler_model/scaler.pkl"
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    
    scaler = joblib.load(model_path)
    print(f"\n... Complete loaded model ...")
    print(f"Model loaded from: {model_path}")
    return scaler