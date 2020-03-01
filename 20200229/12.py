import sys
sys.stdin = open("input12.txt", "rt")

string = input()
res = 0
cnt = 0

for a in string:
    if a.isdecimal():
        res = res*10 + int(a)

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(res)
print(cnt)
