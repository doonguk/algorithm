import sys
sys.stdin = open("input23.txt", "rt")
n, m = map(int, input().split())

a = list()
largest = 0
for i in range(n):
    tmp = int(input())
    a.append(tmp)
    largest = max(largest, tmp)

def check(l):
    tot = 0
    for i in a:
        tot += i//l
    return tot

res = -2147000000
start = 1
end = largest

while start <= end:
    mid = (start + end) // 2
    if check(mid) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)