import sys
sys.stdin = open("input55.txt", "rt")


def DFS(L, s, sum):
    global cnt
    if L == m:
        if sum % div == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    div = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
