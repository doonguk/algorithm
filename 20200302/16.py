import sys
sys.stdin = open("input16.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

max = -2147000000

for y in range(n):
    tot1 = tot2 = 0
    for x in range(n):
        tot1 += a[y][x]
        tot2 += a[x][y]
    if tot1 > max:
        max = tot1
    if tot2 > max:
        max = tot2

tot3 = tot4 = 0
for x in range(n):
    tot3 += a[x][x]
    tot4 += a[n-x-1][x]

if tot3 > max:
    max = tot3
if tot4 > max:
    max = tot4

print(max)


