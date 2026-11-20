
# ACTIVIDAD 3: GESTION DE LISTA DE REPRODUCCION MUSICAL

# 1. Creamos una lista con 5 canciones
canciones = ["Imagine", "Perfect", "Viva la Vida",
             "Yellow", "Blinding Lights"]

print("LISTA DE REPRODUCCION INICIAL")
print(canciones)


# 2. Aplicamos los metodos para agregar canciones

# append() agrega una cancion al final de la lista
canciones.append("Bohemian Rhapsody")
print("Despues de append():", canciones)

# insert() agrega una cancion en la segunda posicion
canciones.insert(1, "Hotel California")
print("Despues de insert():", canciones)

# extend() agrega varios elementos a la lista
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Despues de extend():", canciones)


# 3. Eliminamos canciones de la lista

# remove() elimina una cancion por su nombre
canciones.remove("Perfect")
print("Despues de remove():", canciones)

# pop() elimina la ultima cancion y guarda su valor
cancion_eliminada = canciones.pop()
print("Cancion eliminada con pop():", cancion_eliminada)
print("Despues de pop():", canciones)


# 4. Ordenamos las canciones alfabeticamente
canciones.sort()
print("Lista ordenada alfabeticamente:", canciones)


# 5. Respondemos las preguntas usando metodos

# Contamos cuantas canciones tiene la lista
print("Cantidad de canciones:", len(canciones))

# Buscamos la posicion de la primera cancion agregada con append()
print("Posicion de Bohemian Rhapsody:", canciones.index("Bohemian Rhapsody") + 1)

# Contamos cuantas veces aparece Bonus Track 1
print("Veces que aparece Bonus Track 1:", canciones.count("Bonus Track 1"))
