# Programa que da el promedio de presupuesto de los primeros 3 meses.

enero = int(input("Ingrese el presupuesto de enero: "))
febrero = int(input("Ingrese el presupuesto de febrero: "))
marzo = int(input("Ingrese el presupuesto de marzo: "))

promedio_presupuesto = (enero + febrero + marzo) / 3

print("El promedio de presupuesto es: ", promedio_presupuesto)