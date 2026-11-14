# CLASIFICADOR DE IMC 

#SOLICITUD DE PESO Y ESTATURA 

persona1 = input("Ingrese el nombre de la persona: ")
peso = float(input("Ingrese el peso en kilogramos: "))
estatura = float(input("Ingrese la estatura en metros: "))

IMC = peso / (estatura ** 2)

#CLASIFICACION DEL IMC
if IMC < 18.5:
    clasificacion = "su peso es bajo"
elif 18.5 <= IMC < 18:
    clasificacion = "Esta en el peso normal"
elif 25 <= IMC < 30:
    clasificacion = "Tiene sobrepeso"
else:
    clasificacion = "Tiene obesidad"
    
#MOSTRAR RESULTADOS
print(f"{persona1}, su IMC es: {IMC:.2f} y {clasificacion}")
print(f"El IMC de {persona1} es: {IMC:.2f} y su clasificacion es: {clasificacion}")
