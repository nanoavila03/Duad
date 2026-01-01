#Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

time_seconds = 0
minutes = 10
seconds_minutes = 60 * minutes

time_seconds = int(input("Enter a time in seconds: "))

if (time_seconds < seconds_minutes):
    remaining = seconds_minutes - time_seconds
    print("There are", remaining, "seconds remaining to reach 10 minutes.")
elif (time_seconds > seconds_minutes):
    print("Greater")
else:
    print("Equal")