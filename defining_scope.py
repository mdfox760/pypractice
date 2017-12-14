i = 5 # sets variable

def f(arg=i): # sets a default variable and prints it
    print(arg)
    
i = 6 # resets variable but doesn't work because of default variable is set which overrides the reset. 
f()

def g(a, L=[]):
    L.append(a)
    return L
    
print(g(1))
print(g(2))
print(g(3)) # Returns arrays of [1], [1,2], [1,2,3], repectfully.

def x(a, L=None): # This doesn't allow the default to be shared between calls.
    if L is None:
        L = []
    L.append(a)
    return L
    
print(x(1))
print(x(2))
print(x(3)) 