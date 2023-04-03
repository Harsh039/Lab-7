import sqlite3
from datetime import datetime
from faker import Faker
from pprint import pprint

# Creating the connection with DB
conn = sqlite3.connect('social_network.db')

# Getting a cursor object
crsr = conn.cursor()

# creating table to store the data of people
sql_query_create_table = """ CREATE TABLE IF NOT EXISTS people ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, address TEXT NOT NULL, city TEXT NOT NULL, province TEXT NOT NULL, bio TEXT, age INTEGER, created_at DATETIME NOT NULL, updated_at DATETIME NOT NULL ); """

# Executing the Query
crsr.execute(sql_query_create_table)

# Creating the Faker Object
obj_faker = Faker("en_CA")

# Loop to make 200 insertions
for i in range(200):
    id = i + 1
    name = obj_faker.first_name()
    email = obj_faker.ascii_email()
    address = obj_faker.address()
    city = obj_faker.city()
    province = obj_faker.administrative_unit()
    bio = obj_faker.sentence(nb_words=10)
    age = obj_faker.random_int(min=1, max=100)

    # Current system date and time
    created_at = datetime.now()

    # Current system date and time
    updated_at = datetime.now()

    # Insert Query
    sql_query_insert_people = """ INSERT INTO people ( id, name, email, address, city, province, bio, age, created_at, updated_at ) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?); """

    # Setting the values in Query
    person_data = (id,
                   name,
                   email,
                   address,
                   city,
                   province,
                   bio,
                   age,
                   created_at,
                   updated_at)

    # Executing query to add new people data to table
    crsr.execute(sql_query_insert_people, person_data)

# Committing the changes
conn.commit()
conn.close()
