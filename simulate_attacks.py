from detect_attack import detect_attack
from blockchain_integration import store_threat_in_blockchain
import numpy as np

# Simulate a new attack scenario
test_data = np.random.rand(1, 78)  # Simulated network traffic data

# Detect attack
prediction = detect_attack(test_data)

if prediction == "Attack Detected":
    store_threat_in_blockchain("DDoS Attack Detected")
