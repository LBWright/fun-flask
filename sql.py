import sqlite3

with sqlite3.connect('sample.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(title TEXT, description TEXT)')
    cursor.execute('INSERT INTO posts VALUES("Post title", "Post Content")')
    cursor.execute('INSERT INTO posts VALUES("Second title", "Second Content")')