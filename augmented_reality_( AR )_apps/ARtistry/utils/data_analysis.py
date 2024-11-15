import pandas as pd

def analyze_user_data(user_data):
    df = pd.DataFrame(user_data)
    return df.describe()
