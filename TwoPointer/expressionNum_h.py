def solution(n):
    l, r = 1, 2
    cur = l+r
    ans = 0
    while l <= r and l <= n:
        # print(l, r, cur, ans)
        if cur == n: 
            ans += 1
            cur -= l
            l += 1
            r += 1
            cur += r
        elif cur > n:
            cur -= l
            l += 1
        elif cur < n:
            r += 1
            cur += r

    return ans

print(solution(15))