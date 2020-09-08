import re
def solution(mm, musicinfos):
    ans = ''
    res = []
    mm = mm.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    # print(mm)
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        musicinfos[i][0] = list(map(int, musicinfos[i][0].split(':')))
        musicinfos[i][1] = list(map(int, musicinfos[i][1].split(':')))
        musicinfos[i][3] = musicinfos[i][3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        time = (musicinfos[i][1][0] * 60 + musicinfos[i][1][1]) - (musicinfos[i][0][0] * 60 + musicinfos[i][0][1])
        musicinfos[i][3] = musicinfos[i][3]*(time//len(musicinfos[i][3])) + musicinfos[i][3][:time%len(musicinfos[i][3])]
        # print(re.findall(mm,musicinfos[i][3]))
        if mm in musicinfos[i][3]:
            res.append((musicinfos[i][2], time, i))
    # print(musicinfos)
    res.sort(key=lambda x : (-x[1],x[2]))
    # print(res)
    try:
        return res[0][0]
    except:
        return '(None)'

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))