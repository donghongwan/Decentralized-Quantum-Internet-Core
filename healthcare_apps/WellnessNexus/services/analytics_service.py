import pandas as pd

class AnalyticsService:
    def analyze_wellness(self, user):
        # Logic to analyze overall wellness data
        fitness_df = pd.DataFrame(user.fitness_data)
        nutrition_df = pd.DataFrame(user.nutrition_data)
        mental_health_df = pd.DataFrame(user.mental_health_data)
        # Combine and analyze data
        return {
            "fitness": fitness_df.describe(),
            "nutrition": nutrition_df.describe(),
            "mental_health": mental_health_df.describe()
        }
