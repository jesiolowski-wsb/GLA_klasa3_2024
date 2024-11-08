# Zdobyte punkty: 5/5

with open("tekst.txt", "r") as file:
    tekst = file.read().replace("\n", " ")

# akurat tutaj przekazanie parametru " " nie jest konieczne, bo spacja jest brana domyślnie
# to nie jest problem, ale chciałęm o tym powiedzieć :)
wyniki = [x for x in tekst.split(" ") if len(x) > 3 and x[0].isupper()]
print(tekst.split(" "))
with open("analiza.txt", "w") as file:
    for word in wyniki:
        file.write(f"{word}\n")