def Ltav(str1, str2, h1, h2):
    # ha str1 üres, akkor h2 db beszúrás kell
    if h1 == 0:
        return h2
    # ha str2 üres, akkor h1 db beszúrás kell
    if h2 == 0:
        return h1
    # ha az utolsó karakterük megegyezik, akkor
    # a maradék előző karakterekkel kell kezdeni
    # valamit
    if str1[h1-1] == str2[h2-1]:
        return Ltav(str1, str2, h1-1, h2-1)
    # ha az utolsó karakterek különböznek, akkor
    # a három művelet közül a minimális költségűt
    # választjuk
    return 1 + min(Ltav(str1, str2, h1, h2-1), # beszúr
                   Ltav(str1, str2, h1-1, h2), # töröl
                   Ltav(str1, str2, h1-1, h2-1) # átír
                   )

def Ltav2(str1, str2, h1, h2):
    # készítsünk egy táblázatot, töltsük fel 0-kal
    T = [ [0 for x in range(h2 + 1)] for y in range(h1 + 1)]
    for i in range(h1 + 1):
        for j in range(h2 + 1):
            # ha str1 üres, akkor h2 db beszúrás kell
            if i == 0:
                T[i][j] = j
            # ha str2 üres, akkor h2 db törlés kell
            elif j == 0:
                T[i][j] = i
            # ha az utolsó karakterek egyeznek,
            # vizsgáljuk az eggyel rövidebb stringeket
            elif str1[i-1] == str2[j-1]:
                T[i][j] = T[i-1][j-1]
            # ha az utolsó karakterek különböznek, akkor
            # a három művelet közül a minimális kötségűt
            # választjuk
            else:
                T[i][j] = 1 + min(T[i][j-1], # beszúr
                                  T[i-1][j], # töröl
                                  T[i-1][j-1] # átír
                                  )
    return T[h1][h2]

            
                


while True:
    str1 = input("Kérem az első szót: ")
    str2 = input("Kérem a második szót: ")
    print(Ltav2(str1, str2, len(str1), len(str2)))
