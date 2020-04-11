def solution(baseball):
    case = list(range(123, 987))
    res = 0
    for c in case:
        tmp = str(c)
        if tmp[1] == '0' or tmp[2] == '0':
            continue
        if tmp[0] == tmp[1] or tmp[0] == tmp[2]:
            continue
        if tmp[1] == tmp[2]:
            continue

        for x in baseball:
            n, s, b = x

            tmp_n = str(n)
            sc = 0  # s -> cal
            bc = 0  # b -> cal
            for i in range(3):
                if tmp[i] == tmp_n[i]:
                    sc += 1
                elif tmp.count(tmp_n[i]) == 1:
                    bc += 1
            if sc != s or bc != b:
                break
        else:
            res += 1
    return res