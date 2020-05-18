/*

All combination sum in Leetcode using backtrack

39. Combination Sum

40. Combination Sum II



*/


// LC 39 Combination Sum 
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> inUse;
        search(candidates, inUse, 0, target, res);
        return res;
    }
    
    void search(vector<int>& candidates, vector<int>& inUse, int loc, int target, vector<vector<int>>& res) {
        if (target == 0) {
            res.push_back(inUse);
            return;
        }
        
        if (target < 0) {
            return;
        }
        
        for (int i = loc; i < candidates.size(); ++i){ // set i = loc to avoid duplicated combinations
            int& coin = candidates[i];
            inUse.push_back(coin);
            search(candidates, inUse, i, target-coin, res); 
            inUse.pop_back();
        }
        
        return;
    }
};

// LC 40 Combination Sum II

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> inUse;
        search(candidates, inUse, 0, target, res);
        return res;
    }

    void search(vector<int>& candidates, vector<int> inUse, int idx, int target, vector<vector<int>>& res) {
    	if (target == 0) {
    		res.push_back(inUse);
    		return;
    	}

    	if (target < 0 ) {
    		return;
    	}

    	for (int i = idx; i < candidates.size(); ++i) {
 			if ( i > idx && candidates[i] == candidates[i-1] ) continue;
    		int& n = candidates[i];
    		inUse.push_back(n);
    		search(candidates, inUse, i+1, target-n, res);
    		inUse.pop_back();
    	}

    	return;
    }
};








