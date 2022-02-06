month = int(input())
date = int(input())

if month < 2:
    print("Before")
elif month > 2:
    print("After")
else:
    if date < 18:
        print("Before")
    elif date > 18:
        print("After")
    else:
        print("Special")