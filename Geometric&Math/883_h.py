'''
883. Projection Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.
'''

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        # x 기준으로
        ans += len(grid) * len(grid[0])
        
        # y 기준으로
        for row in grid :
            ans += max(row)
        
        # z 기준으로
        for row in list(zip(*grid)):
            ans += max(row)
        
        # 0 제거
        for row in grid :
            for num in row :
                if num == 0 : ans -= 1
                    
        return ans

'''
3차원의 문제가 나와 당황했지만,
문제의 규칙을 찾으니 쉽게 풀 수 있었다.
list(zip(*matrix))로 numpy 없이 transpose가 가능하며
종종 쓰이니 기억하자.
처음에 0을 처리하지 않아 오답이 나왔다.
특수 상황에 대한 고려를 빼놓지 말자.
'''