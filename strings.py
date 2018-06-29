print('I love eggs.')
print('doesn\'t')
print("doesn't")
# The one below has an indention in the output
print(' "Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

s = 'First line. \nSecond line.'
print(s)

# Sometimes you don't want backslash to escape the next character, like with file names.
print('C:\some\name') # This will make a new line
print(r'C:\some\name') # Note the r before the quote

# multi line strings
print("""\
Usage: thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to
""")

# These concatenate (join together)
print(3 * 'un' + 'ium')
print('Py' 'thon')

prefix = 'Py'
suffix = 'thon'
print(prefix + 'thon')
print(prefix + suffix)

text = ('Put several strings within parens '
        'to have them join together.')
print(text)

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-2], word[-6]) # Last character, second-last character, first character.
# slicing
print(word[0:2]) # returns 'Py'
print(word[2:5]) # returns 'tho', prints characters starting from 3rd to 5th
print(word[:2] + word[2:])
print(word[:4] + word[4:]) # both return 'Python'
print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
print(word[0]) # prints first character
print(word + " TEST") # concatenates string with a space before TEST.
# Python strings are immutable
s = 'supercalifragilisticexpialidocious'
print(len(s))

# I thought this would print
print(s.center) # returns <built-in method center of str object at 0x10b959088>

# Using f before the quotation marks adds something familiar. 
name = "Matt"
likes = "programming for a hobby"
languages = "Ruby and Python"

print(f"My name is {name}. I like {likes}. My favorite languages are {languages}.")
