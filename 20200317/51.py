import sys
sys.stdin = open("input51.txt", "rt")

def DFS(L, sum):
    global min
    if L >= min:
        return
    if sum > t:
        return
    if sum == t:
        if min > L:
            min = L
        return
    else:
        for i in range(n):
            DFS(L+1, sum + a[i])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    t = int(input())
    min = 2147000000
    DFS(0, 0)
    print(min)

