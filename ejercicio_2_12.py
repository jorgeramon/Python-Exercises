print("Ingresa el precio del articulo:")

subtotal  = float(input())

descuento = subtotal * .2

iva = descuento * .15

print("Subtotal:", subtotal)
print("Subtotal con descuento (20%):", subtotal - descuento)
print("IVA (15%):", iva)
print("Total:", (subtotal - descuento) + iva)