# if Statements
print("if Statements")
print("*******")

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
print('\n')   

# for Statements
print("for Statements")
print("*******")

words = [ 'cat', 'window', 'defenestrate' ]
for w in words:
    print(w, len(w))

print("#######")
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)

print("#######")
# range Function
print("range Function")
print("*******")
for i in range(5):
    print(i)
    
print("#######") # This didn't work. It prints like a string.
print(range(5, 10))
print(range(0, 10, 3))
print(range(-10, -100, -30))


