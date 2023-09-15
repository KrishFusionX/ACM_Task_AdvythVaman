from array import array
T = int(input())

for _ in range(T):

    N = int(input())

    list = array('i', range(1,N))

    multiples_of_3 = [x for x in list if x%3==0]
    multiples_of_5 = [x for x in list if x%5==0]
    multiples_of_15 = [x for x in list if x%15==0]

    x = sum(multiples_of_3) + sum(multiples_of_5) - sum(multiples_of_15)

    print(x)


 