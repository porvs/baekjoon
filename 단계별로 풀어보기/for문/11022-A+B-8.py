import sys
t = int(sys.stdin.readline())
ct = 1
for i in range(t):
    a, b = sys.stdin.readline().split()
    print("Case #{0}: {1} + {2} = {3}".format(ct, a, b, int(a)+int(b)))
    ct += 1
