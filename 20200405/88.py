def check(mid, stones, k):
    cnt = 0
    res = 0
    for v in stones:
        if v < mid:
            cnt += 1
        else:
            if cnt > res:
                res = cnt
            cnt = 0
    if cnt > res:
        res = cnt
    return res >= k


def solution(stones, k):
    s = 1
    e = max(stones)
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if check(mid, stones, k):
            e = mid - 1
        else:
            res = mid
            s = mid + 1

    return res