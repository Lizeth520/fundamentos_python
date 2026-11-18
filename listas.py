# LISTAS
#ESTRUCTURA DE UNA LISTA

listas = ["dato_1", "dato _2", "dato_3"]
print(type(listas)) #<class 'list'>

#LISTA MIXTA

lista_mixta = ["Hola", 123, 3.14, True, ["ADSO", "SST"]]
print(type(lista_mixta))   #<class 'list'>

#EJERCICIO DE LISTAS DE APRENDICES SENA ADSO 32333140
#INDICE:         0          1            2        3        4

aprendices = ["Miguel", "Sebastian", "Lizeth", "Oscar", "Elkin"]
print(aprendices)

#ACCEDER A UN ELEMENTO DE LA LISTA

print(aprendices[3])   #Oscar

#MODIFICAR UN ELEMENTO DE LA LISTA

aprendices[0]= "Luis"
print(aprendices)  #['Luis', 'Sebastian', 'Lizeth', 'Oscar', 'Elkin']

#CONSULTAR RANGOS DE ELEMENTOS EN LAS LISTAS 

print(aprendices[0:2])  #['Luis', 'Sebastian']
print(aprendices[2:4])    #['Lizeth', 'Oscar']
print(aprendices[0::2])  #['Luis', 'Lizeth', 'Elkin']

#CONCATENAR 2 LISTAS +

programas_tecnicos = ["Sistemas Teleinformaticos", "Redes"]
programas_tecnologos = ["ADSO", "TOPOGRAFIA"]

programas_SENA = programas_tecnicos+programas_tecnologos
print(programas_SENA)   #['Sistemas Teleinformaticos', 'Redes', 'ADSO', 'TOPOGRAFIA']

#EXTENDER LISTAS CON .EXTEND ()

nuevos_programas_tecnicos = ["Inteligencia Artificial", "Mineria de Datos", "Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)  #['Sistemas Teleinformaticos', 'Redes', 'Inteligencia Artificial', 'Mineria de Datos']

#MEDIR LA LONGITUD DE UNA LISTA .len()

print(len(programas_tecnicos))  #[4]
print(len(programas_tecnologos))  #[2]

#CONTAR ELEMENTOS REPETIDOS EN UNA LISTA  .count()

print(programas_tecnicos)
print(programas_tecnicos.count("Redes")) #[2]

#OBTENER EL INDICE DE UN ELEMENTO .index()

print(aprendices.index("Lizeth"))   #[2]
print(programas_tecnicos.index("Mineria de Datos"))  #[3]
print(programas_tecnologos.index("ADSO"))  #[0]

#COPIAR UNA LISTA NUEVA .copy()

nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

#AGREGAR NUEVOS ELEMENTOS CON .append()

nueva_lista_aprendices.append("Adriana")
nueva_lista_aprendices.append("Diana")
print(nueva_lista_aprendices)

#AGREGAR UN NUEVO ELEMENTO EN UNA POSICION DE INDICE .insert()

nueva_lista_aprendices.insert(1, "Dayana")
print(nueva_lista_aprendices)

#ELIMINAR UN ELEMENTO DE LA LISTA

#. remove () ELIMINA LA PRIMERA OCURRENCIA DE LA LISTA

nueva_lista_aprendices.remove("Oscar")
print(nueva_lista_aprendices)

#.pop() ELIMINA EL ELEMENTO SEGUN SU INDICE

nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)

#.clear() LIMPIA TODOS LOS ELEMENTOS DE LA LISTA
#nueva_lista_aprendices.clear()
#print(nueva_lista_aprendices)

#ORDENAR LAS LISTAS 

#ORDENAR ASCENDENTEMENTE A-Z .sort()

nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

#ORDENAR DESCENDENTEMENTE Z-A .reverse()

nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

#BUSCAR ELEMENTOS EN LA LISTA CON EL OPERADOR IN 

if "Diana" in nueva_lista_aprendices:
    print("Diana se encontro en la lista de aprendices")
else: 
    print("Diana no se encontro en la lista de aprendices")

if "Felipe" in nueva_lista_aprendices:
    print("Felipe se encontro en la lista de aprendices")
else: 
    print("Felipe no se encontro en la lista de aprendices")
    
busqueda = "Diana" in nueva_lista_aprendices
print(busqueda) #True
    