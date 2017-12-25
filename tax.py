# works in python3.6 interpreter on cli.
# In interactive mode, the last printed expression is assigned to the variable _.
# The variable should be treated as read only by the user. Don't explicityly assigned
# a value to it. You would create an independent local variable with the same
# name masking the built-in variable with its magic behavior.

tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)
