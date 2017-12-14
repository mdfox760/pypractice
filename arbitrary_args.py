# Least frequently used option for args
#def write_multiple_items(file, separator, *args):
#    file.write(separator.join(args))
 
# write_multiple_items()  # returns TypeError: write_multiple_items() missing 2 required positional arguments: 'file' and 'separator' 
# print(write_multiple_items) # returns object
# write_multiple_items("py_args.txt", "/") returns errors

def concat(*args, sep = "/" ):
    return sep.join(args)
    
print(concat("earth", "mars", "venus")) # returns earth/mars/venus
print(concat("earth", "mars", "venus", sep=".")) # returns earth.mars.venus