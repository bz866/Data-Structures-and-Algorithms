/*

LC 694. Number of Distinct Islands

Note: 
1. DFS traverse the 2-d array
- recursively go all directions when meet valid location
Time: O(m * n)
Space: O(m * n) -> size of the stack
2. BFS traverse the 2-d array
- Use queue to store all neightbour valid locations

*/

// BFS
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0 ) return 0;
        set<vector<pair<int, int>>> islands;
        
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] != 1) continue;
                vector<pair<int, int>> shape;
                queue<pair<int, int>> que;
                que.push(make_pair(i, j));  // <= BFS queue
                while (que.size() > 0) {
                    int x = que.front().first, y = que.front().second;
                    que.pop();
                    shape.push_back(make_pair(x - i, y - j));
                    grid[x][y] = -1;
                    for (auto& d : directions) {
                        int x_new = x + d[0], y_new = y + d[1];
                        if ( x_new < 0 || x_new >= grid.size() || y_new < 0 || y_new >= grid[0].size() ) continue;
                        if ( grid[x_new][y_new] == 1 ) {
                            que.push(make_pair(x_new, y_new));
                            shape.push_back(make_pair(x_new - i, y_new - j));
                            grid[x_new][y_new] = -1;
                        }
                    }
                }
                islands.insert(shape);
            }
        }
        
        return islands.size();
    }
    
    vector<vector<int>> directions {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
};



// DFS



class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        // when we think about unique, we use hash to drop duplicates
        // each island can be describe as coordinates
        // use relative duplicates to determine the shape of the island
        if ( grid.size() == 0 || grid[0].size() == 0) return 0;
        set<vector<pair<int, int>>> islands;
        
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] != 1) continue;
                vector<pair<int, int>> shape;
                getIslandShape(grid, i, j, i, j, shape); // <= DFS recursive
                islands.insert(shape);
            }
        }
        
        return islands.size();
    }
    
    void getIslandShape(vector<vector<int>>& grid, int i, int j, int ori_i, int ori_j, vector<pair<int, int>>& shape) {
        if ( i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() ) return;
        if ( grid[i][j] != 1 ) return;
        grid[i][j] = 0;
        shape.push_back( make_pair(i - ori_i, j - ori_j) );
        
        for (auto& d : directions ) {
            getIslandShape(grid, i+d[0], j+d[1], ori_i, ori_j, shape);
        }
        
        return;
    }
    
    vector<vector<int>> directions {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    
};