#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

string_string = "Hoy es lunea" + " y manana es martes"
string_int = "Lunes" + 21
int_string = "32" + "Miercoles"
List_List = ["Adidas,Nike,Puma]"] + ["New balance, ON, Reebok "]
string_list = "Marcas de carros: " + ["Toyota, Honda, Ford"]
float_int = 34874.522 + 565
bool_bool = True + False

print(string_string)
print(string_int) #TypeError: can only concatenate str (not "int") to str
print(int_string)
print(List_List)
print(string_list)#TypeError: can only concatenate str (not "list") to str
print(float_int)
print(bool_bool)