class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]        
        c = bin(c)[2:]        
        ans = 0
        # print(a,b,c)
        maxLen = max(len(a), len(b), len(c))
        if len(a) > len(b):
            a,b = b,a
        
        while(len(a) != maxLen):
            a = '0' + a
        while(len(b) != maxLen):
            b = '0' + b
        while(len(c) != maxLen):
            c = '0' + c
        
        # print(a,b,c)
        
        for i in range(len(a)):
            if int(a[i]) | int(b[i]) == int(c[i]) : 
                continue
            if int(a[i]) and int(b[i]) and not int(c[i]) : ans += 2
            # elif not int(a[i]) and not int(b[i]) and int(c[i]) : ans += 1
            else : 
                # print('else: ', a[i], b[i], c[i])
                ans += 1
        
        return ans