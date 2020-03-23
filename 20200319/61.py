import sys
sys.stdin = open("input61.txt", "rt")

def DFS(L, sum):
    if L == n:
        if 0 < sum <= tot:
            res.add(sum)
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum - a[L])
        DFS(L+1, sum)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    res = set()
    DFS(0, 0)
    print(tot - len(res))

