import sqlite3

database = sqlite3.connect("portfolio.db") # will create id db does not exist

cursor = database.cursor()

create_table_query = """
CREATE TABLE investments (
    coin_id TEXT,
    currency TEXT,
    sell INT,
    amount REAL,
    date TIMESTAMP
);
"""

cursor.execute(create_table_query)

database.commit()