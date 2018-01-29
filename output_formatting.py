import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']],[['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped liens."""

print(textwrap.fill(doc, width=40))

# This part didn't work. Traceback follows
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
conv = locale.localeconv() # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, groupig=True)
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
'$1,234,567.80'

# Traceback (most recent call last):
#  File "output_formatting.py", line 13, in <module>
#    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# File "/usr/local/Cellar/python3/3.6.4/Frameworks/Python.framework/Versions/3.6/lib/python3.6/locale.py", line 598, in setlocale
#    return _setlocale(category, locale)
# locale.Error: unsupported locale setting
