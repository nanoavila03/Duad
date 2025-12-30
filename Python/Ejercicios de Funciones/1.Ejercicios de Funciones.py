#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def function_one():
    print("This is the first function.")
    function_two()      
def function_two():
    print("This is the second function.")   
function_one()