
# zdobyte punkty: 2/6
# ✅ Poprawne otwarcie pliku
# ✅ Poprawne stworzenie funkcji licz_wielkie_litery
# ❌ Błąd w implementacji znajdowania słowa z największą liczbą wielkich liter - lista jest inicjowana wewnątrz pętli
# ❌ Próba dostępu do 60 pierwszych linii bez sprawdzenia rzeczywistej długości pliku
# ❌ Brak implementacji znajdowania tajnej wiadomości (tylko definicja funkcji pomocniczej)
# ❌ Brak zapisu wyników do pliku

# zad1
def licz_wielkie_litery(tekst):
    return sum(1 for znak in tekst if znak.isupper())
with open ("tajny_przekaz.txt","r") as tekst:
 slowa=tekst.readlines()
 for i in range (60):
     # Inicjalizuj listę przed pętlą:
     lista=[]
     lista.append(licz_wielkie_litery(slowa[i]))
print("najwieksza liczbe duzych liter ma:",list.index(max(lista)))

def licz_wielkie_litery(tekst):
        return sum(1 for znak in tekst if znak.isupper())
def co_n_ty_znak(tekst, n, start=0):
        return tekst[start::n]

# zdobyte punkty: 2/5
# ✅ Próba implementacji algorytmu wydawania reszty
# ✅ Używa słownika do przechowywania wyników
# ❌ Funkcja nie przyjmuje listy nominałów jako parametru
# ❌ Błąd w przypisaniu: monety[100]=+a zamiast monety[100]+=a lub monety[100]=a
# ❌ Zbyt skomplikowana implementacja - wiele podobnych bloków kodu
# ❌ Niepotrzebne pobieranie kwoty od użytkownika - w zadaniu podane są przykłady

#zad2
nominaly=(1,2,5,10,20,50,100)
doreszty=int(input("podaj kwote z której chcesz reszte"))
def reszta(doreszty):
    monety={100:0,50:0,20:0,10:0,5:0,2:0,1:0}
    while doreszty>100:
        a=(doreszty - (doreszty % 100))/100
        doreszty=doreszty % 100
        monety[100]=+a
    while doreszty>50:
        a = (doreszty - (doreszty % 50)) / 50
        doreszty=doreszty % 50
        monety[50]=+a
    while doreszty>20:
        a = (doreszty - (doreszty % 20)) / 20
        doreszty=doreszty % 20
        monety[20]=+a
    while doreszty>10:
        a = (doreszty - (doreszty % 10)) / 10
        doreszty=doreszty % 10
        monety[10]=+a
    while doreszty>5:
        a = (doreszty - (doreszty % 5)) / 5
        doreszty=doreszty % 5
        monety[5]=+a
    while doreszty>2:
        a = (doreszty - (doreszty % 2)) / 2
        doreszty=doreszty % 2
        monety[2]=+a

    a = doreszty/1

    monety[1]=+a
    return(monety)
print(reszta(doreszty))

# zdobyte punkty: 2/6
# ✅ Próba implementacji sprawdzania ruchów na planszy
# ✅ Sprawdzanie granic planszy
# ❌ Błąd w nazwie zmiennej: plansz zamiast plansza w ostatnim warunku
# ❌ Funkcja drukuje wyniki zamiast zwracać wartość logiczną
# ❌ Funkcja nie przyjmuje punktu docelowego (cel_x, cel_y) jako parametrów
# ❌ Implementacja nie spełnia wymagań zadania (sprawdzenie konkretnego ruchu)

#zad3 pisze pozycje x jako y a y jako x bo to i tak nie ma znaczenia
plansza = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
def mozliwy_ruch(plansza,x,y):
    if x+1<5:
        if plansza[x + 1][y] == 0:
            print("mozna sie ruszyc na pole", x + 1, y)
        else:
            print("nie mozna sie ruszyc na pole", x + 1, y)
    else:
        print("nie mozna sie ruszyc na pole", x + 1, y)
    if y+1<5:
        if plansza[x][y + 1] == 0:
            print("mozna sie ruszyc na pole", x, y + 1)
        else:
            print("nie mozna sie ruszyc na pole", x, y + 1)
    else:
        print("nie mozna sie ruszyc na pole", x, y + 1)
    if x-1>-1:
        if plansza[x - 1][y] == 0:
            print("mozna sie ruszyc na pole", x - 1, y)
        else:
            print("nie mozna sie ruszyc na pole", x - 1, y)
    else:
        print("nie mozna sie ruszyc na pole", x - 1, y)
    if y-1>-1:
        if plansz[x][y - 1] == 0:
            print("mozna sie ruszyc na pole", x, y - 1)
        else:
            print("nie mozna sie ruszyc na pole", x, y - 1)
    else:
        print("nie mozna sie ruszyc na pole", x, y - 1)
x=0
y=0
mozliwy_ruch(plansza,x,y)
