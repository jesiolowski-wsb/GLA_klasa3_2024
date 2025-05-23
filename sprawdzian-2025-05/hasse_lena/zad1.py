def znajdz_pierwsze(n):
    tablica=[True for i in range(n+1)]
    tablica[0]=tablica[1]=False
    pierwsze=[]
    for i in range(2,int(n*0.5)+1):
        if tablica[i]:
            for j in range(i*i,n,i):
                tablica[j]=False
    pierwsze=[x for x in range(n) if tablica[x]==True]
    return pierwsze

print(znajdz_pierwsze(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(znajdz_pierwsze(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
