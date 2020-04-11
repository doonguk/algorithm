def solution(name):
    size = len(name)
    ch = [0] * size
    cnt = 0
    for i in range(size):
        if name[i] != 'A':
            ch[i] = 1
            cnt += 1

    def verticalCheck(target):
        down = ord(target) - 65
        up = 26 - down
        return min(up, down)

    def horizonCheck(cur):
        cnt1 = 0
        left = cur
        while True:
            left -= 1
            cnt1 += 1
            if left < 0:
                left = size - 1
            if ch[left] == 1:
                break

        cnt2 = 0
        right = cur
        while True:
            right += 1
            cnt2 += 1
            if right >= size:
                right = 0
            if ch[right] == 1:
                break
        if cnt1 >= cnt2:
            return [right, cnt2]
        else:
            return [left, cnt1]

    cur = 0
    res = 0
    while True:
        if ch[cur] == 1:
            ch[cur] = 0
            res += verticalCheck(name[cur])
            cnt -= 1

        if cnt != 0:
            next_cur, step = horizonCheck(cur)
            res += step
            cur = next_cur
        else:
            break
    return res