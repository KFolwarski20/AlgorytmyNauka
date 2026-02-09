"""
Powiedzmy, że możemy ukraść jeszcze jeden produkt - odtwarzacz MP3. Urządzenie waży 1 kg i kosztuje 1000 zł.
Czy warto je brać?
"""

# Odpowiedź: Tak. Warto brać MP3, ponieważ będziemy mogli ukraść MP3, IPhone i gitarę o łącznej wartości 4500 zł.

"""
Jedziesz na biwak. Masz plecak o obciążeniu 6 kg i możesz zabrać przedmioty z poniższej listy. Każdy z nich ma
określoną wartość. Im ona wyższa, tym ważniejszy jest dany produkt.
Woda: 3 kg, 10
Książka: 1 kg, 3
Jedzenie: 2 kg, 3
Kurtka: 2 kg, 5
Aparat: 1 kg, 6
Jaki jest optymalny zestaw przedmiotów do zabrania na wycieczkę?
"""

# Odpowiedź: Woda, kurtka, aparat. Wartość zestawu = 21.

"""
if word_a[i] == word_b[j]:              # Litery pasują
    cell[i][j] = cell[i-1][j-1] + 1
else:                                   # Litery nie pasują
    cell[i][j] = 0
"""

"""
if word_a[i] == word_b[j]:              # Litery są takie same
    cell[i][j] = cell[i-1][j-1] + 1
else:                                   # Litery są różne
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
"""


"""
Narysuj i wypełnij danymi siatkę do obliczania najdłuższego wspólnego łańcucha dla napisów blue i clues.
"""

# Odpowiedź:

#   | B | L | U | E
# C | 0 | 0 | 0 | 0
# -------------------
# L | 0 | 1 | 0 | 0
# -------------------
# U | 0 | 0 | 2 | 0
# -------------------
# E | 0 | 0 | 0 | 3
# -------------------
# S | 0 | 0 | 0 | 0

# Najdłuższy wspólny łańcuch wynosi 3.

