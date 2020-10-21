# define a list using square brackets
# a list is a sequence of other objects
myList = ['apples', 'oranges', 'bananas', 'cherries']
print(myList)

# loop through the list
print('---')
for groceryItem in myList:
    print(groceryItem)
print('---')

# print the second item from the list
print(myList[1])

# print the last two items from the list
print(myList[-2:])

# replace the fourth item with peaches
myList[3] = 'peaches'

# sort the list
myList.sort()
print(myList)

# reverse the list
myList.reverse()
print(myList)

