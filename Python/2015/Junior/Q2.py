line = input()
h = line.count(":-)")
s = line.count(":-(")

if h > s:
    print("happy")
elif h < s:
    print("sad")
elif h == s and h != 0 and s != 0:
    print("unsure")
else:
    print("none")