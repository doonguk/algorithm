import sys
sys.stdin = open("input63.txt", "rt")

def DFS(L):
    global res
    if res < max(div) - (min(div) + sum(cv[L:])):
        return
    if L == n:
        if div[0] != div[1] and div[0] != div[2] and div[1] != div[2]:
            tmp = max(div) - min(div)
            if tmp < res:
                res = tmp
    else:
        for i in range(3):
            div[i] += cv[L]
            DFS(L+1)
            div[i] -= cv[L]


if __name__ == '__main__':
    n = int(input())
    cv = list()
    div = [0, 0, 0]
    res = 2147000000
    for _ in range(n):
        cv.append(int(input()))
    DFS(0)
    print(res)