import sys
from collections import deque

if __name__ == '__main__':
    c, b = map(int, input().split())
    MAX = 200001
    dQ = deque()
    dQ.append(b)

    L = 1
    while dQ and c < MAX:
        c += L
        size = len(dQ)
        for _ in range(size):
            now = dQ.popleft()
            for next in (now-1, now+1, 2*now):
                if 0 <= next < MAX:
                    dQ.append(next)
                    if next == c:
                        print(L)
                        sys.exit(0)
        L += 1
    else:
        print(-1)