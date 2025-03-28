def wykrywanie(czujnik1,czujnik2):
    if czujnik1 == 1 or czujnik2 == 1:
        return True
    else:
        return False

def bezpieczenstwo(glowny, awaryjny):
    if glowny == 1 and awaryjny == 1:
        return True
    else:
        return False

def wykryj_awaryjne(status):
    if status == True:
        return False
    else:
        return True

def alarm_przeciwpozarowy(dymu, temp):
    if dymu == temp:
        return False
    elif dymu != temp:
        return True

def stan_systemu():
    ruch = True
    glowny = True
    awaryjny = False
    status = True
    dymu = False
    temp = True

    ruch_znaleziony = wykrywanie(ruch, False)
    zamkniete = bezpieczenstwo(glowny, awaryjny)
    awaria = wykryj_awaryjne(status)
    pozar = alarm_przeciwpozarowy(dymu, temp)

    tabela = [
        ["Czujnik ruchu", ruch_znaleziony],
        ["Drzwi bezpieczne", zamkniete],
        ["Awaria systemu" , awaria],
        ["Alarm przeciwpozarowy", pozar]
    ]
    print(tabela, ["Modul", "Stan"], end = " ")
    print("\n")
stan_systemu()

print(int(wykrywanie(0,0)), "brak ruchu")
print(int(wykrywanie(0,1)), "wykryto ruch!")
print(int(wykrywanie(1,0)), "wykryto ruch!")
print(int(wykrywanie(1,1)), "wykryto ruch!")

print(int(bezpieczenstwo(0,0)), "drzwi nie sa bezpieczne!")
print(int(bezpieczenstwo(0,1)), "drzwi nie sa bezpieczne!")
print(int(bezpieczenstwo(1,0)), "drzwi nie sa bezpieczne!")
print(int(bezpieczenstwo(1,1)), "drzwi sa bezpieczne")

print(int(wykryj_awaryjne(0)), "Nie dziala prawidlowo!")
print(int(wykryj_awaryjne(1)), "Dziala prawidlowo")

print(int(alarm_przeciwpozarowy(0,0)))
print(int(alarm_przeciwpozarowy(0,1)), "Wykryto zagrożenie!")
print(int(alarm_przeciwpozarowy(1,0)), "Wykryto zagrożenie!")
print(int(alarm_przeciwpozarowy(1,1)))
