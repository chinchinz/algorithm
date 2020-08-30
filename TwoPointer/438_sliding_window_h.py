class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S = [ord(x) - ord('a') for x in s]
        P = [ord(x) - ord('a') for x in p]
        res = []
        target = [0]*26
        
        for c in P :
            target[c] += 1
        
        # print(S)
        # print(P)
        # print(target)
        
        window = [0]*26
        
        for i in range(len(S)):
            window[S[i]] += 1
            if i >= len(P) :
                window[S[i-len(P)]] -= 1
            # print(window)
            if window == target:
                res.append(i-len(P)+1)
        # print(res)
        return res