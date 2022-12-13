import sqlite3
  
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('2tim4_1.db')
  
# cursor object
cursor_obj = connection_obj.cursor()
  
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
  
# Creating table
table = """ CREATE TABLE table_name(  
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    content TEXT
);"""
  
cursor_obj.execute(table)
  
print("Table is Ready")
  
# Close the coonection
connection_obj.close()