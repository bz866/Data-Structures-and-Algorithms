/*

Use customized function to sort

1. lambda expression
2. struct expression

Leetcode: 692. Top K Frequent Words

*/

// lambda expression
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freqMap;
        for (auto& w : words) {
            ++freqMap[w];
        }
        
        vector<pair<string, int>> sortedFreq( freqMap.begin(), freqMap.end() );
        // sort(sortedFreq.begin(), sortedFreq.end(), sortByFreq)
        
        auto sortByFreq [] (const <string, int>& pa, const <string, int>& pb) {
        	if (pa.second > pb.second) return true; 
            else if (pa.second < pb.second) return false;
            else return pa.first < pb.first;
        };

        sort(sortedFreq.begin(), sortedFreq.end(), sortByFreq);
        
        vector<string> res(k);
        for (int i = 0; i < k; ++i) {
            res[i] = sortedFreq[i].first;
        }
        
        return res;
    }
};


// struct expression
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freqMap;
        for (auto& w : words) {
            ++freqMap[w];
        }
        
        vector<pair<string, int>> sortedFreq( freqMap.begin(), freqMap.end() );
        // sort(sortedFreq.begin(), sortedFreq.end(), sortByFreq)
        
        sort(sortedFreq.begin(), sortedFreq.end(), sortByFreq);
        
        vector<string> res(k);
        for (int i = 0; i < k; ++i) {
            res[i] = sortedFreq[i].first;
        }
        
        return res;
    }
    
    struct{
        bool operator() (const pair<string,int>& pa, const pair<string,int>& pb) const
        { 
            if (pa.second > pb.second) return true; 
            else if (pa.second < pb.second) return false;
            else return pa.first < pb.first;
        }
    } sortByFreq;
};