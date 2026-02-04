s = 0
t = 0
info1, math1, sci1, eng1 = map(int, input().split())
info2, math2, sci2, eng2 = map(int, input().split())

s = info1 + math1 + sci1 + eng1
t = info2 + math2 + sci2 + eng2

if s > t:
    print(s)
elif t > s:
    print(t)
elif t == s:
    print(s)