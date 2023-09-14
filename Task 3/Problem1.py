limit = 100
elements = input()
list = elements.split()
list = [int(item) for item in list]
list = [x if -100 <= x <= 100 else 0 for x in list]
oddsum=sum([num for num in list if num%2!=0])

if len(list) <= limit:

    print(oddsum)

    
        

