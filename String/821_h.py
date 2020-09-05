class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        indexes = [i for i in range(len(S)) if S[i] == C]
        # print(indexes)
        curIndex = 0
        for i in range(len(S)):
            res.append(abs(indexes[curIndex] - i))
            if curIndex < len(indexes) -1 and i == (indexes[curIndex] + indexes[curIndex+1])//2:
                curIndex += 1
        return res