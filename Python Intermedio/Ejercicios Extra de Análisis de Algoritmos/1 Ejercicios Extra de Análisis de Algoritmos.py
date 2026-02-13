#Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

def manual_add(n):
    result = 0
    for i in range(1, n + 1):  # Error corregido: era 'number'
        result += i
    return result

def add_formula(n):
    return n * (n + 1) // 2  # Error corregido: era 'number'

#Preguntas:
#¿Cuál es la complejidad de cada versión?
# manual_add: O(n) - hace n iteraciones sumando uno por uno
# add_formula: O(1) - solo hace 3 operaciones matemáticas (multiplicación, suma, división)

#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
# Usaría add_formula porque es instantánea (O(1))
# manual_add haría 1,000,000,000 iteraciones (tomaría varios segundos o minutos)
# add_formula hace el cálculo en microsegundos sin importar qué tan grande sea n