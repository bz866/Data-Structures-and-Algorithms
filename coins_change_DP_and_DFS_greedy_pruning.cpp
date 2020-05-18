/*

LC 322. Coin Change
经典背包问题

Approach: 
1. DP 
2. DFS + greedy + pruning (faster than DP)

*/


// DP背包
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        //     0 1 2 3 4 5 6 7 8 9 10 11
        // 1   0 1 2 3 4 5 6 7 8 9 10 11
        // 2   0 1 1 2 2 3
        // 5
        // vector<int> mem (amount+1, INT_MAX);
        vector<int> mem (amount+1, amount+1);
        mem[0] = 0;
        
        for (int i = 0; i < coins.size(); ++i) {
            // for (int j = 1; j < amount+1; ++j) {
            for (int j = coins[i]; j < amount+1; ++j) {   
                // if (j - coins[i] < 0 || mem[j-coins[i]] == INT_MAX) { // handle invalid case
                //     continue;
                // }
                // 背包问题DP
                mem[j] = min( mem[j], mem[j-coins[i]] + 1); // j is the number of current amount, j - coin[i] means using the current coin
            }
        }
        
        // return mem.back() != INT_MAX ? mem.back() : -1;
        return mem.back() != amount+1 ? mem.back() : -1;
    }
};

// DFS + greedy + pruning
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // try to use large coins as much as possible
        // if larger than the current optimal before consume the amount, prune to save time
        sort(coins.rbegin(), coins.rend());
        int best = INT_MAX;
        greedySearch(coins, 0, amount, 0, best);
        
        return best != INT_MAX ? best : -1;
    }
    
    void greedySearch(vector<int>& coins, int loc, int amount, int cnt, int& best) {
        if ( loc == coins.size() && amount != 0 ) return; // not valid 
        if ( loc == coins.size() - 1 && amount % coins[loc] == 0) { // fast end
            best = min(best, cnt + amount / coins[loc] );
            return;
        }
        
        int maxUse = amount / coins[loc];
        for (int i = maxUse; i >= 0; --i) { // greedy
            if ( cnt + i >= best ) break; // pruning
            greedySearch(coins, loc+1, amount-i*coins[loc], cnt+i, best);
        }
        
        return;
    } 
};









