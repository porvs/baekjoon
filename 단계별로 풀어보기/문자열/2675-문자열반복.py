r = int(input())
for i in range(r):
    a, b = input().split()
    for x in b:
        print(x*int(a), end='')
    print()
