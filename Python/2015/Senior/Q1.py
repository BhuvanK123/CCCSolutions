K = int(input())
myList = []
for i in range(K):
    line = int(input())
    if line == 0:
        myList.pop(-1)
    else:
        myList.append(line)
print(sum(myList))