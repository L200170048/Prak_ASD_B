#a
def cek(v,n):
    a = [[v for i in range(v)] for j in range(n)]
    for i in a:
        print (i)
    if v == n:
        print('konsisten')
    else:
        print ('tidak konsisten')

#b
def ukuran(v,n):
    a = [[v for i in range(v)] for j in range(n)]
    for i in a:
        print (i)
    print('matriks ',v, ' x ' ,n)

#c
def menjumlahkan(v,n):
    a = [[n for i in range(v)] for j in range(n)]
    for i in a:
        print (i)
    print('\n',' + \n')

    b = [[v for i in range(v)] for j in range(n)]
    for i in b:
        print (i)
    print('\n','Hasil dari penjumlahan adalah ')

    c = v + n
    d = [[c for i in range(v)] for j in range(n)]
    for i in d:
        print (i)

#d
def mengalikan(v,n):
    a = [[n for i in range(v)] for j in range(n)]
    for i in a:
        print (i)
    print('\n',' x \n')

    b = [[v for i in range(v)] for j in range(n)]
    for i in b:
        print (i)
    print('\n','Hasil dari perkalian adalah ')

    c = v * n
    d = [[c for i in range(v)] for j in range(n)]
    for i in d:
        print (i)

#e
def determinan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determinan(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total


z = [[3,1],[2,5]]
x = [[1,2,1],[3,3,1],[2,1,2]]
v = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
r = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]
d = [[3,4],[2,4],[1,5]]
e = [[5,6,7],[7,8,9]]
print("Ini hasil yang determinan")
print(determinan(z))
print(determinan(x))
print(determinan(v))
print(determinan(r))
print(determinan(d))
print(determinan(e))
