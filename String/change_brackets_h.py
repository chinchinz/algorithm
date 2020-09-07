def isbalanced(s):
    chk = 0
    for c in s:
        if c=='(': chk+=1
        else: chk-=1
    if not chk : return True
    return False

def iscorrect(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) == 0 or stack[-1] == ')' or (stack[-1] == '(' and s[i]=='('):
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0: return True
    return False

def solution(p):
    ans = ''
    u = ''
    v = ''
    if len(p) == 0 or iscorrect(p): return p

    for i in range(2, len(p)+1, 2):
        if isbalanced(p[0:i]):
            u=p[0:i]
            v=p[i:len(p)]
            break
    
    if iscorrect(u):
        ans += u+solution(v)
    else:
        ans += '('+solution(v)+')'
        for c in u[1:-1]:
            if c=='(': ans += ')'
            else: ans+= '('
    return ans

print(solution('()))((()'))