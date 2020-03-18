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
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)

# class Heap:
#     def __init__(self):
#         self.data = [None]
#
#     def insert(self, item):
#         self.data.append(item)
#         i = len(self.data) - 1
#         while i > 1:
#             if self.data[i] > self.data[i//2]:
#                 self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
#             else:
#                 break
#
#     def remove(self):
#         i = len(self.data) - 1
#         if i > 1:
#             self.data[1], self.data[-1] = self.data[-1], self.data[1]
#             data = self.data.pop()
#             self.max_heapify(1)
#         else:
#             data = None
#         return data
#
#     def get_length(self):
#         return len(self.data)
#
#     def max_heapify(self, i):
#         left = 2*i
#         right = 2*i+1
#         largest = i
#         size = len(self.data)
#         if left < size and self.data[i] < self.data[left]:
#             largest = left
#         if right < size and self.data[largest] < self.data[right]:
#             largest = right
#         if largest != i:
#             self.data[largest], self.data[i] = self.data[i], self.data[largest]
#             self.max_heapify(largest)
#
# heap = Heap()
# while True:
#     i = int(input())
#     if i == -1:
#         break
#     elif i == 0:
#         if heap.get_length() > 1:
#             max = heap.remove()
#             print(max)
#         else:
#             print(-1)
#     else:
#         heap.insert(i)