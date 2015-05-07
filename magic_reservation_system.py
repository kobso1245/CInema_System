import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def show_movies():
    result = cursor.execute("SELECT id, name, rating FROM Movies")
    print("Current movies:")
    for row in result:
        print("[{}] - {} ({})".format(row[0], row[1], row[2]))
