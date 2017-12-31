# The brackets in the string is replaced by the arguement after format.
print ("The kid has {} ballons.".format(5))

open_string = "Matt loves {}."
print(open_string.format("open source"))

# Formatters can handle multiple replacements with more brackets in the
# string with more values given.
new_open_string = "Matt loves {} {}."                      #2 {} placeholders
print(new_open_string.format("open-source", "software"))    #Pass 2 strings
# into method, separated by a comma

matt_string = "Matt loves {} {}, and has {} {}."                      #4 {} placeholders
print(matt_string.format("open-source", "software", 5, "balloons"))    #Pass 4
# strings into method

# You can use index numbers to determine what value goes where, otherwise it
# will default to the order given.
print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))

# We can include more parameters within the curly braces of our syntax.
# We’ll use the format code syntax {field_name:conversion}, where field_name
# specifies the index number of the argument to the str.format() method that
# we went through in the reordering section, and conversion refers to the
# conversion code of the data type that you’re using with the formatter.
# The conversion type refers to the the single-character type code that Python
# uses. The codes that we’ll be using here are s for string, d to display
# decimal integers (10-base), and f which we’ll use to display floats with
# decimal places.
# Let’s look at an example where we have an integer passed through the method,
# but want to display it as a float by adding the f conversion type argument:
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))

# In the example above, there are a lot of numbers displaying after the decimal
# point, but you can limit those. When you are specifying f for float values,
# you can additionally specify the precision of that value by including a full
# stop . followed by the number of digits after the decimal you would like to
# include. If Sammy ate 75.765367% of the pizza, but we don’t need to have a
# high level of accuracy, we can limit the places after the decimal to 3 by
# adding .3 before the conversion type f:
print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))

# If you wanted just one decimal place, change the .3 in the line above to .1
# and if you want to lose the decimal places use .0

# You can add padding to the returned text by using < for left align, ^ for
# centered align and > for right aligned text.
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))
print("Sammy has {0:<2} red {1:^8}!".format(5, "balloons"))

# By default, when we make a field larger with formatters, Python will fill
# the field with whitespace characters. We can modify that to be a different
# character by specifying the character we want it to be directly following
# the colon:

print("{:*^20s}".format("Sammy"))


# You can pass values into variables and combine parameters.
sammy = "Sammy has {} balloons today!"
nBalloons = 8
print(sammy.format(nBalloons))

# You can use format to align columns. In a loop:
for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

# To accomodate larger numbers:
for i in range(3,13):
    print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))
