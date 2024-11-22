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
    print(etapy[liczba_pomylkek])
def gra_w_wisielca():
    slowo = input("podaj słowo do odgadnięcia")
    ukryte_slowo = ['_'] * len(slowo)
    proby = 6
    juz_odgadniete = set()
    zgadywane = set()
    print("Spróbuj odgadnąć słowo.")
    while proby > 0 and '_' in ukryte_slowo:
        print("\nAktualny stan słowa:", " ".join(ukryte_slowo))
        print(f'Pozostałe próby: {proby}')
        litera = input("Podaj literę: ").lower()
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
                    ukryte_slowo[i] = litera
        else:
            proby -= 1
            print(f"Litera '{litera}' nie znajduje się w słowie.")
            rysuj_wisielca(6 - proby)
    if '_' not in ukryte_slowo:
        print("Gratulacje! Odgadłeś słowo:", slowo)
    else:
        print("nie udało się. Słowo to:", slowo)
gra_w_wisielca()
