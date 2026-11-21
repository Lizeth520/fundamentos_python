#CICLOS WHILE

#BUCLE INFINITO

"""
while true:
print("Llenando memoria ram")
"""

#ESTRUCTURA DE UN WHILE 

i = 1 # INICIALIZAR LA VARIABLE DE CONTROL 

while i<6: #CONDICION
    print(f"Bloque codigo: {i}")
    i+=1 #INCREMENTAR LA VARIABLE DE CONTROL 

#EJERCICIO: VALIDAR SI ES MENOR DE EDAD 

edad = 16 

while edad < 18:
    print(f"Eres menor de edad, porque tienes {edad} anios")
    edad += 1
else: 
    print("Eres mayor de edad")