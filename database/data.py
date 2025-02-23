import sqlite3

def create_database():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            p1 REAL,
            p2 REAL,
            p3 REAL,
            p4 REAL,
            p5 REAL,
            p6 REAL,
            pass_fail TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_database()