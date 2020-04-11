def solution(dartResult):
    dartResult = dartResult.replace('10', 'K')
    answer = list()
    squ = ['S', 'D', 'T']

    i = -1
    for s in dartResult:
        if s in squ:
            answer[i] **= (squ.index(s) + 1)
        elif s == '*':
            if i >= 1:
                answer[i - 1] *= 2
            answer[i] *= 2
        elif s == '#':
            answer[i] *= -1
        else:
            if s == 'K':
                answer.append(10)
            else:
                answer.append(int(s))
            i += 1
    return sum(answer)