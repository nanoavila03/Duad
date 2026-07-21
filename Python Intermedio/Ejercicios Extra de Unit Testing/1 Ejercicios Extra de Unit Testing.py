#Cree una clase de pruebas que contenga al menos 3 funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
#Un caso con números positivos
#Un caso con números negativos
#Un caso con ceros
#Dada la función:

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

#Cree un test que:
#Valide que dividir(10, 2) retorna 5.0
#Verifique que dividir por cero lanza un ValueError
#Valide que dividir con un string como parámetro también lanza TypeError


import pytest


class Operations:
    def sum(self, a, b):
        return a + b

    def average(self, lst):
        return sum(lst) / len(lst)

    def power(self, base, exponent):
        return base ** exponent


class TestOperations:
    def setup_method(self):
        self.op = Operations()

    def test_sum_positive(self):
        assert self.op.sum(3, 5) == 8

    def test_sum_negative(self):
        assert self.op.sum(-3, -5) == -8

    def test_sum_zeros(self):
        assert self.op.sum(0, 0) == 0

    def test_average_positive(self):
        assert self.op.average([1, 2, 3]) == 2.0

    def test_average_negative(self):
        assert self.op.average([-1, -2, -3]) == -2.0

    def test_average_zeros(self):
        assert self.op.average([0, 0, 0]) == 0.0

    def test_power_positive(self):
        assert self.op.power(2, 3) == 8

    def test_power_negative(self):
        assert self.op.power(-2, 3) == -8

    def test_power_zeros(self):
        assert self.op.power(0, 0) == 1


def divide(number1, number2):
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Parameters must be numbers")
    if number2 == 0:
        raise ValueError("Cannot divide by zero")
    return number1 / number2


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_with_string():
    with pytest.raises(TypeError):
        divide("10", 2)

def test_divide_with_string_as_denominator():
    with pytest.raises(TypeError):
        divide(10, "2")

def test_divide_with_both_strings():
    with pytest.raises(TypeError):
        divide("10", "2")


pytest.main([__file__, "-v"])


