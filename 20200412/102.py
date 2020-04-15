def solution(arr):
    hash = {}
    i = 1
    while True:
        for v in arr:
            tmp = v * i
            hash[tmp] = hash.get(tmp, 0) + 1
            if hash[tmp] == len(arr):
                return tmp
        i += 1