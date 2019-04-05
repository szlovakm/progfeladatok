def binsearch(miben, mit, kezd, veg):
    if kezd > veg:
        return -1
    kozep = (kezd + veg) // 2
    if miben[kozep] == mit:
        return kozep
    if miben[kozep] > x:
        return binsearch(miben, mit, kezd, kozep-1)
    else:
        return binsearch(miben, mit, kozep+1, veg)

lista = [ 1, 3, 5, 7, 8, 9 ]
x = 9

ind = binsearch(lista, x, 0, len(lista))
if ind > -1:
    print("Megtaláltam a(z) {}-t, indexe: {}".format(x, ind))
else:
    print("Nincs ilyen elem.")
    
