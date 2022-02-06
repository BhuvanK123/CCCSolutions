N = int(input())
k = int(input())

total = N

for i in range(k):
    N = N * 10
    total += N

print(total)