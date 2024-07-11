import datetime
import sqlite3

database = sqlite3.connect("portfolio.db") # will create id db does not exist
cursor = database.cursor()

investment = ("bitcoin", "usd", True, 1.0, datetime.datetime.now())

cursor.execute(
    "INSERT INTO investments VALUES (?, ?, ?, ?, ?);",
    investment
)

database.commit()
