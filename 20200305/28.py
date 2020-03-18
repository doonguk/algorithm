import sys
sys.stdin = open("input28.txt", "rt")

n = int(input())
box = list(map(int, input().split()))
m = int(input())
box.sort()
maxIndex = n-1
minIndex = 0

for _ in range(m):
    box[maxIndex] -= 1
    box[minIndex] += 1
    for i in range(n):
        if box[i] < box[minIndex]:
            minIndex = i
        elif box[i] > box[maxIndex]:
            maxIndex = i

print(box[maxIndex] - box[minIndex])

#두번째
# import sys
# sys.stdin = open("input28.txt", "rt")
#
# n = int(input())
# box = list(map(int, input().split()))
# m = int(input())
# box.sort()
# for _ in range(m):
#   box[0] += 1
#   box[n-1] -= 1
#   box.sort()
# print(box[n-1] - box[0])