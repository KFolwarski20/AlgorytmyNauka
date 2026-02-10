"""
W przykładzie dotyczącym Netfliksa dystans dzielący dwóch użytkowników obliczaliśmy za pomocą specjalnego wzoru.
Jednak nie wszyscy użytkownicy oceniają filmy w taki sam sposób. Powiedzmy, że mamy dwóch użytkowników, nazwijmy
ich Yogi i Pinky, którzy mają taki sam gust filmowy. Mimo to Yogi wszystkim filmom, które mu się podobają, przyznaje
piątkę, a Pinky jest bardziej wybredny i najwyższą ocenę przyznaje tylko naprawdę - jego zdaniem - najlepszym filmom.
Choć panowie mają podobne gusty, według naszego algorytmu obliczania dystansu nie są sąsiadami. Co zrobisz,
by uwzględnić w obliczeniach także te odmienne strategie oceniania?
"""

# Odpowiedź: Zastosuje normalizację. Obliczę średnią ocen wydawanych wydawanych przez każdą osobę i na podstawie
# otrzymanego wyniku zastosuję skalowanie ocen.


"""
Powiedzmy, że Netflix wyznacza grupę "liczących się użytkowników". Zaliczają się do nich np. Quentin Tarantino oraz
Wes Anderson i ich oceny liczą się znacznie bardziej niż zwykłych użytkowników. Jak zmodyfikowałbyś system rekomendacji,
aby bardziej zdecydowanie uwzględniał opinię takich osób?
"""

# Odpowiedź: Zastosuję średnią ważoną. Dla osób, których rekomendacje liczą się w znacznym stopniu, przypiszę większą
# wagę.


"""
Netflix ma miliony użytkowników. Opisany w przykładzie system rekomendacji opierał się na analizie cech pięciu
najbliższych sąsiadów. Czy myślisz, że to za dużo? A może za mało?
"""


# Odpowiedź: W przypadku tak dużej liczby użytkowników 5 najbliższych sąsiadów to zbyt mała ilość. Najlepiej stosować
# zasadę, jeśli jest N przypadków, warto zastosować pierwiastek z N sąsiadów.
