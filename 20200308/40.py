import sys
sys.stdin = open("input40.txt", "rt")

p1 = dict()
p2 = dict()
for a in input():
    p1[a] = p1.get(a, 0) + 1

for b in input():
    p2[b] = p2.get(b, 0) + 1

if p1 == p2:
    print('YES')
else:
    print('NO')