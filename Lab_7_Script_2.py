
import sqlite3
import pandas as pds

# Creating the connection with DB
conn = sqlite3.connect('social_network.db')

# Getting a cursor object
crsr = conn.cursor()

# Executing the query to fetch data
crsr.execute('SELECT name,age FROM people where age >= 50 LIMIT 200')

# using fetchall to fetch all the rows
people_data = crsr.fetchall()


# iterating through the for loop
for data in people_data:
    name, age = data
    print(f"{name} is {age} years old.")

# Creating dataframe object and using Pandas instance
datframe = pds.DataFrame(people_data, columns=['Name', 'Age'])
datframe.to_csv('lab_7.csv', index=False)

# Committing the changes
conn.commit()
conn.close()
