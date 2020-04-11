import sys
from collections import deque

sys.stdin = open("review_input.txt", "rt")

if __name__ == '__main__':
    strs = list(input().split())
    if len(strs) == 0:
        print("")
    minLength = 2147000000
    for v in strs:
        if len(v) < minLength:
            minLength = len(v)
    s = 0
    e = minLength
    res = 0

    while s <= e:
        mid = (s + e) // 2
        if all([strs[0][:mid] == x[:mid] for x in strs]):
            res = mid
            s = mid + 1
        else:
            e = mid - 1