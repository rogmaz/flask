import mysql.connector

# Connect to the database
connection = mysql.connector.connect(host='localhost',
                                    user='rogmaz',
                                    password='rogmaz',
                                    database='database')

# Create a cursor
cursor = connection.cursor()

# Create a table
#cursor.execute('''
 #   CREATE TABLE users (
  #      id INTEGER PRIMARY KEY AUTO_INCREMENT,
   #     name VARCHAR(255)
    #)
#''')

# Insert some data
cursor.execute('''
    INSERT INTO users (name) VALUES
    ("Alice"),
    ("Bob"),
    ("Eve"),
    ("Rogelio Mazaeda")
''')

# Commit the changes
connection.commit()

# Perform a SELECT query
cursor.execute('''
    SELECT * FROM users
''')

# Fetch the results
result = cursor.fetchall()

# Print the results
for row in result:
    print(row)

# Close the connection
connection.close()
