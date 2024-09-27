# wynik: 7/7 pkt

while True:
    dane = input('Podaj liczby i operatora w formacie: liczba1 operator liczba2 (pamiętaj o spacji!)')
    czesci = dane.split()
    # a może if dane.lower() =="quit":
    if dane =="quit":
        print('kalkulator zamkniety')
        break
    # genialny sposób sprawdzenia czy parametry się zgadzają
    # w dodatku bez potrzeby angazowania try-except :)
    elif len(czesci)!=3:
        print('Podałeś złe liczby')
        break
    elif czesci[1]=='+':
        # zastanowiłbym się czy nie warto zawrzeć całego skryptu w funkcji tj.
        # rzucanie 'printami' na lewo i prawo jest ciut nieeleganckie :)
        print(int(czesci[0])+int(czesci[2]))
    elif czesci[1]=='-':
        print(int(czesci[0])-int(czesci[2]))
    elif czesci[1]=='*':
        print(int(czesci[0])*int(czesci[2]))
    elif czesci[1]=='/':
        print(int(czesci[0])/int(czesci[2]))
    # może jakiś 'else' dla pokrycia nieobsługiwanych operatorów?