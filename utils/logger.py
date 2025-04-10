import sqlite3
import os

def log_to_db(agent_name, input_data, output_data):
    os.makedirs("memory", exist_ok=True)
    conn = sqlite3.connect('memory/agent_logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            agent TEXT,
            input TEXT,
            output TEXT
        )
    ''')
    c.execute('INSERT INTO logs VALUES (?, ?, ?)', 
              (agent_name, str(input_data), str(output_data)))
    conn.commit()
    conn.close()
