import sys

T = int(sys.stdin.readline())

def is_prime(num):
    if num > 1:
        i = 2

        while i*i <= num:
            if num % i == 0:
                return False

            i += 1
        return True

    else:
       return False

x = 1

for i in range(T):
    line = int(sys.stdin.readline())*2

    for i in range(line):
        y = line - x
        if is_prime(x)==True:
            if is_prime(y)==True:
                print(x,y)
                break
        x = x + 1
    x = 1
    y = 0