n = int(input())
ar = list(map(int, input().split()))
x =max(ar)
count = 0

for i in range(len(ar)):
    if ar[i] == x:
        count += 1
    
print(count)