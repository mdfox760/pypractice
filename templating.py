from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
# Should throw KeyError: 'owner'
t.safe_substitute(d)
