N = int(input())
xCoords = []
yCoords = []

for item in range(N):
    currentLine = input().split(",")
    xCoords.append(currentLine[0])
    yCoords.append(currentLine[1])

xCoords.sort()
yCoords.sort()

smallX = int(xCoords[0])
tSmallX = smallX - 1 

smallY = int(yCoords[0])
tSmallY = smallY - 1

bigX = int(xCoords[-1])
tBigX = bigX + 1 

bigY = int(yCoords[-1])
tBigY = bigY + 1 

print('{},{}'.format(tSmallX, tSmallY))
print('{},{}'.format(tBigX, tBigY))