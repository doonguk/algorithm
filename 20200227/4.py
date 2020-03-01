import sys
sys.stdin = open("input4.txt", "rt")
n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / n)
score = 0
min = 2147000000

for i, x in enumerate(scores):
    dif = abs(x - avg)
    if min > dif:
        min = dif
        score = x
        res = i+1
    elif min == dif:
        if score < x:
            score = x
            res = i+1

print(avg, res)
