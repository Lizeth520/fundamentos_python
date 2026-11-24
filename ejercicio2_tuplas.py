# actividad2_diccionarios.py

#CREACION DE GRUPO

grupo = {
    1234567: {
        "nombre": "Ana Torres", 
        "edad": 18,
        "notas": [4.2, 3.8, 4.5, 4.0],
        "ciudad": "Bogotá"
        },
    8910111: {
        "nombre": "Luis Garcia",
        "edad": 19,
        "notas": [3.0, 2.8, 3.5, 3.2],
        "ciudad": "Medellín"
        },
    2131415: {
        "nombre": "Sara Perez",
        "edad": 20,
        "notas": [4.8, 4.6, 4.9, 4.7], 
        "ciudad": "Cali"
        },
    1617181: {
        "nombre": "Diego Martinez",
        "edad": 18, 
        "notas": [2.5, 3.1, 2.9, 3.4], 
        "ciudad": "Barranquilla"
        },
}

#FORMULA PARA CALCULAR EL PROMEDIO 

def calcular_promedio(notas):
    return sum(notas) / len(notas)

# IMPRIMIR REPORTE 

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"
    print(ficha, datos["nombre"], datos["edad"], round(promedio, 2), estado)

# AGREGAR UN NUEVO APRENDIZ

grupo[5678901] = {
    "nombre": "Valentina",
    "edad": 21,
    "notas": [3.9, 4.1, 3.6, 4.3],
    "ciudad": "Bucaramanga"
    }

grupo[2345678]["ciudad"] = "Nueva Ciudad"

print("\nDespués de los cambios:")

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    print(ficha, datos["nombre"], datos["ciudad"], round(promedio, 2))

# MAYOR PROMEDIO

print("\nRanking:")
for ficha, datos in sorted(grupo.items(), key=clave x: calcular_promedio(x[1]["notas"]), reverse=True):
    print(datos["nombre"], round(calcular_promedio(datos["notas"]), 2))