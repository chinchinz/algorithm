class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c== ')':
                if stack:
                    cur = stack.pop() + '('+cur+')'
            else:
                cur += c
            # print(cur, stack)
        while stack:
            cur = stack.pop() + cur
        return cur