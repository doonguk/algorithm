def check(u): # 올바른 문자열 인지 check
    tmp = list()
    for v in u:
        if v == ')':
            if '(' in tmp:
                tmp.remove('(') # only delete one ( 기준은 index low )
            else:
                return False
        else:
            tmp.append(v)
    else:
        return True

def devide(p):
    u = ''
    for i in range(len(p)):
        u += p[i]
        cnt1 = 0
        cnt2 = 0
        for v in u:
            if  v == '(':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == cnt2:
            return [u, p[i+1:]]

def reverse(u):
    res = ''
    for v in u:
        if v == ')':
            res += '('
        else:
            res += ')'
    return res


def solution(p):
    if not p:
        return ''
    if check(p):
        return p
    else:
        u, v = devide(p)
        if check(u):
            return u + solution(v)
        else:
            return '(' + solution(v)+ ')' + reverse(u[1:-1])