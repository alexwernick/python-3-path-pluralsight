import sqlite3

database = sqlite3.connect("portfolio.db") # will create id db does not exist
cursor = database.cursor()
result = cursor.execute("SELECT * FROM investments;")
all_rows = result.fetchall()

print(all_rows)