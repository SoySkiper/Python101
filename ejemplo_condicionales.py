number1 = 26;
number2 = 5;

string1 = "Anita lava la tina";
string2 = "Cristian Eduardo";

boolean1 = True;
boolean2 = False;

if number1 > number2:
    print('El numero mayor es: ', number1)
else:
    print('El numero menor es: ', number1)

#Ejemplo 2 

resp = input('¿Te gusta Python?') 

if resp == 'si' or number2 == 0:
    print('Excelente')
elif resp == 'no':
    print('No es tan bueno')
elif resp == 'Skiper':
    print('Contraseña correcta')
else:
    print('Seguro te gusta PHP');


#
edad = int(input('¿Cuál es tu edad?'))
if edad >= 18:
    print('Bienvenido')
else:
    print('No puedes ingresar p')