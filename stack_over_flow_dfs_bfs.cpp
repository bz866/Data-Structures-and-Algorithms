/*

LC 17. Letter Combinations of a Phone Number

Note:
1. The recursion uses the built-in system stack depth, easily to get stack overflow. 
2. The BFS uses memory outside the system stack
3. The **Optimal Way** is to write a stack outside to simulate the recursion to 
1) save memory
2) avoid stack overflow  

*/

//BFS 
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) return {};
        
        vector<string> res;
        queue<string> que;
        que.push("");
        int idx = 0;
        while (que.size() > 0) {
            for (int i = que.size(); i > 0; --i) {
                string cur = que.front(); que.pop();
                if (cur.size() == digits.size()) {
                    res.push_back(cur);
                    continue;
                }
                char n = digits[idx];
                for (char l : m_[n]) {
                    cur += l;
                    que.push(cur);
                    cur.pop_back();
                }
                cout << endl;
            }
            ++idx;
        }
        return res;
    }
    
    unordered_map<char, string> m_ {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
};


//DFS (potentially stack overflow)

