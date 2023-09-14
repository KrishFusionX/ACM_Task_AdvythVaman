def addition_of_integer(arr, num):
    for i in range(len(arr)):
        arr[i] += num
    return arr

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

result1 = arr1
result2 = arr2

if len(arr1) == m:
    result1 = addition_of_integer(arr1,a)
if len(arr2) == n:
    result2 = addition_of_integer(arr2,b)

x = 0
for i in range(len(arr1)):
    if s <= result1[i] <= t:
        x += 1
    
y = 0
for i in range(len(arr2)):
    if s <= result2[i] <= t:
        y += 1
    
print(x)
print(y)
            

