/*

DP to get longest common sequence between strings
generalize to string edit problem 

583. Delete Operation for Two Strings
1143. Longest Common Subsequence
72. Edit Distance

Note:
1. mind the consective sequence cases in DP

*/


class Solution {
public:
    int minDistance(string word1, string word2) {
        int maxCommonLen = longestCommonSubsequence(word1, word2);
        return word1.size() - maxCommonLen + word2.size() - maxCommonLen;
    }
    
    
    int longestCommonSubsequence(string text1, string text2) {
        vector<int> mem ( text1.size() + 1, 0 );
        
        for (int i = 0; i < text2.size(); ++i) {
            char cshort = text2[i];
            vector<int> curMem( text1.size() + 1, 0);
            for (int j = 0; j < text1.size(); ++j) {
                char clong = text1[j];
                int increment = clong == cshort ? 1 : 0;
                curMem[j+1] = max( max(mem[j+1], curMem[j]), mem[j] + increment ); // handle the consective case
            }
            swap(mem, curMem);
        }
        
        return mem.back();
    }
};