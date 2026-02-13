#Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

#Preguntas:
#¿Cuál es la complejidad temporal?
# O(n²) - dos ciclos anidados, cada uno recorre todas las n claves
# Si hay n claves, imprime n × n = n² pares

#¿Cuanto dura si hay 1 millón de claves?
# Haría 1,000,000 × 1,000,000 = 1,000,000,000,000 (1 billón) de impresiones
# Asumiendo ~1 microsegundo por print: aproximadamente 11.5 días
# Es totalmente impráctico - la complejidad cuadrática escala muy mal