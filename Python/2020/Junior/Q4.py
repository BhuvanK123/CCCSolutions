T = input()
S = input()

output = "no"

for letter in S:
    if S in T:
        output = "yes"
        break
    else:
        S = S[1:] + S[0]

print(output)