# main.py
from agents.farm_data_analyst import FarmDataAnalyst
from agents.market_trend_advisor import MarketTrendAdvisor  # <-- new
from agents.weather_impact_analyst import WeatherImpactAnalyst  # New agent


def main():
    farm_id = int(input("🔢 Enter Farm ID to analyze: "))

    # FarmerAdvisor
    farm_agent = FarmDataAnalyst()
    farm_result = farm_agent.analyze(farm_id)
    print("\n📊 Farm Data Analyst Output:")
    print(farm_result)

    # MarketTrendAdvisor
    market_agent = MarketTrendAdvisor()
    print("\n💹 Market Trend Advisor Recommendations:")
    for trend in market_agent.get_trend():
        print(trend)

    # WeatherImpactAnalyst
    weather_agent = WeatherImpactAnalyst()
    print("\n🌤️ Weather Impact Analyst Report:")
    weather_result = weather_agent.analyze_weather_impact(farm_id)  
    print(weather_result)

if __name__ == "__main__":
    main()
