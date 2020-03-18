import sys
from collections import deque
sys.stdin = open("input37.txt", "rt")

n, m = map(int, input().split())
dq = deque([(idx, val) for idx, val in enumerate(list(map(int, input().split())))])

cnt = 0
while True:
    i, v = dq.popleft()
    if any(v < x[1] for x in dq):
        dq.append((i, v))
    else:
        cnt += 1
        if i == m:
            break
print(cnt)