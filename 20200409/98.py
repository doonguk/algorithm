def isValid(self, s: str) -> bool:
    open_set = set(["(", "[", "{"])
    bracket_map = {"(": ")", "{": "}", "[": "]"}
    stack = list()
    for v in s:
        if v in open_set:
            stack.append(v)
        elif stack and v == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []