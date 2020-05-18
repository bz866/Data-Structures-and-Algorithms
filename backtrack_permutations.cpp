/*

BackTrack on Permutations 

46. Permutations

47. Permutations II *********

Note:
LC47 duplicated numbers can only be used once

*/

// 46. Permutations
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<bool> used (nums.size(), false);
        vector<int> curVec;
        search(nums, curVec, used, res);
        return res;
    }
    
    void search(vector<int>& nums, vector<int>& curVec, vector<bool>& used, vector<vector<int>>& res) {
        if (curVec.size() == nums.size() ) {
            res.push_back( curVec );
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;
            used[i] = true;
            curVec.push_back(nums[i]);
            search(nums, curVec, used, res);
            curVec.pop_back();
            used[i] = false;
        }
         
        return;
    }
};


// 47. Permutations II
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> curVec;
        vector<bool> used(nums.size(), false);
        search(nums, used, curVec, res);
        return res;
    }
    
    void search(vector<int>& nums, vector<bool>& used, vector<int>& curVec, vector<vector<int>>& res) {
        if (curVec.size() == nums.size()) {
            res.push_back(curVec);
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;
            // *** duplicated numbers can only be used once
            // ******
            if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // NOTE !!!!!!!!
            // ******
            used[i] = true;
            curVec.push_back(nums[i]);
            search(nums, used, curVec, res);
            curVec.pop_back();
            used[i] = false;
        }
        
        return;
    }
};






