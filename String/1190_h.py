class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, cur = [], ''
        
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = ''
            elif c == ')':
                cur = stack.pop()+''.join(reversed(cur))
            else:
                cur += c
            
            # print(cur, stack)
        
        return cur
        