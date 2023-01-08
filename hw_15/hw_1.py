import sqlite3

with sqlite3.connect('chinook.db') as con:
    cur = con.cursor()

    cur.execute('''
        SELECT SUM(Bytes) as SumBytes FROM tracks
        ''')
    cur.execute('''
        SELECT (SELECT COUNT(EmployeeId) FROM employees) + (SELECT COUNT(CustomerId) FROM customers) as SumEntries
        ''')
    cur.execute('''
        SELECT Name FROM tracks as NameTracks WHERE AlbumID = (SELECT AlbumId FROM albums WHERE Title is 'A-Sides')
        ''')
    cur.execute('''
        SELECT Title as AlbumName, SUM(UnitPrice) as AlbumPrice
        FROM albums
        JOIN tracks
        USING(AlbumId)
        GROUP BY AlbumId
        ''')