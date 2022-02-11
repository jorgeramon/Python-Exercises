print("Ingresa la base del triangulo:")

"""
  input(): Permite que el usuario ingrese datos (un texto)
  int(cadena): Convierte la cadena en un número entero
  float(cadena): Convierte la cadena en un número flotante (con punto decimal)
"""
base = float(input())

"""
Normalmente como se hace es:

texto = input()
numero = float(texto)
"""

print("Ingresa la altura del triangulo:")

altura = float(input())

area = (base * altura)/2

print("El area del triangulo es: ", area)