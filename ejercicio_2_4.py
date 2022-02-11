import math

print("Ingrese el precio por hora:")

precio_hora = int(input())

print("Ingrese las horas:")

horas = math.ceil(float(input()))

print("Precio: $", precio_hora * horas)