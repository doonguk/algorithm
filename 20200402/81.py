answer = 0
def solution(numbers):
    size = len(numbers)
    ch = [0] * size
    ch2 = dict()
    def DFS(L, num):
        global answer
        if L == size:
            num = int(num)
            if num > 1 and num not in ch2:
                ch2[num] = 0
                for v in range(2, num):
                    if num % v == 0:
                        break
                else:
                    answer += 1
        else:
            for v in range(size):
                if ch[v] == 0:
                    ch[v] = 1
                    DFS(L+1, num + numbers[v])
                    ch[v] = 0
                else:
                    DFS(L+1, num)
    DFS(0, '')
    return answer