# zdobyte punkty: 5.5/6

# ✅ Poprawne wczytanie pliku
# ✅ Poprawne znalezienie słowa z największą liczbą wielkich liter
# ✅ Poprawne utworzenie tajnej wiadomości
# ✅ Poprawne zapisanie wyników do pliku
# ❌ Brak sprawdzenia czy słowo ma co najmniej 5 liter przed próbą pobrania 5. znaku

with open("tajny_przekaz.txt", "r") as file:
    words = [i.strip() for i in file.readlines()]

old_word = ''
old_counter = 0
for i in words:
    counter = 0
    for j in i:
        if j.isupper(): counter += 1
    if counter > old_counter:
        old_counter = counter
        old_word = i


wiadomosc = ''
for i in words[9::10]:
    # dodalbym tu tego ifa
    if len(i) >= 5:
        wiadomosc += i[4]

with open('wyniki1.txt', 'w') as file:
    file.write(f"Zadanie 1.1:\n{old_word} ({old_counter} wielkie litery)\n\n")
    file.write(f"Zadanie 1.2:\n{wiadomosc}")


