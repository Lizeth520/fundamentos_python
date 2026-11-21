#SENTENCIA MATCH -> SWITCH 

#MATCH - DIAS DE LA SEMANA 

"""dia = int(input("Ingrese el numero del dia de la semana: "))

match dia: 
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("El numero digitado no corresponde a ningun dia de la semana ")
        
    """    
    
#EJERCICIO: FALTAS APRENDIZ SENA 

falta_aprendiz = input("Ingrese la falta del aprendiz: ").lower()  #CONVERTIR TEXTO EN MINUSCULA

match falta_aprendiz:
    case "comer":
        print("Llamado de atencion por comer en formacion")
    case "inpuntualidad":
        print("Llamado de atencion por llegar tarde")
    case "uniforme":
        print("Llamado de atencion por no portar el uniforme adecuadamente")
    case "jugar": 
        print("Llamado de atencion por jugar dentro del aula")
    case _: 
        print("Aprendiz sin faltas")
        
