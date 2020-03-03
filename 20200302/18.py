import sys
sys.stdin = open("input18.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

for _ in range(t):
    num, direction, cnt = map(int, input().split())
    if direction == 0:
        for _ in range(cnt):
            a[num-1].append(a[num-1].pop(0))
    else:
        for _ in range(cnt):
            a[num-1].insert(0, a[num-1].pop())
s = 0
e = n-1
tot = 0
for i in range(n):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(tot)