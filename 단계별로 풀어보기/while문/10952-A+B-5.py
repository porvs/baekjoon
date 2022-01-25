import sys

while True:
    a, b = sys.stdin.readline().split()
    if int(a) and int(b) > 0:
        print(int(a) + int(b))
    else:
        break
