line = input().split()

distances = list(map(int,line))

spectable = ["0"]
table = []
total = 0

for city in range(1,6):
    for i in range(4):
        if city == 1:
            total += distances[i]
            spectable.append(str(total))
        elif city == 2:
            table.append(str(distances[0]))
            table.append("0")
            table.append(str(distances[1]))
            table.append(str(distances[1]+distances[2]))
            table.append(str(distances[1]+distances[3]+distances[2]))
            break
        elif city == 3:
            table.append(str(distances[0]+distances[1]))
            table.append(str(distances[1]))
            table.append("0")
            table.append(str(distances[2]))
            table.append(str(distances[2]+distances[3]))
            break
        elif city == 4:
            table.append(str(distances[0]+distances[1]+distances[2]))
            table.append(str(distances[1]+distances[2]))
            table.append(str(distances[2]))
            table.append("0")
            table.append(str(distances[3]))
            break
        elif city == 5:
            table.append(str(distances[0]+distances[1]+distances[2]+distances[3]))
            table.append(str(distances[1]+distances[2]+distances[3]))
            table.append(str(distances[2]+distances[3]))
            table.append(str(distances[3]))
            table.append("0")
            break
    
    if city == 1:
        print(" ".join(spectable))
    else:
        print(" ".join(table))
    table = []
    total = 0