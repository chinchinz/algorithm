from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1
        1
        # 2
        1+1
        2
        # 3
        1+1+1
        1+2
        2+1
        # 4
        1+1+1+1
        1+2+1
        2+1+1
        1+1+2
        2+2
        
        # 5
        1+1+1+1+1
        1+2+1+1
        2+1+1+1
        2+2+1
        2+1+2
        # 6
        
        # 2가 몇개까지 들어갈 수 있느냐?
        # 그리고 조합의 수를 더하면 됨
        ans = 0        
        div, mod = divmod(n, 2)
        num_of_two = 0
        while num_of_two != div+1 :
            ans += factorial(n-num_of_two)//(factorial(n-2*num_of_two)*factorial(num_of_two))
            num_of_two += 1
        return ans


###### DP ######
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 2
        
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        
        return f[n-1]
        