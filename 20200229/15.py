import sys
sys.stdin = open("input15.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
lt = 0
rt = 1
tot = a[0]

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1


# 방법2
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# cnt = 0
#
# for i in range(1, n):
#     start = 0
#     while start + i < n+1:
#         tmp = sum(a[start : start+i])
#         if tmp == k:
#             cnt += 1
#         start += 1
# print(cnt)
