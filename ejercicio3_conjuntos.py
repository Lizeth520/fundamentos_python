# APRENDICES MATRICULADOS POR PROGRAMA 

python_curso = {"Ana", "Luis", "Marta", "Carlos", "Sofia", "Pedro"}
java_curso = {"Luis", "Carlos", "Pedro", "Laura", "Diego"}
bd_curso = {"Marta", "Sofia", "Laura", "Ana", "Miguel"}

# CALCULAR E IMPRIMIR

todos = python_curso | java_curso | bd_curso
print("Total de aprendices únicos:", len(todos))
print("Aprendices únicos:", todos)

print("Python y Java:", python_curso & java_curso)
print("Solo Python:", python_curso - java_curso - bd_curso)
print("En exactamente dos:", (python_curso & java_curso) | (python_curso & bd_curso) | (java_curso & bd_curso))

# APRENDICES INSCRITOS

inscripciones = ["Ana", "Luis", "Ana", "Marta", "Carlos", "Luis", "Sofia", "Pedro", "Ana"]
unicos = set(inscripciones)
print("\nInscritos únicos:", len(unicos), unicos)

# DICCIONARIO

conteo_programas = {a: (a in python_curso) + (a in java_curso) + (a in bd_curso) for a in todos}
print("\nProgramas por aprendiz:", conteo_programas)

# VERIFICAR QUIEN ESTA MATRICULADO EN VARIOS CURSOS 

print("\nEn los tres programas:", python_curso & java_curso & bd_curso)
