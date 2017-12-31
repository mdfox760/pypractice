# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# You can import the fibo module in the interpreter by using 'import fibo'
# then you can enter something like: fibo.fib(1000) and fibo.fib(100)
# If you intend to use a function often you can assign it to a local name:
# fib = fibo.fib
# fib(500)
