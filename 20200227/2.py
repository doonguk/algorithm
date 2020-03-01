import sys
sys.stdin = open("input2.txt", "rt")
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e+1]
    a.sort()
    print(a[k-1])