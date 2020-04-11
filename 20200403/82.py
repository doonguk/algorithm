def check(mid, budgets, M):
    tot = 0
    for v in budgets:
        if v > mid:
            tot += mid
        else:
            tot += v
    return tot < M


def solution(budgets, M):
    s = 1
    e = max(budgets)
    res = 1

    while s <= e:
        mid = (s + e) // 2
        if check(mid, budgets, M):
            res = mid
            s = mid + 1
        else:
            e = mid - 1

    return res