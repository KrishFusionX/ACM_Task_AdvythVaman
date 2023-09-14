def chocolatefeast(n,c,m):
    chocolates_bought=n//c
    wrappers = chocolates_bought
    while wrappers>=m:
        extrachocs=wrappers//m
        wrappers = wrappers % m + extrachocs
        chocolates_bought += extrachocs

    return chocolates_bought

t = int(input())
for _ in range(t):
    n,c,m = map(int, input().split())
    result = chocolatefeast(n,c,m)
    print(result)
