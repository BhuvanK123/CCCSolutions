row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))
row3 = list(map(int,input().split()))
row4 = list(map(int,input().split()))
col1 = [row1[0],row2[0],row3[0],row4[0]]
col2 = [row1[1],row2[1],row3[1],row4[1]]
col3 = [row1[2],row2[2],row3[2],row4[2]]
col4 = [row1[3],row2[3],row3[3],row4[3]]

if sum(row1) == sum(row2) == sum(row3) == sum(row4):
    if sum(col1) == sum(col2) == sum(col3) == sum(col4):
        print("magic")
    else:
        print("not magic")
else:
    print("not magic")