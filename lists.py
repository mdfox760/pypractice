squares = [1, 4, 9, 16, 25]
print(squares)
# Supports slicing
print(squares[0])
print(squares[:])
print(squares + [36, 49, 64, 81, 100])
# Lists are mutable
cubes = [1, 8, 27, 65, 125]
print(cubes) # We can change a value in the list
cubes[3] = 64
print(cubes)
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# length works
print(len(letters))
print(letters)
# replace some letters
letters[2:5] = ['C', 'D', 'E']
print(letters)
# remove them
letters[2:5] = []
print(letters)
# clear the list
letters[:] = []
print(letters)
print(len(letters)) # len still works
# Fibonacci series: the sum of two elements defines the next. Next line is multiple assignments
# on a single line. 
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
# formatting a string
i = 256 * 256
print("The value of i is ", i) # This only works in python3
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

