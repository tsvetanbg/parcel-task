import sqlite3

def create_db_if_not_exists():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (timestamp TEXT, x REAL, y REAL, image BLOB)''')
    conn.commit()
    conn.close()

def add_data(timestamp, x, y, img_str):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (timestamp, x, y, image) VALUES (?, ?, ?, ?)", (timestamp, x, y, img_str))
    conn.commit()
    conn.close()
    
def get_data_by_x_and_y(x,y):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE x = ? and y = ? ", (x, y,))
    results = c.fetchall()
    conn.close()
    return results