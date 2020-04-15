def solution(relation):
    all_case = list()

    def DFS(L, s):
        if L == length:
            if set(cb) not in all_case:
                all_case.append(set(cb))
        else:
            for i in range(s, len(relation[0])):
                cb[L] = i
                DFS(L + 1, i + 1)

    for length in range(1, len(relation[0]) + 1):
        cb = [0] * length
        DFS(0, 0)

    unique_case = list()
    for combi in all_case:  # all cb
        hash = dict()
        for row in relation:
            tmp = ''
            for column in list(combi):
                tmp += row[column]
            hash[tmp] = hash.get(tmp, 0) + 1
            if hash[tmp] == 2:
                break
        else:
            unique_case.append(combi)

    answer = list()
    for combi in unique_case:
        for ans in answer:
            if combi & ans == ans:
                break
        else:
            answer.append(combi)

    return len(answer)