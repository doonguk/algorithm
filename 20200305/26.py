import sys
sys.stdin = open("input26.txt", "rt")

n = int(input())
meeting = list()
for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))
res = 0
et = 0
for s, e in meeting:
    if s >= et:
        et = e
        res += 1
print(res)

