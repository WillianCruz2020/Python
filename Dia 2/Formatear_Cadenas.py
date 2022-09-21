nombre = input("Cual es tu nombre?: ")
ventas = input("Cuanto fueron tus ventas este mes?: ")
porcentaje_comision = 0.13
comision = round(float(ventas) * porcentaje_comision,2)


print(f"OK, {nombre}, tus comision para este mes son ${comision}")
print(f"OK, {nombre}, tus comision para este mes son ${float(ventas)*0.13}")
print(f"OK, {nombre}, tus comision para este mes son ${round(float(ventas)*13/100,2)}")

