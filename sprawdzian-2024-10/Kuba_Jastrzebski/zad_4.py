# Zdobyte punkty: 2/7

with open("dane.txt") as file:
    # wrzucenie wyniku wczytania pliku od razu do listy zaskutkowalo listą pojedynczych znakow - to moglo utrudnić Ci życie i ogarniecie tego dalej
    liczby = list(file.read().replace("\n", " "))

# no ale to by zadziałało :D ...tylko bez odfiltrowania liczb parzystych
wyniki = [int(x,2) for x in liczby]