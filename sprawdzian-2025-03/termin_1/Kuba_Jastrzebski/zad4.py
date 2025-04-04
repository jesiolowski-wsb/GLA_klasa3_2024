from statistics import median
with open('liczby.txt', 'r') as file:
    liczby = [int(i.strip()) for i in file.readlines()]

with open('wyniki_liczby.txt', 'w') as file:
    file.write("Zadanie 4.1:\n")
    for i in liczby:
        file.write(f"{i} -> binarnie: {bin(i)[2:]}, hex: {hex(i)[2:].upper()}\n")
    file.write("Zadanie 4.2:\n")
    file.write(f"Średnia: {sum(liczby) / len(liczby)}\nMediana: {median(liczby)}\nStatystyki cyfr:\n")
    for j in range(10):
        file.write(f"{j}: {sum([str(i).count(str(j)) for i in liczby])}\n")
