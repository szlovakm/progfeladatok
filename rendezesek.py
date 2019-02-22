def buborek(tomb):
    n = len(tomb)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if tomb[j] > tomb[j+1]:
                tomb[j], tomb[j+1] = tomb[j+1], tomb[j]
    return tomb

def kivalaszt(tomb):
    n = len(tomb)
    for i in range(n-1):
        minindex = i
        for j in range(i+1, n):
            if tomb[j] < tomb[minindex]:
                minindex = j
        tomb[i], tomb[minindex] = tomb[minindex], tomb[i]
    return tomb

def main():
    print("Kérek szóközzel elválasztott egész számokat:")
    be = [ int(x) for x in input().split() ]
    print("buborékrendezéssel rendezve:")
    print(buborek(be))
    #print("kiválasztásos rendezéssel rendezve:")
    #print(kivalaszt(be))

main()
