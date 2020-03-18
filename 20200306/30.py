import sys
sys.stdin = open("input30.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

res = ''
lt = 0
rt = n-1
last = 0
tmp = []

while lt <= rt:
    if a[lt] > last:
       tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        if tmp[0][1] == 'L':
            lt += 1
            res += 'L'
            last = tmp[0][0]
        else:
            rt -= 1
            res += 'R'
            last = tmp[0][0]
    tmp.clear()
print(len(res))
print(res)



