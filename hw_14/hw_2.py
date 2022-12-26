import sqlite3

with sqlite3.connect('my_bd.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_title TEXT
    )''')

    cur.execute('''INSERT INTO category VALUES
    (1, 'Sports'),
    (2, 'Fashion'),
    (3, 'Food')
    ''')