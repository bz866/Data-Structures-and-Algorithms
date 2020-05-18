// BFS
class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        if ( maze.size() == 0 || maze[0].size() == 0 ) return false;
        
        unordered_set<int> seen;
        queue<vector<int>> que;
        que.push(start);
        
        while (que.size() > 0) {
            vector curLoc = que.front(); que.pop();
            // found
            if (curLoc[0] == destination[0] && curLoc[1] == destination[1]) return true;
            // check seen 
            int coord = curLoc[0] * maze[0].size() + curLoc[1];
            if (seen.count(coord)) continue; // seen
            else seen.insert(coord);  // not seen before
            
            for (auto& d : directions) {
                vector<int> newStart = go2End(maze, curLoc, d);
                que.push(newStart);
            }
        }
        
        return false;
    }
    
    vector<int> go2End(vector<vector<int>>& maze, vector<int> loc, vector<int>& d) {
        int x = loc[0], y = loc[1];
        while (true) {
            int x_new = x + d[0], y_new = y + d[1];
            if ( x_new < 0 || x_new == maze.size() || y_new < 0 || y_new == maze[0].size() ) {
                break;
            }
            if ( maze[x_new][y_new] == 1 ) {
                break;
            }
            x += d[0];
            y += d[1];
        }
        
        return {x, y};
    }

    vector<vector<int>> directions {
        {0, 1},
        {0, -1},
        {-1, 0},
        {1, 0}
    };
};


// DFS
class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        if ( maze.size() == 0 || maze[0].size() == 0 ) return false;
        
        unordered_set<int> seen;
        
        return search(maze, start, destination, seen);
    }
    
    bool search(vector<vector<int>>& maze, vector<int> start, vector<int>& destination, unordered_set<int>& seen) {
        if ( start[0] == destination[0] && start[1] == destination[1] ) return true;
        int coord = start[0] * maze[0].size() + start[1];
        if (seen.count(coord)) return false; // seen
        else seen.insert(coord);
        
        bool flag = false;
        for (auto& d : directions) {            
            vector<int> newStart = go2End(maze, start, d);
            flag = flag || search(maze, newStart, destination, seen);
        }
        
        return flag;
    }
    
    vector<int> go2End(vector<vector<int>>& maze, vector<int> loc, vector<int>& d) {
        int x = loc[0], y = loc[1];
        while (true) {
            int x_new = x + d[0], y_new = y + d[1];
            if ( x_new < 0 || x_new == maze.size() || y_new < 0 || y_new == maze[0].size() ) {
                break;
            }
            if ( maze[x_new][y_new] == 1 ) {
                break;
            }
            x += d[0];
            y += d[1];
        }
        
        return {x, y};
    }

    vector<vector<int>> directions {
        {0, 1},
        {0, -1},
        {-1, 0},
        {1, 0}
    };
};