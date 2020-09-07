# class Solution:
#     def makeGood(self, s: str) -> str:
#         i = 0
#         s = list(s)
#         while i < len(s)-1:
#             print(i, s)
#             if abs(ord(s[i])-ord(s[i+1])) == 32:
#                 del s[i+1]
#                 del s[i]
#                 i = i-1 if i-1 > -1 else 0
#             else: i+=1
#             # print(s)       
#         return ''.join(s)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for c in s[1:]:
            # print(c, stack, abs(ord(c) - ord(stack[-1])))
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)