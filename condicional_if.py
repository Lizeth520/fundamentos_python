





































# ESTRUCTURA CONDICIONAL ANIDADA

if True: 
    if False: 
        print("Se ejecuta la instruccion")
    elif True:
        print("Se ejecuta la instruccion")
    else: 
        print("No se ejecuta la instruccion")
else:
    print("No se ejecuta la instruccion")
    
# EJERCICIO: CLASIFICACION DE EDAD IF ANIDADO

edad = 12

if edad < 18:
    if edad > 12 and edad < 18:
        print("Es un adolescente")
    else:
        print("Es un niño")
else:
    if edad > 18 and edad < 60:
        print("Es un adulto")
    else:
        print("Es un adulto mayor")

# EJERCICIO DEL PARTIDO DE COLOMBIA CON IF

marcador_colombia = int(input("Ingrese el marcador de Colombia: "))
marcador_chile = int(input("Ingrese el marcador de Chile: "))

if marcador_colombia > marcador_chile:
    print("Colombia gano el partido")
else: 
    print("Colombia perdio el partido")
    
# OPERADOR TERNARIO

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
    
print("El numero es par" if numero % 2 == 0 else "El numero es impar")