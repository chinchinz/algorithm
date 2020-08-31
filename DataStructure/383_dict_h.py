class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        # print(noteCount, magazineCount)
        
        for key, val in noteCount.items():
            if val > magazineCount.get(key, 0): return False
        
        return True