#Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones (exceptuando el 1 y 2).

import pytest
from funciones import sum_list, reverse_string, count_case, sort_hyphenated_string, filter_primes

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, 0, 1]) == 0
    assert sum_list([10, 20, 30]) == 60
    
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("Unit Testing") == "gnitseT tinU"

def test_count_case(capsys):
    count_case("Hello World")
    captured = capsys.readouterr()
    assert captured.out == "There’s 2 upper cases and 8 lower cases\n"
    
    count_case("PYTHON")
    captured = capsys.readouterr()
    assert captured.out == "There’s 6 upper cases and 0 lower cases\n"
    
    count_case("python")
    captured = capsys.readouterr()
    assert captured.out == "There’s 0 upper cases and 6 lower cases\n"

def test_sort_hyphenated_string():
    assert sort_hyphenated_string("KTM-Husqvarna-Yamaha-Suzuki-Honda") == "Honda-Husqvarna-KTM-Suzuki-Yamaha"
    assert sort_hyphenated_string("Apple-Banana-Cherry-Date") == "Apple-Banana-Cherry-Date"
    assert sort_hyphenated_string("Zebra-Antelope-Giraffe") == "Antelope-Giraffe-Zebra"

def test_filter_primes():
    assert filter_primes([1, 4, 6, 7, 13, 9, 67]) == [7, 13, 67]
    assert filter_primes([10, 15, 20, 25]) == []
    assert filter_primes([2, 3, 5, 11]) == [2, 3, 5, 11]
    
def main():
    test_sum_list()
    test_reverse_string()
    test_count_case()
    test_sort_hyphenated_string()
    test_filter_primes()
    print("All tests passed!")

pytest.main([__file__, "-v"])