def solution(n, words):
    answer = []
    said = set([words[0]])
    for i, word in enumerate(words):
        if i==0: continue
        # print(i,word)
        if word in said or words[i][0] != words[i-1][-1]:
            answer += [i%n +1, i//n +1]
            break
        said.add(word)
    # print(answer)
    if len(answer) == 0:
        # print(answer)
        return [0,0]
    return answer








solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])
# solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'])
# print(solution(5,['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))