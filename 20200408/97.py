def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    minLength = 2147000000
    for v in strs:
        if len(v) < minLength:
            minLength = len(v)
    s = 0
    e = minLength
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if all([strs[0][:mid] == strs[k][:mid] for k in range(1, len(strs))]):
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    return strs[0][:res]