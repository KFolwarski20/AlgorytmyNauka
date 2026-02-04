from collections import deque

"""
Znajdź długość najkrótszej drogi od linii startu do mety.
"""

# Odpowiedź: Start -> Góra -> Meta. Odległość wynosi 2.


"""
Znajdź długość najkrótszej drogi z 'cab' do 'bat'.
"""

# Odpowiedź: cab -> cat -> bat. Odległość wynosi 2.


graph = dict()
graph["ty"] = ["alicja", "bartek", "cecylia"]
graph["bartek"] = ["janusz", "patrycja"]
graph["alicja"] = ["patrycja"]
graph["cecylia"] = ["tamara", "jarek"]
graph["janusz"] = []
graph["patrycja"] = []
graph["tamara"] = []
graph["jarek"] = []


def mango_seller_search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} sprzedaje mango!")
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == "z"


"""
Oto niewielki graf przedstawiający mój typowy poranek.

Z tego grafu wynika, że nie mogę zjeść śniadania, dopóki nie wyszczotkuję zębów. W związku z tym "śniadanie" jest
zależne od "mycia zębów".

A przecież prysznic nie zależy od mycia zębów, ponieważ mogę go wziąć, zanim przystąpie do higieny jamy ustnej. Na
podstawie tego grafu można utworzyć listę przedstawiającą kolejność wykonywania przeze mnie porannych czynności:
1. pobudka,
2. prysznic,
3. mycie zębów,
4. śniadanie.

Miejsce prysznica można zmieniać, więc poniższa lista również jest poprawna.
1. pobudka,
2. mycie zębów,
3. prysznic,
4. śniadanie.
"""

"""
Przyjrzyj się trzem poniższym listom i powiedz, które z nich są poprawne.
"""

# Odpowiedź: B jest tylko poprawna. A - nie, ponieważ nie mogę zjeść śniadania przed myciem zębów, C - nie, ponieważ
# nie mogę wziąć prysznica bez pobudki

"""
Oto nieco większy graf. Utwórz z niego poprawną listę.

Można powiedzieć, że lista ta jest w pewien sposób posortowana. Jeśli zadanie A zależy od B, to zadanie A występuje
w dalszym miejscu w liście. Takie uporządkowanie nazywa się sortowaniem topologicznym i jest jednym ze sposobów
na sporządzenie listy z grafu. Wyobraź sobie, że planujesz ślub i masz duży graf obejmujący różne zadania do wykonania 
- i nie wiesz od czego zacząć. W takim przypadku możesz posortować graf topologicznie, aby otrzymać listę czynności
do wykonania po kolei.
"""

# Odpowiedź:
# 1. Pobudka
# 2. Cwiczenia
# 3. Prysznic
# 4. Ubieranie się
# 5. Mycie zębów
# 6. Śniadanie
# 7. Spakowanie drugiego śniadania

"""
Które z poniższych grafów są także drzewami?
"""

# Odpowiedź: A - drzewo, B - nie drzewo, C - drzewo
# C jest drzewem pochylonym. Drzewa są podzbiorem grafów, więc każde drzewo jest grafem, ale nie każdy graf jest
# drzewem.
