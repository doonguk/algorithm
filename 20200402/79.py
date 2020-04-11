def solution(s):
    s = s[2:-2].split('},{')
    for i in range(len(s)):
        s[i] = set(map(int, s[i].split(',')))
    s.sort(key=len)
    res = [list(s[0])[0]]
    prev =s[0]
    for i in range(1, len(s)):
        res.append(list(s[i] - s[i-1])[0])
    return res