from time import time
bub = 0

def buborek(tomb):
    global bub
    t1 = time()
    n = len(tomb)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if tomb[j] > tomb[j+1]:
                tomb[j], tomb[j+1] = tomb[j+1], tomb[j]
    t2 = time()
    bub = t2-t1
    return tomb

def kivalaszt(tomb):
    global kiv
    t1 = time()
    n = len(tomb)
    for i in range(n):
        minindex = i
        for j in range(i+1, n):
            if tomb[j] < tomb[minindex]:
                minindex = j
        tomb[i], tomb[minindex] = tomb[minindex], tomb[i]
    t2 = time()
    kiv = t2-t1
    return tomb

def pyrend(tomb):
    global pyr
    t1 = time()
    tomb.sort()
    t2 = time()
    pyr = t2-t1
    return tomb

def main():
    print("Kérek szóközzel elválasztott egész számokat:")
    be = [ int(x) for x in input().split() ]
    be2 = be.copy()
    be3 = be.copy()
    print(id(be), id(be2), id(be3))
    print(be[0])
    print("Rendezve:")
    print("buborek")
    print(buborek(be)[0])
    print(be2[0])
    print("kivalasztas")
    print(kivalaszt(be2)[0])
    print(be3[0])
    print("python")
    print(pyrend(be3)[0])
    print(be3[0])
    print(bub)
    print(kiv)
    print(pyr)
main()
