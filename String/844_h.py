class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        S = self.refineString(S)
        T = self.refineString(T)
        
        return S==T
    
    def refineString(self, S):
        i = 0
        while i < len(S):
            if S[i] == '#':
                if i == 0:
                    S = S[1:]
                    continue
                S = S[:i-1] + S[i+1:]
                i -= 1
            else: i += 1
        return S