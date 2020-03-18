import sys
sys.stdin = open("input27.txt", "rt")

n = int(input())
people = list()
for _ in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

people.sort(reverse=True)
largest=0
cnt=0
for x, y in people:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)

# 두번째
# import sys
# sys.stdin = open("input27.txt", "rt")
#
# n = int(input())
# people = list()
# for _ in range(n):
#     h, w = map(int, input().split())
#     people.append((h, w))
#
# people.sort()
# cnt = 0
# for i in range(n-1):
#     w = people[i][1]
#     for j in range(i+1, n):
#         if w <= people[j][1]:
#             break
#     else:
#         cnt += 1
# print(cnt+1) # + 첫번째 값


