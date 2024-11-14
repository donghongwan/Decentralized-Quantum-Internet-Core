import pandas as pd

class AnalyticsUtil:
    def analyze_voter_data(self, data):
        # Logic to analyze voter data
        df = pd.DataFrame(data)
        return df.describe()
