import sqlite3
import os

class MarketTrendAdvisor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.abspath(os.path.join(base_dir, '..', 'data', 'market_insights.db'))

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"❌ Database file not found at: {db_path}")

        self.conn = sqlite3.connect(db_path)

    def get_trend(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT product, price, demand, supply FROM market_data LIMIT 3")
        data = cursor.fetchall()
        return [f"{row[0]} | ₹{row[1]} | Demand: {row[2]} | Supply: {row[3]}" for row in data]
