/*


DP 背包问题
1. LC 322. Coin Change
2. 

Note:
1. Initialize N size dp memory
(0, INT_MAX, INT_MAX, ...)
2. DP formula: mem[i][j] = min( mem[i][j], mem[i][j - coins[i]] + 1 ) // decide if backpack can replace some and hold this one

*/


// 322. Coin Change
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