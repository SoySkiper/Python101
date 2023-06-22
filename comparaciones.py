# Escribe un programa que pida la edad del usuario y 
# que muestre por pantalla si es mayor de edad o no. La cansola te tiene que mostrar true o false.

age = int(input("Introduce tu edad: "))
print(age >= 18)

# Otra forma de hacerlo:
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")