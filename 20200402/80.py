import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)

    cnt = 0
    while True:
        first = hq.heappop(scoville)
        if first > K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        cnt += 1
    return cnt