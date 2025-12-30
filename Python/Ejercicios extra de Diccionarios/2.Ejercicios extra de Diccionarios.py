#Agrupar empleados por departamento
#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:

employees = [
    {"name": "Carlos Martinez", "email": "carlos.martinez@empresa.com", "department": "Ventas"},
    {"name": "Ana Rodriguez", "email": "ana.rodriguez@empresa.com", "department": "TI"},
    {"name": "Luis Fernandez", "email": "luis.fernandez@empresa.com", "department": "Ventas"},
    {"name": "Sofia Gonzalez", "email": "sofia.gonzalez@empresa.com", "department": "RRHH"},
    {"name": "Miguel Torres", "email": "miguel.torres@empresa.com", "department": "TI"},
    {"name": "Laura Sanchez", "email": "laura.sanchez@empresa.com", "department": "Marketing"},
    {"name": "David Lopez", "email": "david.lopez@empresa.com", "department": "Finanzas"},
    {"name": "Carmen Diaz", "email": "carmen.diaz@empresa.com", "department": "Ventas"},
    {"name": "Roberto Perez", "email": "roberto.perez@empresa.com", "department": "TI"},
    {"name": "Patricia Ruiz", "email": "patricia.ruiz@empresa.com", "department": "Marketing"},
    {"name": "Jorge Moreno", "email": "jorge.moreno@empresa.com", "department": "Finanzas"},
    {"name": "Elena Jimenez", "email": "elena.jimenez@empresa.com", "department": "RRHH"}
]

department_dict = {}
for employee in employees:
    departament = employee["department"]
    if departament not in department_dict:
        department_dict[departament] = []
    department_dict[departament].append(employee)
print(department_dict)