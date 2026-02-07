"""
Pracujesz w firmie meblarskiej, w której rozwozisz produkty do różnych miejsc w kraju. Musisz załadować swoją ciężarówkę
pudłami. Pudła te mają różne rozmiary, więc za każdym razem zastanawiasz się, jak najlepiej wykorzystać dostępną
w ciężarówce przestrzeń. Jak ładować pudła, aby spożytować miejsce do maksimum?  Opracuj zachłanną strategię.
Czy pozwala ona uzyskać optymalne rozwiązanie?
"""

# Odpowiedź: Wybierz pudło o największym rozmiarze gabarytowym, które zmieści się w ciężarówce. Wybierz kolejne pudło,
# itd. aż do momentu, gdy nic już nie zmieści się na ciężarówkę. Zachłanna strategia nie pozwoli uzyskać optymalnego
# rozwiązania, gdyż może być lepsza kombinacja pudełek, która pozwoli wykorzystać miejsce w 100%.

"""
Wybierasz się na wycieczkę po Europie i masz siedem dni na obejrzenie jak największej liczby miejsc. Każdemu miejscu
przypisujesz wartość punktową (oznaczającą, jak bardzo chciałbyś je odwiedzić) oraz szacujesz, ile czasu zajmie dojazd.
W jaki sposób uzyskać jak największą sumę punktów (aby dotrzeć do wszystkich miejsc, które chce się zobaczyć) podczas
wycieczki? Opracuj zachłanną strategię. Czy pozwala ona uzyskać optymalne rozwiązanie?
"""

# Odpowiedź: Wybieram miejsce, które ma jak największą ilość punktów, jaką mogę wykonać w czasie, który mi pozostał.
# Kończę pracę, gdy nie będę miał możliwości zrobienia czegokolwiek więcej. W ten sposób nie obliczę optymalnego
# rozwiązania.


def states():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = dict()
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
    print(final_stations)


"""
Dla każdego z tych algorytmów wskaż, czy jest zachłanny, czy nie.
1. Szybkie sortowanie.
2. Wyszukiwanie wszerz.
3. Algorytm Dijkstry.
"""

# Odpowiedź 1: niezachłanny
# Odpowiedź 2: zachłanny
# Odpowiedź 3: zachłanny
