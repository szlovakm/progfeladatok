from functools import lru_cache

K = 5


#@lru_cache(maxsize=None)
def fibo(n):
    print("Ezt számolom: F({})".format(n), sep="", end=", ")
    # alap eset fibo(0) = 0, fibo(1) = 1, fibo(2) = 1
    if n < 2:
        return n
    # rekurzív eset
    else:
        return fibo(n-1) + fibo(n-2)

def fibo2(n):
    fibolista = [0, 1]
    for i in range(2, n+1):
        fibolista.append(fibolista[i-1] + fibolista[i-2])
    return fibolista[n]

def fibo3(n):
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

for i in range(K):
    print(i, fibo3(i))

for i in range(K):
    print(i, fibo2(i))

for i in range(K):
    print("\n", i, fibo(i))
    
