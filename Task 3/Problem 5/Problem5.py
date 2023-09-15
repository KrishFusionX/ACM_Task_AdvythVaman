def prime_factors(n):
    pfactors=[]
    divisor = 2

    while n>1:
        while n%divisor == 0:
            pfactors.append(divisor)
            n//=divisor
        divisor += 1
    return pfactors

T = int(input())

for _ in range(T):
    N = int(input())
    primefs = prime_factors(N)
    x = max(primefs)
    print(x)
