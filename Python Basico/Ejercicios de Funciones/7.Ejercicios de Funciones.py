#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

import random
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_primes(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes
random_numbers = random.sample(range(1, 101), 20)
prime_numbers = filter_primes(random_numbers)
print("Random Numbers:", random_numbers)
print("Prime Numbers:", prime_numbers)