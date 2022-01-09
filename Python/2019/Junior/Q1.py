A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

Asum = A3*3 + A2*2 + A1
Bsum = B3*3 + B2*2 + B1

if Asum == Bsum:
    print("T")
elif Asum < Bsum:
    print("B")
elif Asum > Bsum:
    print("A")