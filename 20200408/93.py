def twoSum(nums, target):
    hash = {}
    for i, v in enumerate(nums):
        n = target - v
        if n in hash:
            return [hash[n], i]
        hash[v] = i
    return list()
