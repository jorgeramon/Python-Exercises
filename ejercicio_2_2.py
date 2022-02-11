print("Ingresa la cantidad en pesos mexicanos:")

pesos = float(input())

if pesos < 0:
  print("No se pueden ingresar cantidades negativas")
  quit() # Termina el programa

valor_dolar = 20.56

dolares = pesos/valor_dolar

print("La cantidad en dolares es: $", dolares)