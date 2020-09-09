def numberOfSubstrings(s: str) -> int:
    a = b = c = 0 
    l = r = 0
    ans = 0
    flag = 1
    while l < len(s) and r < len(s) :
        # print(l, r)
        if flag :
            if s[r] == 'a':
                a += 1
            elif s[r] == 'b':
                b += 1
            elif s[r] == 'c':
                c += 1
        
        if a and b and c:
            ans += len(s) - r
            # print(a,b,c)
            # print(l, r, len(s)-r, ans)
            if s[l] == 'a': a -= 1
            elif s[l] == 'b': b-=1
            elif s[l] == 'c': c -= 1
            l += 1
            flag = 0
        else:
            flag = 1
            r += 1
    return ans

print(numberOfSubstrings('abcabc'))
print(numberOfSubstrings('aaacb'))
print(numberOfSubstrings('abc'))