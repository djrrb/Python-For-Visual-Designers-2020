print('let’s do some math with numbers')
print(16 // 5)
print(16 % 5)
# but we had to type 16 twice and 5 twice, what a pain to change!

print('now let’s do the same thing with variables')

# we only type these numbers once
bigNum = 16
littleNum = 5

# and now we just reference them
howMany = bigNum // littleNum
remainder = bigNum % littleNum
print( howMany )
print( remainder )