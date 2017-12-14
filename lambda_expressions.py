# small anonymous functions with lambda
def make_incrementor(n):
    return lambda x: x + n
    
f = make_incrementor(42)
print(f(0)) # returns 42
print(f(1)) # returns 43

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs) # returns [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
