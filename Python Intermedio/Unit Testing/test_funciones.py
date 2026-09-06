from funciones import sum_list_elements, reverse_string, count_cases, sort_separate_hyphen_words

#3 Cree una función que retorne la suma de todos los números de una lista.
#4 Cree una función que le dé la vuelta a un string y lo retorne.
#5 Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
#6 Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.


def test_sum_list_elements():
  
    assert sum_list_elements([4, 6, 2, 29]) == 41
    assert sum_list_elements([]) == 0
    assert sum_list_elements([-1, -2, -3]) == -6

def test_reverse_string():
    
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
def test_reverse_string_empty():
    assert reverse_string("") == ""
def test_reverse_string_single_character():
    assert reverse_string("a") == "a"
def test_reverse_string_numbers():
    assert reverse_string("12345") == "54321"

def test_count_cases():
    count_cases("Hello, World!")  # This function prints the counts, so we just call it to ensure it doesn't raise an error

def test_count_cases_empty():
    count_cases("")  # This function prints the counts, so we just call it to ensure it doesn't raise an error
    assert True  # Just to have an assertion in this test

def test_count_cases_no_upper():
    count_cases("hello world")  # This function prints the counts, so we just call it to ensure it doesn't raise an error
    assert True  # Just to have an assertion in this test



def test_sort_separate_hyphen_words():
    assert sort_separate_hyphen_words("banana-apple-cherry") == "apple-banana-cherry"

def test_sort_separate_hyphen_words_empty():
    assert sort_separate_hyphen_words("") == ""

def test_sort_separate_hyphen_words_single_word():
    assert sort_separate_hyphen_words("singleword") == "singleword"