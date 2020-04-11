def solution(n, l, r):
    reserve = set(r) - set(l)
    lost = set(l) - set(r)
    answer = n - len(reserve) - len(lost)  # init

    for v in reserve:
        if v - 1 in lost:
            answer += 2
            lost.remove(v - 1)
        elif v + 1 in lost:
            answer += 2
            lost.remove(v + 1)
        else:
            answer += 1

    return answer