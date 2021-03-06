import sys
import heapq as hq
sys.stdin = open("input42.txt", "rt")

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)


# Class 구현 풀이
# class Heap:
#     def __init__(self):
#         self.data = [None]
#
#     def insert(self, item):
#         self.data.append(item)
#         i = len(self.data) - 1
#         while i > 1:
#             if self.data[i] < self.data[(i // 2)]:
#                 self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
#             else:
#                 break
#
#     def remove(self):
#         if len(self.data) > 1:
#             self.data[-1], self.data[1] = self.data[1], self.data[-1]
#             data = self.data.pop()
#             self.min_heapify(1)
#         else:
#             data = None
#         return data
#
#     def min_heapify(self, i):
#         left = 2 * i
#         right = 2 * i + 1
#         smallest = i
#         if left < len(self.data) and self.data[i] > self.data[left]:
#             smallest = i
#         if right < len(self.data) and self.data[left] > self.data[right]:
#             smallest = i
#         if smallest != i:
#             self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
#             self.min_heapify(smallest)
#
#
# heap = Heap()
# while True:
#     i = int(input())
#     if i == -1:
#         break
#     elif i == 0:
#         min = heap.remove()
#         print(min)
#     else:
#         heap.insert(i)