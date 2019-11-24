# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    

    # DFS Solution
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        # Use the DFS
        # change itself and surrounding ones as zeros 
        # so that whenever part of an island is met
        # the island is replaced as all zeros
        # the number of times we do dfs
        # is the number is island
        
        if len(grid) == 0:
            return 0
        
        self.rowSize = len(grid)
        self.colSize = len(grid[0])
        numIslands = 0
        
        for rInd, row in enumerate(grid):
            for cInd, val in enumerate(row):
                if val == '1':
                    self.dfsReplace(grid, rInd, cInd)
                    numIslands += 1
                    
        return numIslands
        
    
    def dfsReplace(self, grid, r, c):
        direction = [ [0, -1], # left
                      [0, 1], # right
                      [-1, 0], # up
                      [1, 0] # down
                    ]
        grid[r][c] = '0'
        for step in direction:
            nrInd, ncInd = r + step[0], c + step[1]
            if (0<= nrInd and nrInd <= len(grid) - 1) and (0<= ncInd and ncInd <= len(grid[0]) - 1): # within the grid
                if grid[nrInd][ncInd] == '1':
                    self.dfsReplace(grid, nrInd, ncInd)

        
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        # Use the BFS
        # still change itself and surrounding ones as zeros
        # so that whenever part of an island is met 
        # the island is replaced as all zeros
        # number of BFS, aka number of queue exhausted, is the number of islands
        
        numIslands = 0
        q = []

        direction = [ [0, -1], # left
                      [0, 1], # right
                      [-1, 0], # up
                      [1, 0] # down
                    ]

        for rInd, row in enumerate(grid):
            for cInd, val in enumerate(grid[rInd]):
                if val == '1':
                    grid[rInd][cInd] = '0'
                    q.append([rInd, cInd])
                    numIslands += 1
                    while q:
                        r, c = q.pop(0)
                        for step in direction:
                            nrInd, ncInd = r + step[0], c + step[1]
                            if ((0<= nrInd and nrInd <= len(grid) - 1) 
                                and (0<= ncInd and ncInd <= len(grid[0]) - 1) # within the grid
                                and (grid[nrInd][ncInd] == '1')):
                                grid[nrInd][ncInd] = '0'
                                q.append([nrInd, ncInd])

        return numIslands






















        
        
        
        