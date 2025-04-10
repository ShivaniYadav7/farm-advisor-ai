import os
from flask import Flask, render_template, request
from agents.farm_data_analyst import FarmDataAnalyst
from agents.market_trend_advisor import MarketTrendAdvisor
from agents.weather_impact_analyst import WeatherImpactAnalyst

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        farm_id = int(request.form['farm_id'])

        # Run all agents
        farm_agent = FarmDataAnalyst()
        farm_result = farm_agent.analyze(farm_id)

        market_agent = MarketTrendAdvisor()
        market_result = market_agent.get_trend()

        weather_agent = WeatherImpactAnalyst()
        weather_result = weather_agent.analyze_weather_impact(farm_id)

        result = {
            "farm": farm_result,
            "market": market_result,
            "weather": weather_result
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

