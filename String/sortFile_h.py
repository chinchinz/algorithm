import re

def solution(files):
    ans = [[None]*3 for _ in range(len(files))]
    for i, file in enumerate(files):
        ans[i][1] = re.findall('\d+', file)[0]
        print(re.split('\d+', file))
        ans[i][0], ans[i][2] = re.split('\d+', file)
    
    ans.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(x) for x in ans]


print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))