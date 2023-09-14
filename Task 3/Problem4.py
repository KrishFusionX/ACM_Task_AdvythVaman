def fibonacci_sequence(limit):
    fibonacci_series = []
    a, b = 0, 1

    while a < limit:
        fibonacci_series.append(a)
        a,b = b,a+b

    return fibonacci_series

T = int(input())
for _ in range(T):
    limit = int(input())
    fib_numbers = fibonacci_sequence(limit)
    even_fib_numbers = [x for x in fib_numbers if x%2==0]
    sum_of_even = sum(even_fib_numbers)
    print(sum_of_even)


