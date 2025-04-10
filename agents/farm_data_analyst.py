class FarmDataAnalyst:
    def analyze(self, farm_id):
        # Dummy sustainability score based on input
        score = 50 + farm_id * 0.3
        suggestions = [
            "🌱 Reduce fertilizer usage to improve sustainability.",
            "🐞 Switch to eco-friendly pest control methods.",
            "💧 Increase irrigation or use water-retentive crops."
        ]
        return {
            "Farm ID": farm_id,
            "Sustainability Score": score,
            "Suggestions": suggestions
        }
