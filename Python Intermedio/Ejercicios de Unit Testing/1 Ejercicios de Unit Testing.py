#Cree los siguientes unit tests para el algoritmo bubble_sort:
#Funciona con una lista pequeña.
#Funciona con una lista grande (de más de 100 elementos.)
#Funciona con una lista vacía.
#No funciona con parámetros que no sean una lista.

import pytest
from bubble_sort import bubble_sort

def test_bubble_sort_small_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_large_list():
    assert bubble_sort([i for i in range(100)]) == [i for i in range(100)]

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_non_list_parameter():
    with pytest.raises(TypeError):
        bubble_sort(1)

def main():
    test_bubble_sort_small_list()
    test_bubble_sort_large_list()
    test_bubble_sort_empty_list()
    test_bubble_sort_non_list_parameter()

pytest.main([__file__, "-v"])