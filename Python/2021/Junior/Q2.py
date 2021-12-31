Hname = None
Hbid = 0

N = int(input())

for i in range(N):
    name = input()
    bid = int(input())
        
    if bid > Hbid:
        Hbid = bid
        Hname = name

print(Hname)