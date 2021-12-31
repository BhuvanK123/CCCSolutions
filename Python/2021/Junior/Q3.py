x = 0
prev = None
while x == 0:
    line = input()
    splitline = list(line)
    if line == "99999":
        break
    add = int(splitline[0])+int(splitline[1])
    if add%2 == 0 and add != 0:
        print("right "+splitline[2]+splitline[3]+splitline[4])
        prev = "right "
    elif add%2 == 1:
        print("left "+splitline[2]+splitline[3]+splitline[4])
        prev = "left "
    elif add == 0:
        print(prev+splitline[2]+splitline[3]+splitline[4])