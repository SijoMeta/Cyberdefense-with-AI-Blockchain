# AI-Powered Intrusion Detection System with Blockchain Integration  

## Content:  
1. **Project Overview**  
   - AI-based network intrusion detection  
   - Blockchain for secure attack logging  

2. **Dataset**  
   - CICIDS2017 (Intrusion Detection Dataset)  
   - Includes IPs, Ports, Protocols, Flow Duration, Packet Lengths, TCP Flags, and Labels  

3. **Project Structure**  
   - `data/` → Contains dataset files  
   - `models/` → Trained ML models  
   - `blockchain/` → Smart contract & transactions  
   - `scripts/` → ML training & detection scripts  
   - `train_model.py` → Train AI model  
   - `detect_intrusion.py` → Run real-time detection  
   - `blockchain_store.py` → Log attack events on blockchain  
   - `requirements.txt` → List of dependencies  

4. **Installation & Usage**  
   - Install dependencies: `pip install -r requirements.txt`  
   - Train model: `python train_model.py`  
   - Run detection: `python detect_intrusion.py`  
   - Store alerts on blockchain: `python blockchain_store.py`  

5. **Future Enhancements**  
   - Improve model accuracy  
   - Real-time dashboard  
   - Smart contract-based security alerts  

6. **License**  
   - Open-source under MIT License  
