# 두 말 의 거리 최대값
import sys
sys.stdin = open("input25.txt", "rt")

n, m = map(int, input().split())
a = list()
for _ in range(n):
    a.append(int(input()))

a.sort()
start = 1
end = a[n-1] - a[0]
res = -2147000000

def check(len):
    cnt = 1
    before = a[0]
    for i in range(1, n):
        if a[i] - before >= len:
            cnt += 1
            before = a[i]
    return cnt

while start <= end:
    mid = (start + end) // 2
    if check(mid) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)

