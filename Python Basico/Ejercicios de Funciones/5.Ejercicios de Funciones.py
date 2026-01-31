#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_case(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")

count_case("I like a trail bike")