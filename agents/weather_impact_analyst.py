# agents/weather_impact_analyst.py

import pandas as pd
import os

class WeatherImpactAnalyst:
    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(project_root, "data", "farmer_advisor_dataset.csv")  # ✅ fixed name
        self.df = pd.read_csv(self.data_path)

    def analyze_weather_impact(self, farm_id: int):
        farm_data = self.df[self.df['Farm_ID'] == farm_id]

        if farm_data.empty:
            return f"🚫 No farm found with ID {farm_id}."

        temp = farm_data['Temperature_C'].values[0]
        rain = farm_data['Rainfall_mm'].values[0]

        insights = []

        if temp > 35:
            insights.append("🔥 High temperature may reduce crop yield. Consider heat-resilient crops.")
        elif temp < 15:
            insights.append("❄️ Low temperature might stunt crop growth. Consider insulation or delayed sowing.")
        else:
            insights.append("🌤️ Temperature is optimal for most crops.")

        if rain < 50:
            insights.append("💧 Low rainfall detected. Consider drip irrigation or drought-tolerant crops.")
        elif rain > 200:
            insights.append("🌊 Excess rainfall risk. Ensure proper drainage and disease control.")
        else:
            insights.append("🌦️ Rainfall is within normal range for crop growth.")

        return {
            "Farm ID": farm_id,
            "Weather Impact Insights": insights
        }
