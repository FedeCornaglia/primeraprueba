import sqlite3

con = sqlite3.connect("chinook.db")
cursor = con.cursor()

respuesta = cursor.execute("select * from genres;")
resultado = respuesta.fetchall()

print(resultado)

respuesta = cursor.execute("select * from artists where artistid=1;")
resultado = respuesta.fetchall()

print(resultado)

respuesta = cursor.execute("select * from employees where employeeid=8;")
resultado = respuesta.fetchall()

print(resultado)

respuesta = cursor.execute("select firstname from customers where firstname='Luis';")
resultado = respuesta.fetchall()

print(resultado)