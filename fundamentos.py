print('Hola Mundo')

#TIPO DE ESCRITURA DE LAS VARIABLES -----------------

#camelCase
aprendizSena = "SENA"

#PascalCase
AprendizSena = "SENA"

#snake_case - OK
aprendiz_sena = "SENA"

#Reglas de las Variables:

nombre_completo = "Lizeth Fonseca"

#TIPOS DE DATOS --------------

nombre = "Lizeth"
print(type(nombre))  #str

edad = 25
print(type(edad))   #int

altura = 1.58
print(type(altura))   #float

activo = True
print(type(activo))   #booleano

complejo = 2+3j
print(type(complejo))  #complex

byte = b"Hola"
print(type(byte)) #bytes

#TIPOS DE DATOS ESTRUCTURADOS ----------------------

lista = ["Python","Javascript"]
print(type(lista))  #list

conjunto = {"HTML","Css"}
print(type(conjunto))  #set 

tupla = ("Java","C#")
print(type(tupla))  #tuple 

diccionario = {"nombre": "Andres", "edad": 25}
print(type(diccionario))   #dict

#CONVERSION DE TIPOS DE DATOS O CASTEO--------------------

#casteo: Entero -> Texto


telefono = 3208223458
print(type(telefono), telefono)

telefono_str = str(telefono)
print(type(telefono_str), telefono_str)

#casteo: Texto -> Entero

cedula = "1002457641"  #string
print(type(cedula), cedula)

cedula_int = int(cedula)  #entero
print(type(cedula_int), cedula_int)

#casteo: booleano -> Entero

matriculado =False
print(type(matriculado)) #bool

matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int)  #entero 

#casteo: Decimal -> Entero 

promedio = 4.13
print(type(promedio), promedio)  #float

promedio_int = int(promedio)
print(type(promedio_int), promedio_int)   #entero 

#casteo: Entero -> Booleano 

edad = 25
print(type(edad), edad)  #int

edad_float = float(edad)
print(type(edad_float), edad_float)  #float 

#casteo: Booleano -> Decimal 

beneficio = True
print(type(beneficio),beneficio)  #bool 

beneficio_float = (beneficio)
print(type(beneficio_float), beneficio_float)  #float

#casteo: Decimal -> Booleano 

descuento = 10.5
print(type(descuento), descuento)  #float

descuento_bool = bool(descuento)
print(type(descuento_bool), descuento_bool)  #bool 

#Este es un comentario de una sola linea 

""""Este es un comentario de varias lineas 
que se utiliza para explicar el codigo de manera mas detallada"""

#IDENTACION DE PYTHON 

#CONDICIONAL IF 

if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")
    
#INPUT: ENTRADA DE DATOS 

nombre_completo = input("Ingresa tu nombre completo: ")
programa = input("Cual es tu programa de formacion? ")

#OUTPUT: SALIDA DE LOS DATOS 

print("Hola " + nombre_completo + "Bienvenido al curso de Python")
print("Hola", nombre_completo, "Bienvenido al curso de Python")

print("Hola mi nombre es: " , nombre_completo, " y estoy en el programa de: ", programa)

#IMPRESION CON FORMATO F-STRING - OK 

print(f"Hola mi nombre es {nombre_completo}, y estoy en el programa de: {programa}")
