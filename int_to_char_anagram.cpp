/*

49. Group Anagrams

Note:
1. convert integer to alphabet letter
2. string(number of copies, char) + to_string(int)

*/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<int>> m;
        
        for (int i = 0; i < strs.size(); ++i) {
            vector<int> bucket (26, 0);
            const string& w = strs[i];
            for (const char& c : w) {
                ++bucket[c-'a']; // bucket count the frequency
            }
            string keyStr = "";
            // convert list of frequency count as a string, as the key of anagrams
            for (int j = 0; j < bucket.size(); ++j) {
                if (bucket[j] == 0) continue;
                // convert int to char and alphabet letters
                keyStr += string(1, j + 'a') + to_string(bucket[j]); // a1b1t1;  a2b3t1 => char: frequency
            }
            m[keyStr].push_back(i);
        }
        
        for (auto& p : m) {
            vector<string> v(p.second.size());
            for (int i = 0 ; i < p.second.size(); ++i) {
                // v.push_back(strs[i]);
                v[i] = strs[p.second[i]];
            }
            res.push_back(v);
        }
        
        return res;
    }
};