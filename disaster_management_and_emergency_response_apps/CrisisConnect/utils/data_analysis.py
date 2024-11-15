import pandas as pd

def analyze_incident_data(incidents```python
):
    df = pd.DataFrame(incidents)
    summary = df.describe()
    return summary
