class Solution:
    def frequencySort(self, s: str) -> str:
        # print(Counter(s))
        counter = []
        for key, val in Counter(s).items():
            counter.append([val, key])
        
        counter.sort(reverse=True)
        res = ''
        for (cnt, c) in counter:
            res += c*cnt
        
        return res