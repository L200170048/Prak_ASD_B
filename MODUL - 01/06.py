def apakahPrima(n):
    n =  int(n)
    assert n >=0
    primaKecil = [2, 3, 5, 7, 11]
    bukanPrKecil = [0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
                break
        else:
            return True
        
# No 6

for i in range(2, 1001):
    if apakahPrima(i) == True:
        print(i)
