def solution(n):
    numbers = ['4', '1', '2']
    ans = ''
    while n:
        ans = numbers[n%3] + ans
        n = n//3 - (n%3==0)
    return ans

print(solution(11))