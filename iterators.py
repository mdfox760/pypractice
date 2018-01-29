for element in [1, 2, 3]:
    print("Element in brackets:", element)

for element in (1, 2, 3):
    print("Element in parens:", element)

for key in {'one':1, 'two':2}:
    print("Key in braces:", key)

for char in "123":
    print("Char:", char)

for line in open("myfile.txt"):
    print(line, end='')
