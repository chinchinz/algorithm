# Stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[' :
                stack.append(c)
            else:
                if not stack : return False
                if c == ')':
                    if stack[-1] != '(' : return False
                elif c == '}':
                    if stack[-1] != '{' : return False
                elif c == ']':
                    if stack[-1] != '[' : return False
                stack.pop()
        if stack : return False
        return True

