import numpy as np
from tensorflow.keras.models import load_model
from preprocess import load_and_preprocess_data

# Load trained model and scaler
model = load_model("../models/intrusion_detection_model.h5")

# Function to detect cyber attacks
def detect_attack(input_data):
    input_data = np.array(input_data).reshape(1, -1)  # Reshape input
    prediction = model.predict(input_data)
    return "Attack Detected" if prediction[0] > 0.5 else "Normal Traffic"

# Example Usage
test_data = np.random.rand(1, 78)  # Simulated data (Replace with real network data)
print(detect_attack(test_data))
