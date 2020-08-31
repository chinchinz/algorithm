class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounter = Counter(chars)
        ans = 0
        for word in words:
            # print(charCounter & Counter(word))
            gyo = charCounter & Counter(word)
            if len(list(gyo.elements())) == len(word):
                ans += len(word)
        return ans