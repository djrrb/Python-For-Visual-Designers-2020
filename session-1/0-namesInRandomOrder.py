# this is the silly script I wrote at the beginning of class
# to randomize the order of names
# but here I have saved it with fake names

# import our friend the random Library
# we will use it to randomize the order of the names
import random

# i just copy/pasted the names from a spreadsheet so they came in this big ugly text block
# i used three quotes """ to designate a multi-line string
theNames = """Fidela    Laws
Angelica    Courtney
Jess    Bouck
Carley  Vallone
Cameron Balmer
Newton  Panella
Ardith  Eggleston
Genaro  Hilson
Vanetta Cockrill
Valentine   Mccleary
Buddy   Choiniere"""

# to convert these names into a proper python list, we will split the string every time we encounter a newline ('\n')
namesList = theNames.split('\n')

# now that we have a list, we can put its contents in a random order using the shuffle() function, which lives in the random library
random.shuffle(namesList)

# now that the list is randomized
# we can loop through it and print each result in the random order
# for each name in our list, we will assign it to the variable theName
for theName in namesList:
    # i only want to print first names
    # so I will split the name by tabs, and grab the first item from that list
    firstName = theName.split('\t')[0]
    # ok let’s print the first name
    print(firstName)