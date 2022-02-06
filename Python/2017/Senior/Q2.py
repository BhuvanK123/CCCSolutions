N = int(input())
line = list(map(int, input().split()))
low_tides = []
high_tides = []
line.sort()
ans = []

if N % 2 == 0:
    for i in range(int(N/2)):
        low_tides.append(line[i])
    low_tides.sort(reverse = True)
    for i in range(int(N/2),N):
        high_tides.append(line[i])
    for i in range(int(N/2)):
        ans.append(str(low_tides[i]))
        ans.append(str(high_tides[i]))
    print(" ".join(ans))
else:
    for i in range(int(N/2)+1):
        low_tides.append(line[i])
    low_tides.sort(reverse = True)
    for i in range(int(N/2)+1,N):
        high_tides.append(line[i])
    for i in range(int(N/2)+1):
        ans.append(str(low_tides[i]))
        if i <= int(N/2)-1:
            ans.append(str(high_tides[i]))
    print(" ".join(ans))