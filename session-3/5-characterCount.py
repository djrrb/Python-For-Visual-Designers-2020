myText = """Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."""

# split the string into a list 
words = myText.split(' ')
# use the len() function to give us the length of the list
print(len(words), 'words')
# and then a length of the string itself
print(len(myText), 'chars')