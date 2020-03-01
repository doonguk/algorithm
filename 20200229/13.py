import sys
sys.stdin = open("input13.txt", "rt")

# 방법1
res = list(range(21)) # 0~21 까지 대입된 리스트 생성
for _ in range(10): # 변수대신 _ 로 대입에 사용되는 수행시간 배제
    p, q = map(int, input().split())
    for i in range((q-p+1)//2):
        res[p+i], res[q-i] = res[q-i], res[p+i]
res.pop(0)
for a in res:
    print(a, end=' ')

# 방법2
res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(10):
    p, q = map(int, input().split())
    tmp = res[p-1:q]
    tmp = tmp[::-1]
    res = res[0:p-1] + tmp + res[q:]

for a in res:
    print(a, end=' ')