import random

def generuj_id():
    letters = ""
    numbers = ""
    for i in range(2):
        letters += random.choice(['A', 'B', 'C', 'D', 'E'])
    for i in range(3):
        numbers += str(random.randint(0, 9))
    return letters+numbers
print(generuj_id())