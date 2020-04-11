def solution(brown, red):
    for i in range(1, red+1):
        if red % i == 0:
            if 2 * (red // i + i) == brown -4:
                return [red//i+2, i+2]