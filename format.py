# Inserting variable into a string.
first_name = "Matt"
last_name = "Fox"
full_name = "Matt Fox"

str = "My first name is "
# print (str) # This works
# These all work.
print ("My first name is {}.".format(first_name)) # This works.
print ("My last name is {}.".format(last_name)) # This works.
print ("My full name is {}.".format(full_name)) # This works.
print ("{} is my first name.".format(first_name))
print ("{} is my last name.".format(last_name))
print ("{} is my full name.".format(full_name))
print ("My first name is {} and it is an okay name.".format(first_name))
print ("My last name is {} and it is an okay name.".format(last_name))
print ("My full name is {} and it is an okay name.".format(full_name))

# It works this way too.
garden = "I love {}."
print(garden.format("my garden")) # This works

pizza = "I want {}."
print(pizza.format("pizza."))

new_open_string = "Sammy loves {} {}."                      #2 {} placeholders
print(new_open_string.format("open-source", "software"))    #Pass 2 strings into method, separated by a comma

# This section works
tool_inventory = 20
print(tool_inventory)
cake_inventory = 12
print(cake_inventory)
total_inventory = 32
print(total_inventory)
print("Matt ate {0:.0f} percent of a pizza.".format(50))
print("*****")
# This section works.
tool_string = "Tool Inventory: {} ".format(tool_inventory)
# print("Tool Inventory: {}".format(tool_inventory)) # Works
print(tool_string)
print("*****")
cake_string = "Cake Inventory: {} ".format(cake_inventory)
print(cake_string)
print("******")
all_inventory = "Total Inventory: {} today.".format(total_inventory) # works
print(all_inventory) # works

# Field size after the colon
print("Total Tool Inventory: {0:4} red {1:16}".format(5, "Belts"))
# Left align number and center the string.
print("Sammy has {0:<4} red {1:^16}".format(5, "ballons"))
# Adding asterisks
print("{:-^20s}".format("Kyle"))
# Add parameters
print("Matt ate {0:5.0f} percent of a pizza.".format(50))

party_guests = 20
print("We need {} party guests to show up.".format(party_guests))

# loop
for i in range(3,13):
    print(i, i*i, i*i*i)

# make space for the output
for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
