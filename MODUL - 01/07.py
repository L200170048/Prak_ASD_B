def faktorPrima(n):
    kampret = []
    i=2
    while i <= n:
        if n%i == 0:
            n = n/i
            kampret.append(i)
        else:
            i += 1
    heu = tuple(kampret)
    print(heu)
