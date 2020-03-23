import sys
sys.stdin = open("input62.txt", "rt")

def DFS(L, sum):
    global cnt
    if sum > target:
        return
    if L == n:
        if sum == target:
            cnt += 1
    else:
        for i in range(amount[L]+1):
            DFS(L+1, sum + c[L] * i)


if __name__ == '__main__':
    target = int(input())
    n = int(input())
    c = list()
    amount = list()
    for _ in range(n):
        p, q = map(int, input().split())
        c.append(p)
        amount.append(q)
    cnt = 0
    DFS(0, 0)
    print(cnt)