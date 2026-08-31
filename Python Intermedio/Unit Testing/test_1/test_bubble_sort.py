# Unit tests for bubble_sort:
#
#   Funciona con una lista pequeña.
#   Funciona con una lista grande (de más de 100 elementos.)
#   Funciona con una lista vacía.
#   No funciona con parámetros que no sean una lista.
from Module.bubble_sort import bublesort

def test_bubble_sort_small_list():
    #AAA
    # Arrange
    test_list = [5, 2, 9, 1, 5, 6]
    # Act
    expected_result = [1, 2, 5, 5, 6, 9]
    # Assert
    assert bublesort(test_list) == expected_result

def test_bubble_sort_large_list():  
    # Arrange
    test_list = list(range(100, 0, -1))  # Lista de 100 elementos en orden descendente
    # Act
    expected_result = list(range(1, 101))  # Lista de 100 elementos en orden ascendente
    # Assert
    assert bublesort(test_list) == expected_result

def test_bubble_sort_empty_list():
    # Arrange
    test_list = []
    # Act
    expected_result = []
    # Assert
    assert bublesort(test_list) == expected_result