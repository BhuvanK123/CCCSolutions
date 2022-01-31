N = int(input()) #number of responses
villages = []
answers = []

for i in range(N):
    V = int(input()) #Village
    villages.append(V)

villages.sort()

for i in range(1,N-1):
    ans = ((villages[i] - villages[i-1])/2) + ((villages[i+1] - villages[i])/2)
    answers.append(ans)

print(min(answers))