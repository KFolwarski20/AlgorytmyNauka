def binary_search(numbers: list[int], item: int) -> int | None:
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


"""
Powiedzmy, że mamy posortowaną listę 128 nazwisk i chcemy ją przeszukać za pomocą algorytmu wyszukiwania binarnego. 
Ile maksymalnie prób zgadywania będzie trzeba wykonać?
"""
# Odpowiedź: log2(128) = c => 128 = 2^(c) => c = 7

"""
Ile maksymalnie prób zgadywania trzeba będzie wykonać, jeśli podwoi się liczbę elementów w liście?
"""

# Odpowiedź: log2(256) = c => 256 = 2^(c) => c = 8

"""
Dane jest nazwisko i trzeba znaleźć numer telefonu osoby o tym nazwisku w książce telefonicznej.
"""

# Odpowiedź: O(log n)

"""
Dany jest numer telefonu i trzeba znaleźć nazwisko właściciela tego numeru w książce telefonicznej.
"""

# Odpowiedź: O(n)

"""
Chcesz przeczytać numery wszystkich osób w książce telefonicznej.
"""

# Odpowiedź: O(n)

"""
Chcesz przeczytać numery tylko osób o nazwiskach na A.
"""

# Odpowiedź: O(n). Teoretycznie przeszukuję tylko osoby z nazwiskami na A, czyli 1 z 26 znaków.
# Jednak nie ma zapisu O(n/26) - jest to niepoprawne.


"""
Wyobraź sobie, że tworzysz aplikację do zarządzania domowymi finansami.
    1. warzywa
    2. film
    3. członkostwo w sfbc
Codziennie zapisujesz wszystkie swoje wydatki. Na koniec miesiąca przeglądasz notatki i podsumowujesz, ile wydałeś.
W związku z tym często dodajesz nowe elementy i rzadko odczytujesz dane. Czy w takim razie dla Ciebie lepsza będzie
tablica czy lista?
"""

# Odpowiedź: W takim wypadku lepsza będzie lista powiązana. Rzadko odczytuję dane, często dodaję nowe elementy, więc
# to będzie lepsze rozwiązanie niż tablica. Lista powiązana charakteryzuje się szybkim czasem dodawania nowych elementów
# jednak wadą jest długi czas odczytu. W przypadku tablicy jest zupełnie odwrotnie.
