from random import shuffle
# get path to internal mac dictonary
# can redirect this to any text file with a new word on each line
wordPath = '/usr/share/dict/words'
# open it as a file and read it into a list
with open(wordPath,encoding="utf-8") as wordsFile:
    words = wordsFile.readlines()
    # randomize the word order
    shuffle(words)
    # keep track of how many word we process 
    tick = 0
    # loop through the words
    for word in words:
        # remove any whitespace
        word = word.strip()
        # print word if it meets a conditional
        # match length and the last two letters
        if len(word) == 5 and word[-2:] == 'gy':
            print(word)
        # if we hit a limit, break the loop
        # this prevents the script from running too long
        if tick > 50:
            break