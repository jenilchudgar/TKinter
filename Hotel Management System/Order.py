import sqlite3

def start():
    global conn,cursor
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # CREATE TABLE IF NOT EXISTS FOOD
    cursor.execute("""CREATE TABLE IF NOT EXISTS ORDERS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USER TEXT NOT NULL,
            FOOD_ITEMS TEXT NOT NULL
        );""")

def add_food(user,food_items):
    cursor.execute(f"INSERT INTO ORDERS (USER,FOOD_ITEMS) VALUES('{user}','{food_items}')")
    conn.commit()

def show_all():
    cursor.execute("SELECT * FROM ORDERS")
    records = cursor.fetchall()
    return records

def close():
    conn.close()
    cursor.close()

start()