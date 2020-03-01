import sys
sys.stdin = open("input10.txt", "rt")
n = int(input())
answers = list(map(int, input().split()))
cnt = 0
res = 0

for i in range(n):
    if answers[i] == 1:
        cnt += 1
        res += cnt
    else:
        cnt = 0

print(res)