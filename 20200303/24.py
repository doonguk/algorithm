import sys
sys.stdin = open("input24.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
start = 1
end = 0

for i in range(m):
    end += a[-1-i]

def check(v, musics):
    cnt = 1
    tmp = 0
    for m in musics:
        if tmp + m > v:
            tmp = m
            cnt += 1
        else:
            tmp += m
    return cnt

min = -2147000000
maxx = max(a)
while start <= end:
    mid = (start + end) // 2
    if maxx <= mid and check(mid, a) <= m:
        min = mid
        end = mid - 1
    else:
        start = mid + 1

print(min)