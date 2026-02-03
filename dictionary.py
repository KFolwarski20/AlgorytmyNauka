"""
Które z poniższych funkcji są konsekwentne w tej kwestii?
5.1. f(x) = 1 <- zwraca 1 dla wszystkich danych wejściowych.
5.2. f(x) = rand() <- za każdym razem zwraca losową liczbę.
5.3. f(x) = next_empty_slot() <- zwraca indeks następnej pustej komórki w tablicy skrótów.
5.4. f(x) = len(x) <- jako indeksu używa długości łańcucha.
"""

# 5.1. Odpowiedź: konsekwentna
# 5.2. Odpowiedź: niekonsekwentna
# 5.3. Odpowiedź: niekonsekwentna
# 5.4. Odpowiedź: konsekwentna

voted = {}


def check_voter(name):
    if voted.get(name):
        return "Pogonić go!"
    else:
        voted[name] = True
        return "Niech zagłosuje!"


# cache = {}
#
#
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data
#         return data


"""
Dobra funkcja obliczania skrótów powinna zapewniać równomierną dystrybucję, tzn. powinna jak najszerzej rozmieszczać
elementy w strukturze. Najgorsza jest funkcja przypisująca wszystkie elementy do tej samej miejscówki w tablicy skrótów.

Wyobraź sobie, że masz cztery poniższe funkcje obliczania skrótów pobierające łańcuchy.
A. Funkcja zwracająca 1 dla wszystkich danych wejściowych.
B. Funkcja wykorzystująca jako indeks długość otrzymanego na wejściu łańcucha.
C. Funkcja wykorzystująca jako indeks pierwszą literę otrzymanego na wejściu łańcucha, tak że wszystkie napisy
zaczynające się na a są grupowane w jednej komórce itd.
D. Funkcja zamieniająca każdą literę na liczbę pierwszą: a = 2, b = 3, c = 5, d = 7, e = 11 itd. Dla podanego łańcucha
funkcja obliczania skrótów oblicza sumę wszystkich znaków i dzieli ją bez reszty przez rozmiar tablicy skrótów. Jeśli
np. rozmiar tablicy skrótów wynosi 10 i zostanie przekazany łańcuch "gad", to indeks tego łańcucha wyniesie
17 + 2 + 7 % 10 = 26 % 10 = 2.

Która z powyższych funkcji zapewniłaby dobry rozkład w poniższych przypadkach przy założeniu, że rozmiar tablicy
skrótów wynosi 10 miejsc.
"""

"""
5.5. Książka telefoniczna, w której kluczami są imiona, a wartościami numery telefonów. Dane są następujące imiona:
Eliza, Bernard, Bożydar, Daniel.
"""

# Odpowiedź: Dobry rozkład w tym przypadku to podpunkt C i D.

"""
5.6. Przypisanie rozmiaru baterii do jej mocy. Dostępne są rozmiary A, AA, AAA oraz AAAA.
"""

# Odpowiedź: Dobry rozkład zapewni podpunkt B i D.

"""
5.7. Przypisanie tytułów książek do autorów. Dane są następujące tytuły: Maus, Fun Home i Watchmen.
"""

# Odpowiedź: Dobry rozkład zapewni podpunkt B, C i D.
