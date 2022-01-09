L = int(input())

string = []

for i in range(L):
    code = input().split()
    for i in range(int(code[0])):
        string.append(code[1])
    print("".join(string))
    string = []