import sqlite3

with sqlite3.connect('my_bd.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    login TEXT,
    email TEXT,
    register_date DATE
    )''')

    cur.execute('''INSERT INTO users (
    first_name,
    last_name,
    gender,
    login,
    email,
    register_date
    ) VALUES
('Aleksei', 'Podilo', 'male', 'aleksei_podilo', 'aleksei_podilo@gmail.com', '2022-12-25'),
('Tanja', 'Podilo', 'female', 'tanja_podilo', 'tanja_podilo@gmail.com', '2022-12-26'),
('Alex', 'Podilo', 'male', 'alex_podilo', 'alex_podilo@gmail.com', '2022-12-27')
    ''')