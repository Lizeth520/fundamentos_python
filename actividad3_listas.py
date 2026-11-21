# ACTIVIDAD 3: GESTION DE LISTA DE REPRODUCCION MUSICAL

# 1. LISTA DER CANCIONES

canciones = ["Imagine", "Perfect", "Viva la Vida","Yellow", "Blinding Lights"]

print("LISTA DE REPRODUCCION INICIAL")
print(canciones)

# 2. APLICACION DE METODOS PARA AGREGAR CANCIONES CON .append (), .insert () y .extend()

canciones.append("Bohemian Rhapsody")
print("Despues de append():", canciones)

canciones.insert(1, "Hotel California")
print("Despues de insert():", canciones)

canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Despues de extend():", canciones)

# 3. ELIMINAR CANCIONES CON .remove() y .pop()

canciones.remove("Perfect")
print("Despues de remove():", canciones)

cancion_eliminada = canciones.pop()
print("Cancion eliminada con pop():", cancion_eliminada)
print("Despues de pop():", canciones)

# 4. ORDENAMOS LAS CANCIONES CON .sort()

canciones.sort()
print("Lista ordenada alfabeticamente:", canciones)

# 5. PREGUNTAS 

# Contamos cuantas canciones tiene la lista

print("Cantidad de canciones:", len(canciones))

# Buscamos la posicion de la primera cancion agregada con append()

print("Posicion de Bohemian Rhapsody:", canciones.index("Bohemian Rhapsody") + 1)

# Contamos cuantas veces aparece Bonus Track 1

print("Veces que aparece Bonus Track 1:", canciones.count("Bonus Track 1"))
