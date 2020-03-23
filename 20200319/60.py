import sys

sys.stdin = open("input60.txt", "rt")

def DFS(L, money_sum):
    global max
    if L == n+1:
        if max < money_sum:
            max = money_sum
    else:
        if L + times[L] <= n+1:
            DFS(L + times[L], money_sum + money[L])
        DFS(L+1, money_sum)



if __name__ == '__main__':
    n = int(input())
    times = [0]
    money = [0]
    for _ in range(n):
        t, m = map(int, input().split())
        times.append(t)
        money.append(m)
    max = - 2147000000
    DFS(1, 0)
    print(max)