# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visit = [False]*len(rooms)
#         visit[0] = True
#         cnt = 1
        
#         def dfs(n):
#             nonlocal cnt
#             for key in rooms[n]:
#                 if visit[key] : continue
#                 cnt += 1
#                 visit[key] = True
#                 dfs(key)
        
#         dfs(0)
#         # print(cnt)
#         return cnt == len(rooms)
    
###############

class Solution:
    def canVisitAllRooms(self, rooms) :
        visit = [False]*len(rooms)
        visit[0] = True
        cnt = 1
        
        stack = [0]
        
        while stack:
            cur = stack.pop()
            for key in rooms[cur]:
                if visit[key] : continue
                cnt += 1
                visit[key] = True
                stack.append(key)
        
        # print(cnt)
        return cnt == len(rooms)