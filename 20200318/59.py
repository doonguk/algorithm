import sys

sys.stdin = open("input59.txt", "rt")

def DFS(L, score_sum, time_sum):
    global max
    if time_sum > m:
        return
    if L == n:
        if max < score_sum:
            max = score_sum
    else:
        DFS(L+1, score_sum + scores[L], time_sum + times[L])
        DFS(L+1, score_sum, time_sum)

if __name__ == '__main__':
    n, m = map(int, input().split())
    scores = list()
    times = list()
    for _ in range(n):
        s, t = map(int, input().split())
        scores.append(s)
        times.append(t)

    max = -2147000000
    DFS(0, 0, 0)
    print(max)
