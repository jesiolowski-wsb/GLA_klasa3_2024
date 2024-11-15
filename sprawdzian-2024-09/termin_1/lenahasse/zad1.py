while True:
    dane = input('Podaj liczby i operatora w formacie: liczba1 operator liczba2 (pamiętaj o spacji!)')
    czesci = dane.split()
    if dane =="quit":
        print('kalkulator zamkniety')
        break
    elif len(czesci)!=3:
        print('Podałeś złe liczby')
        break
    elif czesci[1]=='+':
        print(int(czesci[0])+int(czesci[2]))
    elif czesci[1]=='-':
        print(int(czesci[0])-int(czesci[2]))
    elif czesci[1]=='*':
        print(int(czesci[0])*int(czesci[2]))
    elif czesci[1]=='/':
        print(int(czesci[0])/int(czesci[2]))