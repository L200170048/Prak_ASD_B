#a
def buatnol(m,n):
    matriks = [[0 for i in range (m)] for j in range(n)]
    for baris in matriks:
        print (baris)
    print ('Matriks nol berordo ',m,' x ',n)

def buatNol(m):
    matriks = [[0 for i in range(m)] for j in range(m)]
    for baris in matriks :
        print (baris)
    print ('Matriks nol berordo ',m,' x ',m)
    
#b
def buatIdentitas(m) :
    matriks = [[1 if j==i else 0 for j in range (m)] for i in range(m)]
    for baris in matriks :
        print (baris)
    print ('Matriks nol berordo ', m, ' x ',m)


