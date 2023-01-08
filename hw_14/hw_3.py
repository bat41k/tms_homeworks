import sqlite3

with sqlite3.connect('my_bd.db') as con:
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date_create DATE,
        content TEXT(140),
        post_author_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        post_category_id INTEGER REFERENCES category(category_id) ON DELETE SET NULL
        )
        ''')

    cur.execute('''
        INSERT INTO posts (
        title,
        date_create,
        content,
        post_author_id,
        post_category_id
        ) VALUES
        ('What is sport?', '2022-12-25', 'Sport pertains to any form of competitive physical activity or game that aims\
        to use, maintain, or improve physical ability and skills...', 1, 1),
        ('What is fashion?', '2022-12-26', 'Fashion is a form of self-expression and autonomy at a particular period\
        and place and in a specific context, of clothing, footwear...', 2, 2),
        ('What is food?', '2022-12-27', 'Food is any substance consumed by an organism for nutritional support. Food is\
        usually of plant, animal, or fungal origin, and contains...', 3, 3)
        ''')