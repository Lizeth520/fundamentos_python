#CONJUNTOS - SETS 

#ESTRUCTURA DE UN CONJUNTO 

conjunto = {"elemento_1", "elemento_2", "elemento_3"}
print(type(conjunto))   #<class 'set'>

#DECLARAR UN CONJUNTO VACIO 

conjunto_2 = set()
print(type(conjunto_2))   # <class 'set'>

conjunto_3 = {}
print(type(conjunto_3))  #<class 'dict'>

#CREAR UN CONJUNTO (NO PERMITE ELEMENTOS DUPLICADOS)

programas = {"ADSO","SST", "MINERIA", "ADSO", "SST"}
print(programas)  #{'MINERIA', 'SST', 'ADSO'}  

#METODOS DE LOS CONJUNTOS 

frutas = {"guayaba", "mango", "mora", "mandarina"}

#AGREGAR UN NUEVO ELEMENTO AL CONJUNTO

frutas.add("fresas")
print(frutas)  #{'mango', 'mora', 'guayaba', 'fresas'}

frutas.add("mora")  #ELEMENTO DUPLICADO
print(frutas)  

#ELIMINAR UN ELEMENTO DEL CONJUNTO

#METODO .remove()

frutas.remove("mango")
print(frutas)

#frutas.remove("pera") #LANZA KEYERRROR PORQUE NO EXISTE
#print(frutas)

#METODO .DISCARD()

frutas.discard("mora")
print(frutas)

#METODO .pop()

elemento = frutas.pop()  #ELMINIACION ALEATORIA
print(elemento)
print(frutas)

#METODO .clear()

frutas.clear()
print(frutas)  #set()

#ELIMINAR TODO EL CONJUNTO CON EL METODO "DEL"

#del frutas
#print(frutas) #NameError: name 'frutas' is not defined

#VERIFICAR LA PERTENENCIA DE UN ELEMENTO EN UN CONJUNTO: BUSQUEDA

aprendices = {"Felipe", "Luis", "Pepito"}

print("Felipe" in aprendices)  #True
print("Juan" in aprendices)   #False

#OPERACIONES DE LA TEORIA DE CONJUNTOS 

aprendices_formacion = {"jenifer", "lizeth", "alejandra", "diana", "adriana"}
aprendices_apoyo = {"sebastian", "luis", "elkin", "diana"}

#UNION: EXTRAE TODOS LOS ELEMENTOS DE LOS DOS CONJUNTOS 

union_aprendices = aprendices_formacion | aprendices_apoyo
print(union_aprendices)

#METODO UNION ()

union_aprendices2 = aprendices_formacion.union(aprendices_apoyo)
print(union_aprendices2)

#{'manrique', 'elkin', 'jenifer', 'sebastian', 'alejandra', 'luis', 'adriana', 'lizeth', 'diana'}

#INTERSECCION: EXTRAE LOS ELEMENTOS QUE SE REPITEN EN LOS DOS CONJUNTOS 

#OPERADOR INTERSECCION "&"

interseccion_aprendices = aprendices_formacion & aprendices_apoyo
print(interseccion_aprendices)  #{'diana'}

#METODO INTERSECCION()

interseccion_aprendices2 = aprendices_formacion.intersection(aprendices_apoyo)
print(interseccion_aprendices2)  #{'diana'}

#DIFERENCIA: EXTRAE LOS ELEMENTOS QUE NO SE REPITEN EN LOS DOS CONJUNTOS 

# Operador DIFERENCIA "-"
diferencia_aprendices = aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices) # {'jennifer', 'alejandra', 'lizeth'}

# Metodo DIFERENCIA()
diferencia_aprendices_2 = aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices_2) # {'jennifer', 'alejandra', 'lizeth'}

#DIFERENCIA SIMETRICA: EXTRAE LOS ELEMENTOS QUE NO SE REPITEN EN LOS DOS CONJUNTOS 

#OPERADOR DIFERENCIA SIMETRICA"^"

diferencia_aprendices = aprendices_formacion ^ aprendices_apoyo
print(diferencia_aprendices)  #{'jenifer', 'alejandra', 'adriana', 'lizeth'}

#METODO DIFERENCIA SIMETRICA()

diferencia_simetrica_aprendices2 = aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(diferencia_simetrica_aprendices2)  #{'alejandra', 'adriana', 'lizeth', 'jenifer', 'elkin', 'sebastian', 'luis'}

