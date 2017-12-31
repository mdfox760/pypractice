# Fibonacci numbers module: goes with fibo.py

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
# When you run it like: python3.6 fibo.py <arguments>
# the code in the module will be executed, just as if you imported it, but with
# the __name__ set to "__main__". That means that by adding this code at the
# end of your module:

# if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))
#
# you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:
