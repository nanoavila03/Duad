#Experimente con el concepto de scope:
#Intente accesar a una variable definida dentro de una función desde afuera.

favorite_motorcycle = "Ducati"
def show_favorite_motorcycle():
    motorcycle_model = 'Panigale V4'
    print("My favorite motorcycle is " + favorite_motorcycle)
show_favorite_motorcycle()

print(motorcycle_model) 

#  print(motorcycle_model)
#          ^^^^^^^^^^^^^^^^
#NameError: name 'motorcycle_model' is not defined