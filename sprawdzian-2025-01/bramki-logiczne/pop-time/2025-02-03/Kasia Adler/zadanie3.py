def wykryj_wlamanie(ruch, wibracje, godziny_otwarcia):
    return (ruch or wibracje) and not godziny_otwarcia

dane_testowe = [

    (False, False, False),
    (True, False, False),
    (False, True, False),
    (True,True,False),
    (False, False,True),
    (True,False,True),
    (False,True,True),
    (True,True,True)
]


print("Ruch | Wibracje | Godziny | Alarm")
print ("-" * 33)
for ruch, wibracje, otwarte in dane_testowe:
    alarm = wykryj_wlamanie(ruch, wibracje, otwarte)
    print(f"{int(otwarte)}    |    {int(wibracje)}    |    {int(ruch)}    |    {int(alarm)}")
