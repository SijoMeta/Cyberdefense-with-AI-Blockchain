# AI-Powered Cyber Defense with Blockchain  

This project is an AI-powered cybersecurity system that detects network intrusions and logs threats securely using blockchain. The AI model analyzes network traffic to identify anomalies, unauthorized access, and bot-like activities. Once a threat is detected, the details are stored in a tamper-proof blockchain ledger for future reference and security audits.  

## How It Works  
1. The system processes network traffic data using a machine learning model trained on the CICIDS2017 dataset.  
2. It detects suspicious activities based on various network parameters.  
3. If an attack is identified, the system records the event securely on a blockchain, preventing any modifications.  

## Files and Folders  
- `data/` → Contains the network traffic dataset.  
- `models/` → Stores the trained AI model.  
- `train_model.py` → Trains the AI model on network traffic data.  
- `detect_intrusion.py` → Runs real-time intrusion detection.  
- `blockchain_store.py` → Saves detected threats to a blockchain ledger.  
- `requirements.txt` → Lists all necessary dependencies.  

## How to Use  
1. Install the required libraries using `pip install -r requirements.txt`.  
2. Train the AI model by running `python train_model.py`.  
3. Start real-time intrusion detection with `python detect_intrusion.py`.  
4. Log detected threats into the blockchain using `python blockchain_store.py`.  

This project enhances cybersecurity by combining AI-driven threat detection with blockchain’s security and transparency.  
