import sys
sys.stdin = open("input57.txt", "rt")

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        p, q, r = map(int, input().split())
        a[p][q] = r

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(a[i][j], end=' ')
        print()