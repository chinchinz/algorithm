def solution(skill, skilltrees):
    answer = 0
    
    for skilltree in skilltrees :
        order = ''
        for sk in skilltree :
            if sk in skill:
                order += sk
        if skill.startswith(str(order)):
            answer += 1
    return answer