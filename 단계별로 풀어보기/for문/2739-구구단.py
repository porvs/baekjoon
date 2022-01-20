from calendar import c


a = int(input())
b = 1
for i in range(1, 10):
    print("{0} * {1} = {2}" .format(a, b, a * b))
    b += 1
