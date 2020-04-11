def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    else:
        stack = list()
        for v in s:
            if v == '(' or v == '{' or v == '[':
                stack.append(v)
            else:
                if not stack:
                    return False
                else:
                    if v == ')':
                        if stack.pop() != '(':
                            return False
                    elif v == ']':
                        if stack.pop() != '[':
                            return False
                    elif v == '}':
                        if stack.pop() != '{':
                            return False
        if stack:
            return False
        return True