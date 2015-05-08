from settings import DB_FILE_NAME, DB_SCRIPT
import sqlite3

conn = sqlite3.connect(DB_FILE_NAME)
cursor = conn.cursor()
with open(DB_SCRIPT, 'r') as fle:
    cursor.executescript(fle.read())
