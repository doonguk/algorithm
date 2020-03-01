import sys
sys.stdin = open("input5.txt", "rt")

n, m = map(int, input().split())
a = [0] * (n + m + 1)
max = -2147000000

for i in range(1, n+1):
    for m in range(1, m+1):
        a[i+m] += 1

for j in range(1, n+m+1):
    if a[j] > max:
        max = a[j]

for i in range(1, n+m+1):
    if a[i] == max:
        print(i, end=' ')