# ACTIVIDAD 2: ANALISIS DE TEMPERATURAS SEMANALES

# 1. Creamos la lista con las temperaturas de los 14 dias
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 2. Utilizamos indices para mostrar temperaturas especificas

print("ANALISIS DE TEMPERATURAS")

# Primer dia
print("Temperatura del primer dia:", temperaturas[0])

# Ultimo dia
print("Temperatura del ultimo dia:", temperaturas[-1])

# Dia 7 (mitad de la lista)
print("Temperatura del dia 7:", temperaturas[6])

# Penultimo dia
print("Temperatura del penultimo dia:", temperaturas[-2])


# 3. Utilizamos slicing para extraer diferentes partes de la lista

# Temperaturas de la primera semana (dias 1 al 7)
primera_semana = temperaturas[0:7]
print("Primera semana:", primera_semana)

# Temperaturas de la segunda semana (dias 8 al 14)
segunda_semana = temperaturas[7:14]
print("Segunda semana:", segunda_semana)

# Temperaturas de los dias pares (2, 4, 6, 8, 10, 12 y 14)
dias_pares = temperaturas[1::2]
print("Temperaturas de los dias pares:", dias_pares)

# Lista de temperaturas en orden invertido
invertidas = temperaturas[::-1]
print("Temperaturas en orden invertido:", invertidas)


# 4. Calculamos el promedio de cada semana

promedio_semana1 = sum(primera_semana) / len(primera_semana)
promedio_semana2 = sum(segunda_semana) / len(segunda_semana)

print("Promedio de la primera semana:", round(promedio_semana1, 2))
print("Promedio de la segunda semana:", round(promedio_semana2, 2))


# 5. BONUS: Comparamos los promedios de las dos semanas

if promedio_semana1 > promedio_semana2:
    print("La primera semana tuvo mayor temperatura promedio.")

elif promedio_semana2 > promedio_semana1:
    print("La segunda semana tuvo mayor temperatura promedio.")

else:
    print("Las dos semanas tuvieron el mismo promedio de temperatura.")
