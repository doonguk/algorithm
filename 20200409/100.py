def solution(pb):
    book = dict()
    for i in range(len(pb)):
        book[pb[i]] = i

    for i in range(len(pb)):
        for j in range(1, len(pb[i])):
            if pb[i][:j] in book and book[pb[i][:j]] != i:
                return False
    return True