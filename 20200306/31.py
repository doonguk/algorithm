import sys
sys.stdin = open("input31.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            a[i] -= 1

print(res)

# n 부터 처리
# import sys
# sys.stdin = open("input31.txt", "rt")
#
# n = int(input())
# a = list(map(int, input().split()))
#
# res = []
# for v in a[::-1]:
#     res.insert(v, n)
#     n -= 1
#
# print(res)