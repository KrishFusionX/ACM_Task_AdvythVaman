def simpleArraySum(ar):
    total_sum=0
    
    for num in ar:
        total_sum += num
        
    return total_sum


n = int(input())
ar = list(map(int, input().split()))
result = simpleArraySum(ar)

if len(ar)==n:
    print(result)



    

