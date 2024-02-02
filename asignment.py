import mysql.connector
import pandas as pd

print('Connecting to mysql...')

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="sakila"
)

try :
    if mydb.is_connected() :
        print('Connected')
except Exception as e :
    print('Error connecting: ', e)

cursor = mydb.cursor()

# sql_query = "INSERT INTO actor (first_name, last_name, last_update) VALUES ('Agus', 'Ismawan', NOW())"
# cursor.execute(sql_query)
# mydb.commit()

# df = pd.read_sql_query(sql_query, mydb)

try :
    sql_query = "UPDATE actor SET first_name = 'BAGOES' WHERE actor_id = 201"
    cursor.execute(sql_query)
    mydb.commit()
except Exception as e:
    print(e)

sql_query = 'SELECT * FROM actor;'
cursor.execute(sql_query)
result = cursor.fetchall()

for i in result :
    print(i)