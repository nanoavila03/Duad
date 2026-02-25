#3
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
result = sum_list([3,10,30, 2025])

#4
def reverse_string(s):
    return s[::-1]  
result = reverse_string("Pura Vida Costa Rica")
print(result)

#5
def count_case(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")

#6
def sort_hyphenated_string(hyphenated_string):
    words_list = hyphenated_string.split('-')
    words_list.sort()
    sorted_string = '-'.join(words_list)
    return sorted_string
result = sort_hyphenated_string("KTM-Husqvarna-Yamaha-Suzuki-Honda")

#7
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