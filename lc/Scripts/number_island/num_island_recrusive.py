from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_num = 0

        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(rows):
            for col in range(cols):
                print(f"Checking cell ({row}, {col}) with value {grid[row][col]}")
                if grid[row][col] == "1":
                    island_num += 1
                dfs(row, col)

        return island_num
    
data = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
data = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

solution = Solution()
print(solution.numIslands(data))
