"""
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "Znaleziono klucz!"
"""

"""
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print "Znaleziono klucz!"
"""

"""
def countdown(i):
    print i
    if i <= 0: # Przypadek podstawowy
        return
    else: # Przypadek rekurencyjny
        countdown(i-1)
"""

"""
def greet(name):
    print "Cześć, " + name + "!"
    greet2(name)
    print "Przygotowanie do pożegnania..."
    bye()
    
def greet2(name):
    print "Jak się masz, " + name + "?"
    
def bye():
    print "OK, cześć!"
"""

"""
Spójrz na poniższy stos wywołań.
Jakie informacje możesz podać na podstawie tego stosu?
Teraz zobaczymy, co się dzieje na stosie wywołań podczas wykonywania funkcji rekurencyjnej.
"""

# 1. Wywołanie funkcji greet z parametrem name = Magda
# 2. Następnie funkcja greet wywołała funkcję greet2 z parametrem name = Magda.
# 3. W tym momencie wykonywanie funkcji greet jeszcze się nie zakończyło i znajduje się ona w stanie zawieszenia.
# 4. Aktualnie wykonywane jest wywołanie funkcji greet2.
# 5. Po zakończeniu wykonywania tej funkcji następnie wznowienie wykonywania funkcji greet.


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


"""
Wyobraź sobie, że przez przypadek napisałeś nieskończoną funkcję rekurencyjną. Jak już wiesz, dla każdego wywołania 
funkcji komputer przydziela pamięć na stosie. Co się dzieje ze stosem, gdy funkcja nigdy się nie kończy?
"""

# Odpowiedź: Stos nigdy nie przestanie rosnąć. Każdy program ma przydzieloną ograniczoną ilość miejsca na stosie
# wywołań. Kiedy program wyczerpie całą dostępną mu pamięć (w końcu do tego dojdzie), ulegnie awarii z powodu błędu
# przepełnienia stosu.
