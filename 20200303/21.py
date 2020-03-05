import sys
sys.stdin = open("input21.txt", "rt")
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if a[i+k][j] != a[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)





#두번째
# def check(list):
#     for i in range(2):
#         if list[i] != list[4-i]:
#             return False
#     else:
#         return True
#
# cnt = 0
#
# for y in range(7):
#     for x in range(3):
#         tmp = a[y][x:5+x]
#         if check(tmp):
#             cnt += 1
# #행
#
# for x in range(7):
#     for i in range(3):
#         tmp = list()
#         for y in range(5):
#             tmp.append(a[y+i][x])
#         if(check(tmp)):
#             cnt += 1
#
#
# print(cnt)
