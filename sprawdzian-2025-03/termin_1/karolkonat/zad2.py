def wydaj_reszte(kwota, n):
    n.sort(reverse=True)
    bs = {}
    for b in n:
        while kwota-b >= 0:
            if not b in bs:
                bs[b] = 1
            else:
                bs[b] += 1
            kwota -= b
        if kwota == 0:
            return bs
    else:
        print("No sie nie da")
        return None

print(wydaj_reszte(142, [1, 5, 10, 25, 100]))
print(wydaj_reszte(8, [5, 10, 25]))
