import sys
from collections import deque
sys.stdin = open("input36.txt", "rt")

n, m = map(int, input().split())
people = deque(list(range(1,n+1)))

for _ in range(n-1):
    for _ in range(m-1):
        people.append(people.popleft())
    people.popleft()

print(people[0])