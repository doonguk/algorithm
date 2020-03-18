import sys

sys.stdin = open("input49.txt", "rt")


def DFS(L, sum, t_sum):
    global res
    if sum + (tot - t_sum) < res:
        return
    if sum > n:
        return
    if L == m:
       if sum > res:
           res = sum
    else:
        DFS(L + 1, sum + a[L], t_sum + a[L])
        DFS(L + 1, sum, t_sum + a[L])


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    res = -2147000000
    tot = sum(a)
    DFS(0, 0, 0)
    print(res)
