#Experimente con el concepto de scope:
#Intente accesar a una variable global desde una función y cambiar su valor.

global_var = "I am a global variable."
def my_function():
    global global_var
    local_var = "I am a local variable."
    print(local_var)  
    print(global_var) 
    global_var = "I have been changed inside the function."
my_function()       
print(global_var)
