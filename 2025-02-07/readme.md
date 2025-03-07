## Rozwiązywanie zadania z arkuszy maturalnych:

https://arkusze.pl/maturalne/informatyka-2018-maj-matura-rozszerzona-2.pdf

Zadanie i plik wejściowy tj. `sygnaly.txt` częścią linku https://arkusze.pl/matura-informatyka-2018-maj-poziom-rozszerzony/ (Matura informatyka – maj 2018 – poziom rozszerzony **cz.2**)

### rozwiązanie:

```python
zadanie4_1 = str()
zadanie4_2 = str()
zadanie4_3 = list()
with open("../Dane_1805/sygnaly.txt") as file:
    licznik = 1
    zadanie4_2_maksimum = 0
    for line in file:
        line = line.rstrip()
        # 4.1
        if licznik % 40 == 0:
            zadanie4_1 = zadanie4_1 + line[9]
        licznik += 1
        # 4.2
        if len(set(line)) > zadanie4_2_maksimum:
            zadanie4_2 = line
            zadanie4_2_maksimum = len(set(line))
        # 4.3
        string = "".join(sorted(line))
        if ord(string[len(string)-1]) - ord(string[0]) <= 10:
            zadanie4_3.append(line)

with open("wyniki4.txt", 'w') as file:
    file.write(f"Zadanie 4.1\n{zadanie4_1}\n\n")
    file.write(f"Zadanie 4.2\n{zadanie4_2} {zadanie4_2_maksimum}\n\n")
    file.write(f"Zadanie 4.3\n")
    for x in zadanie4_3:
        file.write(x+"\n")
```
