# Fibonacci series:
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

# print function
i = 256 & 256
print("The value of i is", i)

# Keyword arguement 'end' avoids a new line. Output is horizontal.
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

# python has functions (like ruby methods)
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
fib(2000)

def fib2(n): #reurn Finonacci series up to n
    """Return a list containing the Finbonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
f100 = fib2(100) # call it
f100            # write the result. This doesn't return anything. fib2 doesn't exist to the machine.
