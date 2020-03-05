import sys
sys.stdin = open("input22.txt", "rt")

n, target = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
start = 0
end = n-1
while start <= end:
    mid = (start + end) // 2
    if a[mid] == target:
        print(mid+1)
        break
    elif a[mid] > target:
        end = mid - 1
    else:
        start = mid + 1



# 방법2
# start = 0
#
# def binarySearch(start, end, target, data):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if target == data[mid]:
#         return mid + 1
#     elif target > data[mid]:
#         start = mid + 1
#     else:
#         end = mid-1
#     return binarySearch(start, end, target, data)
#
#
# print(binarySearch(start, n-1, target, sorted(a)))