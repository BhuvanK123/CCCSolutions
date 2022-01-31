N = int(input())
yest = input()
today = input()
counter = 0

for i in range(N):
    if yest[i] == "C" and today[i] == "C":
        counter = counter + 1
    else:
        pass
print(counter)