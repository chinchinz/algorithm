'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0
        for num in arr : 
            if num % 2 == 0 : consecutive = 0
            else : 
                consecutive += 1 
                if consecutive == 3 : return True
        
        return False

'''
Flag를 이용하여 조건 확인
'''