#Cree una clase Employee con los siguientes requisitos:
#Atributos privados: _name, _salary
#Use @property y @<atributo>.setter para:
#Mostrar el nombre y el salario
#Validar que el salario nunca sea negativo
#Cree un método promote que aumente el salario un porcentaje definido


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary

    def promote(self, percentage):
        self._salary += self._salary * percentage / 100


def main():
    employee = Employee("John", 1000)
    employee.promote(10)
    print(employee.salary)


if __name__ == "__main__":
    main()  