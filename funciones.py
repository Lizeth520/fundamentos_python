# FUNCIONES 

#ESTRUCTURA DE UNA FUNCION

#DECLARAR O DEFINIR UNA FUNCION 
def nombre_funcion():
    print("Hola, soy una funcion")
    
#LLAMAR O INVOCAR UNA FUNCION 

nombre_funcion()

#FUNCION CON PARAMETROS DE ENTRADA 

def saludar(nombre):
    resultado = f"Hola, Lizeth Bienvenido a la programacion con Python"
    return resultado

print(saludar("Lizeth"))

def saludar(nombre, apellido, ficha=3233140):
    print(f"Hola, {nombre} {apellido} de la ficha {ficha} Bienvenida a la programacion con Python")
    
saludar("Lizeth", "Fonseca")  #atributo predeterminado
saludar("Paula", "Perez", "1234567")
saludar("Lopez", "Juan","89101112")

#DIGILENCIAR LOS ARGUMENTOS EN DIFERENTE ORDEN DEFINIENDO LA CLAVE VALOR 
saludar(ficha=3233140, apellido= "Castellanos", nombre="Kevin")

#FUNCION CON TIPO DE DATO, LISTA COMO ARGUMENTO DE ENTRADA 

def imprimir_aprendices(lista_aprendices, ficha):
    for aprendiz in lista_aprendices:
        print(f"El aprendiz {aprendiz} esta en la ficha {ficha}")
    
#LISTA DE APRENDICES
aprendices_3233140 =["Luis","Juan","Maria"]
aprendices_3233149 =["James","Falcao","Carlos"]

imprimir_aprendices(aprendices_3233140,"3233150")
imprimir_aprendices(aprendices_3233140,"3233150")

#AGREGAR APRENDIZ

def agregar_aprendiz(ficha, aprendiz):
    ficha.append(aprendiz)
    print("El aprendiz {aprendiz} ha sido agregado exitosamente a la ficha {ficha}")
    
agregar_aprendiz(aprendices_3233140, "Juanito")
agregar_aprendiz(aprendices_3233140, "Juanita")

agregar_aprendiz(aprendices_3233149, "Luis")

#MODIFICAR UN APRENDIZ 

def modificar_aprendiz(ficha, aprendiz_viejo, aprendiz_nuevo):
    if aprendiz_viejo in ficha: #VALIDAR SI EXISTE EL APRENDIZ
        indice_aprendiz = ficha.index(aprendiz_viejo)  #BUSCAR EL INDEX
        ficha [indice_aprendiz] = aprendiz_nuevo   #MODIFICAMOS EL NOMBRE DEL APRENDIZ
        print(f"El aprendiz ha sido modificado exitosamente {ficha}")  
    else:
        print(f"El aprendiz {aprendiz_viejo} no se encuentra registrado en la ficha")

modificar_aprendiz(aprendices_3233149, "James", "David")
modificar_aprendiz(aprendices_3233149, "Lucas", "Pedro")
modificar_aprendiz(aprendices_3233149, "Marcos", "David")

#ELIMINAR UN APRENDIZ (delete)

def eliminar_aprendiz(ficha, aprendiz_borrado):
    if aprendiz_borrado in ficha: #VALIDAR SI EXISTE EL APRENDIZ
        ficha.remove(aprendiz_borrado)  #BORRAR EL APRENDIZ
        print(f"El aprendiz {aprendiz_borrado} ha sido eliminado de la ficha {ficha}")
    else:
        print(f"El aprendiz {aprendiz_borrado} no se encuentra registrado en la ficha")

eliminar_aprendiz(aprendices_3233149, "Falcao")

#APLICACION DE CONSOLA PARA GESTIONAR APRENDICES

ficha_nueva = []
opcion = int(input("Selecciona una opcion : \n 1. Agregar Aprendiz \n 2. Modificar Aprendiz \n 3. Eliminar Aprendiz \n 4. Imprimir Aprendiz \n 5. Salir \n "))

while opcion !=5:
    if opcion ==1:
        nuevo_aprendiz = input("Ingrese el nombre del nuevo aprendiz")
        
        agregar_aprendiz(ficha_nueva, nuevo_aprendiz)
    elif opcion == 2:
        aprendiz_viejo = input("Ingrese el nombre del aprendiz a modificar").capitalize()
        aprendiz_nuevo = input("Ingrese el nuevo nombre del aprendiz").capitalize()
        
        modificar_aprendiz(ficha_nueva,aprendiz_viejo, aprendiz_nuevo)
    elif opcion ==3:
        aprendiz_eliminado = input("Ingrese el nombre del aprendiz a eliminar").capitalize()
        
        eliminar_aprendiz(ficha_nueva, aprendiz_eliminado)
    elif opcion ==4:
        imprimir_aprendices(ficha_nueva)
    else:
        print("Opcion No Valida")
        