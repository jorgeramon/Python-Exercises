import datetime

anio_actual = datetime.date.today().year # Obtiene el año actual

print("Ingresa tu año de nacimiento:")

anio_nacimiento = int(input())

edad = anio_actual - anio_nacimiento

print("Tu edad es:", edad, "años")