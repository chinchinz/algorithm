import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

ans = 0

r, c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(map(int,input().split())))
arrSave = copy.deepcopy(arr)

def spread(arr) :
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 2: continue
            for k in range(4):
                ny = dy[k] + i
                nx = dx[k] + j
                if nx < 0 or ny < 0 or nx == c or ny == r: continue
                if arr[ny][nx] == 0 : arr[ny][nx] = 2

def safeZone(arr):
    count = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 : continue
            count += 1
            arr[i][j] = 1
            for k in range(4):
                ny, nx = dy[k]+i, dx[k]+j
                if nx < 0 or ny < 0 or nx == c or ny == r: continue
                if arr[ny][nx] == 0:
                    count += 1
                    arr[ny][nx] = 1
    return count

def makeWall(y, x, count):
    if count == 3:
        global ans
        copyArr = copy.deepcopy(arr)
        spread(copyArr)
        print(copyArr)
        ans = max(safeZone(arr), ans)

    for i in range(y, r):
        for j in range(x, c):
            if arr[i][j] == 0:
                arr[i][j] = 1
                try: makeWall(i, j+1, count+1)
                except: makeWall(i+1, 0, count+1)
                arr[i][j] = 0
makeWall(0,0,0)
print(ans)