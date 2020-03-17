def solution(s):
    min = len(s)
    for i in range(1, len(s)//2+1):
        before = s[0:i]
        cnt = 1  # 압축 cnt
        cha = ''
        for j in range(i, len(s), i):
            current = s[j:j+i]
            if before == current:
                cnt += 1
            else:
                if cnt > 1:
                    cha += str(cnt)
                cha += before
                cnt = 1
                before = current
            if j + i >= len(s):
                if cnt > 1:
                    cha += str(cnt)
                cha += current
        if len(cha) < min:
            min = len(cha)
    return min