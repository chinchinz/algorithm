class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = Counter(s)
        tCounter = Counter(t)
        
        for key in tCounter:
            if sCounter[key] != tCounter[key] : return key
    