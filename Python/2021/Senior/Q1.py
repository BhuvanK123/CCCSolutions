N = int(input()) #number of shapes
heights = input().split()
widths = input().split()

answers = []
x = 0

for i in widths:
    ans = int(i) * (int(heights[x])+int(heights[x+1]))/2
    answers.append(ans)
    x = x + 1

sumOfList = sum(answers)

print(sumOfList)