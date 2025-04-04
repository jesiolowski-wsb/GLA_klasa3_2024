def wydaj_reszte(kwota, nominaly):
        output = []
        old_kwota = 0
        nominaly.sort(reverse=True)
        while old_kwota != kwota:
            for i in nominaly:
                while i < kwota:
                    kwota -= i
                    output.append(i)
            if old_kwota == kwota: break
            old_kwota = kwota
        return output

#!!!!!!! NIEDOKOŃCZONE NIE DZIAŁA!!!!!!!!!!!!!!!
nominaly = [1, 5, 10, 25, 100]
nominaly.sort()
print(wydaj_reszte(142, [1, 5, 10, 25, 100]))