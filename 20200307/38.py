import sys
from collections import deque
sys.stdin = open("input38.txt", "rt")

must = input()
n = int(input())

for i in range(n):
    plan = input()
    mustDq = deque(must)
    for s in plan:
        if s in mustDq:
            if s != mustDq.popleft():
                print('#%d NO' %(i+1))
                break
    else:
        if len(mustDq) == 0:
            print('#%d YES' %(i+1))
        else:
            print('#%d NO' %(i+1))
