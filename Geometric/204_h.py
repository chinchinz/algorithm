class Solution:
    def countPrimes(self, n: int) -> int:
        chae = [0]*(n)
        cnt = 0
        
        for i in range(2, len(chae)):
            if not chae[i] :
                cnt += 1
                k = i
                while k < len(chae):
                    chae[k] = -1
                    k += i
            # print(chae)
        return cnt