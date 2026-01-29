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

"""
Wyobraź sobie, że tworzysz aplikację do przyjmowania zamówień od klientów w restauracji. 
Jedną z funkcji jest zapisywanie listy zamówień. Kelnerzy cały czas dodają nowe zamówienia, a szefowie kuchni
je pobierają i przygotowują potrawy. Jest to kolejka zamówień: kelnerzy dodają zamówienia na końcu kolejki, a szefowie
kuchni pobierają je z początku kolejki i gotują dania. Czy do implementacji takiej kolejki użyłbyś tablicy, czy listy
powiązanej. (Podpowiedź: listy powiązane są dobre we wstawianiu i usuwaniu elementów, a tablice są lepsze w dostępie
swobodnym. Które operacje będziesz wykonywać w tym przypadku?).
"""

# W tym przypadku najlepiej będzie użyć listy powiązanej, ponieważ potrzebujemy mieć krótki czas wykonania
# operacji dodawania i usuwania. Listy powiązane mają znacznie krótszy czas niż tablice. Dla tej aplikacji nie będę
# potrzebował dostępu swobodnego do elementów, ponieważ kucharze zawsze pobierają zamówienia do realizacji po kolei.

"""
Proponuję eksperyment myślowy. Powiedzmy, że Facebook przechowuje listę nazw użytkowników. Gdy ktoś próbuje zalogować
się na konto, system szuka podanej przez tego kogoś nazwy użytkownika. Jeśli ją znajdzie, może nastąpić zalogowanie.
Ludzie bardzo często logują się na Facebook, więc lista nazw użytkowników jest bardzo często przeszukiwana. Powiedzmy,
że do jej przeszukiwania portal używa algorytmu wyszukiwania binarnego. Algorytm ten wymaga dostępu swobodnego - musi
mieć natychmiastowy dostęp do środkowego elementu listy. Czy dysponując tą wiedzą, zaimplementowałbyś listę nazw
użytkowników na bazie tablicy, czy listy powiązanej?
"""

# Zaimplementowałbym listę nazw użytkowników jako tablicę, ponieważ muszę mieć swobodny dostęp do elementów listy.
# Drugim argumenetem jest to, że ludzie bardzo często logują się na Facebook, więc musi być szybki odczyt danych.

"""
Na Facebooku także bardzo często tworzone są nowe konta. Powiedzmy, że listę użytkowników postanowiliśmy przechowywać
w tablicy. Jakie są wady tablicy, jeśli chodzi o wstawianie elementów? Innymi słowy, pomyśl sobie, że szukasz loginów
za pomocą wyszukiwania binarnego. Co się stanie, gdy dodasz nowych użytkowników do tablicy?
"""

# Wady tablicy to długi czas wstawiania i usuwania elementów. Jeśli loginy są wyszukiwane za pomocą wyszukiwania
# binarnego, tablica musi być posortowana. Jeśli dodamy nowego użytkownika do tablicy, za każdym razem wykonywania
# operacji powinniśmy posortować tablicę.

"""
W rzeczywistości Facebook nie przechowuje informacji ani w tablicy, ani w liście powiązanej. Zastanówmy się więc nad
hybrydową strukturą danych, czyli tablicą list powiązanych. Mamy tablicę z 26 miejscami. Każde z nich wskazuje listę
powiązaną. Pierwsze miejsce np. wskazuje listę powiązaną zawierającą wszystkie nazwy użytkowników zaczynające się na
literę a. Drugie miejsce wskazuje listę powiązaną zawierającą wszystkie nazwy użytkowników zaczynające się na literę b
itd. Powiedzmy, że na Facebooku postanawia założyć konto Adit B i chcemy dodać go do listy. Przechodzimy do pierwszego
miejsca w tablicy, następnie idziemy do wskazywanej przez niego listy powiązanej i dodajemy Adit B na końcu. A teraz
wyobraź sobie, że chcesz znaleźć użytkownika o nazwie Zakhir H. Idziemy więc do miejsca 26. w tablicy, które wskazuje
listę powiązaną zawierającą wszystkie nazwy na Z. Następnie w liście tej szukamy użytkownika Zakhir H. Porównaj tę
strukturę danych z tablicami i listami powiązanymi. Czy będzie szybsza, czy wolniejsza podczas wyszukiwania i wstawiania
danych w porównaniu z tymi strukturami? Nie musisz podawać czasów wykonywania operacji dużego O - wystarczy, że powiesz
czy ta nowa struktura będzie szybsza, czy wolniejsza.
"""

# Wstawianie elementów będzie szybsze niż w tablicach, tak samo szybkie jak w listach powiązanych. Utworzona struktura
# jest wolniejsza od tablic, jeśli chodzi o wyszukiwanie, ale szybsza od nich i tak samo szybka jak listy powiązane we
# wszystkich operacjach. Tablice i listy powiązane są cegiełkami, z którym tworzy się bardziej złożone struktury danych.
