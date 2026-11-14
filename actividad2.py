# Actividad 2: Calculadora de Notas

calificacion1 = float(input("Ingrese la primera nota: "))
calificacion2 = float(input("Ingrese la segunda nota: "))
calificacion3 = float(input("Ingrese la tercera nota: "))

# CALCULAR EL PROMEDIO DE LAS NOTAS 

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# PUNTOS QUE FALTAN PARA LLEGAR A 5.0

faltante = 5.0 - promedio

# DETERMINAR SI EL ESTUDIANTE APRUEBA O REPRUEBA

# MOSTRAR RESULTADOS 

print("RESULTADOS")
print("Promedio:", round(promedio, 2))
print("Puntos que faltan para llegar a 5.0:", round(max(0, faltante), 2))

if promedio >= 3.0:
    print("Resultado: El estudiante APROBÓ")
else:
    print("Resultado: El estudiante REPROBÓ")
