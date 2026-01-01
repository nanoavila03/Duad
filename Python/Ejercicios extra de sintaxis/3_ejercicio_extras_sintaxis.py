#Convertidor de unidades de temperatura
#Pida al usuario ingresar una temperatura en Celsius
#Conviértala a Fahrenheit y Kelvin
#Muestre los tres valores

celsius = 0
fahrenheit = 0
kelvin = 0

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15

print(f'Temperature in Celsius: {celsius} C')
print(f'Temperature in Fahrenheit: {fahrenheit} F')
print(f'Temperature in Kelvin: {kelvin} K')