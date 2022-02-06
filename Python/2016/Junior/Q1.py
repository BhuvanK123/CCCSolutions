w_counter = 0
for i in range(6):
    line = input()
    if line == "W":
        w_counter += 1
if w_counter == 5 or w_counter == 6:
    print(1)
elif w_counter == 3 or w_counter == 4:
    print(2)
elif w_counter == 1 or w_counter == 2:
    print(3)
else:
    print(-1)