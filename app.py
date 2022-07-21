import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="debian-sys-maint",
  password="ijJ7W0EbqVthUjvY",
   database="mydatabase"
)

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted")

# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

# print("1 record inserted, ID:", mycursor.lastrowid)


# mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT name, address From customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)

# sql = "SELECT * FROM customers WHERE address ='Park lane 38'"
# sql = "SELECT * FROM customers WHERE address Like '%way%'"
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)
# sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "DELETE FROM customers WHERE address = %s, name = %s "
# adr = ("Yellow Garden 2")


# mycursor.execute(sql, adr)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# sql ="UPDATE customers SET address =%s  WHERE address = %s "
# val= ('Valley 345', 'Canyon 123')

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)