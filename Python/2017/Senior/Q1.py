N = int(input())
swifts = list(map(int,input().split()))
semaphores = list(map(int, input().split()))

max = 0
days = 1
sum1 = 0
sum2 = 0

for i in range(N):
    sum1 += swifts[i]
    sum2 += semaphores[i]
    if sum1 == sum2:
        max = days
    days = days + 1
print(max)