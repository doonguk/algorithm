import sys
sys.stdin = open("input14.txt", "rt")

a = int(input())
list1 = list(map(int, input().split()))
b = int(input())
list2 = list(map(int, input().split()))

p1 = p2 = 0
res = []

while p1 < a and p2 < b:
    if list1[p1] >= list2[p2]:
        res.append(list2[p2])
        p2 += 1
    else:
        res.append(list1[p1])
        p1 += 1
if p1 < a:
    res = res + list1[p1:]
else:
    res = res + list2[p2:]
print(res)