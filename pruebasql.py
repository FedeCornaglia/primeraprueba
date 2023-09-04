import sqlite3

con = sqlite3.connect("chinook.db")
cursor = con.cursor()

respuesta = cursor.execute("select * from genres;")
resultado = respuesta.fetchall()

print(resultado)

respuesta = cursor.execute("select * from artists where artistid=10;")
resultado = respuesta.fetchall()

print(resultado)

respuesta = cursor.execute("select firstname from customers where firstname='Luis';")
resultado = respuesta.fetchall()

print(resultado),

respuesta = cursor.execute("select firstname from customers where firstname='Robert';")
resultado = respuesta.fetchall()

print(resultado),