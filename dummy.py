import sqlite3

conn = sqlite3.connect('data/market_insights.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS market_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    price REAL,
    demand REAL,
    supply REAL
)
''')

# Insert dummy data
cursor.executemany('''
INSERT INTO market_data (product, price, demand, supply)
VALUES (?, ?, ?, ?)
''', [
    ('Wheat', 25.5, 80, 70),
    ('Rice', 32.0, 90, 85),
    ('Corn', 20.0, 60, 75)
])

conn.commit()
conn.close()
