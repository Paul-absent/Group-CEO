myName = input("Please type your name:")
print(f'Hello {myName}')

rawHeight = input("Please type in your height in CMs: ")
myHeight = int(rawHeight)
booleanA = myHeight > 140

booleanB = (myHeight % 2) == 0
booleanC = booleanA and booleanB

print(booleanC)
print(f'Your height is {myHeight}cms')
