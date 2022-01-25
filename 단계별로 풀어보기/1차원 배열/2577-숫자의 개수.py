a = int(input())
b = int(input())
c = int(input())
Count = 0

Sum = a * b * c
num_list = list(map(int, str(Sum)))
for i in range(10):
    print(num_list.count(Count))
    Count += 1
