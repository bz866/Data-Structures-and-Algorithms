/*

istringstream works for " " split

ss >> target_variable

ss is true before .eof()

when over access the last token, ss becomes false 

*/

// Leetcode 165. Compare Version Numbers

class Solution {
public:
    int compareVersion(string version1, string version2) {
        for (auto& c : version1) if (c == '.') c = ' ';
        for (auto& c : version2) if (c == '.') c = ' ';
        
        istringstream s1(version1), s2(version2);
        while (1) {
            int n1, n2;
            if (not (s1 >> n1)) n1 = 0;
            if (not (s2 >> n2)) n2 = 0;
            if (not s1 && not s2) return 0;
            if (n1 > n2) return 1;
            if (n1 < n2) return -1;
        }
        
    }
};


// OR

class Solution {
public:
    int compareVersion(string version1, string version2) {
        for (auto& c : version1) if (c == '.') c = ' ';
        for (auto& c : version2) if (c == '.') c = ' ';

        istringstream s1(version1), s2(version2);
        
        while (1) {
            int n1, n2;
            s1 >> n1;
            s2 >> n2;
            if (not s1) n1 = 0;
            if (not s2) n2 = 0;
            if (not s1 && not s2) return 0;
            if (n1 > n2) return 1;
            if (n1 < n2) return -1;
        }
        
    }
};