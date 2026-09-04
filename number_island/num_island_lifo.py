# https://leetcode.com/problems/number-of-islands/solutions/8401886/number-of-islands-dfs-flood-fill-with-in-9ciw/?q=number+island
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_num = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_num += 1
                    grid[row][col] = "0"
                    stack = [(row, col)]
                    while stack:
                        r, c = stack.pop()
                        ur = r -1
                        if ur >= 0 and grid[ur][c] == "1":
                            grid[ur][c] = "0"
                            stack.append((ur, c))
                        dr = r + 1
                        if dr < rows and grid[dr][c] == "1":
                            grid[dr][c] = "0"
                            stack.append((dr, c))
                        lc = c - 1
                        if lc >= 0 and grid[r][lc] == "1":
                            grid[r][lc] = "0"
                            stack.append((r, lc))
                        rc = c + 1
                        if rc < cols and grid[r][rc] == "1":
                            grid[r][rc] = "0"
                            stack.append((r, rc))
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
