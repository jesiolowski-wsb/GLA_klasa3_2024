# zdobyto punktów: 4/20

# zadanie 1
# zdobyte punkty: 4/6
# 1
def czujniki_ruchu(czujnik1, czujnik2):
    # zbędny if-else, wystarczyłobv `return czujnik1 or czujnik2`
    if czujnik1 or czujnik2:
        return True
    else:
        return False
    # kod po return nigdy się nie wykona
    if czujniki_ruchu(czujnik1, czujnik2):
        print("wykryto ruch")
    else:
        print("brak ruchu")

# 2
def drzwi_bezpieczne(zamek_glowny, zamek_awaryjny):
    # zbędny if-else. wystarczyłoby `return zamek_glowny and zamek_awaryjny`
    if zamek_glowny and zamek_awaryjny:
        return True
    else:
        return False
    # kod po return nigdy się nie wykona
    if drzwi_bezpieczne(zamek_glowny, zamek_awaryjny):
        print("drzwi sa bezpieczne")
    else:
        print("drzwi nie sa bezpieczne")

# 3
def wykryj_awarie(status_systemu):
    return not status_systemu
    # kod po return nigdy się nie wykona
    if wykryj_awarie(status_systemu):
        print("system nie dziala prawidlowo")
    else:
        print("system dziala")

# 4
def alarm_przeciwpozarowy(czujnik_dymu, czujnik_temperatury):
    # brawo za poprawnie zaimplementowaną logikę
    return (czujnik_dymu or czujnik_temperatury) and not (czujnik_dymu and czujnik_temperatury)
    # kod po return nigdy się nie wykona
    if alarm_przeciwpozarowy(czujnik_dymu, czujnik_temperatury):
        print("alarm wlaczony, wykryto zagrozenie")
    else:
        print("alarm wylaczony")
