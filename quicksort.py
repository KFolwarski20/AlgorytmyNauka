def sum_digits(arr):
    total = 0
    for x in arr:
        total += x
    return total


"""
Napisz kod źródłowy wcześniejszej funkcji sum.
"""


def sum_code(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + sum_code(arr)


"""
Napisz funkcję rekurencyjną liczącą elementy w liście.
"""


def count_list_elements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_list_elements(arr[1:])


"""
Znajdź największą liczbę w liście.
"""


def find_max_digit(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max_digit(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


"""
Pamiętasz wyszukiwanie binarne z rozdziału 1.? To też jest algorytm typu "dziel i rządź". Potrafisz określić
przypadki bazowy i rekurencyjny dla wyszukiwania binarnego?
"""


# Odpowiedź: Przypadek bazowy to ograniczenie długości listy do jednego elementu. Przypadek rekurencyjny: zmniejszenie
# długości listy o połowę.
