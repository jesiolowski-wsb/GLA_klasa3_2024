# Zdobyte punkty: 1/4
# świetny początek, ale zadanie jeszcze niestety niefunkcjonalne

import random

def generuj_id():
    letters = ''.join(random.choice('ABCDE') for _ in range(2))
    numbers = ''.join(random.choice('0123456789') for _ in range(3))

with open("id.txt", "w") as file: file.write(new_id)

