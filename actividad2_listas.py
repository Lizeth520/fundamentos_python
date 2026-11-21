# ACTIVIDAD 2: ANALISIS DE TEMPERATURAS SEMANALES

# 1. CREACION DE LISTAS CON LAS TEMPERATURAS DE DOS SEMANAS

temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 2. UTILIZAMOS INDEX PARA MOSTRAR LOS VALORES QUE SE NECESITAN 

print("ANALISIS DE TEMPERATURAS")
print("Temperatura del primer dia:", temperaturas[0])
print("Temperatura del ultimo dia:", temperaturas[-1])
print("Temperatura del dia 7:", temperaturas[6])
print("Temperatura del penultimo dia:", temperaturas[-2])

# 3. UTILIZAMOS SLICING PARA EXTRAER E IMPRIMIR

# TEMPERATURA DE LA SEMANA 1 (dias 1 al 7)

primera_semana = temperaturas[0:7]
print("Primera semana:", primera_semana)

# TEMPERATURA DE LA SEMANA 2 (dias 8 al 14)

segunda_semana = temperaturas[7:14]
print("Segunda semana:", segunda_semana)

#TEMPERATURAS DE LOS DIAS PARES (2, 4, 6, 8, 10, 12 y 14)

dias_pares = temperaturas[1::2]
print("Temperaturas de los dias pares:", dias_pares)

#LISTA DE TEMPERATURAS

invertidas = temperaturas[::-1]
print("Temperaturas en orden invertido:", invertidas)


# 3. CALCULAR E IMPRIMIR EL PROMEDIO DE CADA SEMANA

promedio_semana1 = sum(primera_semana) / len(primera_semana)
promedio_semana2 = sum(segunda_semana) / len(segunda_semana)

print("Promedio de la primera semana:", round(promedio_semana1, 2))
print("Promedio de la segunda semana:", round(promedio_semana2, 2))


#RESULTADO DE TEMPERATURA 

if promedio_semana1 > promedio_semana2:
    print("La primera semana tuvo mayor temperatura promedio.")
elif promedio_semana2 > promedio_semana1:
    print("La segunda semana tuvo mayor temperatura promedio.")
else:
    print("Las dos semanas tuvieron el mismo promedio de temperatura.")
