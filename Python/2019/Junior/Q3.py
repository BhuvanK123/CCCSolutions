N = int(input())

myList = []

for i in range(N):
    line = input()

    prev = line[0]
    counter = 0

    for letter in line:
        if prev == letter:
            counter = counter + 1
        elif prev != letter:
            myList.append(str(counter))
            myList.append(prev)
            counter = 1
            prev = letter
    myList.append(str(counter))
    myList.append(prev)
    counter = 1
    prev = letter

    print(" ".join(myList))

    myList = []