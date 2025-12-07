import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(path):
    """CSV dosyasını yükler."""
    df = pd.read_csv(path)
    return df

def rename_columns(df):
    """Sütun isimlerini kısaltır."""
    df.rename(columns={'Annual Income (k$)': 'income'}, inplace=True)
    df.rename(columns={'Spending Score (1-100)': 'score'}, inplace=True)
    return df

def normalize_data(df):
    """Veriyi MinMaxScaler ile normalize eder."""
    scaler = MinMaxScaler()
    
    scaler.fit(df[['income']])
    df['income'] = scaler.transform(df[['income']])
    
    scaler.fit(df[['score']])
    df['score'] = scaler.transform(df[['score']])
    
    return df

def prepare_data(path):
    """Veriyi yükler, düzenler ve normalize eder."""
    df = load_data(path)
    df = rename_columns(df)
    df = normalize_data(df)
    return df
