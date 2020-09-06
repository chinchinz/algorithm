class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for c in S:
            if c.isalpha():
                res = [i+j for i in res for j in [c.upper(), c.lower()]]
            else:
                res = [i+c for i in res]
            # print(res)
        return res
                