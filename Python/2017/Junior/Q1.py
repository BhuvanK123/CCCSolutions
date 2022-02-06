x = int(input())
y = int(input())

if x > 0 and y > 0: #If x and y are positive
    print(1)
elif x < 0 and y < 0: #If x and y are negative
    print(3)
elif x > 0 and y < 0: #If x is positive and y is negative
    print(4)
elif x < 0 and y > 0: #If x is negative and y is positive
    print(2)