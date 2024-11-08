# Zdobyte punkty: 4/4
# brak zapisu do pliku (-1 punkt), ale +1 punkt (ponad skalę maks 4) za świetne rozwiązanie z range

import random

def generuj_id():
    letters = ""
    numbers = ""
    # aaaaale fajny pomysł z wykonywaniem tego w range!
    for i in range(2):
        letters += random.choice(['A', 'B', 'C', 'D', 'E'])
    for i in range(3):
        numbers += str(random.randint(0, 9))
    return letters+numbers
print(generuj_id())