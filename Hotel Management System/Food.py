import sqlite3

def start():
    global conn,cursor
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS FOOD(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            PRICE REAL NOT NULL
        );""")

def add_food(food_name,food_price):
    cursor.execute(f"INSERT INTO FOOD (NAME,PRICE) VALUES('{food_name}','{food_price}')")
    conn.commit()

def show_all(food_only=False):
    a = "NAME" if food_only else "*"
    cursor.execute(f"SELECT {a} FROM FOOD")
    records = cursor.fetchall()
    return records

def close():
    conn.close()
    cursor.close()