import sys
from collections import deque
sys.stdin = open("input29.txt", "rt")

n, maxWeight = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
weights = deque(a)

cnt = 0
while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] <= maxWeight:
        weights.popleft()
        weights.pop()
        cnt += 1
    else:
        weights.pop()
        cnt += 1

print(cnt)