# actividad2_diccionarios.py

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
def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_reporte(diccionario):
    print(f"{'Ficha':<10}{'Nombre':<18}{'Edad':<6}{'Promedio':<10}{'Estado'}")
    print("-" * 55)
    for ficha, datos in diccionario.items():
        promedio = calcular_promedio(datos["notas"])
        estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
        print(f"{ficha:<10}{datos['nombre']:<18}{datos['edad']:<6}{promedio:<10.2f}{estado}")

# Punto 3: reporte inicial

mostrar_reporte(grupo)

# Punto 4: nuevo aprendiz y actualización de ciudad

grupo [5678901] = {
    "nombre": "Valentina Ruiz",
    "edad": 21,
    "notas": [3.9, 4.1, 3.6, 4.3],
    "ciudad": "Bucaramanga",
}

grupo[2345678]["ciudad"] = "Nueva Ciudad"

print("\nDespués de los cambios:")
mostrar_reporte(grupo)

# Punto 5 (bonus): ordenado de mayor a menor promedio

print("\nRanking de aprendices (mejor a peor promedio):")
ranking = sorted(
    grupo.items(),
    key=lambda item: calcular_promedio(item[1]["notas"]),
    reverse=True,
)
for ficha, datos in ranking:
    print(f"{datos['nombre']:<18} {calcular_promedio(datos['notas']):.2f}")
