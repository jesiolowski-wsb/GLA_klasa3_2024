def rysuj_wisielca(liczba_pomylkek):
    etapy = [
        '''
           ------
           |    |
                |
                |
                |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
                |
                |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
           |    |
                |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
          /|    |
                |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
          /|\   |
                |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
          /|\   |
          /     |
                |
        ________|
        ''',
        '''  
           ------
           |    |
           O    |
          /|\   |
          / \   |
                |
        ________|
        '''
    ]
    # szkoda ze uzyles print a nie return, ale strasznie podoba mi sie idea ascii-art :D
    print(etapy[liczba_pomylkek])

def gra_w_wisielca():
    slowo = input("podaj słowo do odgadnięcia: ")
    ukryte_slowo = ['_'] * len(slowo)
    proby = 6
    juz_odgadniete = set()

    # zmienna nigdzie nie jest wykorzystywana
    zgadywane = set()
    print("Spróbuj odgadnąć słowo.")

    # fajny pomysl ze sprawdzaniem czy istnieje jeszcze jakis podkreslnik
    # ale co w wuypadku gdy w haśle jest podkreślnik (tj. jako czesc hasła) :D?
    # nigdy nie bedziemy w stanie zakonczyc gry z sukcesem
    while proby > 0 and '_' in ukryte_slowo:
        print("\nAktualny stan słowa:", " ".join(ukryte_slowo))
        print(f'Pozostałe próby: {proby}')
        # fajne zadbanie aby dzialaly i male i duze literki!
        litera = input("Podaj literę: ").lower()
        # gratki za znajomość isalpha(), ale co z wymysleniem hasla? tam mozemy zrobić !@#$%
        if len(litera) != 1 or not litera.isalpha():
            print("Proszę podać tylko jedną literę.")
            continue
        if litera in juz_odgadniete:
            print("Już podałeś tę literę. Spróbuj inną.")
            continue
        juz_odgadniete.add(litera)
        if litera in slowo:
            print(f"Litera '{litera}' jest w słowie.")
            for i, lit in enumerate(slowo):
                if lit == litera:
                    # świetnie! jeden z bardziej czytelnych mechanizmow podmiany liter ktore widzialem
                    ukryte_slowo[i] = litera
        else:
            proby -= 1
            print(f"Litera '{litera}' nie znajduje się w słowie.")
            # pierdołka - w wypadku zmiany ilośći prób trzeba będzie pamiętc aby zmienic to w dwoch miejscach
            # fajniej byloby wyciagnac ten element do osobnej zmiennej
            rysuj_wisielca(6 - proby)
    if '_' not in ukryte_slowo:
        print("Gratulacje! Odgadłeś słowo:", slowo)
    else:
        print("nie udało się. Słowo to:", slowo)
gra_w_wisielca()
