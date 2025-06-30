print("hello world")
print(4*8)

for loopCounter in range(5,21,1):
    counterIsEven = (loopCounter % 2) == 0
    if counterIsEven:
        print(f'{loopCounter} is even')
    else:
        print(f'{loopCounter} is odd')