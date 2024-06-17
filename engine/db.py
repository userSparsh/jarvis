
import csv
import sqlite3

# Connect to the database
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

# Create table if it doesn't exist
'''
query = 
CREATE TABLE IF NOT EXISTS sys_command(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    path VARCHAR(1000)
)

cursor.execute(query)

# insert into table..

query = "INSERT INTO sys_command VALUES(NULL,'tableau','C:\\Program Files\\Tableau\\Tableau 2024.1\\bin\\tableau.exe')"
cursor.execute(query)
con.commit()


query = 
CREATE TABLE IF NOT EXISTS web_command(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    url VARCHAR(1000)
)

cursor.execute(query)


query = "INSERT INTO web_command VALUES(NULL,'hd hub for you','https://hdhub4u.wales/')"
cursor.execute(query)
con.commit()

#Delete specific rows from the table
# Change this to the ID you want to delete
#query = "DELETE FROM web_command WHERE id = 3 "
#cursor.execute(query)

# Commit the changes and close the connection
#con.commit()

# testing module

app_name = 'android studio'
cursor.execute('SELECT url FROM web_command WHERE name IN (?)',(app_name,))
results = cursor.fetchall()
print(results[0][0])

'''

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobil_no VARCHAR(255) ,email VARCHAR(255) NULL)''')

# specify the column indices you want to import(0-based index)
# Example :Importing the 1st and 3rd columns

#desired_columns_indices = [0, 31]

# Read data from CSV and insert into SQLite table for the desored columns

#with open('contacts.csv','r',encoding='utf-8') as csvfile:
 #   csvreader = csv.reader(csvfile)
 #   for row in csvreader:
  #      selected_data = [row[i] for i in desired_columns_indices]
 #       cursor.execute('''INSERT INTO contacts (id,'name','mobil_no') VALUES (null,?, ?);''',tuple(selected_data))

# commit changes and close connection
#con.commit()
#con.close()

#query = "INSERT INTO contacts VALUES (null,'anjali','7754930276','null')"
#cursor.execute(query)
#con.commit()

#query = "ravi"
#query = query.strip().lower()

#cursor.execute("SELECT mobil_no FROM contacts WHERE LOWER(name) LIKE? or LOWER(name) LIKE ?",('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])