from array import array

ar = list(map(int, input().split()))

ar1 = sorted(ar)

max = ar1[1] + ar1[2] + ar1[3] + ar1[4]
min = ar1[0] + ar1[1] + ar1[2] + ar1[3]

if len(ar)==5:
    print(min,max)


