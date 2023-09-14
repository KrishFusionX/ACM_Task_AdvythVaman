def palindrome_check(number):
    string = str(number)
    return string == string[::-1]

def largest_palindrome_product(N):
    max_palindrome=0

    for i in range (100,1000):
        for j in range (i,1000):
            product = i*j

            if product >= N:
                break

            if palindrome_check(product):
                max_palindrome = max(max_palindrome, product)
            
    return max_palindrome

T = int(input())
for _ in range(T):
    N = int(input())
    result = largest_palindrome_product(N)
    print(result)