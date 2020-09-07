class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while i<len(pushed):
            # print(pushed[i])
            if pushed[i] == popped[j]:
                j += 1
                while j < len(popped) and stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
            else:
                stack += [pushed[i]]
            i += 1
            # print(stack)
        
        for i in range(len(stack)-1, -1, -1):
            if stack[i] != popped[j]: return False
            j += 1
        
        return True