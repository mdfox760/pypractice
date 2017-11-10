# Dictionaries are kind of hash-table type.
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

grades = { 'Paul': '87', 'Mary': '98', 'Sue': '100' }
grades = {
  'Paul': '87',
  'Mary': '98',
  'Sue': '100' }
print (grades)
print (grades['Paul']) # Prints the grade of Paul
print ("Paul's grade: " + grades['Paul']) # Print a nicely formatted string including Pauls grade

# English to German dictionary
en_de = { "red" : "rot", "green" : "grun", "blue" : "blau", "yellow" : "gelb" }
print (en_de)
print ("The German word for red is: " + en_de["red"])
print ("The German word for green is: " + en_de["green"])
print ("The German word for blue is: " + en_de["blue"])
print ("The German word for yellow is: " + en_de["yellow"])

# English to French dictionary
en_fr = { "red" : "rouge", "green" : "vert", "blue" : "bleu", "yellow" : "jaune" }
print (en_fr)
print ("The French word for red is: " + en_fr["red"])
print ("The French word for green is: " + en_fr["green"])
print ("The French word for blue is: " + en_fr["blue"])
print ("The French word for yellow is: " + en_fr["yellow"])

dictionaries = { "en_de" : en_de, "en_fr" : en_fr }
print (dictionaries["en_de"]["blue"])

morse = {
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
"0" : "-----",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"." : ".-.-.-",
"," : "--..--"
}

print ("A" in morse) # Returns true, small case won't work 
