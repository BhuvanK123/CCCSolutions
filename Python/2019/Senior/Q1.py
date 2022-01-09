flips = input()

myList = [1,2,3,4]
newList = []

for letter in flips:
    if letter == "H":
        newList.append(myList[2])
        newList.append(myList[3])
        newList.append(myList[0])
        newList.append(myList[1])
        myList = newList
        newList = []
    elif letter == "V":
        newList.append(myList[1])
        newList.append(myList[0])
        newList.append(myList[3])
        newList.append(myList[2])
        myList = newList
        newList = []

print(myList[0], myList[1])
print(myList[2], myList[3])