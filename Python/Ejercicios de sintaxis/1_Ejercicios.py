#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

string_string = "Today is Monday" + " and tomorrow is Tuesday"
string_int = "Monday" + 21
int_string = "32" + "Wednesday"
list_list = ["Adidas", "Nike", "Puma"] + ["New Balance", "ON", "Reebok"]
string_list = "Car brands: " + ["Toyota", "Honda", "Ford"]
float_int = 34874.522 + 565
bool_bool = True + False

print(string_string)
print(string_int) #TypeError: can only concatenate str (not "int") to str
print(int_string)
print(list_list)
print(string_list) #TypeError: can only concatenate str (not "list") to str
print(float_int)
print(bool_bool)