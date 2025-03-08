import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

def load_and_preprocess_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    
    # Drop irrelevant columns
    columns_to_drop = ["Src IP dec", "Dst IP dec", "Timestamp"]
    df.drop(columns=columns_to_drop, inplace=True, errors="ignore")

    # Handle categorical features
    df = pd.get_dummies(df, columns=["Protocol"], drop_first=True)
    
    # Encode labels
    le = LabelEncoder()
    df["Label"] = le.fit_transform(df["Label"])
    
    # Normalize numerical features
    scaler = StandardScaler()
    feature_columns = [col for col in df.columns if col != "Label"]
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    
    # Split dataset
    X = df.drop(columns=["Label"])
    y = df["Label"]
    
    return X, y, scaler, le

# Save processed data
X, y, scaler, label_encoder = load_and_preprocess_data("../dataset/CICIDS2017.csv")
np.save("../dataset/X.npy", X)
np.save("../dataset/y.npy", y)
