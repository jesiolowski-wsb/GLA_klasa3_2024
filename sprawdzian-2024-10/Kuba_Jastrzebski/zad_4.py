with open("dane.txt") as file:
    liczby = list(file.read().replace("\n", " "))
wyniki = [int(x,2) for x in liczby]