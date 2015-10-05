from settings import DB_FILE_NAME, DB_INSERT
import sqlite3

conn = sqlite3.connect(DB_FILE_NAME)
cursor = conn.cursor()

with open(DB_INSERT, 'r') as fle:
    cursor.executescript(fle.read())
