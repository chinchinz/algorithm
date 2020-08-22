def solution(s):
    answer = 1341241234
    for length in range(1, len(s)//2 + 1):
        ret = ""
        counter = 1
        
        prev = s[:length]
        
        for i in range(length, len(s)+length, length):
            if prev == s[i:i+length]:
                counter += 1
            else:
                if counter != 1:
                    ret = ret + str(counter) + prev
                else:
                    ret = ret + prev
                prev = s[i:i+length]
                counter = 1
        answer = min(answer, len(ret))
    return min(answer, len(s))