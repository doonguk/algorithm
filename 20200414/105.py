import math

def solution(str1, str2):
    hash1 = {}
    set1 = set()
    hash2 = {}
    set2 = set()
    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2]
        if tmp.isalpha():
            tmp = tmp.lower()
            hash1[tmp] = hash1.get(tmp, 0) + 1
            set1.add(tmp)
    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if tmp.isalpha():
            tmp = tmp.lower()
            hash2[tmp] = hash2.get(tmp, 0) + 1
            set2.add(tmp)

    common = 0
    for value in list(set1 & set2):
        _min = min(hash1.get(value), hash2.get(value))
        common += _min

    total = 0
    for value in list(set1 | set2):
        _max = max(hash1.get(value, 0), hash2.get(value, 0))
        total += _max

    if total == 0:
        return 65536
    return math.floor((common / total) * 65536)