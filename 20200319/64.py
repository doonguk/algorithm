import sys

sys.stdin = open("input64.txt", "rt")

def DFS(L, P):
    global cnt
    if L == size:
        for i in range(P):
            print(chr(res[i] + 64), end='')
        print()
        cnt += 1
    else:
        for i in range(1, 27):
            if a[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and a[L] == i//10 and a[L+1] == i % 10:
                res[P] = i
                DFS(L+2, P+1)

if __name__ == '__main__':
    a = list(map(int, input()))
    size = len(a)
    res = [0] * size
    a.append(-1)
    cnt = 0
    DFS(0, 0)
    print(cnt)
